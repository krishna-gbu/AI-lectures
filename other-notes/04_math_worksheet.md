# Transformer Math Worksheet - Pen & Paper Edition

> Poora Transformer ek baar haath se solve karo. Har step mein actual numbers hain.
> Pehle khud calculate karo, phir ✅ ANSWER se verify karo.

---

## SETUP - Ye Numbers Poore Worksheet Mein Use Honge

```
Sentence:    "the cat sat"
Tokens:      [0, 1, 2]

Vocabulary:
┌──────┬───────┐
│ Word │ Index │
├──────┼───────┤
│ the  │   0   │
│ cat  │   1   │
│ sat  │   2   │
│ on   │   3   │
│ mat  │   4   │
└──────┴───────┘

Hyperparameters:
┌────────────┬───────┬─────────────────────────┐
│ Parameter  │ Value │ Meaning                 │
├────────────┼───────┼─────────────────────────┤
│ vocab_size │   5   │ Total words             │
│ d_model    │   4   │ Embedding dimension     │
│ n_heads    │   2   │ Number of heads         │
│ d_k        │   2   │ d_model ÷ heads = 4÷2   │
│ d_ff       │   8   │ FFN inner dimension     │
│ seq_len    │   3   │ Sentence length         │
└────────────┴───────┴─────────────────────────┘

NOTE: Real Transformer mein d_model=512, heads=8, d_k=64, d_ff=2048
      Hum chhote numbers use kar rahe hain taaki pen se calculate ho sake.
```

### Rounding Rule
```
Har step mein 2 DECIMAL PLACES tak round karo (e.g., 0.5651 → 0.57)
Lekin ANSWERS mein 4 decimal places dikhaye hain for accuracy.
Tumhara answer agar 0.01 ke andar hai → CORRECT hai! ✓
```

---

# ═══════════════════════════════════════════════
# PART A: INPUT PROCESSING
# ═══════════════════════════════════════════════

---

## Section 1: Token IDs

```
📌 CONCEPT: Har word ko ek number (index) milta hai

Sentence: "the cat sat"

Step 1: Vocabulary mein se index nikalo
```

### 📝 CALCULATE KARO:

```
"the" → index = ?
"cat" → index = ?
"sat" → index = ?

Token sequence = [?, ?, ?]
```

### ✅ ANSWER:

```
"the" → 0
"cat" → 1
"sat" → 2

Token sequence = [0, 1, 2]
```

---

## Section 2: Embedding Lookup + Scaling

```
📌 CONCEPT: Token index → Vector (numbers ki list)
            Har word ko d_model=4 numbers se represent karte hain

📌 FORMULA: One-hot vector × Embedding Matrix = Word vector
            (ya simply: row lookup by index)

            Scaling: X_scaled = X_embed × √d_model
            (Transformer paper mein embeddings ko √d_model se multiply karte hain)
```

### 📥 GIVEN: Embedding Matrix E (5×4)

```
        dim0  dim1  dim2  dim3
the(0): [0.1,  0.2,  0.3,  0.4]
cat(1): [0.5,  0.6,  0.7,  0.8]
sat(2): [0.2,  0.4,  0.6,  0.8]
on (3): [0.3,  0.5,  0.7,  0.9]
mat(4): [0.4,  0.3,  0.2,  0.1]
```

### 📝 CALCULATE KARO:

```
Step 1: Embedding lookup (row nikalo by index)

   "the" → index 0 → E[0] = [?, ?, ?, ?]
   "cat" → index 1 → E[1] = [?, ?, ?, ?]
   "sat" → index 2 → E[2] = [?, ?, ?, ?]

   X_embed (3×4) = ?

Step 2: Scale by √d_model

   √d_model = √4 = ?

   X_scaled = X_embed × √4

   Row 0: [0.1×?, 0.2×?, 0.3×?, 0.4×?] = [?, ?, ?, ?]
   Row 1: [0.5×?, 0.6×?, 0.7×?, 0.8×?] = [?, ?, ?, ?]
   Row 2: [0.2×?, 0.4×?, 0.6×?, 0.8×?] = [?, ?, ?, ?]
```

### ✅ ANSWER:

```
Step 1:
   X_embed = [[0.1, 0.2, 0.3, 0.4],      ← the
              [0.5, 0.6, 0.7, 0.8],      ← cat
              [0.2, 0.4, 0.6, 0.8]]      ← sat

Step 2:
   √d_model = √4 = 2

   X_scaled = [[0.2, 0.4, 0.6, 0.8],      ← ×2
               [1.0, 1.2, 1.4, 1.6],      ← ×2
               [0.4, 0.8, 1.2, 1.6]]      ← ×2

   Shape: (3, 4) = (seq_len, d_model)
```

---

## Section 3: Positional Encoding

```
📌 CONCEPT: Model ko word ki POSITION batani padti hai
            "the cat sat" vs "sat the cat" → different meaning
            Position information add karte hain sinusoidal functions se

📌 FORMULA:
   PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
   PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

   pos     = word ki POSITION sentence mein (0, 1, 2, ...)
             "the cat sat"
               ↓   ↓   ↓
              pos=0 pos=1 pos=2

   2i      = EVEN dimension index (0, 2, 4, ...) → SIN lagao
   2i+1    = ODD dimension index  (1, 3, 5, ...) → COS lagao
   i       = pair index (0, 1, 2, ...)
   d_model = 4

📌 DIMENSIONS PAIRS MEIN KAAM KARTI HAIN:
   d_model = 4 → 4 dimensions → 2 pairs
   Pair 0 (i=0): dim 0 = sin,  dim 1 = cos
   Pair 1 (i=1): dim 2 = sin,  dim 3 = cos

📌 FORMULA KO SIMPLIFY KARO:
   pos / 10000^(2i/d_model) = pos × (1 / 10000^(2i/d_model))
                             = pos × freq

   freq = 1 / 10000^(2i/d_model)   ← "frequency" nikaal lo

   DONO SAME HAIN:
   sin(pos / 10000^(2i/d_model))  =  sin(pos × freq)
   ─────────────────────────────      ────────────────
        ORIGINAL formula                 SHORT form
        (divide by big number)           (multiply by freq)

   Example:
   i=0: freq = 1/10000^(0/4) = 1/1 = 1
        sin(pos / 1) = sin(pos × 1)  ← SAME ✓

   i=1: freq = 1/10000^(2/4) = 1/100 = 0.01
        sin(pos / 100) = sin(pos × 0.01)  ← SAME ✓

📌 NOTE: sin/cos values haath se calculate karna mushkil hai.
         Neeche formula samjho, values provided hain.
```

### 📝 SAMJHO (Calculate nahi karna, samajhna hai):

