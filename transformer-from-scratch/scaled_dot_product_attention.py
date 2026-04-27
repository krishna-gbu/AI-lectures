from __future__ import annotations

import math
from typing import Iterable


NEG_INF = -10**30


def infer_shape(value):
    if not isinstance(value, list):
        return ()
    if not value:
        return (0,)
    return (len(value),) + infer_shape(value[0])


def _assert_uniform_rows(matrix, name):
    if not matrix:
        return
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise ValueError(f"{name} must have uniform row lengths")


def _validate_rank_2_or_3(tensor, name):
    shape = infer_shape(tensor)
    if len(shape) not in (2, 3):
        raise ValueError(f"{name} must be rank-2 or rank-3, got shape {shape}")
    return shape


def _ensure_batched(tensor, name):
    shape = _validate_rank_2_or_3(tensor, name)
    if len(shape) == 2:
        return [tensor], True
    return tensor, False


def _validate_batch_inputs(query, key, value, mask):
    q_shape = infer_shape(query)
    k_shape = infer_shape(key)
    v_shape = infer_shape(value)

    if q_shape[0] != k_shape[0] or q_shape[0] != v_shape[0]:
        raise ValueError("query, key, and value must share batch size")

    if q_shape[2] != k_shape[2]:
        raise ValueError("query and key must have the same d_k")

    if k_shape[1] != v_shape[1]:
        raise ValueError("key and value must share key_len")

    if mask is None:
        return

    m_shape = infer_shape(mask)
    if m_shape[0] != q_shape[0] or m_shape[1] != q_shape[1] or m_shape[2] != k_shape[1]:
        raise ValueError("mask shape must be [batch][query_len][key_len]")


def dot(left, right):
    if len(left) != len(right):
        raise ValueError("dot product inputs must have equal length")
    return sum(a * b for a, b in zip(left, right))


def softmax(values):
    if not values:
        raise ValueError("softmax received an empty row")

    max_value = max(values)
    exp_values = []
    for value in values:
        if value <= NEG_INF / 2:
            exp_values.append(0.0)
        else:
            exp_values.append(math.exp(value - max_value))

    total = sum(exp_values)
    if total == 0:
        raise ValueError("all positions were masked; softmax is undefined")

    return [value / total for value in exp_values]


def causal_mask(size, batch_size=1):
    if size <= 0:
        raise ValueError("size must be positive")
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")

    batches = []
    for _ in range(batch_size):
        mask = []
        for row in range(size):
            mask.append([1 if col <= row else 0 for col in range(size)])
        batches.append(mask)
    return batches


def scaled_dot_product_attention(query, key, value, mask=None):
    query, query_was_rank_2 = _ensure_batched(query, "query")
    key, key_was_rank_2 = _ensure_batched(key, "key")
    value, value_was_rank_2 = _ensure_batched(value, "value")

    if query_was_rank_2 != key_was_rank_2 or query_was_rank_2 != value_was_rank_2:
        raise ValueError("query, key, and value must all have the same rank")

    if mask is not None:
        mask, mask_was_rank_2 = _ensure_batched(mask, "mask")
        if mask_was_rank_2 != query_was_rank_2:
            raise ValueError("mask rank must match query/key/value rank")

    _validate_batch_inputs(query, key, value, mask)

    d_k = len(query[0][0])
    scale = math.sqrt(d_k)

    all_outputs = []
    all_weights = []

    for batch_index, query_batch in enumerate(query):
        key_batch = key[batch_index]
        value_batch = value[batch_index]
        mask_batch = None if mask is None else mask[batch_index]

        _assert_uniform_rows(query_batch, "query")
        _assert_uniform_rows(key_batch, "key")
        _assert_uniform_rows(value_batch, "value")

        batch_outputs = []
        batch_weights = []

        for query_index, query_vector in enumerate(query_batch):
            logits = [dot(query_vector, key_vector) / scale for key_vector in key_batch]

            if mask_batch is not None:
                masked_logits = []
                for logit, keep in zip(logits, mask_batch[query_index]):
                    masked_logits.append(logit if keep else NEG_INF)
                logits = masked_logits

            attention_weights = softmax(logits)

            output_vector = []
            for value_dim in range(len(value_batch[0])):
                weighted_sum = 0.0
                for key_index, weights in enumerate(attention_weights):
                    weighted_sum += weights * value_batch[key_index][value_dim]
                output_vector.append(weighted_sum)

            batch_outputs.append(output_vector)
            batch_weights.append(attention_weights)

        all_outputs.append(batch_outputs)
        all_weights.append(batch_weights)

    if query_was_rank_2:
        return all_outputs[0], all_weights[0]
    return all_outputs, all_weights


def pretty_print_matrix(matrix):
    for row in matrix:
        print([round(value, 4) for value in row])


def run_demo():
    query = [[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]
    key = [[[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]]
    value = [[[10.0, 0.0], [0.0, 20.0], [5.0, 5.0]]]
    mask = causal_mask(size=3, batch_size=1)

    output, weights = scaled_dot_product_attention(query, key, value, mask=mask)

    print("Causal mask:")
    pretty_print_matrix(mask[0])
    print("\nAttention weights:")
    pretty_print_matrix(weights[0])
    print("\nOutput:")
    pretty_print_matrix(output[0])


if __name__ == "__main__":
    run_demo()
