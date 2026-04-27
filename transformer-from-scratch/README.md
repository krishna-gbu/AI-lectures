# Transformer From Scratch

Ye folder `other-notes` ke theory track ko actual code me convert karne ke liye banaya gaya hai.

Current status:

- Milestone 1 implemented: `Scaled Dot-Product Attention`
- external dependencies: `none`
- language: pure `Python`

## Files

- [scaled_dot_product_attention.py](./scaled_dot_product_attention.py)
- [tests/test_scaled_dot_product_attention.py](./tests/test_scaled_dot_product_attention.py)

## Tensor Convention

Inputs:

- `query`: `[batch][query_len][d_k]`
- `key`: `[batch][key_len][d_k]`
- `value`: `[batch][key_len][d_v]`
- `mask`: `[batch][query_len][key_len]`

Mask meaning:

- `1` or `True` = keep
- `0` or `False` = mask out

## Run

Demo:

```bash
python3 scaled_dot_product_attention.py
```

Tests:

```bash
python3 -m unittest discover -s tests -v
```

## Why Pure Python

Current workspace me `torch` aur `numpy` install nahi mile. Isliye pehla milestone pure Python me rakha gaya hai taaki:

- attention math clear rahe
- masking behavior inspect ho sake
- tests immediately run ho saken

Later port path:

1. pure Python version samjho
2. NumPy version banao
3. PyTorch `nn.Module` version banao

## Next Milestones

Recommended next coding order:

1. causal mask helper ko separate utility file me nikaalo
2. multi-head attention
3. positional encoding
4. feed-forward network
5. add & norm block
6. encoder layer