```
For d_model = 4, we have 2 frequency pairs:

Pair i=0 (dimensions 0,1):
   freq = 1 / 10000^(0/4) = 1/1 = 1  (FAST changing ⏱️ second ka kanta)
   dim 0: sin(pos × 1)
   dim 1: cos(pos × 1)

Pair i=1 (dimensions 2,3):
   freq = 1 / 10000^(2/4) = 1/100 = 0.01  (SLOW changing 🕐 hour ka kanta)
   dim 2: sin(pos × 0.01)
   dim 3: cos(pos × 0.01)

ANALOGY: Ghadi (Clock) ke kante
   Fast freq  = second ka kanta → har position pe bahut change
   Slow freq  = hour ka kanta   → bahut dheere change
   Dono milke EXACT position batate hain!

──────────────────────────────────────────────────

Position 0 (pehla word "the", pos=0):

   Pair 0 (i=0, freq=1):
      dim 0 = sin(0 × 1) = sin(0) = 0.00
      dim 1 = cos(0 × 1) = cos(0) = 1.00

   Pair 1 (i=1, freq=0.01):
      dim 2 = sin(0 × 0.01) = sin(0) = 0.00
      dim 3 = cos(0 × 0.01) = cos(0) = 1.00

   PE(0) = [0.00, 1.00, 0.00, 1.00]
   📌 pos=0 pe: sin(0)=0, cos(0)=1 HAMESHA

──────────────────────────────────────────────────

Position 1 (doosra word "cat", pos=1):

   Pair 0 (i=0, freq=1):
      dim 0 = sin(1 × 1) = sin(1) = 0.84
                                      ↑ (1 radian = 57.3°)
      dim 1 = cos(1 × 1) = cos(1) = 0.54

   Pair 1 (i=1, freq=0.01):
      dim 2 = sin(1 × 0.01) = sin(0.01) = 0.01  ← bahut chhota angle
      dim 3 = cos(1 × 0.01) = cos(0.01) = 1.00  ← almost 1

   PE(1) = [0.84, 0.54, 0.01, 1.00]
   📌 Fast pair BAHUT badla (0→0.84), Slow pair mushkil se hila (0→0.01)

──────────────────────────────────────────────────

Position 2 (teesra word "sat", pos=2):

   Pair 0 (i=0, freq=1):
      dim 0 = sin(2 × 1) = sin(2) = 0.91  (2 radian = 114.6°)
      dim 1 = cos(2 × 1) = cos(2) = -0.42 ← NEGATIVE! Direction change

   Pair 1 (i=1, freq=0.01):
      dim 2 = sin(2 × 0.01) = sin(0.02) = 0.02
      dim 3 = cos(2 × 0.01) = cos(0.02) = 1.00

   PE(2) = [0.91, -0.42, 0.02, 1.00]
   📌 cos NEGATIVE ho gaya! Position 0 se clearly DIFFERENT

──────────────────────────────────────────────────

KYUN KAAM KARTA HAI:
1. Har position ka PE vector UNIQUE hai
2. Paas ki positions → similar PE, door ki → different PE
3. Multiple frequencies → lambi sequence tak unique (repeat nahi hota)
4. Sin+Cos PAIR → PE(pos+k) ko PE(pos) se linear transform se nikaal sakte hain
   → Model RELATIVE positions seekh sakta hai
```

### 📥 GIVEN: PE values (rounded for pen-paper)

```
              dim0   dim1   dim2   dim3
PE[pos=0] = [ 0.0,   1.0,   0.0,   1.0]
PE[pos=1] = [ 0.8,   0.5,   0.0,   1.0]
PE[pos=2] = [ 0.9,  -0.4,   0.0,   1.0]

Shape: (3, 4)

Observation karo:
- dim 0,1 (fast): values BAHUT change ho rahe hain (0→0.8→0.9, 1→0.5→-0.4)
- dim 2,3 (slow): values BAHUT DHEERE change ho rahe hain (0→0→0, 1→1→1)
- Isse model nearby positions ko similar aur door positions ko different samjhta hai
```

---

## Section 4: Input X = Scaled Embedding + PE

```
📌 FORMULA: X = X_scaled + PE  (simple vector addition)
```

### 📥 GIVEN:

```
X_scaled = [[0.2, 0.4, 0.6, 0.8],
            [1.0, 1.2, 1.4, 1.6],
            [0.4, 0.8, 1.2, 1.6]]

PE =       [[0.0, 1.0, 0.0, 1.0],
            [0.8, 0.5, 0.0, 1.0],
            [0.9,-0.4, 0.0, 1.0]]
```

### 📝 CALCULATE KARO:

```
X = X_scaled + PE (element-wise addition)

Row 0 ("the", pos 0):
   [0.2+0.0, 0.4+1.0, 0.6+0.0, 0.8+1.0] = [?, ?, ?, ?]

Row 1 ("cat", pos 1):
   [1.0+0.8, 1.2+0.5, 1.4+0.0, 1.6+1.0] = [?, ?, ?, ?]

Row 2 ("sat", pos 2):
   [0.4+0.9, 0.8+(-0.4), 1.2+0.0, 1.6+1.0] = [?, ?, ?, ?]

X (3×4) = ?
```

### ✅ ANSWER:

```
X = [[0.2,  1.4,  0.6,  1.8],      ← "the" at position 0
     [1.8,  1.7,  1.4,  2.6],      ← "cat" at position 1
     [1.3,  0.4,  1.2,  2.6]]      ← "sat" at position 2

Shape: (3, 4) = (seq_len, d_model)

⭐ YE X AAGE POORE TRANSFORMER MEIN USE HOGA!
   Ye hai input to the encoder.
   Isme word meaning (embedding) + position info (PE) dono hain.
```

---

# ═══════════════════════════════════════════════
# PART B: SELF-ATTENTION (Single Head)
# ═══════════════════════════════════════════════

```
📌 FORMULA: Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V

Steps:
   1. Q = X × W_Q    (Query: "main kya dhundh raha hun?")
   2. K = X × W_K    (Key: "mere paas kya hai?")
   3. V = X × W_V    (Value: "meri actual information")
   4. scores = Q × K^T      (kitna relevant hai?)
   5. scores = scores / √d_k  (scale down)
   6. weights = softmax(scores) (probabilities mein convert)
   7. output = weights × V     (weighted combination)
```

---

## Section 5: Q, K, V Projection (Head 1)

```
📌 FORMULA: Q = X × W_Q,  K = X × W_K,  V = X × W_V
            Matrix multiplication: (3×4) × (4×2) = (3×2)
            Har word ka 4-dim vector → 2-dim query/key/value

📌 Q, K, V ALAG KYUN?
   Same word ke 3 alag roles hain:
   ┌────────────┬─────────────────────────────┬─────────────────────────┐
   │ Projection │ Matlab                      │ Analogy                 │
   ├────────────┼─────────────────────────────┼─────────────────────────┤
   │ Q (Query)  │ "Main kya dhundh raha hun?" │ Library mein tumhara    │
   │            │                             │ sawaal                  │
   ├────────────┼─────────────────────────────┼─────────────────────────┤
   │ K (Key)    │ "Mere paas kya hai?"        │ Book ka title/label     │
   ├────────────┼─────────────────────────────┼─────────────────────────┤
   │ V (Value)  │ "Meri actual information"   │ Book ke andar ka content│
   └────────────┴─────────────────────────────┴─────────────────────────┘

   W_Q, W_K, W_V ALAG hain → same X se 3 DIFFERENT compressed views
   Isliye Q["cat"] ≠ K["cat"] ≠ V["cat"]

📌 SHAPE (4×2) KYUN?
   4 rows  → input 4-dim hai (d_model=4)
   2 cols  → output 2-dim chahiye (d_k = d_model ÷ heads = 4÷2 = 2)

📌 MATRIX MULTIPLY YAAD KARO:
   result[i,j] = Row i of first × Column j of second
               = sum of element-wise products
```

### 📥 GIVEN: Weight Matrices (Head 1)

```
W_Q1 (4×2):          W_K1 (4×2):          W_V1 (4×2):
[[0.2, 0.1],         [[0.1, 0.2],         [[0.2, 0.3],
 [0.1, 0.3],          [0.3, 0.1],          [0.1, 0.2],
 [0.3, 0.2],          [0.2, 0.3],          [0.3, 0.1],
 [0.1, 0.1]]          [0.1, 0.1]]          [0.2, 0.1]]
```

### 📝 CALCULATE KARO: Q1 = X × W_Q1

