# Transformer Implementation Guide - Complete Hinglish Explanation

> Yeh document Transformer ko implement karne ka complete roadmap hai with KYU, KYA, KAISE explanation and examples.

---

# TABLE OF CONTENTS

1. [Transformer Complete Flow](#transformer-complete-flow-bird-eye-view)
2. [Prerequisites](#phase-0-prerequisites)
3. [Scaled Dot-Product Attention](#step-1-scaled-dot-product-attention)
4. [Multi-Head Attention](#step-2-multi-head-attention)
5. [Positional Encoding](#step-3-positional-encoding)
6. [Feed-Forward Network](#step-4-position-wise-feed-forward-network)
7. [Layer Normalization & Residual](#step-5-layer-normalization--residual-connection)
8. [Embeddings](#step-6-embeddings)
9. [Encoder Layer](#step-7-encoder-layer)
10. [Decoder Layer](#step-8-decoder-layer)
11. [Complete Transformer](#step-9-complete-transformer)
12. [Training Setup](#phase-3-training-setup)
13. [Inference](#phase-4-inference)

---

# TRANSFORMER COMPLETE FLOW (Bird Eye View)

> Pehle poora flow samjho, phir individual components!

## Transformer Ka Complete Flow (Step by Step)

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRANSFORMER FLOW                             │
└─────────────────────────────────────────────────────────────────┘

INPUT: "I love coding"
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: TOKENIZATION                                            │
│                                                                 │
│   "I love coding" → [101, 2034, 5678]  (token IDs)              │
│   Shape: (batch=1, seq_len=3)                                   │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: EMBEDDING                                               │
│                                                                 │
│   Token IDs → Dense Vectors                                     │
│   [101, 2034, 5678] → [[0.2, -0.5, ...], [0.8, 0.1, ...], ...]  │
│   Shape: (1, 3, 512)                                            │
│                                                                 │
│   + SCALING: Multiply by √512 ≈ 22.6                            │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: POSITIONAL ENCODING                                     │
│                                                                 │
│   KYU? Model ko word ki position pata nahi!                     │
│                                                                 │
│   "I love coding" vs "coding love I" → Same embeddings!         │
│   Position info add karna zaroori hai                           │
│                                                                 │
│   Final = Embedding + Positional Encoding                       │
│   Shape: (1, 3, 512) + (1, 3, 512) = (1, 3, 512)                │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: DROPOUT                                                 │
│                                                                 │
│   Randomly 10% values zero kar do (regularization)              │
│   Shape: (1, 3, 512)                                            │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 5: ENCODER (×6 layers)                                     │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ ENCODER LAYER (repeat 6 times)                          │   │
│   │                                                         │   │
│   │   5a. Multi-Head Self-Attention                         │   │
│   │       → Har word doosre words ko attend kare            │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   5b. Add & Norm                                        │   │
│   │       → Residual + LayerNorm                            │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   5c. Feed-Forward Network                              │   │
│   │       → 512 → 2048 → 512                                │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   5d. Add & Norm                                        │   │
│   │       → Residual + LayerNorm                            │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   Output: MEMORY (encoder output for decoder)                   │
│   Shape: (1, 3, 512)                                            │
└─────────────────────────────────────────────────────────────────┘
         │
         │ (Memory goes to Decoder)
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 6: DECODER (×6 layers)                                     │
│                                                                 │
│   Input: Target sequence (shifted right)                        │
│   "<s> Main tumse" → Predict "Main tumse pyaar"                 │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │ DECODER LAYER (repeat 6 times)                          │   │
│   │                                                         │   │
│   │   6a. MASKED Multi-Head Self-Attention                  │   │
│   │       → Future words dekh nahi sakta (cheating prevent) │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   6b. Add & Norm                                        │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   6c. Cross-Attention (Encoder-Decoder)                 │   │
│   │       → Q from decoder, K,V from encoder (memory)       │   │
│   │       → Source sentence ko attend kare                  │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   6d. Add & Norm                                        │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   6e. Feed-Forward Network                              │   │
│   │       → Shape: (1, 3, 512)                              │   │
│   │                     │                                   │   │
│   │                     ▼                                   │   │
│   │   6f. Add & Norm                                        │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   Output Shape: (1, 3, 512)                                     │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 7: LINEAR LAYER                                            │
│                                                                 │
│   Project 512 dim → vocab_size (e.g., 50000)                    │
│   Shape: (1, 3, 512) → (1, 3, 50000)                            │
│                                                                 │
│   Har position ke liye vocabulary mein har word ka score        │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 8: SOFTMAX                                                 │
│                                                                 │
│   Scores → Probabilities                                        │
│   Shape: (1, 3, 50000)                                          │
│                                                                 │
│   Position 1: [0.001, 0.002, ..., 0.4(Main), ..., 0.001]        │
│   Position 2: [0.001, 0.35(tumse), ..., 0.001]                  │
│   Position 3: [0.001, ..., 0.45(pyaar), ..., 0.001]             │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ STEP 9: OUTPUT                                                  │
│                                                                 │
│   Highest probability tokens select karo:                       │
│   → "Main tumse pyaar"                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Shape Journey Through Transformer

```
Step                          Shape                    Example
─────────────────────────────────────────────────────────────────
Input Text                    -                        "I love coding"
Tokenization                  (B, S)                   (1, 3)
Embedding                     (B, S, 512)              (1, 3, 512)
+ Positional Encoding         (B, S, 512)              (1, 3, 512)
Encoder Output                (B, S, 512)              (1, 3, 512)
Decoder Output                (B, T, 512)              (1, 3, 512)
Linear                        (B, T, Vocab)            (1, 3, 50000)
Softmax                       (B, T, Vocab)            (1, 3, 50000)
─────────────────────────────────────────────────────────────────
B = Batch size
S = Source sequence length
T = Target sequence length
Vocab = Vocabulary size
```

---

## Implementation Order (Code Likhne Ka Order)

```
1️⃣  Scaled Dot-Product Attention    ← FOUNDATION (sabse pehle!)
         │
         ▼
2️⃣  Multi-Head Attention            ← Uses #1
         │
         ▼
3️⃣  Positional Encoding             ← Independent component
         │
         ▼
4️⃣  Feed-Forward Network            ← Independent component
         │
         ▼
5️⃣  Layer Norm + Residual           ← Wraps #2 and #4
         │
         ▼
6️⃣  Embeddings                      ← Independent component
         │
         ▼
7️⃣  Encoder Layer                   ← Combines #2, #4, #5
         │
         ▼
8️⃣  Decoder Layer                   ← Like #7 but with masking + cross-attention
         │
         ▼
9️⃣  Full Transformer                ← Combines everything!
         │
         ▼
🔟  Training Loop                    ← Loss, Optimizer, LR Schedule
         │
         ▼
1️⃣1️⃣ Inference                       ← Greedy / Beam Search
```

---

## Quick Summary Table

| Step | Component | Input Shape | Output Shape | Kya Karta Hai |
|------|-----------|-------------|--------------|---------------|
| 1 | Tokenization | Text | (B, S) | Words → Token IDs |
| 2 | Embedding | (B, S) | (B, S, 512) | IDs → Dense Vectors |
| 3 | Pos Encoding | (B, S, 512) | (B, S, 512) | Position info ADD |
| 4 | Encoder ×6 | (B, S, 512) | (B, S, 512) | Context samjho |
| 5 | Decoder ×6 | (B, T, 512) | (B, T, 512) | Output generate |
| 6 | Linear | (B, T, 512) | (B, T, Vocab) | Vocab scores |
| 7 | Softmax | (B, T, Vocab) | (B, T, Vocab) | Probabilities |
| 8 | Argmax | (B, T, Vocab) | (B, T) | Final tokens |

---

## Encoder vs Decoder - Key Differences

| Feature | Encoder | Decoder |
|---------|---------|---------|
| Self-Attention | Normal (see all) | MASKED (see only past) |
| Cross-Attention | No | Yes (attends to encoder) |
| Sub-layers | 2 (Attn + FFN) | 3 (Masked Attn + Cross Attn + FFN) |
| Purpose | Understand input | Generate output |
| Input | Source sentence | Target sentence (shifted) |

---

## Data Flow Example

```
Translation Task: English → Hindi
Source: "I love coding"
Target: "Main coding pasand karta hoon"

TRAINING:
─────────
Encoder Input:  "I love coding"
Decoder Input:  "<s> Main coding pasand karta hoon"      (shifted right)
Expected Output: "Main coding pasand karta hoon </s>"    (next tokens)

INFERENCE:
──────────
Step 1: Encoder("I love coding") → Memory
Step 2: Decoder("<s>", Memory) → "Main"
Step 3: Decoder("<s> Main", Memory) → "coding"
Step 4: Decoder("<s> Main coding", Memory) → "pasand"
Step 5: Decoder("<s> Main coding pasand", Memory) → "karta"
Step 6: Decoder("<s> Main coding pasand karta", Memory) → "hoon"
Step 7: Decoder("<s> Main coding pasand karta hoon", Memory) → "</s>"
STOP!

Final Output: "Main coding pasand karta hoon"
```

---

# PHASE 0: PREREQUISITES

## Pehle Yeh Samjho (Before You Start)

### 1. Tensors Kya Hote Hain?

**KYA:** Tensor ek multi-dimensional array hai (like numpy array but GPU-friendly)

**Example:**
```
Scalar (0D tensor):     5
Vector (1D tensor):     [1, 2, 3, 4, 5]
Matrix (2D tensor):     [[1, 2], [3, 4], [5, 6]]
3D tensor:              [[[1,2], [3,4]], [[5,6], [7,8]]]
```

**Transformer mein shapes:**
```
Input sentence: "I love coding"
After tokenization: [101, 2342, 5765]  → Shape: (3,) - 1D

Batch of sentences:
  "I love coding"    → [101, 2342, 5765]
  "Hello world"      → [102, 5643, 0]     (0 = padding)
Batch shape: (2, 3) → (batch_size, sequence_length)

After embedding (dim=512):
Shape: (2, 3, 512) → (batch_size, sequence_length, embedding_dim)
```

### 2. Matrix Multiplication (MatMul) Kya Hai?

**KYA:** Do matrices ko multiply karna

**KYU:** Attention mein Q aur K ka dot product chahiye

**Example:**
```
A = [[1, 2],      B = [[5, 6],
     [3, 4]]          [7, 8]]

A × B = [[1×5 + 2×7, 1×6 + 2×8],
         [3×5 + 4×7, 3×6 + 4×8]]
      = [[19, 22],
         [43, 50]]

Shape rule: (m, n) × (n, p) = (m, p)
```

**Transformer mein:**
```
Q shape: (batch, seq_len, d_k) = (32, 10, 64)
K^T shape: (batch, d_k, seq_len) = (32, 64, 10)

Q × K^T shape: (32, 10, 10) → Attention scores for each position!
```

### 3. Softmax Kya Hai?

**KYA:** Numbers ko probabilities mein convert karta hai (sum = 1)

**KYU:** Attention weights chahiye jo sum karke 1 hon

**Formula:**
```
softmax(x_i) = exp(x_i) / sum(exp(x_j)) for all j
```

**Example:**
```
Input scores: [2.0, 1.0, 0.5]

Step 1: exp of each
  exp(2.0) = 7.39
  exp(1.0) = 2.72
  exp(0.5) = 1.65

Step 2: sum = 7.39 + 2.72 + 1.65 = 11.76

Step 3: divide each by sum
  7.39/11.76 = 0.63
  2.72/11.76 = 0.23
  1.65/11.76 = 0.14

Output: [0.63, 0.23, 0.14] → Sum = 1.0!

Interpretation:
  - Position 1 ko 63% attention
  - Position 2 ko 23% attention
  - Position 3 ko 14% attention
```

### 4. Dot Product Kya Hai?

**KYA:** Do vectors ko multiply karke sum karna

**KYU:** Similarity measure karne ke liye - similar vectors ka dot product high hota hai

**Example:**
```
a = [1, 2, 3]
b = [4, 5, 6]

a · b = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32

Similarity example:
"king" vector  = [0.9, 0.1, 0.8]
"queen" vector = [0.85, 0.15, 0.75]
"car" vector   = [0.1, 0.9, 0.2]

king · queen = 0.9×0.85 + 0.1×0.15 + 0.8×0.75 = 1.38 (HIGH - similar!)
king · car   = 0.9×0.1 + 0.1×0.9 + 0.8×0.2 = 0.34 (LOW - different!)
```

---

# STEP 1: SCALED DOT-PRODUCT ATTENTION

## KYA Hai Yeh?

Scaled Dot-Product Attention Transformer ka **CORE** component hai. Yeh decide karta hai ki ek word ko doosre words pe kitna attention dena chahiye.

## KYU Chahiye?

**Problem:** Sentence mein har word ka matlab context pe depend karta hai.

**Example:**
```
Sentence 1: "The bank of the river was beautiful"
Sentence 2: "I went to the bank to withdraw money"

"bank" ka meaning:
  - Sentence 1 mein: River bank (kinara)
  - Sentence 2 mein: Financial bank

Attention helps:
  - Sentence 1: "bank" attends to "river" → samajh gaya ki kinara hai
  - Sentence 2: "bank" attends to "withdraw", "money" → samajh gaya ki financial hai
```

## KAISE Kaam Karta Hai?

### Components:
```
Q (Query):  "Main kya dhundh raha hoon?"
K (Key):    "Har word ka label/identifier"
V (Value):  "Har word ki actual information"
```

### Formula:
```
Attention(Q, K, V) = softmax(QK^T / √d_k) × V
```

### Step-by-Step Process:

**Example Sentence:** "I love coding"

```
Step 1: Create Q, K, V for each word
────────────────────────────────────
Word "love" wants to know which words to attend to.

Q_love = [0.5, 0.3, 0.8, 0.2]  (Query: "Main kya dhundh raha hoon?")

K_I      = [0.1, 0.2, 0.3, 0.1]  (Key for "I")
K_love   = [0.5, 0.3, 0.8, 0.2]  (Key for "love")
K_coding = [0.7, 0.6, 0.9, 0.4]  (Key for "coding")

V_I      = [0.9, 0.1, 0.2, 0.3]  (Value/info for "I")
V_love   = [0.4, 0.5, 0.6, 0.7]  (Value/info for "love")
V_coding = [0.2, 0.8, 0.1, 0.9]  (Value/info for "coding")
```

```
Step 2: Calculate Dot Products (Q · K)
──────────────────────────────────────
"love" ka query saare keys se compare karo:

Q_love · K_I      = 0.5×0.1 + 0.3×0.2 + 0.8×0.3 + 0.2×0.1 = 0.37
Q_love · K_love   = 0.5×0.5 + 0.3×0.3 + 0.8×0.8 + 0.2×0.2 = 1.02
Q_love · K_coding = 0.5×0.7 + 0.3×0.6 + 0.8×0.9 + 0.2×0.4 = 1.33

Scores: [0.37, 1.02, 1.33]

Interpretation:
  - "love" ka "coding" se highest match (1.33)
  - "love" ka "I" se lowest match (0.37)
```

```
Step 3: Scale by √d_k
─────────────────────
d_k = 4 (dimension of keys)
√d_k = √4 = 2

Scaled scores = [0.37/2, 1.02/2, 1.33/2] = [0.185, 0.51, 0.665]

KYU SCALE KARTE HAIN?
- Bade dimensions mein dot products bahut bade ho jaate hain
- Bade values pe softmax bahut peaked ho jaata hai (almost 0 ya 1)
- Peaked softmax = small gradients = slow learning

Example without scaling (d_k = 512):
  Scores: [45, 52, 48]
  Softmax: [0.001, 0.997, 0.002] ← Almost one-hot, gradients dead!

With scaling (divide by √512 ≈ 22.6):
  Scores: [2.0, 2.3, 2.1]
  Softmax: [0.27, 0.40, 0.33] ← Smooth, good gradients!
```

```
Step 4: Apply Softmax
─────────────────────
Scaled scores: [0.185, 0.51, 0.665]

Softmax calculation:
  exp(0.185) = 1.20
  exp(0.51)  = 1.67
  exp(0.665) = 1.94

  Sum = 1.20 + 1.67 + 1.94 = 4.81

  Attention weights:
    α_I      = 1.20/4.81 = 0.25 (25%)
    α_love   = 1.67/4.81 = 0.35 (35%)
    α_coding = 1.94/4.81 = 0.40 (40%)

Final weights: [0.25, 0.35, 0.40]
```

```
Step 5: Weighted Sum of Values
──────────────────────────────
Output = 0.25 × V_I + 0.35 × V_love + 0.40 × V_coding

V_I      = [0.9, 0.1, 0.2, 0.3]
V_love   = [0.4, 0.5, 0.6, 0.7]
V_coding = [0.2, 0.8, 0.1, 0.9]

Output = 0.25×[0.9, 0.1, 0.2, 0.3] +
         0.35×[0.4, 0.5, 0.6, 0.7] +
         0.40×[0.2, 0.8, 0.1, 0.9]

       = [0.225, 0.025, 0.05, 0.075] +
         [0.14, 0.175, 0.21, 0.245] +
         [0.08, 0.32, 0.04, 0.36]

       = [0.445, 0.52, 0.30, 0.68]

This is the NEW representation of "love" that incorporates
context from all other words!
```

### Matrix Form (All words at once):

```
Q = [[q_I], [q_love], [q_coding]]       Shape: (3, 4)
K = [[k_I], [k_love], [k_coding]]       Shape: (3, 4)
V = [[v_I], [v_love], [v_coding]]       Shape: (3, 4)

Step 1: QK^T
┌─────────────────────────────────────┐
│         K_I   K_love  K_coding      │
│ Q_I    [0.xx   0.xx    0.xx  ]      │
│ Q_love [0.37   1.02    1.33  ]      │
│ Q_cod  [0.xx   0.xx    0.xx  ]      │
└─────────────────────────────────────┘
Shape: (3, 4) × (4, 3) = (3, 3)

Step 2: Scale by √d_k
  Divide entire matrix by 2

Step 3: Softmax (row-wise)
  Each row sums to 1

Step 4: Multiply by V
  (3, 3) × (3, 4) = (3, 4)

  Output shape same as input: (3, 4)
  But now each word has context from all other words!
```

### Implementation Pseudocode:

```
function scaled_dot_product_attention(Q, K, V, mask=None):
    # Q, K, V shapes: (batch, seq_len, d_k)

    d_k = K.shape[-1]

    # Step 1: MatMul Q and K^T
    scores = matmul(Q, K.transpose(-2, -1))  # (batch, seq_len, seq_len)

    # Step 2: Scale
    scores = scores / sqrt(d_k)

    # Step 3: Mask (optional - for decoder)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -infinity)

    # Step 4: Softmax
    attention_weights = softmax(scores, dim=-1)

    # Step 5: MatMul with V
    output = matmul(attention_weights, V)

    return output, attention_weights
```

---

# STEP 2: MULTI-HEAD ATTENTION

## KYA Hai Yeh?

Single attention ke bajaye, **multiple attention heads** parallel mein run karte hain. Har head different aspect pe focus karta hai.

## KYU Chahiye?

**Problem:** Single attention sirf ek type ki relationship capture kar sakta hai.

**Example:**
```
Sentence: "The cat sat on the mat because it was tired"

Different relationships to capture:
1. Syntactic: "cat" → "sat" (subject-verb)
2. Positional: "on" → "mat" (preposition-object)
3. Coreference: "it" → "cat" (pronoun reference)
4. Semantic: "tired" → "cat" (who is tired?)

Single head: Sirf ek relationship achhe se capture hogi
Multi-head: Har head alag relationship capture karega!
```

**Analogy:**
```
Single Head = Ek doctor se checkup
  - Sirf ek perspective

Multi-Head = Team of specialists
  - Head 1: Cardiologist (heart check)
  - Head 2: Neurologist (brain check)
  - Head 3: Orthopedic (bones check)
  - Head 4: Dermatologist (skin check)
  ... Final diagnosis = Combined opinion of all!
```

## KAISE Kaam Karta Hai?

### Parameters:
```
d_model = 512 (total dimension)
h = 8 (number of heads)
d_k = d_v = d_model / h = 512 / 8 = 64 (dimension per head)
```

### Step-by-Step Process:

```
Step 1: Linear Projections
──────────────────────────
Input X shape: (batch, seq_len, d_model) = (32, 10, 512)

For each head i (0 to 7):
  Q_i = X × W_Q_i    where W_Q_i shape: (512, 64)
  K_i = X × W_K_i    where W_K_i shape: (512, 64)
  V_i = X × W_V_i    where W_V_i shape: (512, 64)

Result: 8 sets of (Q, K, V), each with dimension 64
```

**Example:**
```
Original "love" embedding: [0.1, 0.2, ..., 0.5]  (512 dimensions)

After projection for Head 1:
  Q_1 = [0.3, 0.1, ..., 0.4]  (64 dimensions)
  K_1 = [0.2, 0.5, ..., 0.3]  (64 dimensions)
  V_1 = [0.4, 0.2, ..., 0.6]  (64 dimensions)

After projection for Head 2:
  Q_2 = [0.5, 0.3, ..., 0.2]  (64 dimensions) - DIFFERENT!
  K_2 = [0.1, 0.4, ..., 0.5]  (64 dimensions)
  V_2 = [0.3, 0.6, ..., 0.1]  (64 dimensions)

... same for heads 3-8
```

```
Step 2: Parallel Attention
──────────────────────────
Run scaled dot-product attention on EACH head:

head_1 = Attention(Q_1, K_1, V_1)  → Shape: (batch, seq_len, 64)
head_2 = Attention(Q_2, K_2, V_2)  → Shape: (batch, seq_len, 64)
head_3 = Attention(Q_3, K_3, V_3)  → Shape: (batch, seq_len, 64)
...
head_8 = Attention(Q_8, K_8, V_8)  → Shape: (batch, seq_len, 64)

Each head learns different attention patterns!
```

**What different heads might learn:**
```
Head 1 attention for "it" in "The cat... because it was tired":
  → High attention on "cat" (coreference)

Head 2 attention for "it":
  → High attention on "was" (subject-verb)

Head 3 attention for "it":
  → High attention on "tired" (semantic relationship)

Different heads = Different perspectives!
```

```
Step 3: Concatenate
───────────────────
Concat(head_1, head_2, ..., head_8)

Shape: (batch, seq_len, 64) × 8 → (batch, seq_len, 512)

Example for "love":
  head_1 output: [0.1, 0.2, ..., 0.3]  (64 dims)
  head_2 output: [0.4, 0.5, ..., 0.6]  (64 dims)
  ...
  head_8 output: [0.7, 0.8, ..., 0.9]  (64 dims)

  Concatenated: [0.1, 0.2, ..., 0.3, 0.4, 0.5, ..., 0.9]  (512 dims)
```

```
Step 4: Final Linear Projection
───────────────────────────────
Output = Concat × W_O    where W_O shape: (512, 512)

Shape: (batch, seq_len, 512) × (512, 512) = (batch, seq_len, 512)

This combines information from all heads into final representation!
```

### Visual Representation:

```
                    Input X (512 dim)
                          │
            ┌─────────────┼─────────────┐
            │             │             │
         ┌──▼──┐       ┌──▼──┐       ┌──▼──┐
         │Head1│       │Head2│  ...  │Head8│
         │64dim│       │64dim│       │64dim│
         └──┬──┘       └──┬──┘       └──┬──┘
            │             │             │
            └─────────────┼─────────────┘
                          │
                    Concat (512 dim)
                          │
                    Linear W_O
                          │
                    Output (512 dim)
```

### Implementation Pseudocode:

```
class MultiHeadAttention:
    def __init__(d_model=512, h=8):
        d_k = d_v = d_model // h  # 64

        # Linear projections for each head
        W_Q = Linear(d_model, d_model)  # Actually projects to h * d_k
        W_K = Linear(d_model, d_model)
        W_V = Linear(d_model, d_model)
        W_O = Linear(d_model, d_model)

    def forward(Q, K, V, mask=None):
        batch_size = Q.shape[0]

        # Step 1: Linear projections
        Q = W_Q(Q)  # (batch, seq_len, 512)
        K = W_K(K)
        V = W_V(V)

        # Reshape for multiple heads: (batch, seq_len, h, d_k)
        Q = Q.view(batch_size, -1, h, d_k).transpose(1, 2)
        K = K.view(batch_size, -1, h, d_k).transpose(1, 2)
        V = V.view(batch_size, -1, h, d_v).transpose(1, 2)
        # New shape: (batch, h, seq_len, d_k)

        # Step 2: Attention (parallel for all heads)
        attn_output = scaled_dot_product_attention(Q, K, V, mask)
        # Shape: (batch, h, seq_len, d_v)

        # Step 3: Concatenate heads
        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.view(batch_size, -1, d_model)
        # Shape: (batch, seq_len, 512)

        # Step 4: Final projection
        output = W_O(attn_output)

        return output
```

---

# STEP 3: POSITIONAL ENCODING

## KYA Hai Yeh?

Positional Encoding har word ko uski position ki information deta hai sequence mein.

## KYU Chahiye?

**Problem:** Transformer mein koi recurrence nahi hai, toh model ko pata nahi ki word kahan hai!

**Example:**
```
Sentence 1: "Dog bites man"  (Normal news)
Sentence 2: "Man bites dog"  (Surprising news!)

Without position info:
  Both look same to Transformer: {dog, bites, man}

With position info:
  Sentence 1: dog(pos=0), bites(pos=1), man(pos=2)
  Sentence 2: man(pos=0), bites(pos=1), dog(pos=2)
  Now Transformer knows the difference!
```

**Another Example:**
```
"I ate breakfast before going to office"
"I went to office before eating breakfast"

Word order changes meaning completely!
Positional encoding preserves this information.
```

## KAISE Kaam Karta Hai?

### Formula:
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Where:
  pos = position in sequence (0, 1, 2, ...)
  i = dimension index (0, 1, 2, ..., d_model/2 - 1)
  d_model = 512
```

### Step-by-Step Calculation:

```
Let's calculate PE for position 0 and position 1 with d_model = 8

For position 0:
───────────────
PE(0, 0) = sin(0 / 10000^(0/8)) = sin(0) = 0
PE(0, 1) = cos(0 / 10000^(0/8)) = cos(0) = 1
PE(0, 2) = sin(0 / 10000^(2/8)) = sin(0) = 0
PE(0, 3) = cos(0 / 10000^(2/8)) = cos(0) = 1
PE(0, 4) = sin(0 / 10000^(4/8)) = sin(0) = 0
PE(0, 5) = cos(0 / 10000^(4/8)) = cos(0) = 1
PE(0, 6) = sin(0 / 10000^(6/8)) = sin(0) = 0
PE(0, 7) = cos(0 / 10000^(6/8)) = cos(0) = 1

PE(pos=0) = [0, 1, 0, 1, 0, 1, 0, 1]
```

```
For position 1:
───────────────
PE(1, 0) = sin(1 / 10000^0) = sin(1) = 0.841
PE(1, 1) = cos(1 / 10000^0) = cos(1) = 0.540
PE(1, 2) = sin(1 / 10000^0.25) = sin(1/17.78) = sin(0.056) = 0.056
PE(1, 3) = cos(1 / 10000^0.25) = cos(0.056) = 0.998
PE(1, 4) = sin(1 / 10000^0.5) = sin(1/100) = sin(0.01) = 0.01
PE(1, 5) = cos(1 / 10000^0.5) = cos(0.01) = 0.9999
PE(1, 6) = sin(1 / 10000^0.75) = sin(0.00056) = 0.00056
PE(1, 7) = cos(1 / 10000^0.75) = cos(0.00056) = 0.9999

PE(pos=1) = [0.841, 0.540, 0.056, 0.998, 0.01, 0.9999, 0.00056, 0.9999]
```

### KYU Sine/Cosine?

```
Reason 1: Unique encoding for each position
───────────────────────────────────────────
Each position gets a different pattern of values.

Reason 2: Relative position learning
────────────────────────────────────
For any fixed offset k:
  PE(pos + k) can be written as linear function of PE(pos)

Mathematical property:
  sin(a + b) = sin(a)cos(b) + cos(a)sin(b)
  cos(a + b) = cos(a)cos(b) - sin(a)sin(b)

This means model can easily learn:
  "Word at pos+2 relative to word at pos"

Reason 3: Bounded values
────────────────────────
sin and cos are always between -1 and 1
No exploding values!

Reason 4: Extrapolation
───────────────────────
Can handle longer sequences than seen in training!
(Unlike learned positional embeddings)
```

### Visual Pattern:

```
Position vs Dimension heatmap:

Dimension→  0    1    2    3    4    5    6    7
Position 0  [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
Position 1  [0.8, 0.5, 0.1, 1.0, 0.0, 1.0, 0.0, 1.0]
Position 2  [0.9, -0.4, 0.1, 1.0, 0.0, 1.0, 0.0, 1.0]
Position 3  [0.1, -1.0, 0.2, 1.0, 0.0, 1.0, 0.0, 1.0]
...

Pattern:
- Low dimensions (0,1): Fast oscillation (high frequency)
- High dimensions (6,7): Slow oscillation (low frequency)
- Creates unique "fingerprint" for each position
```

### How to Add to Embeddings:

```
Sentence: "I love coding"

Word Embeddings (learned):
  E_I      = [0.2, 0.5, -0.1, ..., 0.3]  (512 dims)
  E_love   = [0.8, -0.2, 0.4, ..., 0.1]  (512 dims)
  E_coding = [-0.1, 0.6, 0.2, ..., 0.7]  (512 dims)

Positional Encodings (fixed):
  PE_0 = [0, 1, 0, 1, ..., 0.99]  (position 0)
  PE_1 = [0.84, 0.54, 0.05, ..., 0.99]  (position 1)
  PE_2 = [0.91, -0.42, 0.11, ..., 0.99]  (position 2)

Final Input = Embedding + Positional Encoding:
  Input_I      = E_I + PE_0      = [0.2+0, 0.5+1, -0.1+0, ...]
  Input_love   = E_love + PE_1   = [0.8+0.84, -0.2+0.54, ...]
  Input_coding = E_coding + PE_2 = [-0.1+0.91, 0.6-0.42, ...]
```

### Implementation Pseudocode:

```
class PositionalEncoding:
    def __init__(d_model=512, max_len=5000):
        # Create matrix of shape (max_len, d_model)
        pe = zeros(max_len, d_model)

        # Position indices: [0, 1, 2, ..., max_len-1]
        position = arange(0, max_len).unsqueeze(1)  # (max_len, 1)

        # Dimension indices for sin: [0, 2, 4, ..., d_model-2]
        # Create division term: 10000^(2i/d_model)
        div_term = exp(arange(0, d_model, 2) * (-log(10000.0) / d_model))

        # Apply sin to even indices
        pe[:, 0::2] = sin(position * div_term)

        # Apply cos to odd indices
        pe[:, 1::2] = cos(position * div_term)

        # Add batch dimension
        pe = pe.unsqueeze(0)  # (1, max_len, d_model)

        # Register as buffer (not a parameter, but saved with model)
        register_buffer('pe', pe)

    def forward(x):
        # x shape: (batch, seq_len, d_model)
        seq_len = x.shape[1]

        # Add positional encoding (broadcasts over batch)
        x = x + pe[:, :seq_len, :]

        return x
```

---

# STEP 4: POSITION-WISE FEED-FORWARD NETWORK

## KYA Hai Yeh?

Ek simple neural network jo har position pe independently apply hota hai. 2 linear layers with ReLU activation.

## KYU Chahiye?

**Problem:** Attention sirf information mix karta hai, transform nahi karta.

**Analogy:**
```
Attention = Meeting mein sab ki baat sunna (information gathering)
FFN = Apna decision banana based on gathered info (processing)

Attention captures: "Kaun kaun relevant hai?"
FFN processes: "Ab in relevant info ko kaise use karein?"
```

**Mathematical Need:**
```
Attention is LINEAR (weighted sum)
FFN adds NON-LINEARITY (ReLU)

Without FFN: Model is just linear transformations
With FFN: Model can learn complex patterns
```

## KAISE Kaam Karta Hai?

### Formula:
```
FFN(x) = max(0, xW1 + b1)W2 + b2

Or breaking it down:
  hidden = ReLU(x @ W1 + b1)
  output = hidden @ W2 + b2
```

### Dimensions:
```
d_model = 512 (input/output dimension)
d_ff = 2048 (hidden layer dimension = 4 × d_model)
```

### Step-by-Step:

```
Input: x = [0.1, 0.2, -0.3, ..., 0.5]  (512 dimensions)

Step 1: First Linear Layer (Expand)
───────────────────────────────────
hidden = x @ W1 + b1

W1 shape: (512, 2048)
b1 shape: (2048,)

Result: (512,) @ (512, 2048) + (2048,) = (2048,)
hidden = [0.5, -0.3, 0.8, ..., -0.1]  (2048 dimensions)

Why expand? More parameters = more capacity to learn!
```

```
Step 2: ReLU Activation
───────────────────────
ReLU(x) = max(0, x)

hidden = [0.5, -0.3, 0.8, 1.2, -0.1, ...]

After ReLU:
hidden = [0.5, 0, 0.8, 1.2, 0, ...]

Negative values become 0!
This introduces NON-LINEARITY.
```

```
Step 3: Second Linear Layer (Compress)
──────────────────────────────────────
output = hidden @ W2 + b2

W2 shape: (2048, 512)
b2 shape: (512,)

Result: (2048,) @ (2048, 512) + (512,) = (512,)
output = [0.3, -0.1, 0.6, ..., 0.2]  (512 dimensions)

Back to original dimension!
```

### Why This Architecture?

```
1. Expand then Contract:
   512 → 2048 → 512

   Think of it as:
   - Expand: Break info into many features (2048 neurons can detect 2048 patterns)
   - Contract: Combine useful features back

2. ReLU in middle:
   - Adds non-linearity
   - Creates sparsity (many zeros)
   - Allows different neurons to specialize

3. Position-wise:
   - Same FFN applied to EACH position independently
   - No interaction between positions here (attention did that)
   - Like applying same function to each word
```

### Visual:

```
Input x (512)
     │
     ▼
┌─────────────┐
│ Linear      │  W1: (512, 2048)
│ 512 → 2048  │
└─────────────┘
     │
     ▼
┌─────────────┐
│   ReLU      │  max(0, x)
└─────────────┘
     │
     ▼
┌─────────────┐
│ Linear      │  W2: (2048, 512)
│ 2048 → 512  │
└─────────────┘
     │
     ▼
Output (512)
```

### Implementation Pseudocode:

```
class FeedForward:
    def __init__(d_model=512, d_ff=2048):
        self.linear1 = Linear(d_model, d_ff)
        self.linear2 = Linear(d_ff, d_model)
        self.relu = ReLU()

    def forward(x):
        # x shape: (batch, seq_len, d_model)

        hidden = self.linear1(x)    # (batch, seq_len, d_ff)
        hidden = self.relu(hidden)  # (batch, seq_len, d_ff)
        output = self.linear2(hidden)  # (batch, seq_len, d_model)

        return output
```

---

# STEP 5: LAYER NORMALIZATION & RESIDUAL CONNECTION

## KYA Hai Yeh?

**Residual Connection:** Input ko directly output mein add karna (skip connection)
**Layer Normalization:** Values ko normalize karna (mean=0, variance=1)

## KYU Chahiye?

### Residual Connection KYU?

**Problem:** Deep networks mein gradient vanish ho jaata hai.

```
Without Residual (Deep network):
  Layer 1 → Layer 2 → Layer 3 → ... → Layer 20

  Gradient flow:
  ← 0.001 ← 0.01 ← 0.1 ← ... ← 1.0

  By the time gradient reaches early layers, it's almost 0!
  Early layers don't learn!
```

```
With Residual:
  Input ─────────────────────────────┐
    │                                 │
    ▼                                 │
  Layer 1                             │
    │                                 │
    ▼                                 │
  Output = Layer(Input) + Input  ◄───┘

  Gradient can flow directly through the "+" operation!
  Even if layer gradient is small, input gradient flows through.
```

**Analogy:**
```
Without Residual = Telephone game (Chinese whispers)
  Person 1 → Person 2 → ... → Person 20
  Original message gets distorted!

With Residual = Direct hotline + Telephone game
  Even if telephone game fails, direct hotline carries the message.
```

### Layer Normalization KYU?

**Problem:** During training, layer inputs' distribution keeps changing (internal covariate shift)

```
Without Normalization:
  Epoch 1: Input values range [-100, 100]
  Epoch 2: Input values range [-500, 500]
  Epoch 3: Input values range [-10, 10]

  Network constantly adjusting to different scales!
  Training becomes unstable.
```

```
With Layer Normalization:
  Every input normalized to mean=0, variance=1
  Stable input distribution
  Faster, more stable training!
```

## KAISE Kaam Karta Hai?

### Residual Connection:

```
Formula:
  output = x + Sublayer(x)

Example:
  x = [0.2, 0.5, -0.3, 0.1]  (input)
  Sublayer(x) = [0.1, -0.2, 0.4, 0.3]  (attention or FFN output)

  output = [0.2+0.1, 0.5-0.2, -0.3+0.4, 0.1+0.3]
         = [0.3, 0.3, 0.1, 0.4]
```

### Layer Normalization:

```
Formula:
  LayerNorm(x) = γ * (x - μ) / √(σ² + ε) + β

Where:
  μ = mean of x (across features)
  σ² = variance of x (across features)
  ε = small constant for numerical stability (1e-6)
  γ, β = learnable parameters (scale and shift)
```

**Step-by-Step Example:**

```
Input x = [1.0, 2.0, 3.0, 4.0]

Step 1: Calculate mean (μ)
─────────────────────────
μ = (1 + 2 + 3 + 4) / 4 = 2.5

Step 2: Calculate variance (σ²)
───────────────────────────────
σ² = [(1-2.5)² + (2-2.5)² + (3-2.5)² + (4-2.5)²] / 4
   = [2.25 + 0.25 + 0.25 + 2.25] / 4
   = 5.0 / 4
   = 1.25

Step 3: Normalize
─────────────────
x_norm = (x - μ) / √(σ² + ε)
       = (x - 2.5) / √1.25
       = (x - 2.5) / 1.118

x_norm[0] = (1.0 - 2.5) / 1.118 = -1.34
x_norm[1] = (2.0 - 2.5) / 1.118 = -0.45
x_norm[2] = (3.0 - 2.5) / 1.118 = 0.45
x_norm[3] = (4.0 - 2.5) / 1.118 = 1.34

x_norm = [-1.34, -0.45, 0.45, 1.34]

Verify: mean ≈ 0, variance ≈ 1 ✓

Step 4: Scale and Shift (learnable)
───────────────────────────────────
If γ = [1, 1, 1, 1] and β = [0, 0, 0, 0] (initial values):
  output = γ * x_norm + β = x_norm

If γ = [2, 2, 2, 2] and β = [1, 1, 1, 1] (learned values):
  output = 2 * [-1.34, -0.45, 0.45, 1.34] + 1
         = [-1.68, 0.1, 1.9, 3.68]
```

### Combined: Add & Norm

```
In Transformer:
  output = LayerNorm(x + Sublayer(x))

Example flow:
  x = [0.2, 0.5, -0.3, 0.1]                 # Input
  sublayer_out = Attention(x) = [0.1, -0.2, 0.4, 0.3]  # Sublayer
  residual = x + sublayer_out = [0.3, 0.3, 0.1, 0.4]   # Add
  output = LayerNorm(residual)              # Normalize
```

### Visual in Transformer:

```
        Input x
           │
           ├──────────────────┐
           │                  │
           ▼                  │
    ┌──────────────┐          │
    │  Sublayer    │          │
    │ (Attention   │          │
    │  or FFN)     │          │
    └──────┬───────┘          │
           │                  │
           ▼                  │
    ┌──────────────┐          │
    │     Add      │◄─────────┘  (Residual Connection)
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  LayerNorm   │
    └──────┬───────┘
           │
           ▼
        Output
```

### Implementation Pseudocode:

```
class SublayerConnection:
    def __init__(d_model=512, dropout=0.1):
        self.layer_norm = LayerNorm(d_model)
        self.dropout = Dropout(dropout)

    def forward(x, sublayer):
        # sublayer is either Attention or FeedForward

        # Sublayer processing
        sublayer_output = sublayer(x)

        # Dropout for regularization
        sublayer_output = self.dropout(sublayer_output)

        # Residual connection + Layer Norm
        output = self.layer_norm(x + sublayer_output)

        return output
```

---

# STEP 6: EMBEDDINGS

## KYA Hai Yeh?

Embedding words (tokens) ko dense vectors mein convert karta hai.

## KYU Chahiye?

**Problem:** Neural networks numbers samajhte hain, words nahi!

```
Computer samajhta hai: [0.2, -0.5, 0.8, ...]
Computer nahi samajhta: "love"

We need to convert words → numbers (vectors)
```

**Why not One-Hot Encoding?**

```
Vocabulary size = 50,000 words

One-Hot for "love" (word index 1234):
  [0, 0, 0, ..., 1, ..., 0, 0]  (50,000 dimensions!)
  Only one '1' at position 1234

Problems:
1. Very high dimensional (50,000!)
2. All words equally different (no similarity)
3. "king" and "queen" as different as "king" and "banana"
```

**Embedding Solution:**

```
Embedding for "love":
  [0.2, -0.5, 0.8, 0.1, ...]  (512 dimensions only!)

Benefits:
1. Lower dimensional (512 vs 50,000)
2. Similar words have similar vectors:
   king  = [0.9, 0.1, 0.8, ...]
   queen = [0.85, 0.15, 0.75, ...]  (similar!)
   banana = [0.1, 0.9, 0.2, ...]    (different!)
```

## KAISE Kaam Karta Hai?

### Embedding Matrix:

```
Vocabulary: {<pad>: 0, <unk>: 1, "I": 2, "love": 3, "coding": 4, ...}
Vocab size = 50,000
Embedding dim = 512

Embedding Matrix shape: (50,000, 512)

Row 0: [0.0, 0.0, ..., 0.0]      # <pad> token
Row 1: [0.1, -0.2, ..., 0.3]    # <unk> token
Row 2: [0.2, 0.5, ..., -0.1]    # "I"
Row 3: [0.8, -0.3, ..., 0.6]    # "love"
Row 4: [-0.1, 0.7, ..., 0.4]    # "coding"
...
```

### Lookup Process:

```
Sentence: "I love coding"
Token IDs: [2, 3, 4]

Embedding lookup (just matrix indexing!):
  E[2] = [0.2, 0.5, ..., -0.1]    # "I"
  E[3] = [0.8, -0.3, ..., 0.6]    # "love"
  E[4] = [-0.1, 0.7, ..., 0.4]    # "coding"

Output shape: (3, 512)
```

### Scaling:

```
In Transformer, embeddings are scaled by √d_model:

scaled_embedding = embedding * √512 = embedding * 22.6

KYU?
- Positional encodings have values in range [-1, 1]
- Embeddings learned values might be small
- Scaling brings them to similar magnitude
- Prevents positional encoding from dominating
```

### Weight Sharing:

```
Transformer shares weights between:
1. Input embedding (encoder)
2. Output embedding (decoder)
3. Pre-softmax linear layer

Benefits:
- Fewer parameters (3x reduction in embedding params)
- Better generalization
- Semantic consistency between input and output
```

### Implementation Pseudocode:

```
class Embeddings:
    def __init__(vocab_size=50000, d_model=512):
        self.embedding = Embedding(vocab_size, d_model)
        self.d_model = d_model

    def forward(x):
        # x shape: (batch, seq_len) - token IDs

        # Lookup embeddings
        embedded = self.embedding(x)  # (batch, seq_len, d_model)

        # Scale by sqrt(d_model)
        scaled = embedded * sqrt(self.d_model)

        return scaled
```

---

## DEEP DIVE: 512 Numbers Kya Hain? (Detailed Explanation)

### Simple Answer:

```
"love" → [0.2, -0.5, 0.8, 0.1, -0.3, ..., 0.6]
          ↑     ↑     ↑    ↑    ↑         ↑
          1st   2nd   3rd  4th  5th  ... 512th number

Yeh 512 numbers word ka "MEANING" represent karte hain in numerical form!
```

### 1. Initially: RANDOM Hote Hain!

```
Training START pe:

"love"   → [0.234, -0.567, 0.891, ...]  ← Random initialized!
"hate"   → [0.123, 0.456, -0.789, ...]  ← Random initialized!
"coding" → [-0.345, 0.678, 0.012, ...]  ← Random initialized!

Computer ko initially kuch nahi pata ki "love" kya hai!
Sab random numbers se start hota hai.
```

### 2. Training Ke Baad: MEANINGFUL Ho Jaate Hain!

```
Training ke baad (millions of examples dekhne ke baad):

"love"   → [0.9, 0.1, 0.8, 0.7, ...]
"like"   → [0.85, 0.15, 0.75, 0.65, ...]  ← Similar to "love"!
"hate"   → [-0.8, 0.2, -0.7, 0.1, ...]    ← Opposite to "love"!

Model LEARN kar leta hai ki:
- Similar words → Similar vectors
- Opposite words → Opposite vectors
```

### KYU 512 Numbers? Ek Number Enough Nahi Hai!

```
Agar sirf 1 number se represent karte:
  "love" = 5
  "like" = 4.8
  "hate" = 1
  "dog"  = 7
  "cat"  = 6.5

Problem:
  - "love" (5) aur "dog" (7) close hain
  - But unka koi relation nahi!
  - 1 dimension mein sab kuch capture nahi ho sakta
```

### 512 Numbers = 512 Different Aspects!

```
Imagine each dimension captures something:

Dimension 1: Positive vs Negative emotion
  "love" = +0.9 (positive)
  "hate" = -0.8 (negative)

Dimension 2: Human vs Non-human
  "love" = +0.1 (human emotion)
  "dog"  = -0.7 (non-human)

Dimension 3: Action vs State
  "run"  = +0.8 (action)
  "love" = -0.3 (state/emotion)

Dimension 4: Concrete vs Abstract
  "table" = +0.9 (concrete)
  "love"  = -0.8 (abstract)

... 508 more dimensions for other subtle features!
```

### Famous Example: King - Man + Woman = Queen

```
king  = [0.9,  0.8,  0.7, -0.2, ...]
man   = [0.1,  0.9,  0.1,  0.0, ...]
woman = [0.1,  0.1,  0.9,  0.0, ...]

king - man + woman = ?

[0.9, 0.8, 0.7, -0.2] - [0.1, 0.9, 0.1, 0.0] + [0.1, 0.1, 0.9, 0.0]
= [0.9-0.1+0.1, 0.8-0.9+0.1, 0.7-0.1+0.9, -0.2-0.0+0.0]
= [0.9, 0.0, 1.5, -0.2]
≈ queen embedding!

This works because:
- "king" - "man" = "royalty" concept
- "royalty" + "woman" = "queen"

512 dimensions allow such rich relationships!
```

### Embedding Matrix - Complete Picture

```
Vocabulary size = 50,000 words
Embedding dimension = 512

Embedding Matrix shape: (50000, 512)

                    512 dimensions →
               ┌─────────────────────────────────────┐
    Word 0     │ 0.00  0.00  0.00  ...  0.00  0.00   │  ← <PAD>
    Word 1     │ 0.12 -0.34  0.56  ... -0.78  0.90   │  ← <UNK>
    Word 2     │ 0.23  0.45 -0.67  ...  0.89 -0.12   │  ← "the"
    Word 3     │ 0.34 -0.56  0.78  ... -0.90  0.23   │  ← "a"
       ↓       │  ...  ...  ...   ...  ...  ...     │
    Word 1234  │ 0.20 -0.50  0.80  ...  0.10  0.30   │  ← "love"
       ↓       │  ...  ...  ...   ...  ...  ...     │
    Word 49999 │ 0.11 -0.22  0.33  ... -0.44  0.55   │  ← "xyz"
               └─────────────────────────────────────┘

Total parameters = 50,000 × 512 = 25.6 Million numbers!
Sab LEARNABLE hain - training mein update hote hain!
```

### Step-by-Step: Word → Numbers

```
Input: "I love coding"

Step 1: Tokenization (Word → ID)
────────────────────────────────
Vocabulary lookup:
  "I"      → ID 101
  "love"   → ID 1234
  "coding" → ID 5678

Result: [101, 1234, 5678]


Step 2: Embedding Lookup (ID → Vector)
──────────────────────────────────────
Embedding matrix se row select karo:

  ID 101  → Row 101  → [0.1, 0.2, -0.3, ..., 0.5]   (512 numbers)
  ID 1234 → Row 1234 → [0.2, -0.5, 0.8, ..., 0.3]   (512 numbers)
  ID 5678 → Row 5678 → [-0.1, 0.7, 0.4, ..., 0.2]   (512 numbers)

Result shape: (3, 512) - 3 words, each with 512 numbers
```

### Numbers Ka Range

```
Typically embeddings are:
- Mean ≈ 0
- Values between -2 to +2 (mostly)
- Learned during training

Example values:
  [0.234, -0.567, 0.891, -1.234, 0.012, -0.345, ...]
   ↑       ↑       ↑       ↑       ↑       ↑
  Small  Small  Small   Larger  Small   Small
  positive negative positive negative positive negative
```

### Training Mein Kaise Update Hote Hain?

```
BEFORE TRAINING (Random):
─────────────────────────
"good" = [0.123, -0.456, 0.789, ...]
"bad"  = [0.234, -0.567, 0.890, ...]
Distance: Could be anything!


TRAINING PROCESS:
─────────────────
Model sees: "The movie was good" → Positive review
Model sees: "The movie was bad"  → Negative review

Backpropagation adjusts embeddings so that:
- "good" moves towards positive sentiment region
- "bad" moves towards negative sentiment region


AFTER TRAINING (Meaningful):
────────────────────────────
"good"      = [0.9, 0.8, 0.7, ...]
"great"     = [0.85, 0.82, 0.68, ...]  ← Close to "good"
"excellent" = [0.88, 0.79, 0.72, ...]  ← Close to "good"
"bad"       = [-0.8, -0.7, 0.1, ...]   ← Far from "good"

Similar words cluster together!
```

### Visual: 2D Simplified View

```
Imagine we reduce 512D to 2D for visualization:

        Positive ↑
                 │
    "excellent"  │  "amazing"
         ★       │      ★
    "good" ★     │
                 │    "love" ★
    ─────────────┼─────────────→ Emotion
                 │
         "bad" ★ │
                 │  "hate" ★
    "terrible" ★ │
                 │
        Negative ↓

In reality, this is 512-dimensional space!
But the concept is same - similar words are close.
```

### Numerical Example (Simplified 4D)

```python
# Simplified example with 4 dimensions instead of 512

embeddings = {
    "king":  [0.9,  0.8,  0.2, -0.1],
    "queen": [0.9,  0.1,  0.9, -0.1],
    "man":   [0.2,  0.9,  0.1,  0.0],
    "woman": [0.2,  0.1,  0.9,  0.0],
    "apple": [-0.5, 0.0,  0.0,  0.8],
    "banana":[-0.4, 0.0,  0.0,  0.7],
}

# Dimension meanings (learned, not predefined):
# Dim 0: Royalty (high = royal)
# Dim 1: Male (high = male)
# Dim 2: Female (high = female)
# Dim 3: Fruit (high = fruit)

# king  = high royalty, high male, low female, not fruit
# queen = high royalty, low male, high female, not fruit
# apple = not royal, neutral gender, is fruit
```

### Summary Table - 512 Numbers

| Question | Answer |
|----------|--------|
| **512 numbers kya hain?** | Word ka meaning in numerical form |
| **Initially random hain?** | Haan! Training se pehle random |
| **Kaise meaningful bante hain?** | Training mein backpropagation se learn hote hain |
| **Kyun 512?** | More dimensions = more nuances capture |
| **Values ka range?** | Typically -2 to +2 |
| **Total parameters?** | vocab_size × 512 (e.g., 50000 × 512 = 25.6M) |
| **Learnable hain?** | Haan! Training mein update hote hain |

### PyTorch Code Example

```python
import torch
import torch.nn as nn

# Create embedding layer
vocab_size = 50000
embedding_dim = 512
embedding = nn.Embedding(vocab_size, embedding_dim)

# Check initial values (RANDOM!)
print(embedding.weight[1234])  # Random numbers
# Output: tensor([0.0123, -0.0456, 0.0789, ..., 0.0234])

# After training, these will be MEANINGFUL!

# Lookup example
word_ids = torch.tensor([101, 1234, 5678])  # "I", "love", "coding"
vectors = embedding(word_ids)
print(vectors.shape)  # torch.Size([3, 512])
```

---

# STEP 7: ENCODER LAYER

## KYA Hai Yeh?

Ek complete encoder layer jo sabko combine karta hai:
1. Multi-Head Self-Attention
2. Add & Norm
3. Feed-Forward Network
4. Add & Norm

## KYU Chahiye?

**Each component ka role:**

```
1. Self-Attention: Words ke beech relationships samjho
   "The cat sat" → "cat" learns it's connected to "sat"

2. Add & Norm (1st): Stabilize attention output

3. Feed-Forward: Process the gathered information
   Transform representations

4. Add & Norm (2nd): Stabilize FFN output
```

## KAISE Kaam Karta Hai?

### Complete Flow:

```
Input x: (batch=32, seq_len=10, d_model=512)

┌─────────────────────────────────────────────────────────────┐
│                    ENCODER LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  x ─────────────────────────────┐                           │
│  │                              │                           │
│  ▼                              │                           │
│  ┌────────────────────────┐     │                           │
│  │ Multi-Head             │     │                           │
│  │ Self-Attention         │     │                           │
│  │ Q=x, K=x, V=x          │     │                           │
│  └──────────┬─────────────┘     │                           │
│             │                   │                           │
│             ▼                   │                           │
│  ┌────────────────────────┐     │                           │
│  │      Add & Norm        │◄────┘  (Residual)               │
│  └──────────┬─────────────┘                                 │
│             │                                               │
│             ├─────────────────────────────┐                 │
│             │                             │                 │
│             ▼                             │                 │
│  ┌────────────────────────┐               │                 │
│  │   Feed-Forward         │               │                 │
│  │   Network              │               │                 │
│  └──────────┬─────────────┘               │                 │
│             │                             │                 │
│             ▼                             │                 │
│  ┌────────────────────────┐               │                 │
│  │      Add & Norm        │◄──────────────┘  (Residual)     │
│  └──────────┬─────────────┘                                 │
│             │                                               │
│             ▼                                               │
│          Output                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Output shape: (batch=32, seq_len=10, d_model=512)  # Same as input!
```

### Step-by-Step Example:

```
Input: "I love coding" embeddings
x = [[0.2, 0.5, ...],    # "I"
     [0.8, -0.3, ...],   # "love"
     [-0.1, 0.7, ...]]   # "coding"
Shape: (1, 3, 512)

Step 1: Self-Attention
──────────────────────
Q = K = V = x (all from same source - that's why "self")

attention_output = MultiHeadAttention(Q, K, V)

What happens:
- "I" attends to ["I", "love", "coding"]
- "love" attends to ["I", "love", "coding"]
- "coding" attends to ["I", "love", "coding"]

Each word gets new representation incorporating context!

attention_output shape: (1, 3, 512)
```

```
Step 2: Add & Norm (1st)
────────────────────────
residual_1 = x + attention_output
norm_1 = LayerNorm(residual_1)

Shape: (1, 3, 512)
```

```
Step 3: Feed-Forward
────────────────────
ffn_output = FFN(norm_1)
           = ReLU(norm_1 @ W1 + b1) @ W2 + b2

Each position processed independently:
  ffn("I")      = FFN([0.3, 0.4, ...])
  ffn("love")   = FFN([0.5, 0.2, ...])
  ffn("coding") = FFN([0.1, 0.6, ...])

Shape: (1, 3, 512)
```

```
Step 4: Add & Norm (2nd)
────────────────────────
residual_2 = norm_1 + ffn_output
output = LayerNorm(residual_2)

Final output shape: (1, 3, 512)
```

### Implementation Pseudocode:

```
class EncoderLayer:
    def __init__(d_model=512, h=8, d_ff=2048, dropout=0.1):
        self.self_attention = MultiHeadAttention(d_model, h)
        self.feed_forward = FeedForward(d_model, d_ff)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.dropout = Dropout(dropout)

    def forward(x, mask=None):
        # x shape: (batch, seq_len, d_model)

        # Self-Attention + Add & Norm
        attn_output = self.self_attention(Q=x, K=x, V=x, mask=mask)
        attn_output = self.dropout(attn_output)
        x = self.norm1(x + attn_output)  # Residual + Norm

        # Feed-Forward + Add & Norm
        ffn_output = self.feed_forward(x)
        ffn_output = self.dropout(ffn_output)
        x = self.norm2(x + ffn_output)  # Residual + Norm

        return x
```

### Full Encoder (Stack of N=6 Layers):

```
class Encoder:
    def __init__(N=6, d_model=512, h=8, d_ff=2048):
        self.layers = [EncoderLayer(d_model, h, d_ff) for _ in range(N)]
        self.norm = LayerNorm(d_model)

    def forward(x, mask=None):
        # x shape: (batch, seq_len, d_model)

        for layer in self.layers:
            x = layer(x, mask)

        # Final normalization
        x = self.norm(x)

        return x  # This is "memory" for decoder

Flow:
  Input → Layer1 → Layer2 → Layer3 → Layer4 → Layer5 → Layer6 → Output

  Each layer refines the representations!
```

---

# STEP 8: DECODER LAYER

## KYA Hai Yeh?

Decoder layer encoder se thoda different hai - isme **3 sub-layers** hain:
1. **Masked** Multi-Head Self-Attention
2. Multi-Head Cross-Attention (Encoder-Decoder Attention)
3. Feed-Forward Network

## KYU Chahiye?

### Masked Self-Attention KYU?

```
Problem: During training, decoder has access to full target sequence.
But during inference, it generates one token at a time!

Training target: "Main tumse pyaar karta hoon"

Without mask:
  When predicting "pyaar", model can see "karta hoon" (CHEATING!)

With mask:
  When predicting "pyaar", model can only see "Main tumse"
  Fair game - same as inference time!
```

### Cross-Attention KYU?

```
Decoder needs to look at source sentence (encoder output)!

Example:
  Source: "I love coding"
  Target: "Main coding pasand karta hoon"

When generating "coding" in Hindi:
  - Decoder looks at encoder output
  - Finds "coding" in English
  - Uses that information to generate

Cross-attention connects decoder to encoder.
```

## KAISE Kaam Karta Hai?

### Masking Mechanism:

```
Target: "Main tumse pyaar karta"

Mask matrix (lower triangular):
              Main  tumse  pyaar  karta
    Main    [  1      0      0      0  ]
    tumse   [  1      1      0      0  ]
    pyaar   [  1      1      1      0  ]
    karta   [  1      1      1      1  ]

1 = can attend
0 = cannot attend (masked)

When computing attention for "pyaar":
  - Can attend to: Main (1), tumse (1), pyaar (1)
  - Cannot attend to: karta (0) - it's in the future!
```

### How Mask is Applied:

```
Attention scores before mask:
              Main  tumse  pyaar  karta
    pyaar   [ 0.5    0.8    1.2    0.9  ]

Mask for "pyaar" row:
            [  1      1      1      0  ]

After masking (0 positions get -infinity):
              Main  tumse  pyaar  karta
    pyaar   [ 0.5    0.8    1.2   -inf  ]

After softmax:
  exp(0.5) = 1.65
  exp(0.8) = 2.23
  exp(1.2) = 3.32
  exp(-inf) = 0  ← Future position gets ZERO attention!

  Sum = 7.2
  Weights = [0.23, 0.31, 0.46, 0.00]

  "karta" gets 0% attention - effectively invisible!
```

### Cross-Attention (Encoder-Decoder):

```
In cross-attention:
  Q comes from DECODER (previous layer output)
  K, V come from ENCODER (encoder output / memory)

Example:
  Encoder output (memory) for "I love coding":
    M = [[enc_I], [enc_love], [enc_coding]]

  Decoder state for generating position 3:
    D = [[dec_Main], [dec_tumse], [dec_?]]

  Cross-attention for position 3:
    Q = dec_? (query: "What should I generate?")
    K = [enc_I, enc_love, enc_coding] (keys from encoder)
    V = [enc_I, enc_love, enc_coding] (values from encoder)

  Attention weights might be:
    [0.1, 0.2, 0.7]  → Heavily attending to "coding"!

  Output = 0.1*enc_I + 0.2*enc_love + 0.7*enc_coding
```

### Complete Decoder Layer Flow:

```
┌─────────────────────────────────────────────────────────────┐
│                    DECODER LAYER                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  x (from previous decoder layer or output embedding)        │
│  │                                                          │
│  ├──────────────────────────────┐                           │
│  │                              │                           │
│  ▼                              │                           │
│  ┌────────────────────────┐     │                           │
│  │ MASKED Multi-Head      │     │                           │
│  │ Self-Attention         │     │                           │
│  │ Q=x, K=x, V=x          │     │                           │
│  │ + Causal Mask          │     │                           │
│  └──────────┬─────────────┘     │                           │
│             │                   │                           │
│             ▼                   │                           │
│  ┌────────────────────────┐     │                           │
│  │      Add & Norm        │◄────┘                           │
│  └──────────┬─────────────┘                                 │
│             │                                               │
│             ├──────────────────────────────┐                │
│             │                              │                │
│             ▼                              │                │
│  ┌────────────────────────┐                │                │
│  │ Multi-Head             │                │                │
│  │ Cross-Attention        │◄── memory      │                │
│  │ Q=x, K=memory, V=memory│    (encoder    │                │
│  └──────────┬─────────────┘     output)    │                │
│             │                              │                │
│             ▼                              │                │
│  ┌────────────────────────┐                │                │
│  │      Add & Norm        │◄───────────────┘                │
│  └──────────┬─────────────┘                                 │
│             │                                               │
│             ├──────────────────────────────┐                │
│             │                              │                │
│             ▼                              │                │
│  ┌────────────────────────┐                │                │
│  │   Feed-Forward         │                │                │
│  │   Network              │                │                │
│  └──────────┬─────────────┘                │                │
│             │                              │                │
│             ▼                              │                │
│  ┌────────────────────────┐                │                │
│  │      Add & Norm        │◄───────────────┘                │
│  └──────────┬─────────────┘                                 │
│             │                                               │
│             ▼                                               │
│          Output                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Implementation Pseudocode:

```
class DecoderLayer:
    def __init__(d_model=512, h=8, d_ff=2048, dropout=0.1):
        self.self_attention = MultiHeadAttention(d_model, h)
        self.cross_attention = MultiHeadAttention(d_model, h)
        self.feed_forward = FeedForward(d_model, d_ff)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.norm3 = LayerNorm(d_model)
        self.dropout = Dropout(dropout)

    def forward(x, memory, src_mask=None, tgt_mask=None):
        # x shape: (batch, tgt_seq_len, d_model)
        # memory shape: (batch, src_seq_len, d_model)

        # 1. Masked Self-Attention
        self_attn_output = self.self_attention(
            Q=x, K=x, V=x, mask=tgt_mask  # tgt_mask is causal mask!
        )
        self_attn_output = self.dropout(self_attn_output)
        x = self.norm1(x + self_attn_output)

        # 2. Cross-Attention (Encoder-Decoder)
        cross_attn_output = self.cross_attention(
            Q=x, K=memory, V=memory, mask=src_mask
        )
        cross_attn_output = self.dropout(cross_attn_output)
        x = self.norm2(x + cross_attn_output)

        # 3. Feed-Forward
        ffn_output = self.feed_forward(x)
        ffn_output = self.dropout(ffn_output)
        x = self.norm3(x + ffn_output)

        return x


def create_causal_mask(size):
    # Create lower triangular mask
    mask = torch.tril(torch.ones(size, size))
    return mask

# Example:
# create_causal_mask(4) =
# [[1, 0, 0, 0],
#  [1, 1, 0, 0],
#  [1, 1, 1, 0],
#  [1, 1, 1, 1]]
```

---

# STEP 9: COMPLETE TRANSFORMER

## KYA Hai Yeh?

Complete Transformer = Encoder + Decoder + Embeddings + Final Linear Layer

## Complete Architecture:

```
┌─────────────────────────────────────────────────────────────────────┐
│                         TRANSFORMER                                 │
├────────────────────────────────┬────────────────────────────────────┤
│          ENCODER               │            DECODER                 │
├────────────────────────────────┼────────────────────────────────────┤
│                                │                                    │
│                                │         Output Probabilities       │
│                                │                ↑                   │
│                                │           ┌─────────┐              │
│                                │           │ Softmax │              │
│                                │           └────┬────┘              │
│                                │                ↑                   │
│                                │           ┌─────────┐              │
│                                │           │ Linear  │              │
│                                │           │(d→vocab)│              │
│                                │           └────┬────┘              │
│                                │                ↑                   │
│   ┌──────────────────────┐     │    ┌──────────────────────┐        │
│   │                      │     │    │                      │        │
│   │   Encoder Layer 6    │     │    │   Decoder Layer 6    │        │
│   │                      │     │    │                      │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │   Encoder Layer 5    │     │    │   Decoder Layer 5    │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │   Encoder Layer 4    │     │    │   Decoder Layer 4    │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │   Encoder Layer 3    │─────┼───►│   Decoder Layer 3    │        │
│   └──────────┬───────────┘  memory  └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │   Encoder Layer 2    │     │    │   Decoder Layer 2    │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │   Encoder Layer 1    │     │    │   Decoder Layer 1    │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │      Add             │     │    │        Add           │        │
│   │ Embedding + PosEnc   │     │    │  Embedding + PosEnc  │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              │                 │               │                    │
│   ┌──────────┴───────────┐     │    ┌──────────┴───────────┐        │
│   │  Input Embedding     │     │    │  Output Embedding    │        │
│   └──────────┬───────────┘     │    └──────────┬───────────┘        │
│              ↑                 │               ↑                    │
│           INPUTS               │       OUTPUTS (shifted right)      │
│       "I love coding"          │       "<s> Main tumse pyaar"       │
│                                │                                    │
└────────────────────────────────┴────────────────────────────────────┘
```

## Training vs Inference:

### Training (Teacher Forcing):

```
Source: "I love coding"
Target: "<s> Main tumse pyaar karta hoon </s>"

Input to Encoder: "I love coding"
Input to Decoder: "<s> Main tumse pyaar karta hoon"  (shifted right)
Expected Output:  "Main tumse pyaar karta hoon </s>" (next token at each position)

Decoder sees FULL target during training (but masked so can't cheat)
This is called "Teacher Forcing"
```

### Inference (Auto-regressive):

```
Source: "I love coding"

Step 1:
  Encoder input: "I love coding"
  Decoder input: "<s>"
  Model predicts: "Main"

Step 2:
  Decoder input: "<s> Main"
  Model predicts: "tumse"

Step 3:
  Decoder input: "<s> Main tumse"
  Model predicts: "pyaar"

... continues until </s> is generated

One token at a time!
```

### Implementation Pseudocode:

```
class Transformer:
    def __init__(
        src_vocab_size=50000,
        tgt_vocab_size=50000,
        d_model=512,
        N=6,
        h=8,
        d_ff=2048,
        dropout=0.1,
        max_len=5000
    ):
        # Embeddings
        self.src_embedding = Embedding(src_vocab_size, d_model)
        self.tgt_embedding = Embedding(tgt_vocab_size, d_model)

        # Positional Encoding
        self.positional_encoding = PositionalEncoding(d_model, max_len)

        # Encoder & Decoder
        self.encoder = Encoder(N, d_model, h, d_ff, dropout)
        self.decoder = Decoder(N, d_model, h, d_ff, dropout)

        # Final Linear Layer
        self.output_linear = Linear(d_model, tgt_vocab_size)

        # Scaling factor
        self.scale = sqrt(d_model)

        # Dropout
        self.dropout = Dropout(dropout)

    def encode(self, src, src_mask):
        # Embed + Scale + PosEnc
        src = self.src_embedding(src) * self.scale
        src = self.positional_encoding(src)
        src = self.dropout(src)

        # Encode
        memory = self.encoder(src, src_mask)
        return memory

    def decode(self, tgt, memory, src_mask, tgt_mask):
        # Embed + Scale + PosEnc
        tgt = self.tgt_embedding(tgt) * self.scale
        tgt = self.positional_encoding(tgt)
        tgt = self.dropout(tgt)

        # Decode
        output = self.decoder(tgt, memory, src_mask, tgt_mask)
        return output

    def forward(self, src, tgt, src_mask, tgt_mask):
        # Encode source
        memory = self.encode(src, src_mask)

        # Decode target
        decoder_output = self.decode(tgt, memory, src_mask, tgt_mask)

        # Project to vocabulary
        logits = self.output_linear(decoder_output)

        return logits  # Shape: (batch, tgt_len, vocab_size)
```

---

# PHASE 3: TRAINING SETUP

## Data Preparation

### Tokenization:

```
Raw text: "I love coding"

Step 1: Tokenize
  - Word-level: ["I", "love", "coding"]
  - BPE/WordPiece: ["I", "lov", "##e", "cod", "##ing"]  (handles rare words!)

Step 2: Convert to IDs
  Vocabulary: {"I": 101, "love": 2034, "coding": 5678, ...}
  Token IDs: [101, 2034, 5678]

Step 3: Add special tokens
  [CLS] I love coding [SEP]
  [101, 102, 2034, 5678, 103]

Step 4: Padding (for batching)
  Batch of 2 sentences:
  "I love coding"     → [101, 2034, 5678, 0, 0]
  "Hello world today" → [201, 302, 403, 504, 0]

  0 = padding token
```

### Batching Strategy:

```
Problem: Different length sentences

Solution: Group similar lengths together

Batch 1: ["I love", "Hi there", "Good morning"]  (short sentences)
Batch 2: ["I love coding so much", "Hello world program"]  (medium)
Batch 3: ["Very long sentence...", "Another long one..."]  (long)

Benefits:
- Less padding = Less computation waste
- More efficient training
```

## Loss Function

### Cross-Entropy Loss:

```
Model output (logits): [2.0, 1.0, 0.5, ...]  (vocab_size probabilities)
True label: 3  (index of correct word)

Step 1: Softmax on logits
  probs = [0.4, 0.25, 0.15, 0.2, ...]

Step 2: Cross-entropy
  loss = -log(probs[3]) = -log(0.2) = 1.61

Lower loss = Model is more confident about correct word
```

### Label Smoothing:

```
Without smoothing:
  Target = [0, 0, 0, 1, 0, 0, ...]  (one-hot)
  Model tries to be 100% confident

With smoothing (epsilon = 0.1):
  Target = [0.02, 0.02, 0.02, 0.92, 0.02, 0.02, ...]
  Model learns to be slightly uncertain

Benefits:
- Prevents overconfidence
- Better generalization
- Higher BLEU scores!
```

### Ignoring Padding:

```
Sentence with padding: "I love [PAD] [PAD]"
Labels: [2034, 5678, 0, 0]

We should NOT compute loss for padding tokens!

Solution: Mask padding in loss computation
  losses = [1.2, 0.8, -, -]  (- = ignored)
  final_loss = (1.2 + 0.8) / 2 = 1.0
```

## Optimizer & Learning Rate

### Adam Optimizer:

```
Parameters:
  β1 = 0.9   (momentum for gradient)
  β2 = 0.98  (momentum for squared gradient)
  ε = 1e-9   (for numerical stability)

Adam adapts learning rate for each parameter!
```

### Warmup + Decay Schedule:

```
Formula:
  lr = d_model^(-0.5) × min(step^(-0.5), step × warmup_steps^(-1.5))

With d_model=512, warmup_steps=4000:

Step 1:    lr = 0.000022  (very small)
Step 100:  lr = 0.00022   (increasing)
Step 1000: lr = 0.0007    (increasing)
Step 4000: lr = 0.001     (peak!)
Step 8000: lr = 0.0007    (decreasing)
Step 16000: lr = 0.0005   (decreasing)
...

Visualization:
  lr
   │        /\
   │       /  \
   │      /    \____
   │     /          \____
   │    /                \____
   └───┴──────────────────────→ steps
       4000
```

**Why Warmup?**

```
Initially:
  - Model parameters random
  - Gradients unreliable
  - Big updates = Unstable training

With warmup:
  - Start with small learning rate
  - Gradually increase as model stabilizes
  - Then decrease for fine-tuning
```

## Regularization

### Dropout:

```
During training:
  Randomly set 10% of neurons to 0

Example:
  Before: [0.5, 0.3, 0.8, 0.2, 0.6]
  After:  [0.5, 0, 0.8, 0.2, 0]  (30% scaled to compensate)

Where to apply:
1. After each attention output
2. After FFN output
3. On embeddings + positional encodings
```

### Training Loop Pseudocode:

```
optimizer = Adam(model.parameters(), lr=1, betas=(0.9, 0.98))
scheduler = WarmupScheduler(optimizer, d_model=512, warmup=4000)
criterion = CrossEntropyLoss(label_smoothing=0.1, ignore_index=PAD_IDX)

for epoch in range(num_epochs):
    for batch in dataloader:
        src, tgt = batch

        # Create masks
        src_mask = create_padding_mask(src)
        tgt_mask = create_causal_mask(tgt.size(1))

        # Forward pass
        optimizer.zero_grad()
        output = model(src, tgt[:, :-1], src_mask, tgt_mask)

        # Compute loss
        loss = criterion(
            output.reshape(-1, vocab_size),
            tgt[:, 1:].reshape(-1)  # Shifted target
        )

        # Backward pass
        loss.backward()

        # Gradient clipping (optional but recommended)
        clip_grad_norm_(model.parameters(), max_norm=1.0)

        # Update weights
        optimizer.step()
        scheduler.step()

        print(f"Loss: {loss.item()}")
```

---

# PHASE 4: INFERENCE

## Greedy Decoding

### KYA Hai?

Har step pe highest probability wala token select karo.

### KAISE Kaam Karta Hai?

```
Source: "I love coding"

Step 1:
  Decoder input: [<s>]
  Model output probabilities for position 1:
    "Main": 0.4, "Mujhe": 0.3, "I": 0.1, ...
  Select highest: "Main"

Step 2:
  Decoder input: [<s>, Main]
  Model output for position 2:
    "ko": 0.35, "tumse": 0.25, "ne": 0.2, ...
  Select highest: "ko"

Step 3:
  Decoder input: [<s>, Main, ko]
  ...

Continue until </s> is generated or max_length reached.

Final output: "Main ko coding pasand hai"
```

### Implementation:

```
def greedy_decode(model, src, max_len=50):
    # Encode source
    memory = model.encode(src)

    # Start with <s> token
    ys = torch.tensor([[START_TOKEN]])

    for i in range(max_len):
        # Create causal mask
        tgt_mask = create_causal_mask(ys.size(1))

        # Decode
        output = model.decode(ys, memory, None, tgt_mask)

        # Get last position logits
        logits = model.output_linear(output[:, -1, :])

        # Get highest probability token
        next_token = logits.argmax(dim=-1, keepdim=True)

        # Append to sequence
        ys = torch.cat([ys, next_token], dim=1)

        # Stop if end token
        if next_token.item() == END_TOKEN:
            break

    return ys
```

## Beam Search

### KYA Hai?

Multiple candidates maintain karo, best final sequence select karo.

### KYU Better Than Greedy?

```
Greedy problem:
  Step 1: "Main" (0.4) selected
  Step 2 given "Main": "ko" (0.35) selected
  Total probability: 0.4 × 0.35 = 0.14

But maybe:
  Step 1: "Mujhe" (0.3)
  Step 2 given "Mujhe": "coding" (0.6)
  Total probability: 0.3 × 0.6 = 0.18  ← Better!

Greedy misses this because it only looks at current step!
```

### KAISE Kaam Karta Hai?

```
Beam size = 3 (keep top 3 candidates)

Step 1:
  All candidates: [<s>]
  Top 3 next tokens: "Main" (0.4), "Mujhe" (0.3), "I" (0.2)

  Beams after step 1:
    Beam 1: [<s>, Main]   score: log(0.4) = -0.92
    Beam 2: [<s>, Mujhe]  score: log(0.3) = -1.20
    Beam 3: [<s>, I]      score: log(0.2) = -1.61

Step 2:
  For each beam, get top 3 next tokens (total 9 candidates)

  From Beam 1 [Main]:
    "ko" (0.35)     → score: -0.92 + log(0.35) = -1.97
    "ne" (0.25)     → score: -0.92 + log(0.25) = -2.31
    "tumse" (0.20)  → score: -0.92 + log(0.20) = -2.53

  From Beam 2 [Mujhe]:
    "coding" (0.60) → score: -1.20 + log(0.60) = -1.71  ← Best!
    "ko" (0.15)     → score: -1.20 + log(0.15) = -3.10
    ...

  From Beam 3 [I]:
    ...

  Keep top 3 from all 9:
    Beam 1: [<s>, Mujhe, coding]  score: -1.71
    Beam 2: [<s>, Main, ko]      score: -1.97
    Beam 3: [<s>, Main, ne]      score: -2.31

Continue until all beams reach </s>

Final: Return beam with highest score!
```

### Length Penalty:

```
Problem: Shorter sequences have higher probability (fewer multiplications)

Solution: Normalize by length

score = log_prob / (length ^ alpha)

alpha = 0.6 (typical value)

Example:
  Sequence 1: "Hi" (length 2), log_prob = -0.5
    Normalized: -0.5 / (2^0.6) = -0.33

  Sequence 2: "Hello there friend" (length 4), log_prob = -1.0
    Normalized: -1.0 / (4^0.6) = -0.44

Without penalty: Sequence 1 wins (shorter = higher prob)
With penalty: Sequence 1 still wins but gap is smaller, longer sequences have a chance!
```

---

# SUMMARY: COMPLETE IMPLEMENTATION CHECKLIST

```
□ Phase 1: Prerequisites
  □ Understand tensors and shapes
  □ Understand matrix multiplication
  □ Understand softmax
  □ Understand dot product

□ Phase 2: Core Components
  □ Scaled Dot-Product Attention
  □ Multi-Head Attention
  □ Positional Encoding
  □ Feed-Forward Network
  □ Layer Normalization + Residual
  □ Embeddings

□ Phase 3: Architecture
  □ Encoder Layer
  □ Encoder Stack (N=6)
  □ Decoder Layer (with masking)
  □ Decoder Stack (N=6)
  □ Complete Transformer

□ Phase 4: Training
  □ Data tokenization & batching
  □ Loss function (with label smoothing)
  □ Optimizer (Adam)
  □ Learning rate schedule (warmup + decay)
  □ Regularization (dropout)
  □ Training loop

□ Phase 5: Inference
  □ Greedy decoding
  □ Beam search
  □ Length penalty

□ Phase 6: Evaluation
  □ BLEU score calculation
  □ Qualitative analysis
```

---

# COMMON ERRORS & SOLUTIONS

| Error | Cause | Solution |
|-------|-------|----------|
| Shape mismatch | Wrong dimensions | Print shapes at each step |
| NaN loss | Exploding gradients | Add gradient clipping |
| Model not learning | Learning rate too high/low | Use warmup schedule |
| Overfitting | Not enough regularization | Add dropout, label smoothing |
| Slow training | Not using GPU | Move tensors to CUDA |
| Memory error | Batch too large | Reduce batch size |
| Attention looks random | Not enough training | Train longer |
| Repetitive output | No length penalty | Add beam search with penalty |

---

*Document created for Transformer implementation guidance - Hinglish Edition*
*Follow this roadmap step by step for successful implementation!*