```
X (3×4) × W_Q1 (4×2) = Q1 (3×2)

Row 0 of Q1 ("the" ka query):
   Q1[0,0] = X[0] · W_Q1[:,0] # "saari rows ka column 0 nikalo" 
            = 0.2×0.2 + 1.4×0.1 + 0.6×0.3 + 1.8×0.1
            = ?    + ?    + ?    + ?
            = ?

   Q1[0,1] = X[0] · W_Q1[:,1]
            = 0.2×0.1 + 1.4×0.3 + 0.6×0.2 + 1.8×0.1
            = ?    + ?    + ?    + ?
            = ?

Row 1 of Q1 ("cat" ka query):
   Q1[1,0] = 1.8×0.2 + 1.7×0.1 + 1.4×0.3 + 2.6×0.1 = ?
   Q1[1,1] = 1.8×0.1 + 1.7×0.3 + 1.4×0.2 + 2.6×0.1 = ?

Row 2 of Q1 ("sat" ka query):
   Q1[2,0] = 1.3×0.2 + 0.4×0.1 + 1.2×0.3 + 2.6×0.1 = ?
   Q1[2,1] = 1.3×0.1 + 0.4×0.3 + 1.2×0.2 + 2.6×0.1 = ?

Similarly calculate K1 = X × W_K1 and V1 = X × W_V1
```

### ✅ ANSWER:

```
Q1 = X × W_Q1:
   Q1[0,0] = 0.04 + 0.14 + 0.18 + 0.18 = 0.54
   Q1[0,1] = 0.02 + 0.42 + 0.12 + 0.18 = 0.74
   Q1[1,0] = 0.36 + 0.17 + 0.42 + 0.26 = 1.21
   Q1[1,1] = 0.18 + 0.51 + 0.28 + 0.26 = 1.23
   Q1[2,0] = 0.26 + 0.04 + 0.36 + 0.26 = 0.92
   Q1[2,1] = 0.13 + 0.12 + 0.24 + 0.26 = 0.75

   Q1 (3×2) = [[0.54, 0.74],
                [1.21, 1.23],
                [0.92, 0.75]]

K1 = X × W_K1:
   K1 (3×2) = [[0.74, 0.54],
                [1.23, 1.21],
                [0.75, 0.92]]

V1 = X × W_V1:
   V1 (3×2) = [[0.72, 0.58],
                [1.47, 1.28],
                [1.18, 0.85]]

Shapes: (3, 4) × (4, 2) = (3, 2)  ✓
Each word: 4-dim → 2-dim (d_k = 2)
```

### 📌 DEEP UNDERSTANDING: Yeh multiplication kya kar raha hai?

```
Q1[i,j] = X ki row i  ×  W_Q1 ka column j
           (word vector)   (recipe)

Example: Q1[1,0] = "cat" ka new dim0 kaise bana?

   X row 1 ("cat") =  [1.8,  1.7,  1.4,  2.6]
   W_Q1 column 0 =    [0.2,  0.1,  0.3,  0.1]
                        ↓     ↓     ↓     ↓
                      1.8×0.2 + 1.7×0.1 + 1.4×0.3 + 2.6×0.1
                      = 0.36 +  0.17  +  0.42  +  0.26
                      = 1.21 ✓

   Isme kya hua?
   → "cat" ke dim0 (1.8) ne 0.2 weight ke saath contribute kiya = 0.36
   → "cat" ke dim1 (1.7) ne 0.1 weight ke saath contribute kiya = 0.17
   → "cat" ke dim2 (1.4) ne 0.3 weight ke saath contribute kiya = 0.42 ← sabse zyada
   → "cat" ke dim3 (2.6) ne 0.1 weight ke saath contribute kiya = 0.26

   Contribution = X ki value × W_Q1 ka weight (dono milke decide karte hain)
   dim2 ka weight sabse bada (0.3) hai, lekin dim3 ki value badi (2.6)
   hai isliye dim3 ka contribution (0.26) bhi significant hai

   W_Q1 ka column = "recipe" (training se seekhi hui, fixed)
   X ki row = "ingredient" (har word ka alag)
   Output = recipe × ingredient

   4-dim → 2-dim COMPRESS hota hai, lekin INTENTIONAL hai
   Q ko poori info nahi chahiye, sirf "searching" wali chahiye

📌 W_Q1 KE VALUES KAHAN SE AAYE?
   → RANDOM se start hote hain (initialization)
   → Training mein backpropagation se update hote hain
   → Lakho iterations baad MEANINGFUL ban jaate hain
   → Worksheet mein simple numbers hain sirf practice ke liye
```

---

## Section 6: Attention Scores

```
📌 FORMULA: scores = Q × K^T
            (3×2) × (2×3) = (3×3)

📌 INTUITION: scores[i][j] = "word i kitna word j pe attend kare?"
              Higher score = zyada attention
              (3×3) matrix = har word ka har word se score
```

### 📝 CALCULATE KARO:

```
First: K1 transpose (K1.T) - rows ↔ columns swap karo

K1 = [[0.74, 0.54],       K1.T = [[0.74, 1.23, 0.75],
      [1.23, 1.21],  →            [0.54, 1.21, 0.92]]
      [0.75, 0.92]]

Now: scores = Q1 × K1.T

NOTE: scores[i,j] = Q1[i] · K1[j]  (K1.T ka col j = K1 ka row j)

scores[0,0] = Q1[0] · K1[0] = 0.54×0.74 + 0.74×0.54 = ? + ? = ?
scores[0,1] = Q1[0] · K1[1] = 0.54×1.23 + 0.74×1.21 = ? + ? = ?
scores[0,2] = Q1[0] · K1[2] = 0.54×0.75 + 0.74×0.92 = ? + ? = ?

scores[1,0] = Q1[1] · K1[0] = 1.21×0.74 + 1.23×0.54 = ?
scores[1,1] = Q1[1] · K1[1] = 1.21×1.23 + 1.23×1.21 = ?
scores[1,2] = Q1[1] · K1[2] = 1.21×0.75 + 1.23×0.92 = ?

scores[2,0] = Q1[2] · K1[0] = 0.92×0.74 + 0.75×0.54 = ?
scores[2,1] = Q1[2] · K1[1] = 0.92×1.23 + 0.75×1.21 = ?
scores[2,2] = Q1[2] · K1[2] = 0.92×0.75 + 0.75×0.92 = ?
```

### ✅ ANSWER:

```
scores (3×3):
            the     cat     sat
   the  [ 0.7992, 1.5596, 1.0858]
   cat  [ 1.5596, 2.9766, 2.0391]
   sat  [ 1.0858, 2.0391, 1.3800]

Detailed:
   [0,0] = 0.3996 + 0.3996 = 0.7992
   [0,1] = 0.6642 + 0.8954 = 1.5596
   [0,2] = 0.4050 + 0.6808 = 1.0858
   [1,0] = 0.8954 + 0.6642 = 1.5596
   [1,1] = 1.4883 + 1.4883 = 2.9766
   [1,2] = 0.9075 + 1.1316 = 2.0391
   [2,0] = 0.6808 + 0.4050 = 1.0858
   [2,1] = 1.1316 + 0.9075 = 2.0391
   [2,2] = 0.6900 + 0.6900 = 1.3800

Observation: scores[i,j] = scores[j,i] (symmetric hai!)
             Kyunki Q aur K ke weights similar pattern mein hain
             "cat" ka score sabse zyada hai (longest vector)
```

---

## Section 7: Scaling

```
📌 FORMULA: scaled_scores = scores / √d_k

📌 WHY? Bina scaling ke, agar d_k bada ho toh dot products
         bahut bade ho jaate hain → softmax bahut sharp ho jata hai
         → gradients bahut chhote → training slow

         √d_k se divide → values moderate range mein rehte hain
```

### 📝 CALCULATE KARO:

```
d_k = 2
√d_k = √2 = 1.4142  (ye yaad rakh lo)

Har element ko 1.4142 se divide karo:

scaled[0,0] = 0.7992 / 1.4142 = ?
scaled[0,1] = 1.5596 / 1.4142 = ?
scaled[0,2] = 1.0858 / 1.4142 = ?
... (baaki 6 elements bhi)
```

### ✅ ANSWER:

```
scaled_scores (3×3):

            the     cat     sat
   the  [ 0.5651, 1.1028, 0.7678]
   cat  [ 1.1028, 2.1048, 1.4419]
   sat  [ 0.7678, 1.4419, 0.9758]

Observation: Values smaller ho gaye (manageable range mein)
```

---

## Section 8: Softmax

```
📌 FORMULA: softmax(x_i) = exp(x_i) / Σ exp(x_j)
            Har ROW pe separately apply hota hai
            Result: 0 se 1 ke beech, har row ka sum = 1

📌 NOTE: exp() values haath se calculate karna hard hai.
         Neeche exp() table diya hai. Use karo.
```

### 📥 exp() TABLE (common values):

```
┌──────┬────────┐  ┌──────┬────────┐  ┌──────┬────────┐
│  x   │ exp(x) │  │  x   │ exp(x) │  │  x   │ exp(x) │
├──────┼────────┤  ├──────┼────────┤  ├──────┼────────┤
│ 0.0  │ 1.0000 │  │ 0.8  │ 2.2255 │  │ 1.6  │ 4.9530 │
│ 0.1  │ 1.1052 │  │ 0.9  │ 2.4596 │  │ 1.7  │ 5.4739 │
│ 0.2  │ 1.2214 │  │ 1.0  │ 2.7183 │  │ 1.8  │ 6.0496 │
│ 0.3  │ 1.3499 │  │ 1.1  │ 3.0042 │  │ 1.9  │ 6.6859 │
│ 0.4  │ 1.4918 │  │ 1.2  │ 3.3201 │  │ 2.0  │ 7.3891 │
│ 0.5  │ 1.6487 │  │ 1.3  │ 3.6693 │  │ 2.1  │ 8.1662 │
│ 0.6  │ 1.8221 │  │ 1.4  │ 4.0552 │  │ 2.2  │ 9.0250 │
│ 0.7  │ 2.0138 │  │ 1.5  │ 4.4817 │  │ 2.5  │12.1825 │
└──────┴────────┘  └──────┴────────┘  └──────┴────────┘
```

### 📝 CALCULATE KARO:

```
Row 0: [0.5651, 1.1028, 0.7678]

   Step 1: exp() nikalo (table se interpolate karo)
      exp(0.5651) → 0.5 aur 0.6 ke beech → 1.6487 aur 1.8221 ke beech ≈ 1.76
      exp(1.1028) → 1.1 ke paas → 3.0042 ke paas ≈ 3.00
      exp(0.7678) → 0.7 aur 0.8 ke beech → 2.0138 aur 2.2255 ke beech ≈ 2.16

   Step 2: Sum nikalo
      sum = 1.76 + 3.00 + 2.16 = ?

   Step 3: Divide karo
      softmax[0,0] = 1.76 / sum = ?
      softmax[0,1] = 3.00 / sum = ?
      softmax[0,2] = 2.16 / sum = ?

   Check: sum = 1.0?

Row 1: [1.1028, 2.1048, 1.4419]
   (same process)

Row 2: [0.7678, 1.4419, 0.9758]
   (same process)
```

### ✅ ANSWER:

```
Attention Weights (3×3):

                   the      cat      sat      sum
   the →        [ 0.2540,  0.4349,  0.3111]   = 1.0 ✓
   cat →        [ 0.1950,  0.5312,  0.2738]   = 1.0 ✓
   sat →        [ 0.2385,  0.4679,  0.2936]   = 1.0 ✓

Detailed (Row 0):
   exp(0.5651) = 1.7597
   exp(1.1028) = 3.0126
   exp(0.7678) = 2.1550
   sum = 6.9272
   softmax = [1.7597/6.9272, 3.0126/6.9272, 2.1550/6.9272]
           = [0.2540, 0.4349, 0.3111]

📌 INTERPRETATION:
   "the" → 43% attention on "cat", 31% on "sat", 25% on "the"
   "cat" → 53% attention on ITSELF, 27% on "sat", 20% on "the"
   "sat" → 47% attention on "cat", 29% on "sat", 24% on "the"

   "cat" sabko attract kar raha hai! (highest scores kyunki longest vector)
```

---

## Section 9: Weighted Sum (Attention Output)

```
📌 FORMULA: output = weights × V
            (3×3) × (3×2) = (3×2)

📌 INTUITION: Har word ka naya representation =
              Weighted average of ALL words' values
              Weights = attention probabilities (Section 8 se)
```

### 📝 CALCULATE KARO:

```
weights (3×3) × V1 (3×2) = output (3×2)

V1 = [[0.72, 0.58],     ← "the" ki value
      [1.47, 1.28],     ← "cat" ki value
      [1.18, 0.85]]     ← "sat" ki value

Output Row 0 ("the" ka new representation):
   out[0,0] = 0.2540×0.72 + 0.4349×1.47 + 0.3111×1.18
            = ?       + ?        + ?
            = ?

   out[0,1] = 0.2540×0.58 + 0.4349×1.28 + 0.3111×0.85
            = ?

Output Row 1 ("cat" ka new representation):
   out[1,0] = 0.1950×0.72 + 0.5312×1.47 + 0.2738×1.18 = ?
   out[1,1] = 0.1950×0.58 + 0.5312×1.28 + 0.2738×0.85 = ?

Output Row 2 ("sat" ka new representation):
   out[2,0] = 0.2385×0.72 + 0.4679×1.47 + 0.2936×1.18 = ?
   out[2,1] = 0.2385×0.58 + 0.4679×1.28 + 0.2936×0.85 = ?
```

### ✅ ANSWER:

```
Head 1 Output (3×2):

   the → [1.1893, 0.9684]
   cat → [1.2443, 1.0258]
   sat → [1.2060, 0.9868]

Detailed (Row 0):
   out[0,0] = 0.1829 + 0.6393 + 0.3671 = 1.1893
   out[0,1] = 0.1473 + 0.5567 + 0.2644 = 0.9684

📌 OBSERVATION: Output values ek doosre ke kaafi close hain
   Kyunki attention weights relatively uniform thay.
   Real Transformer mein (trained), weights zyada focused hote hain.
```

---

# ═══════════════════════════════════════════════
# PART C: MULTI-HEAD ATTENTION
# ═══════════════════════════════════════════════

```
📌 CONCEPT: Ek head se ek "perspective" milta hai.
            Multiple heads = multiple perspectives simultaneously.
            h=2 heads, phir concat karke original dimension pe project.

📌 FLOW:
   Head 1: X × W_Q1/K1/V1 → Attention → Output1 (3×2)
   Head 2: X × W_Q2/K2/V2 → Attention → Output2 (3×2)
   Concat: [Output1 | Output2] = (3×4)
   Project: Concat × W_O = (3×4)
```

---

## Section 10: Head 2 (same process, different weights)

### 📥 GIVEN: Head 2 Weight Matrices

```
W_Q2 (4×2):          W_K2 (4×2):          W_V2 (4×2):
[[0.3, 0.1],         [[0.2, 0.3],         [[0.1, 0.2],
 [0.1, 0.2],          [0.2, 0.1],          [0.3, 0.1],
 [0.2, 0.3],          [0.1, 0.2],          [0.2, 0.3],
 [0.1, 0.2]]          [0.3, 0.1]]          [0.1, 0.2]]
```

### 📝 CALCULATE KARO:

```
Same steps as Head 1:
   Q2 = X × W_Q2    (3×4) × (4×2) = (3×2)
   K2 = X × W_K2
   V2 = X × W_V2
   scores2 = Q2 × K2.T
   scaled2 = scores2 / √2
   weights2 = softmax(scaled2)
   output2 = weights2 × V2

TRY IT: At least Q2 ke kuch elements calculate karo:
   Q2[0,0] = 0.2×0.3 + 1.4×0.1 + 0.6×0.2 + 1.8×0.1 = ?
```

### ✅ ANSWER:

```
Q2 (3×2) = [[0.50, 0.84],
             [1.25, 1.46],
             [0.93, 1.09]]

K2 (3×2) = [[0.92, 0.50],
             [1.62, 1.25],
             [1.24, 0.93]]

V2 (3×2) = [[0.74, 0.72],
             [1.23, 1.47],
             [0.75, 1.18]]

Scores2 (3×3) = [[0.88,   1.86,   1.40],
                  [1.88,   3.85,   2.91],
                  [1.40,   2.87,   2.17]]

Scaled2 (3×3) = [[0.62,   1.32,   0.99],
                  [1.33,   2.72,   2.06],
                  [0.99,   2.03,   1.53]]

Weights2 (3×3):
                   the      cat      sat
   the →        [ 0.2250,  0.4498,  0.3252]
   cat →        [ 0.1409,  0.5675,  0.2915]
   sat →        [ 0.1804,  0.5095,  0.3101]

Head 2 Output (3×2) = [[0.9637, 1.2070],
                        [1.0210, 1.2798],
                        [0.9928, 1.2448]]

📌 COMPARE Head 1 vs Head 2:
   Head 1 weights for "cat": [0.20, 0.53, 0.27]
   Head 2 weights for "cat": [0.14, 0.57, 0.29]
   → Different heads, slightly different attention patterns!
   → Real Transformer mein ye BAHUT different hote hain.
```

---

## Section 11: Concatenation

```
📌 FORMULA: Concat = [Head1_output | Head2_output]
            (3×2) | (3×2) = (3×4)
            Simply dono outputs ko side-by-side rakh do
```

### 📝 CALCULATE KARO:

```
Head 1 Output:              Head 2 Output:
[[1.1893, 0.9684],          [[0.9637, 1.2070],
 [1.2443, 1.0258],    |      [1.0210, 1.2798],
 [1.2060, 0.9868]]           [0.9928, 1.2448]]

Concat (3×4):
Row 0: [1.1893, 0.9684, ?, ?]
Row 1: [?, ?, ?, ?]
Row 2: [?, ?, ?, ?]
```

### ✅ ANSWER:

```
Concat (3×4):
   the → [1.1893, 0.9684, 0.9637, 1.2070]
   cat → [1.2443, 1.0258, 1.0210, 1.2798]
   sat → [1.2060, 0.9868, 0.9928, 1.2448]

Shape: (3, 4) = (seq_len, d_model)  ← back to original dimension!
```

---

## Section 12: Output Projection

```
📌 FORMULA: MHA_output = Concat × W_O
            (3×4) × (4×4) = (3×4)

📌 WHY? Concat ne sirf heads ko chipka diya.
        W_O unhe MIX karta hai - heads ki information combine hoti hai.
```

### 📥 GIVEN:

```
W_O (4×4):
[[0.2, 0.1, 0.1, 0.3],
 [0.1, 0.3, 0.2, 0.1],
 [0.3, 0.1, 0.1, 0.2],
 [0.1, 0.2, 0.3, 0.1]]
```

### 📝 CALCULATE KARO:

```
MHA_output = Concat × W_O

Row 0:
   MHA[0,0] = 1.1893×0.2 + 0.9684×0.1 + 0.9637×0.3 + 1.2070×0.1
            = ?
   ... (baaki 3 columns bhi)

(Ye tedious hai! Kam se kam Row 0 ka first element karo,
 baaki answers se verify karo)
```

### ✅ ANSWER:

```
MHA_output (3×4):
   the → [0.7445, 0.7472, 0.7711, 0.7671]
   cat → [0.7857, 0.7902, 0.8156, 0.8081]
   sat → [0.7622, 0.7649, 0.7907, 0.7835]

⭐ YE HAI MULTI-HEAD ATTENTION KA FINAL OUTPUT!
   Shape: (3, 4) = same as input X
```

---

# ═══════════════════════════════════════════════
# PART D: ADD & NORM + FFN
# ═══════════════════════════════════════════════

---

## Section 13: Residual Connection

```
📌 FORMULA: Residual = X + MHA_output
            (original input + attention output)

📌 WHY RESIDUAL?
   - Gradient flow easy rehta hai (shortcut path)
   - Original information preserve hoti hai
   - Deep networks train ho paate hain
   - Bina residual ke 6 layers train karna bahut hard
```

### 📝 CALCULATE KARO:

```
X          = [[0.2,  1.4,  0.6,  1.8],
              [1.8,  1.7,  1.4,  2.6],
              [1.3,  0.4,  1.2,  2.6]]

MHA_output = [[0.7445, 0.7472, 0.7711, 0.7671],
              [0.7857, 0.7902, 0.8156, 0.8081],
              [0.7622, 0.7649, 0.7907, 0.7835]]

Residual = X + MHA_output (element-wise add):

Row 0: [0.2+0.7445, 1.4+0.7472, 0.6+0.7711, 1.8+0.7671]
     = [?, ?, ?, ?]

Row 1: [1.8+0.7857, 1.7+0.7902, 1.4+0.8156, 2.6+0.8081]
     = [?, ?, ?, ?]

Row 2: [1.3+0.7622, 0.4+0.7649, 1.2+0.7907, 2.6+0.7835]
     = [?, ?, ?, ?]
```

### ✅ ANSWER:

```
Residual1 (3×4):
   the → [0.9445,  2.1472,  1.3711,  2.5671]
   cat → [2.5857,  2.4902,  2.2156,  3.4081]
   sat → [2.0622,  1.1649,  1.9907,  3.3835]
```

---

## Section 14: Layer Normalization

```
📌 FORMULA: LayerNorm(x) = (x - mean) / √(variance + ε)

   For each token (row) separately:
   1. mean = average of all 4 values
   2. variance = average of (x - mean)² values
   3. normalize: (x - mean) / √(var + ε)

   ε = 0.00001 (avoid division by zero, practically ignore karo)

📌 RESULT: mean ≈ 0, standard deviation ≈ 1
```

### 📝 CALCULATE KARO (Token 0 = "the"):

```
Token 0: [0.9445, 2.1472, 1.3711, 2.5671]

Step 1: Mean
   mean = (0.9445 + 2.1472 + 1.3711 + 2.5671) / 4
        = ? / 4
        = ?

Step 2: Deviations (x - mean):
   0.9445 - mean = ?
   2.1472 - mean = ?
   1.3711 - mean = ?
   2.5671 - mean = ?

Step 3: Squared deviations:
   (deviation_0)² = ?
   (deviation_1)² = ?
   (deviation_2)² = ?
   (deviation_3)² = ?

Step 4: Variance = mean of squared deviations
   variance = (? + ? + ? + ?) / 4 = ?

Step 5: √(variance + ε) = ?

Step 6: Normalize
   norm[0] = deviation_0 / √(variance + ε) = ?
   norm[1] = deviation_1 / √(variance + ε) = ?
   norm[2] = deviation_2 / √(variance + ε) = ?
   norm[3] = deviation_3 / √(variance + ε) = ?

Verify: mean of normalized ≈ 0? std ≈ 1?

Similarly for Token 1 and Token 2.
```

### ✅ ANSWER:

```
Token 0: [0.9445, 2.1472, 1.3711, 2.5671]
   mean = 7.0299 / 4 = 1.7575
   deviations: [-0.8130, 0.3897, -0.3864, 0.8096]
   squared:    [0.6610, 0.1519, 0.1493, 0.6555]
   variance = 1.6177 / 4 = 0.4044
   √(var) = 0.6359
   normalized: [-1.2784, 0.6129, -0.6076, 1.2731]

Token 1: [2.5857, 2.4902, 2.2156, 3.4081]
   mean = 2.6749
   variance = 0.1976
   √(var) = 0.4446
   normalized: [-0.2006, -0.4154, -1.0331, 1.6491]

Token 2: [2.0622, 1.1649, 1.9907, 3.3835]
   mean = 2.1503
   variance = 0.6313
   √(var) = 0.7945
   normalized: [-0.1109, -1.2403, -0.2009, 1.5521]

LayerNorm1 output (3×4):
   the → [-1.2784,  0.6129, -0.6076,  1.2731]
   cat → [-0.2006, -0.4154, -1.0331,  1.6491]
   sat → [-0.1109, -1.2403, -0.2009,  1.5521]

📌 CHECK: Har row ka mean ≈ 0, std ≈ 1 ✓
```

---

## Section 15: Feed-Forward Network

```
📌 FORMULA: FFN(x) = ReLU(x × W1 + b1) × W2 + b2

   Step 1: Hidden = x × W1 + b1     (4 → 8: EXPAND)
   Step 2: Hidden = ReLU(Hidden)     (negative → 0)
   Step 3: Output = Hidden × W2 + b2 (8 → 4: COMPRESS)

📌 ReLU kya hai?
   ReLU(x) = max(0, x)
   Positive values → unchanged
   Negative values → 0

📌 WHY EXPAND-COMPRESS?
   4 → 8: Zyada "space" milta hai complex patterns seekhne ke liye
   8 → 4: Wapas original dimension pe compress
   Real Transformer: 512 → 2048 → 512

📌 NOTE: FFN mein bahut saare weights hain (4×8 + 8×4 = 64 numbers).
         Neeche sirf concept samjho. Ek-do elements calculate karo,
         baaki answer se verify karo.
```

### 📥 GIVEN:

```
W1 (4×8):
[[ 0.2, -0.1,  0.3,  0.1,  0.2, -0.1,  0.1,  0.3],
 [ 0.1,  0.2, -0.1,  0.3, -0.1,  0.2,  0.3,  0.1],
 [-0.1,  0.3,  0.2,  0.1,  0.3, -0.2,  0.1,  0.2],
 [ 0.3,  0.1,  0.1, -0.1,  0.1,  0.3, -0.1,  0.2]]

b1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

W2 (8×4):
[[ 0.1,  0.2, -0.1,  0.3],
 [ 0.2, -0.1,  0.3,  0.1],
 [ 0.3,  0.1,  0.2, -0.1],
 [-0.1,  0.3,  0.1,  0.2],
 [ 0.2,  0.1, -0.1,  0.3],
 [ 0.1, -0.2,  0.3,  0.1],
 [-0.1,  0.3,  0.1,  0.2],
 [ 0.3,  0.1, -0.1,  0.1]]

b2 = [0.1, 0.1, 0.1, 0.1]
```

### 📝 CALCULATE KARO (Token 0 ka ek element):

```
Input: LayerNorm1[0] = [-1.2784, 0.6129, -0.6076, 1.2731]

Step 1: Hidden[0,0] = input · W1[:,0] + b1[0]
   = (-1.2784×0.2) + (0.6129×0.1) + (-0.6076×(-0.1)) + (1.2731×0.3) + 0.1
   = (-0.2557) + (0.0613) + (0.0608) + (0.3819) + 0.1
   = ?

Step 2: ReLU
   If result > 0 → keep it
   If result < 0 → make it 0
```

### ✅ ANSWER:

```
Step 1: Hidden (before ReLU) for Token 0:
   [0.3483, 0.2954, -0.3390, -0.0320, -0.2719, 0.8539, -0.0320, -0.0891]

Step 2: After ReLU (negatives → 0):
   [0.3483, 0.2954,  0.0000,  0.0000,  0.0000, 0.8539,  0.0000,  0.0000]
   ← 5 out of 8 neurons "dead" (zero)! Only 3 active. This is NORMAL.

Step 3: FFN output for all tokens:
   (Token 1, 2 ke liye same process: Hidden → ReLU → W2 × hidden + b2)
   the → [0.2793, -0.0307,  0.4100,  0.3194]
   cat → [0.2838,  0.0917,  0.2556,  0.3669]
   sat → [0.3958,  0.1957,  0.1769,  0.3485]
```

---

## Section 16: Residual + LayerNorm 2

```
📌 Same as Sections 13-14, but now with FFN output.
   Residual2 = LayerNorm1_output + FFN_output
   Then LayerNorm again.
```

### 📝 CALCULATE KARO:

```
Residual2 = LayerNorm1 + FFN_output

LayerNorm1[0] = [-1.2784,  0.6129, -0.6076,  1.2731]
FFN_output[0] = [ 0.2793, -0.0307,  0.4100,  0.3194]
                 ─────────────────────────────────────
Residual2[0]  = [    ?   ,    ?   ,    ?   ,    ?   ]

(Token 1 aur 2 bhi karo)
```

### ✅ ANSWER:

```
Residual2 (3×4):
   the → [-0.9991,  0.5822, -0.1976,  1.5925]
   cat → [ 0.0832, -0.3237, -0.7775,  2.0161]
   sat → [ 0.2849, -1.0446, -0.0240,  1.9006]

LayerNorm2 (same process as Section 14):
   the → [-1.2977,  0.3524, -0.4614,  1.4067]
   cat → [-0.1563, -0.5386, -0.9649,  1.6597]
   sat → [ 0.0054, -1.2518, -0.2868,  1.5332]

⭐ YE HAI ENCODER KA FINAL OUTPUT!
   Shape: (3, 4) = (seq_len, d_model)
   Har word ka representation ab "enriched" hai -
   usme apni info + doosre words ki info (attention se) + FFN processing sab hai.
```

---

# ═══════════════════════════════════════════════
# PART E: DECODER CONCEPTS
# ═══════════════════════════════════════════════

```
📌 DECODER vs ENCODER:

   ENCODER: Reads input      → "the cat sat" ko samjho
   DECODER: Generates output → Ek ek word predict karo

   Decoder ke 2 EXTRA cheezein:
   1. MASKED Self-Attention → Future words nahi dekh sakta
   2. CROSS-Attention → Encoder output ko "query" karta hai
```

---

## Section 17: Causal Masking (Decoder Self-Attention)

```
📌 PROBLEM: Decoder mein, agar word 0 predict karte waqt
            word 1, 2, 3... dikh jaaye → CHEATING!
            Model ko future nahi dekhna chahiye.

📌 SOLUTION: Causal Mask
            Future positions ke scores = -∞
            softmax(-∞) = 0 → zero attention on future

📌 EXAMPLE with 2 tokens for simplicity:
```

### 📥 GIVEN: Decoder input (2 tokens):

```
X_dec = [[0.3, 0.8, 0.5, 1.2],    ← token 0
         [0.9, 1.0, 0.6, 1.5]]    ← token 1

Scaled attention scores (pre-computed for demo, masking samjhne ke liye):
scores = [[0.28, 0.40],
          [0.40, 0.57]]
```

### 📝 CALCULATE KARO:

```
Step 1: Causal Mask banao
   Token 0 can see: [token 0 only]        → mask = [0, -∞]
   Token 1 can see: [token 0, token 1]    → mask = [0,  0]

   Mask = [[  0, -∞],
           [  0,   0]]

Step 2: Add mask to scores
   masked = scores + mask
   masked = [[0.28 + 0,    0.40 + (-∞)],
             [0.40 + 0,    0.57 + 0    ]]
          = [[0.28,  -∞],
             [0.40,  0.57]]

Step 3: Softmax
   Row 0: softmax([0.28, -∞]) = ?
      exp(0.28) = 1.32,  exp(-∞) = 0
      → [1.32/1.32, 0/1.32] = [?, ?]

   Row 1: softmax([0.40, 0.57]) = ?
      exp(0.40) = 1.49,  exp(0.57) = 1.77
      sum = 3.26
      → [1.49/3.26, 1.77/3.26] = [?, ?]
```

### ✅ ANSWER:

```
Masked Attention Weights:
   Token 0 → [1.0000, 0.0000]  ← 100% attention on ITSELF only!
   Token 1 → [0.4584, 0.5416]  ← Can see both tokens

📌 KEY INSIGHT:
   Token 0: CANNOT see token 1 (future) → forced to attend only to itself
   Token 1: CAN see token 0 and itself → distributes attention

   Ye hai AUTOREGRESSIVE generation ka secret!
   Isliye GPT ek-ek word generate karta hai, peeche dekh sakta hai, aage nahi.
```

---

## Section 18: Cross-Attention

```
📌 CONCEPT: Decoder "asks questions" to the Encoder

   Q = from DECODER (main kya dhundh raha hun)
   K = from ENCODER (encoder ke paas kya kya hai)
   V = from ENCODER (encoder ki information)

   "Decoder word X ke liye, encoder ki kaunsi word relevant hai?"

📌 IMPORTANT: Cross-attention mein NO MASKING!
             Decoder ko encoder ka POORA output dekhne milta hai.
             (Masking sirf decoder ke self-attention mein hota hai)

📌 EXAMPLE: Translation task mein:
   Encoder: "the cat sat" (English)
   Decoder: "le chat" (French generate kar raha hai)

   Jab decoder "chat" predict karta hai, cross-attention se
   encoder mein "cat" pe zyada attention dega!
```

### 📥 GIVEN:

```
NOTE: Cross-attention mein Q, K, V kaise bante hain?
   Q = Decoder_output × W_Q   (decoder se)
   K = Encoder_output × W_K   (encoder se)
   V = Encoder_output × W_V   (encoder se)

   Encoder output (3×4) hai, W_K/W_V (4×2) se multiply → (3×2)
   Decoder output (2×4) hai, W_Q (4×2) se multiply → (2×2)

   Neeche pre-computed values diye hain demo ke liye:

Decoder Q (from decoder × W_Q): (2×2)
   [[0.41, 0.49],
    [0.61, 0.66]]

Encoder K (from encoder × W_K): (3×2)
   [[ 0.02, -0.22],
    [-0.20, -0.21],
    [-0.28, -0.06]]

Encoder V (from encoder × W_V): (3×2)
   [[-0.08, -0.22],
    [-0.04, -0.09],
    [ 0.10, -0.12]]
```

### 📝 SAMJHO (shapes dekho):

```
Q: (2×2)   ← 2 decoder tokens, d_k=2
K: (3×2)   ← 3 encoder tokens, d_k=2
V: (3×2)   ← 3 encoder tokens, d_v=2

scores = Q × K.T = (2×2) × (2×3) = (2×3)
   → Har decoder token ka har ENCODER token se score!

weights = softmax(scores) = (2×3)
output = weights × V = (2×3) × (3×2) = (2×2)
```

### ✅ ANSWER:

```
Cross-attention weights (2×3):
                encoder_the  encoder_cat  encoder_sat
   dec_tok0 →   [ 0.3436,     0.3231,      0.3332]
   dec_tok1 →   [ 0.3497,     0.3189,      0.3314]

📌 Weights almost uniform kyunki ye UNTRAINED model hai.
   Trained model mein, "chat" would attend more to "cat" (high weight).

Cross-attention output (2×2):
   [[-0.0096, -0.1459],
    [-0.0101, -0.1467]]
```

---

# ═══════════════════════════════════════════════
# PART F: OUTPUT
# ═══════════════════════════════════════════════

```
📌 FLOW: Encoder Output → Linear Layer → Softmax → Predicted Word

   Linear: (3, 4) × (4, 5) = (3, 5)  → 5 scores per position
   Softmax: 5 scores → 5 probabilities
   Predicted word = highest probability
```

---

## Section 19: Linear Projection to Vocabulary

```
📌 FORMULA: logits = encoder_output × W_vocab
            (3×4) × (4×5) = (3×5)
            Har position ke liye 5 words ke scores
```

### 📥 GIVEN:

```
Encoder Output (3×4):
   the → [-1.2977,  0.3524, -0.4614,  1.4067]
   cat → [-0.1563, -0.5386, -0.9649,  1.6597]
   sat → [ 0.0054, -1.2518, -0.2868,  1.5332]

W_vocab (4×5):
         the   cat   sat    on   mat
       [[0.2,  0.1,  0.3,  0.1,  0.2],
        [0.1,  0.3,  0.1,  0.2,  0.1],
        [0.3,  0.2,  0.1,  0.3,  0.1],
        [0.1,  0.1,  0.2,  0.1,  0.3]]
```

### 📝 CALCULATE KARO (Row 0 ka ek element):

```
logits[0, "the"] = (-1.2977)×0.2 + 0.3524×0.1 + (-0.4614)×0.3 + 1.4067×0.1
                 = (-0.2595) + (0.0352) + (-0.1384) + (0.1407)
                 = ?
```

### ✅ ANSWER:

```
Logits (3×5):
             the      cat      sat      on      mat
   pos 0: [-0.2221,  0.0243, -0.1189, -0.0570,  0.1516]
   pos 1: [-0.2086, -0.2042,  0.1347, -0.2468,  0.3163]
   pos 2: [-0.0568, -0.2790,  0.1544, -0.1825,  0.3072]

📌 Ye RAW SCORES hain, probabilities nahi.
   Negative bhi ho sakte hain. Softmax se probabilities banenge.
```

---

## Section 20: Softmax → Probabilities

```
📌 FORMULA: P(word) = exp(logit) / Σ exp(logits)
            Same as Section 8, but now over 5 vocab words
```

### 📝 CALCULATE KARO (Position 0):

```
Logits[0] = [-0.2221, 0.0243, -0.1189, -0.0570, 0.1516]

NOTE: Negative values ke liye → exp(-x) = 1/exp(x)
   Example: exp(-0.22) = 1/exp(0.22) = 1/1.2461 ≈ 0.80

exp() nikalo:
   exp(-0.22) = 1/exp(0.22) = 1/1.2461 ≈ 0.80
   exp(0.02)  → 0.0 ke paas → 1.0000 ke paas ≈ 1.02
   exp(-0.12) = 1/exp(0.12) = 1/1.1275 ≈ 0.89
   exp(-0.06) = 1/exp(0.06) = 1/1.0618 ≈ 0.94
   exp(0.15)  → 0.1 aur 0.2 ke beech → 1.1052 aur 1.2214 ke beech ≈ 1.16

sum = 0.80 + 1.02 + 0.89 + 0.94 + 1.16 = ?

P(the) = 0.80 / sum = ?
P(cat) = 1.02 / sum = ?
P(sat) = 0.89 / sum = ?
P(on)  = 0.94 / sum = ?
P(mat) = 1.16 / sum = ?

Predicted word = highest probability = ?
```

### ✅ ANSWER:

```
Position 0 probabilities:
   P(the) = 0.1661    P(cat) = 0.2125    P(sat) = 0.1842
   P(on)  = 0.1959    P(mat) = 0.2413  ← HIGHEST
   → Predicted: "mat" (BUT almost uniform → untrained model!)

Position 1 probabilities:
   P(the) = 0.1648    P(cat) = 0.1656    P(sat) = 0.2323
   P(on)  = 0.1586    P(mat) = 0.2786  ← HIGHEST
   → Predicted: "mat"

Position 2 probabilities:
   P(the) = 0.1867    P(cat) = 0.1495    P(sat) = 0.2306
   P(on)  = 0.1646    P(mat) = 0.2686  ← HIGHEST
   → Predicted: "mat"

📌 OBSERVATION:
   Sabhi positions "mat" predict kar rahe hain!
   Probabilities almost uniform (≈ 0.20 each)
   Kyunki ye UNTRAINED model hai - random weights se kya hi predict karega!
   Training ke baad ye focused ho jayenge.
```

---

## Section 21: Cross-Entropy Loss

```
📌 FORMULA: Loss = -log(P(correct_word))

📌 INTUITION:
   P(correct) HIGH → Loss LOW  (good prediction)
   P(correct) LOW  → Loss HIGH (bad prediction)

📌 TARGET: "the cat sat" → next words = "cat sat on"
   Position 0: correct = "cat" (index 1)
   Position 1: correct = "sat" (index 2)
   Position 2: correct = "on"  (index 3)
```

### 📥 GIVEN: log() table

```
┌──────┬─────────┐  ┌──────┬─────────┐
│  x   │ -log(x) │  │  x   │ -log(x) │
├──────┼─────────┤  ├──────┼─────────┤
│ 0.10 │  2.3026 │  │ 0.50 │  0.6931 │
│ 0.15 │  1.8971 │  │ 0.60 │  0.5108 │
│ 0.16 │  1.8326 │  │ 0.70 │  0.3567 │
│ 0.17 │  1.7720 │  │ 0.80 │  0.2231 │
│ 0.20 │  1.6094 │  │ 0.90 │  0.1054 │
│ 0.21 │  1.5606 │  │ 0.95 │  0.0513 │
│ 0.23 │  1.4697 │  │ 0.99 │  0.0101 │
│ 0.25 │  1.3863 │  │ 1.00 │  0.0000 │
└──────┴─────────┘  └──────┴─────────┘
```

### 📝 CALCULATE KARO:

```
Position 0: target = "cat" (index 1)
   P(cat) = 0.2125
   Loss_0 = -log(0.2125) ≈ -log(0.21) ≈ ?

Position 1: target = "sat" (index 2)
   P(sat) = 0.2323
   Loss_1 = -log(0.2323) ≈ -log(0.23) ≈ ?

Position 2: target = "on" (index 3)
   P(on) = 0.1646
   Loss_2 = -log(0.1646) ≈ -log(0.16) ≈ ?

Average Loss = (Loss_0 + Loss_1 + Loss_2) / 3 = ?
```

### ✅ ANSWER:

```
Position 0: P(cat) = 0.2125,  Loss = -log(0.2125) = 1.5488
Position 1: P(sat) = 0.2323,  Loss = -log(0.2323) = 1.4595
Position 2: P(on)  = 0.1646,  Loss = -log(0.1646) = 1.8041

Average Loss = (1.5488 + 1.4595 + 1.8041) / 3 = 1.6041

📌 CONTEXT:
   Perfect prediction:  Loss = -log(1.0) = 0.0  (impossible with softmax)
   Random guess (1/5):  Loss = -log(0.2) = 1.6094
   Our untrained model: Loss = 1.6041 ≈ random!  (expected)
   Good trained model:  Loss ≈ 0.1 - 0.5

   Training ka goal: Is loss ko minimize karna.
   Backpropagation se weights update hote hain → loss kam hota hai
   → model better predict karta hai.
```

---

# ═══════════════════════════════════════════════
# COMPLETE TRANSFORMER FLOW SUMMARY
# ═══════════════════════════════════════════════

```
INPUT: "the cat sat" → [0, 1, 2]
                          │
                    ┌─────▼──────┐
                    │ Embedding  │ Token → Vector
                    │  Lookup    │ (3) → (3, 4)
                    └─────┬──────┘
                          │ × √d_model
                    ┌─────▼──────┐
                    │ Positional │ + Position info
                    │  Encoding  │ (3, 4)
                    └─────┬──────┘
                          │
              ┌───────────▼──────────────┐
              │   Multi-Head Attention   │
              │                          │
              │  Head 1        Head 2    │
              │  Q1,K1,V1     Q2,K2,V2  │
              │  scores→      scores→   │
              │  scale→       scale→    │
              │  softmax→     softmax→  │
              │  output1      output2   │
              │       \        /        │
              │     [Concat] → W_O     │
              └───────────┬──────────────┘
                          │
                    ┌─────▼──────┐
                    │ Add & Norm │ X + Attention → LayerNorm
                    └─────┬──────┘
                          │
                    ┌─────▼──────┐
                    │    FFN     │ Linear → ReLU → Linear
                    │  4→8→4    │
                    └─────┬──────┘
                          │
                    ┌─────▼──────┐
                    │ Add & Norm │ + Residual → LayerNorm
                    └─────┬──────┘
                          │
              ╔═══════════▼═══════════╗
              ║   ENCODER OUTPUT      ║
              ║   (3, 4)              ║
              ╚═══════════╤═══════════╝
                          │
                    ┌─────▼──────┐
                    │  Linear    │ (3,4) → (3,5) vocab scores
                    └─────┬──────┘
                          │
                    ┌─────▼──────┐
                    │  Softmax   │ scores → probabilities
                    └─────┬──────┘
                          │
                    ┌─────▼──────┐
                    │   Loss     │ -log(P(correct))
                    └────────────┘

YOUR RESULTS:
   Input:    "the cat sat" → [[0.2, 1.4, 0.6, 1.8], ...]
   Encoder:  → [[-1.30, 0.35, -0.46, 1.41], ...]
   Logits:   → [[-0.22, 0.02, -0.12, -0.06, 0.15], ...]
   Probs:    → [[0.17, 0.21, 0.18, 0.20, 0.24], ...]
   Loss:     → 1.6041 (≈ random guess, untrained)
```

---

# SHAPES JOURNEY (ek nazar mein)

```
┌─────────────────────────┬──────────────┐
│ Step                    │ Shape        │
├─────────────────────────┼──────────────┤
│ Token IDs               │ (3,)         │
│ Embedding Lookup        │ (3, 4)       │
│ + Positional Encoding   │ (3, 4)       │
│ Q, K, V (per head)      │ (3, 2)       │
│ Attention Scores        │ (3, 3)       │
│ Attention Weights       │ (3, 3)       │
│ Head Output             │ (3, 2)       │
│ Concat (2 heads)        │ (3, 4)       │
│ After W_O               │ (3, 4)       │
│ After Residual          │ (3, 4)       │
│ After LayerNorm         │ (3, 4)       │
│ FFN Hidden              │ (3, 8)       │
│ FFN Output              │ (3, 4)       │
│ After Residual+Norm     │ (3, 4)       │
│ Logits (to vocab)       │ (3, 5)       │
│ Probabilities           │ (3, 5)       │
│ Loss                    │ scalar (1,)  │
└─────────────────────────┴──────────────┘

Real Transformer:
(batch, seq_len, d_model) = (32, 100, 512)
Q,K,V per head: (32, 100, 64)
Scores: (32, 100, 100)
FFN hidden: (32, 100, 2048)
Logits: (32, 100, 30000)  ← 30k vocab!
```

---

# KEY TAKEAWAYS

```
1. Transformer = Matrix Multiplications ka chain
   Almost har step: tensor × weight_matrix

2. Attention ka core = Q × K.T (similarity scores)
   Phir softmax (probabilities) → V se weighted sum

3. Multi-head = Multiple parallel attention (different perspectives)
   Concat → W_O se mix

4. Residual connections = Original + Processed
   Gradient flow aur information preserve

5. LayerNorm = Normalize to mean=0, std=1
   Training stable rehti hai

6. FFN = Expand → ReLU → Compress
   Non-linearity add karta hai

7. Masking = Future words hide (decoder self-attention)
   softmax(-∞) = 0

8. Cross-attention = Decoder asks, Encoder answers
   Q from decoder, K,V from encoder

9. Output = Linear → Softmax → Probabilities → Loss

10. UNTRAINED MODEL ≈ RANDOM PREDICTIONS
    Training (backpropagation) se weights improve hote hain!
```

---

## Verification Script

```
Apne answers verify karne ke liye run karo:
   cd "research paper"
   source transformer_env/bin/activate
   python worksheet_compute.py
```

---

*Created: 2026-02-17*
*Purpose: Complete Transformer forward pass with pen-and-paper calculations*
*Verified: All answers computed and verified with PyTorch*
