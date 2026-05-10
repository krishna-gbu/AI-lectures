# Input Embedding - Deep Dive

> Transformer ke liye sabse pehla step: Words ko numbers mein convert karna

---

# PART 1: Mathematics of Embeddings

> Pure mathematical understanding - precise aur clear

---

## Step 1: Vector Kya Hai?

```
Vector = Ordered list of numbers

Example:
a = [3, 5]         ← 2D vector
b = [1, 2, 3]      ← 3D vector
c = [0.5, 0.8, -0.3, 0.2, ...]  ← 512D vector

"king" = ek 512D vector hai
```

---

## Step 2: Vector as Point

```
2D mein:

Vector [3, 5] = Point at (3, 5)

        Y
        ↑
      5 │     ● [3,5]
        │    /
        │   /
        │  /
        │ /
    ────┼─────────→ X
        0    3


512D mein:
Vector [0.5, 0.8, -0.3, ...] = Point at (0.5, 0.8, -0.3, ...)

(Visualize nahi kar sakte, but mathematically same concept)
```

---

## Step 3: Embedding Matrix

```
Embedding = Matrix of shape (V × D)

V = Vocabulary size (kitne unique words)
D = Dimension (512)

Example: V=5 words, D=4 dimensions

        ┌                          ┐
        │  0.2   0.5  -0.3   0.8   │  ← Row 0: "pad"
        │  0.1   0.9   0.4  -0.2   │  ← Row 1: "hello"
   E =  │  0.7  -0.1   0.6   0.3   │  ← Row 2: "world"
        │  0.4   0.8   0.2  -0.5   │  ← Row 3: "king"
        │  0.5   0.7   0.1  -0.4   │  ← Row 4: "queen"
        └                          ┘

        Shape: (5, 4)
```

---

## Step 4: Lookup = Row Selection

```
Word "king" ka ID = 3

Embedding("king") = E[3] = Row 3 of matrix E

E[3] = [0.4, 0.8, 0.2, -0.5]

Mathematically:

        ┌                          ┐
        │  0.2   0.5  -0.3   0.8   │
        │  0.1   0.9   0.4  -0.2   │
   E =  │  0.7  -0.1   0.6   0.3   │
        │  0.4   0.8   0.2  -0.5   │  ← SELECT THIS ROW
        │  0.5   0.7   0.1  -0.4   │
        └                          ┘

Result: [0.4, 0.8, 0.2, -0.5]
```

---

## Step 5: One-Hot × Matrix = Lookup

```
One-hot vector for "king" (ID=3):

one_hot = [0, 0, 0, 1, 0]
              ↑     ↑
           index 3 = 1, rest = 0


Embedding lookup = Matrix multiplication:

                    ┌                          ┐
                    │  0.2   0.5  -0.3   0.8   │
                    │  0.1   0.9   0.4  -0.2   │
[0, 0, 0, 1, 0]  ×  │  0.7  -0.1   0.6   0.3   │
                    │  0.4   0.8   0.2  -0.5   │
                    │  0.5   0.7   0.1  -0.4   │
                    └                          ┘
      (1×5)                    (5×4)

= [0×0.2 + 0×0.1 + 0×0.7 + 1×0.4 + 0×0.5,
   0×0.5 + 0×0.9 + 0×(-0.1) + 1×0.8 + 0×0.7,
   0×(-0.3) + 0×0.4 + 0×0.6 + 1×0.2 + 0×0.1,
   0×0.8 + 0×(-0.2) + 0×0.3 + 1×(-0.5) + 0×(-0.4)]

= [0.4, 0.8, 0.2, -0.5]

Same result! Row 3 select ho gaya.
```

---

## Step 6: Distance Between Vectors

### Euclidean Distance Formula:

```
d(a, b) = √[Σᵢ (aᵢ - bᵢ)²]
```

### Example 1: king vs queen (Similar words)

```
king  = [0.4, 0.8, 0.2, -0.5]
queen = [0.5, 0.7, 0.1, -0.4]

d(king, queen) = √[(0.4-0.5)² + (0.8-0.7)² + (0.2-0.1)² + (-0.5-(-0.4))²]
               = √[(-0.1)² + (0.1)² + (0.1)² + (-0.1)²]
               = √[0.01 + 0.01 + 0.01 + 0.01]
               = √0.04
               = 0.2

SMALL distance = Similar words! ✓
```

### Example 2: king vs hello (Different words)

```
king  = [0.4, 0.8, 0.2, -0.5]
hello = [0.1, 0.9, 0.4, -0.2]

d(king, hello) = √[(0.4-0.1)² + (0.8-0.9)² + (0.2-0.4)² + (-0.5-(-0.2))²]
               = √[(0.3)² + (-0.1)² + (-0.2)² + (-0.3)²]
               = √[0.09 + 0.01 + 0.04 + 0.09]
               = √0.23
               = 0.48

LARGER distance = Less similar! ✓
```

---

## Step 7: Dot Product

### Formula:

```
a · b = Σᵢ (aᵢ × bᵢ) = a₁×b₁ + a₂×b₂ + a₃×b₃ + ...
```

### Example:

```
king  = [0.4, 0.8, 0.2, -0.5]
queen = [0.5, 0.7, 0.1, -0.4]

king · queen = (0.4×0.5) + (0.8×0.7) + (0.2×0.1) + (-0.5×-0.4)
             = 0.20 + 0.56 + 0.02 + 0.20
             = 0.98

HIGH dot product = Similar direction = Similar meaning! ✓
```

---

## Step 8: Cosine Similarity

### Formula:

```
                  a · b
cos(θ) = ─────────────────────
          ||a|| × ||b||

where ||a|| = √(Σᵢ aᵢ²)  (magnitude/length of vector)
```

### Example:

```
Step 1: Calculate magnitudes

||king|| = √(0.4² + 0.8² + 0.2² + 0.5²)
         = √(0.16 + 0.64 + 0.04 + 0.25)
         = √1.09
         = 1.04

||queen|| = √(0.5² + 0.7² + 0.1² + 0.4²)
          = √(0.25 + 0.49 + 0.01 + 0.16)
          = √0.91
          = 0.95

Step 2: Calculate cosine similarity

cos(king, queen) = 0.98 / (1.04 × 0.95)
                 = 0.98 / 0.988
                 = 0.99
```

### Interpretation:

```
Range: -1 to +1

+1  = Exactly same direction (identical meaning)
 0  = Perpendicular (unrelated)
-1  = Opposite direction (opposite meaning)

0.99 = VERY similar! ✓
```

---

## Step 8.1: Euclidean Distance vs Dot Product vs Cosine - IMPORTANT!

> Teen measures hain - teen DIFFERENT cheezein measure karte hain!

### Quick Answer:

```
Euclidean Distance = KITNI DOOR hai? (physical distance)
Dot Product        = KITNA ALIGN hai? (direction + magnitude)
Cosine Similarity  = SAME DIRECTION mein hai? (sirf direction)

DIFFERENT concepts - DIFFERENT use cases!
```

### Visual Difference:

```
Case 1: Same direction, different lengths

        A ────────────────────► (magnitude 10)
        B ────────►              (magnitude 5)

        Euclidean Distance: LARGE (5 units apart)
        Dot Product:        HIGH (same direction, considers length)
        Cosine Similarity:  1.0 (perfect alignment!)


Case 2: Different directions, same length

        A ────────►

        B
        │
        │
        ▼

        Euclidean Distance: MEDIUM
        Dot Product:        ZERO (perpendicular!)
        Cosine Similarity:  0 (no alignment)


Case 3: Opposite directions

        A ────────►
        B ◄────────

        Euclidean Distance: LARGE
        Dot Product:        NEGATIVE (opposite!)
        Cosine Similarity:  -1 (completely opposite)
```

### Mathematical Comparison:

```
┌─────────────────────────────────────────────────────────────┐
│ Euclidean Distance:                                         │
│                                                             │
│ d(a,b) = √[(a₁-b₁)² + (a₂-b₂)² + ...]                      │
│                                                             │
│ - Measures: How FAR apart are the points?                   │
│ - Range: 0 to ∞                                             │
│ - 0 = Same point                                            │
│ - Large = Far apart                                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Dot Product:                                                │
│                                                             │
│ a·b = a₁×b₁ + a₂×b₂ + ...                                  │
│                                                             │
│ - Measures: How much do vectors ALIGN? (with magnitude)     │
│ - Range: -∞ to +∞                                           │
│ - Positive = Same direction                                 │
│ - Zero = Perpendicular                                      │
│ - Negative = Opposite direction                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Cosine Similarity:                                          │
│                                                             │
│ cos(θ) = (a·b) / (||a|| × ||b||)                           │
│                                                             │
│ - Measures: Direction alignment ONLY (ignores length)       │
│ - Range: -1 to +1                                           │
│ - +1 = Same direction                                       │
│ - 0 = Perpendicular                                         │
│ - -1 = Opposite direction                                   │
└─────────────────────────────────────────────────────────────┘
```

### Example: Same Numbers, Different Results

```
Vector A = [3, 0]
Vector B = [0, 3]
Vector C = [6, 0]

        Y
        ↑
      3 │  ● B(0,3)
        │
        │
    ────┼──●────────●────→ X
        0  A(3,0)   C(6,0)
```

**Euclidean Distances:**
```
d(A, B) = √[(3-0)² + (0-3)²] = √[9+9] = √18 = 4.24
d(A, C) = √[(3-6)² + (0-0)²] = √[9+0] = √9  = 3.0

Result: A is CLOSER to C than to B (distance-wise)
```

**Dot Products:**
```
A·B = (3×0) + (0×3) = 0 + 0 = 0      (perpendicular!)
A·C = (3×6) + (0×0) = 18 + 0 = 18    (aligned!)

Result: A is more ALIGNED with C than B
```

**Cosine Similarities:**
```
cos(A,B) = 0 / (3 × 3) = 0           (perpendicular)
cos(A,C) = 18 / (3 × 6) = 1.0        (same direction)

Result: A and C point SAME direction
```

### Key Insight: Length Problem with Dot Product

```
Problem:

A = [1, 0]       (small vector)
B = [1000, 0]    (huge vector, same direction as A)
C = [0.9, 0.1]   (similar to A, slightly different direction)

Dot Products:
A·B = 1×1000 = 1000   (huge!)
A·C = 0.9 + 0 = 0.9   (small)

Dot Product says: A is more similar to B than C
But A and C are actually more "similar" in meaning!

Solution: Use Cosine Similarity

cos(A,B) = 1000 / (1 × 1000) = 1.0
cos(A,C) = 0.9 / (1 × 0.906) = 0.99

Now both show high similarity (direction-wise)
```

### Word Embedding Scenario:

```
Problem with raw Dot Product:

"the"  = [0.001, 0.002, ...]  (common word, trained more, small values)
"king" = [0.5, 0.8, ...]      (less common, larger values)

Dot Product("the", "king") = Small (misleading!)

Solution: Cosine Similarity ignores magnitude
cos("the", "king") = Better comparison
```

### When to Use What?

| Measure | Use When | Example Use Case |
|---------|----------|------------------|
| Euclidean Distance | Actual distance in space matters | Clustering words into groups |
| Dot Product | Direction + magnitude both matter | Attention scores (Q·K) |
| Cosine Similarity | Only direction matters, not length | Finding semantically similar words |

### In Transformer (Attention):

```
Attention uses DOT PRODUCT:

scores = Q @ K.T    ← Dot Product!

Why Dot Product (not Cosine)?
1. Faster computation (no normalization needed)
2. Magnitude CAN carry meaning in attention
3. Scaled by √d_k to control large values

Formula:
Attention = softmax(Q @ K.T / √d_k) × V
                           ↑
                    scaling fixes magnitude issue
```

### Summary Comparison Table:

| Aspect | Euclidean | Dot Product | Cosine |
|--------|-----------|-------------|--------|
| Measures | Distance | Alignment + Size | Direction only |
| Formula | √Σ(aᵢ-bᵢ)² | Σ(aᵢ×bᵢ) | (a·b)/(‖a‖×‖b‖) |
| Range | 0 to ∞ | -∞ to +∞ | -1 to +1 |
| Length sensitive | ✅ Yes | ✅ Yes | ❌ No |
| Perpendicular vectors | Some distance | 0 | 0 |
| Opposite vectors | Large distance | Negative | -1 |
| Best for | Clustering | Attention | Word similarity |

### One Line Summary:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Euclidean = "Kitni door hai?" (distance in space)         │
│  Dot Product = "Kitna match karta hai?" (with magnitude)    │
│  Cosine = "Same direction mein hai?" (ignore magnitude)     │
│                                                             │
│  Different questions → Different measures → Different uses! │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Step 9: Word Analogy Mathematics

### The Famous: king - man + woman = queen

```
Vector arithmetic:

king  = [0.8, 0.6, 0.9, 0.7]
man   = [0.3, 0.2, 0.4, 0.8]
woman = [0.4, 0.8, 0.3, 0.7]

Calculation:
result = king - man + woman
       = [0.8-0.3+0.4, 0.6-0.2+0.8, 0.9-0.4+0.3, 0.7-0.8+0.7]
       = [0.9, 1.2, 0.8, 0.6]
```

### Finding nearest word:

```
queen = [0.9, 1.1, 0.8, 0.5]

Distance from result to queen:
d = √[(0.9-0.9)² + (1.2-1.1)² + (0.8-0.8)² + (0.6-0.5)²]
  = √[0 + 0.01 + 0 + 0.01]
  = √0.02
  = 0.14

VERY CLOSE! So answer ≈ queen ✓
```

### Visual:

```
        man ─────────────────► woman
         │                       │
         │  (same direction!)    │
         ▼                       ▼
       king ─────────────────► queen
```

---

## Step 10: Training Mathematics

### Objective:

```
Find matrix E such that:
- Similar words → Similar rows (small distance)
- Different words → Different rows (large distance)
```

### Loss Function:

```
L = Σ (predicted_similarity - actual_similarity)²
```

### Gradient Descent:

```
Repeat until convergence:
    1. Calculate loss L
    2. Calculate gradient ∂L/∂E
    3. Update: E_new = E_old - η × (∂L/∂E)

    where η = learning rate
```

### Update Rule:

```
For each element E[i][j]:

E[i][j] = E[i][j] - η × ∂L/∂E[i][j]
```

---

## Complete Mathematical Summary

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  INPUT:  word_id ∈ {0, 1, 2, ..., V-1}                     │
│                                                             │
│  EMBEDDING MATRIX:  E ∈ ℝ^(V×D)                            │
│                     V = vocabulary size                     │
│                     D = embedding dimension (512)           │
│                                                             │
│  LOOKUP:  e = E[word_id] ∈ ℝ^D                             │
│           or                                                │
│           e = one_hot(word_id) × E                         │
│                                                             │
│  SIMILARITY MEASURES:                                       │
│     Dot Product:  a·b = Σᵢ(aᵢ × bᵢ)                        │
│     Cosine:       (a·b)/(||a|| × ||b||)                    │
│     Euclidean:    √(Σᵢ(aᵢ - bᵢ)²)                          │
│                                                             │
│  TRAINING:  minimize L = Σ(pred - actual)²                 │
│             using gradient descent                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Formula Reference Table

| Concept | Formula |
|---------|---------|
| Embedding Matrix | E ∈ ℝ^(V×D) |
| Lookup | e = E[id] |
| One-hot Lookup | e = one_hot × E |
| Dot Product | a·b = Σᵢ(aᵢ × bᵢ) |
| Magnitude | \|\|a\|\| = √(Σᵢ aᵢ²) |
| Cosine Similarity | (a·b) / (\|\|a\|\| × \|\|b\|\|) |
| Euclidean Distance | d(a,b) = √(Σᵢ(aᵢ - bᵢ)²) |
| Word Analogy | a - b + c ≈ d |
| Gradient Update | E = E - η × ∇L |

---

## Step 11: 512D Visualization Techniques

> 512D directly visualize nahi ho sakta, but techniques hain!

### Problem:

```
Human brain: Max 3D visualize kar sakta hai
Embedding:   512D hai

512D → 2D/3D kaise laayein?
```

### Solution: Dimensionality Reduction

```
512 dimensions ──────► 2 or 3 dimensions
                 ↑
        (Mathematical techniques)
```

---

### Technique 1: PCA (Principal Component Analysis)

**Idea:**
```
512D mein bahut si directions hain
But MOST IMPORTANT directions sirf kuch hain

PCA finds: Top 2-3 most important directions
```

**Mathematics:**
```
Step 1: Data ka mean nikalo
        μ = (1/n) × Σ xᵢ

Step 2: Covariance matrix banao
        C = (1/n) × Σ (xᵢ - μ)(xᵢ - μ)ᵀ
        Shape: (512 × 512)

Step 3: Eigenvectors nikalo
        C × v = λ × v

        Top 2 eigenvectors = 2 most important directions

Step 4: Project karo
        x_2D = x_512D × [v₁, v₂]

        (512D) × (512×2) = (2D)
```

> **Complete Example:** [07_pca.md](./07_pca.md) - Har step ka detailed calculation with numbers

**Visual:**
```
Before PCA (512D - impossible to see):
"king"  = [0.4, 0.8, 0.2, ..., -0.5]  (512 numbers)
"queen" = [0.5, 0.7, 0.1, ..., -0.4]  (512 numbers)

After PCA (2D - can plot!):
"king"  = [2.3, 1.5]   ← Plot on graph!
"queen" = [2.1, 1.7]   ← Nearby point!
```

**Result:**
```
        Y (PC2)
        ↑
        │     • queen
        │     • king
        │           • prince
        │
        │                    • car
        │                    • truck
        │
    ────┼────────────────────────→ X (PC1)
        │
        │  • dog
        │  • cat
```

---

### Technique 2: t-SNE

**Idea:**
```
PCA: Global structure preserve karta hai
t-SNE: LOCAL structure preserve karta hai (clusters better dikhte)
```

**Mathematics (Simplified):**
```
Step 1: 512D mein har pair ka similarity nikalo

        p_ij = similarity("king", "queen") in 512D

        Using Gaussian:
        p_ij ∝ exp(-||xᵢ - xⱼ||² / 2σ²)

Step 2: 2D mein random points rakho

Step 3: 2D mein bhi similarity nikalo

        q_ij = similarity in 2D

        Using t-distribution:
        q_ij ∝ (1 + ||yᵢ - yⱼ||²)⁻¹

Step 4: p_ij aur q_ij ko match karo

        Minimize: KL(P || Q) = Σ pᵢⱼ × log(pᵢⱼ / qᵢⱼ)

        Using gradient descent!

Step 5: 2D points adjust hote hain until clusters form
```

**Visual Result:**
```
t-SNE typically gives better clusters:

        ┌─────────┐
        │ • king  │
        │ • queen │ Royalty
        │ • prince│ cluster
        └─────────┘
                        ┌─────────┐
                        │ • car   │
                        │ • truck │ Vehicle
                        │ • bus   │ cluster
                        └─────────┘

        ┌─────────┐
        │ • happy │
        │ • sad   │ Emotion
        │ • angry │ cluster
        └─────────┘
```

---

### Technique 3: UMAP

**Idea:**
```
Similar to t-SNE but:
- Faster
- Better global structure
- More scalable
```

**Mathematics (High-level):**
```
1. Build a graph of nearest neighbors in 512D
2. Optimize a low-dimensional representation
3. Preserve both local AND global structure
```

---

### Comparison Table:

| Technique | Speed | Local Structure | Global Structure | Best For |
|-----------|-------|-----------------|------------------|----------|
| PCA | Fast | ❌ | ✅ | Quick overview |
| t-SNE | Slow | ✅✅ | ❌ | Clusters |
| UMAP | Medium | ✅ | ✅ | Best of both |

---

### Real Example: Word Embeddings Visualization

```
Original 512D:
"king"    = [0.50, 0.68, -0.59, ..., 0.12]  (512 numbers)
"queen"   = [0.48, 0.71, -0.55, ..., 0.15]  (512 numbers)
"man"     = [0.32, 0.45, -0.71, ..., 0.08]  (512 numbers)
"woman"   = [0.35, 0.52, -0.68, ..., 0.11]  (512 numbers)
"car"     = [-0.45, 0.23, 0.67, ..., -0.34] (512 numbers)
"truck"   = [-0.42, 0.25, 0.64, ..., -0.31] (512 numbers)

After t-SNE to 2D:
"king"    = [3.2, 4.1]
"queen"   = [3.4, 4.3]    ← Close to king!
"man"     = [2.8, 3.5]
"woman"   = [3.0, 3.7]    ← Close to man!
"car"     = [-2.1, -1.5]
"truck"   = [-1.9, -1.3]  ← Close to car!
```

**Plot:**
```
            Y
            ↑
          5 │         • queen
            │        • king
          4 │
            │       • woman
            │      • man
          3 │
            │
          2 │
            │
          1 │
            │
    ────────┼────────────────────→ X
         -3 │-2  -1   0   1   2   3
            │
         -1 │    • truck
            │   • car
         -2 │
```

---

### Key Point:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  512D → 2D = INFORMATION LOSS hota hai!                    │
│                                                             │
│  But RELATIVE positions preserve hoti hain:                 │
│  - Similar words still close                                │
│  - Different words still far                                │
│                                                             │
│  Visualization ke liye enough hai                           │
│  Actual computation mein 512D hi use hota hai               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Visualization Summary:

| Question | Answer |
|----------|--------|
| 512D visualize ho sakta? | Directly nahi |
| Solution? | Reduce to 2D/3D |
| Techniques? | PCA, t-SNE, UMAP |
| Information loss? | Haan, but relative positions same |
| Best technique? | t-SNE for clusters, UMAP for both |

---

## Step 12: Weight Initialization

> Embedding matrix ke values initially kaise set hote hain?

### Problem:

```
Embedding Matrix E ∈ ℝ^(V×D)

V = 30,000 (vocab size)
D = 512 (dimensions)

Total values = 30,000 × 512 = 15,360,000

Ye 15 million values initially kya honge?
```

### Answer: Random Initialization

```
Values randomly initialize hote hain!

Common methods:

1. Normal Distribution:
   E[i][j] ~ N(0, σ²)
   where σ = 1/√D = 1/√512 ≈ 0.044

2. Uniform Distribution:
   E[i][j] ~ U(-a, a)
   where a = 1/√D

3. Xavier/Glorot Initialization:
   E[i][j] ~ N(0, 2/(fan_in + fan_out))
```

### Why Small Values?

```
Large initial values → Large gradients → Unstable training
Small initial values → Controlled gradients → Stable training

Typical range: -0.1 to +0.1
```

### Mathematical Example:

```
Normal initialization with σ = 0.044:

"king" initially = [0.023, -0.041, 0.015, -0.038, 0.052, ...]
"queen" initially = [-0.019, 0.033, -0.047, 0.028, -0.011, ...]

Completely RANDOM! No meaning yet.
After training → meaningful values
```

---

## Step 13: Special Tokens - IMPORTANT!

> Vocabulary mein kuch special words hote hain jo language nahi, control ke liye hain

### List of Special Tokens:

```
┌─────────────────────────────────────────────────────────────────┐
│ Token    │ Full Form           │ Purpose                        │
├──────────┼─────────────────────┼────────────────────────────────┤
│ <PAD>    │ Padding             │ Sequence length equal karna    │
│ <UNK>    │ Unknown             │ Out-of-vocabulary words        │
│ <SOS>    │ Start of Sequence   │ Decoder ko start signal        │
│ <EOS>    │ End of Sequence     │ Sentence khatam hua            │
│ <MASK>   │ Mask                │ BERT-style masked prediction   │
│ <CLS>    │ Classification      │ BERT mein sentence embedding   │
│ <SEP>    │ Separator           │ Do sentences alag karna        │
│ <BOS>    │ Beginning of Seq    │ Same as <SOS>                  │
└──────────┴─────────────────────┴────────────────────────────────┘
```

### Token IDs (Typical):

```
Vocab = {
    "<PAD>": 0,    ← Usually 0 (important for masking!)
    "<UNK>": 1,
    "<SOS>": 2,
    "<EOS>": 3,
    "<MASK>": 4,
    "<CLS>": 5,
    "<SEP>": 6,
    "the": 7,
    "a": 8,
    ...
    "king": 1523,
    ...
}
```

### <PAD> Token - Padding

```
Problem: Different length sentences

Sentence 1: "I love AI"           (3 words)
Sentence 2: "Machine learning is great"  (4 words)

Batch processing ke liye SAME length chahiye!

Solution: Padding

Sentence 1: "I love AI <PAD>"     (4 words) ✓
Sentence 2: "Machine learning is great"  (4 words) ✓

Token IDs:
Sentence 1: [5, 127, 893, 0]      ← 0 is <PAD>
Sentence 2: [234, 567, 89, 432]
```

### <UNK> Token - Unknown Words

```
Problem: Word not in vocabulary

Vocab has 30,000 words
User inputs: "cryptocurrency" (not in vocab!)

Solution: Replace with <UNK>

"I bought cryptocurrency" → "I bought <UNK>"
Token IDs: [5, 234, 1]    ← 1 is <UNK>
```

### <SOS> and <EOS> Tokens

```
Used in Sequence-to-Sequence models (Translation, etc.)

Encoder input:  "I love AI"
Decoder input:  "<SOS> मुझे AI पसंद है"
Decoder output: "मुझे AI पसंद है <EOS>"

<SOS> tells decoder: "Start generating!"
<EOS> tells decoder: "Stop generating!"
```

### <CLS> and <SEP> Tokens (BERT)

```
BERT input format:

Single sentence:
[<CLS>] I love AI [<SEP>]

Two sentences:
[<CLS>] I love AI [<SEP>] AI is amazing [<SEP>]

<CLS> embedding → Used for classification tasks
<SEP> → Separates sentences
```

### Special Token Embeddings

```
Special tokens bhi embedding matrix mein hote hain!

E[0] = <PAD> embedding = [0.01, -0.02, 0.03, ...]
E[1] = <UNK> embedding = [0.05, 0.02, -0.01, ...]
E[2] = <SOS> embedding = [-0.03, 0.04, 0.02, ...]

Ye bhi LEARNABLE hain! Training mein update hote hain.
```

---

## Step 14: Out-of-Vocabulary (OOV) Problem

> Kya karein jab word vocabulary mein nahi hai?

### Problem Statement:

```
Training vocabulary: 30,000 words
User input: "transformerify" (made-up word, not in vocab!)

Options:
1. Error throw karo? ❌ Bad UX
2. Ignore karo? ❌ Information loss
3. <UNK> use karo? ⚠️ Works, but loses meaning
4. Subword tokenization? ✅ Best solution!
```

### Solution 1: <UNK> Token (Simple but Lossy)

```
"I love transformerify" → "I love <UNK>"

Problem:
"transformerify" ≈ "cryptocurrency" ≈ "pneumonoultramicroscopicsilicovolcanoconiosis"

All become <UNK>! All meaning lost!
```

### Solution 2: Subword Tokenization (Better!)

```
"transformerify" → ["transform", "##er", "##ify"]

Each subword has its own embedding!
Meaning partially preserved:
- "transform" → related to change
- "##er" → agent suffix
- "##ify" → verb suffix
```

---

## Step 15: Subword Tokenization

> Words ko smaller pieces mein todna

### Why Subwords?

```
Problem with word-level:
- Huge vocabulary needed (100k+ words)
- OOV problem
- "playing", "played", "plays" = 3 different tokens

Problem with character-level:
- Too long sequences
- "hello" = ['h', 'e', 'l', 'l', 'o'] = 5 tokens
- Hard to learn meaning

Subword = Best of both!
- Moderate vocabulary (30k-50k)
- No OOV (can break any word)
- Meaningful pieces
```

### BPE (Byte Pair Encoding) Algorithm:

```
Step 1: Start with character vocabulary
        vocab = {a, b, c, ..., z, <space>}

Step 2: Count all adjacent pairs in corpus
        "low lower lowest"
        Pairs: (l,o)=3, (o,w)=3, (w,e)=2, (e,r)=1, (e,s)=1, (s,t)=1

Step 3: Merge most frequent pair
        (l,o) → "lo"
        vocab = {a, b, ..., z, lo}

Step 4: Repeat until vocab_size reached
        (lo,w) → "low"
        vocab = {a, b, ..., z, lo, low}

Final tokenization:
"lowest" → ["low", "est"]
"lower" → ["low", "er"]
```

### WordPiece (BERT uses this):

```
Similar to BPE, but uses likelihood instead of frequency

"playing" → ["play", "##ing"]
"unhappiness" → ["un", "##happy", "##ness"]

"##" prefix = continuation of previous token
```

### Example Tokenization:

```
Word-level:
"I love playing football" → ["I", "love", "playing", "football"]
4 tokens

Subword-level (WordPiece):
"I love playing football" → ["I", "love", "play", "##ing", "foot", "##ball"]
6 tokens (but smaller vocab, no OOV!)

Unknown word:
"transformerify" → ["transform", "##er", "##ify"]
3 tokens (no <UNK> needed!)
```

### Vocabulary Size Trade-off:

```
Small vocab (8k):
  + Less memory
  + Faster training
  - Longer sequences
  - More subwords per word

Large vocab (50k):
  + Shorter sequences
  + More whole words
  - More memory
  - Slower training

Sweet spot: 30k-50k for most tasks
```

---

## Step 16: Batch Processing and Padding

> Multiple sentences ek saath process karna

### Why Batching?

```
One sentence at a time:
- GPU underutilized
- Very slow training

Batch of 32 sentences:
- GPU fully utilized (parallel processing)
- 32x faster!
```

### Problem: Different Lengths

```
Batch of 3 sentences:

Sentence 1: "I love AI"           → 3 tokens
Sentence 2: "Hello"               → 1 token
Sentence 3: "This is amazing"     → 3 tokens

Cannot make a matrix! Different lengths!
```

### Solution: Padding

```
Find max length in batch = 3
Pad shorter sentences with <PAD> (token_id = 0)

Sentence 1: [23, 456, 789]       → [23, 456, 789]
Sentence 2: [12]                 → [12, 0, 0]      ← padded!
Sentence 3: [34, 56, 78]         → [34, 56, 78]

Now shape = (3, 3) = (batch_size, max_seq_len) ✓
```

### Padding Strategies:

```
1. Right Padding (most common):
   "Hello" → "Hello <PAD> <PAD>"
   [12, 0, 0]

2. Left Padding (for some generation tasks):
   "Hello" → "<PAD> <PAD> Hello"
   [0, 0, 12]
```

### After Embedding Lookup:

```
Input: (batch=3, seq_len=3)
       [[23, 456, 789],
        [12,   0,   0],
        [34,  56,  78]]

After Embedding: (batch=3, seq_len=3, d_model=512)
       [[[0.2, 0.3, ...],    ← "I"
         [0.4, 0.1, ...],    ← "love"
         [0.5, 0.2, ...]],   ← "AI"

        [[0.1, 0.4, ...],    ← "Hello"
         [0.01, 0.01, ...],  ← <PAD> embedding
         [0.01, 0.01, ...]],← <PAD> embedding

        [[0.3, 0.2, ...],    ← "This"
         [0.2, 0.5, ...],    ← "is"
         [0.4, 0.3, ...]]]   ← "amazing"
```

---

## Step 17: Padding Mask - CRITICAL!

> Attention ko batana ki <PAD> tokens ignore karo

### Problem:

```
Sentence: "Hello <PAD> <PAD>"

Without mask:
Attention will attend to <PAD> tokens!
"Hello" will look at <PAD> for context
→ Meaningless attention!
→ Wrong results!
```

### Solution: Padding Mask

```
Padding Mask = Boolean matrix
True = valid token (attend karo)
False = padding (ignore karo)

Sentence: [12, 0, 0]  ("Hello <PAD> <PAD>")
Mask:     [1, 0, 0]   (True, False, False)

Or: [True, False, False]
```

### How Mask is Applied:

```
Attention scores BEFORE mask:
scores = Q @ K.T
       = [[0.5, 0.3, 0.2],    ← "Hello" attending to all
          [0.4, 0.4, 0.2],
          [0.3, 0.3, 0.4]]

Mask: [1, 0, 0]

Attention scores AFTER mask:
scores = [[0.5, -∞, -∞],      ← <PAD> positions = -infinity
          [0.4, -∞, -∞],
          [0.3, -∞, -∞]]

After softmax:
attention = [[1.0, 0, 0],      ← All attention on "Hello"
             [1.0, 0, 0],
             [1.0, 0, 0]]

<PAD> tokens get ZERO attention! ✓
```

### Mask Mathematics:

```
mask = [1, 0, 0]

# Convert to attention mask
# 0 → -infinity, 1 → 0
attn_mask = (1 - mask) × (-∞)
          = [0, -∞, -∞]

# Add to scores
scores = scores + attn_mask
       = [0.5, 0.3, 0.2] + [0, -∞, -∞]
       = [0.5, -∞, -∞]

# Softmax
softmax([0.5, -∞, -∞]) = [1.0, 0, 0]

# e^(-∞) = 0, so padded positions become 0!
```

### Batch Mask:

```
Batch:
[[23, 456, 789],     mask: [[1, 1, 1],
 [12,   0,   0],            [1, 0, 0],
 [34,  56,   0]]            [1, 1, 0]]
```

---

## Step 18: Weight Tying / Embedding Sharing

> Input embedding aur Output embedding same use karna

### Normal Setup (Without Tying):

```
Input Embedding:  E_in  ∈ ℝ^(V×D)   → 30k × 512 = 15M params
Output Embedding: E_out ∈ ℝ^(D×V)   → 512 × 30k = 15M params

Total: 30M parameters just for embeddings!
```

### With Weight Tying:

```
E_in = E_out.T

Only ONE embedding matrix needed!
E ∈ ℝ^(V×D) → 15M parameters

Output projection: logits = hidden @ E.T

Saves 15M parameters! (50% reduction in embedding params)
```

### Why Does This Work?

```
Intuition:

If "king" embedding = [0.5, 0.8, 0.3, ...]

Input: "king" → lookup E["king"] → [0.5, 0.8, 0.3, ...]

Output: hidden = [0.5, 0.8, 0.3, ...]
        → should predict "king"
        → logits = hidden @ E.T
        → highest score for "king" ✓

Same embedding works for both directions!
```

### Transformer Paper:

```
"We share the same weight matrix between the two embedding layers
 and the pre-softmax linear transformation"

Three places, ONE matrix:
1. Source embedding
2. Target embedding
3. Output projection (before softmax)
```

---

## Step 19: Pre-trained vs Train from Scratch

> Kab pre-trained embeddings use karein?

### Option 1: Train from Scratch

```
Start: Random embeddings
Train: On your specific data
Result: Task-specific embeddings

When to use:
- Large dataset available (>1M examples)
- Domain-specific vocabulary (medical, legal)
- End-to-end training with Transformer
```

### Option 2: Pre-trained Embeddings

```
Popular pre-trained embeddings:

1. Word2Vec (Google, 2013)
   - 300 dimensions
   - Trained on Google News (100B words)

2. GloVe (Stanford, 2014)
   - 50, 100, 200, 300 dimensions
   - Trained on Wikipedia + Common Crawl

3. FastText (Facebook, 2016)
   - Subword-based
   - Handles OOV better

When to use:
- Small dataset
- Quick start
- General domain
```

### Comparison:

```
┌─────────────────────────────────────────────────────────────┐
│ Aspect          │ From Scratch    │ Pre-trained            │
├─────────────────┼─────────────────┼────────────────────────┤
│ Data needed     │ Lots (>1M)      │ Little                 │
│ Training time   │ Long            │ Short                  │
│ Domain fit      │ Perfect         │ General                │
│ OOV handling    │ Based on vocab  │ Based on pre-trained   │
│ Memory          │ Same            │ Same                   │
│ Recommended     │ Large projects  │ Small projects/POC     │
└─────────────────┴─────────────────┴────────────────────────┘
```

### Modern Approach (Transformers):

```
Don't use Word2Vec/GloVe!

Use pre-trained Transformer models instead:
- BERT (embeddings + contextualized)
- GPT (embeddings + contextualized)
- RoBERTa, ALBERT, etc.

These include embeddings that are:
- Contextual (same word, different meanings)
- Subword-based (no OOV)
- Much better performance
```

---

## Step 20: Memory and Computation Cost

> Embedding kitna resource leta hai?

### Memory Calculation:

```
Embedding Matrix: E ∈ ℝ^(V×D)

V = 30,000 (vocabulary size)
D = 512 (embedding dimension)

Total parameters = V × D = 30,000 × 512 = 15,360,000

Memory (float32 = 4 bytes):
= 15,360,000 × 4 bytes
= 61,440,000 bytes
= 61.44 MB

Memory (float16 = 2 bytes):
= 15,360,000 × 2 bytes
= 30.72 MB
```

### Comparison with Full Transformer:

```
Transformer Base:
- Embedding: 15M params (≈ 23% of total)
- Encoder/Decoder: 50M params
- Total: ~65M params

Transformer Large:
- Embedding: 30M params
- Encoder/Decoder: 300M params
- Total: ~330M params

GPT-3:
- Embedding: ~800M params
- Total: 175B params
- Embedding = 0.5% of total
```

### Computation Cost:

```
Embedding Lookup: O(1)

Just index into matrix - NO computation!
E[token_id] → direct memory access

This is why embeddings are efficient:
- No matrix multiplication
- No activation functions
- Just lookup!
```

### Batch Computation:

```
Batch of 32 sentences, each 100 tokens:
Total lookups = 32 × 100 = 3,200 lookups

Each lookup: O(1)
Total: O(batch × seq_len) = O(3,200)

Very fast! Embedding is NOT the bottleneck.
Attention is the bottleneck: O(n²)
```

---

# PART 2: Conceptual Understanding

> Intuition aur analogies se samjho

---

## Problem: Computer ko text nahi samajh aata

```
"Hello world" → Computer: ???

Computer sirf numbers samajhta hai!
```

---

## Solution 1: One-Hot Encoding (Purana tarika)

Vocabulary = [cat, dog, bird, fish] (4 words)

```
cat  → [1, 0, 0, 0]
dog  → [0, 1, 0, 0]
bird → [0, 0, 1, 0]
fish → [0, 0, 0, 1]
```

### Problems:

| Issue | Explanation |
|-------|-------------|
| Sparse | 10,000 vocab = 10,000 length vector, mostly zeros |
| No meaning | "cat" aur "dog" ka distance = "cat" aur "fish" ka distance |
| No relationship | Similar words bhi equally different dikhte hain |

---

## Solution 2: Embeddings (Modern tarika)

Har word → **Dense vector** (small, meaningful numbers)

```
cat  → [0.2, 0.8, -0.1, 0.5]    (sirf 4 numbers!)
dog  → [0.3, 0.7, -0.2, 0.4]    (cat ke paas!)
bird → [-0.5, 0.1, 0.9, 0.2]    (door)
fish → [-0.4, 0.0, 0.8, 0.3]    (bird ke paas!)
```

### Benefits:

| Benefit | Explanation |
|---------|-------------|
| Dense | 512 dimensions mein poora meaning |
| Semantic | Similar words → similar vectors |
| Learned | Training mein automatically seekhta hai |

---

## Embedding Kaise Kaam Karta Hai?

### Step 1: Vocabulary Banana

```
Vocab = {"<pad>": 0, "<sos>": 1, "<eos>": 2, "hello": 3, "world": 4, ...}

Total words = vocab_size (e.g., 30,000)
```

### Step 2: Embedding Matrix (Lookup Table)

```
Embedding Matrix shape: (vocab_size, d_model)
                        (30,000 × 512)

Row 0    → <pad> ka 512-dim vector
Row 1    → <sos> ka 512-dim vector
Row 3    → "hello" ka 512-dim vector
Row 4    → "world" ka 512-dim vector
...
Row 29999 → last word ka vector
```

### Step 3: Lookup Operation

```
Input: "hello world"
        ↓
Token IDs: [3, 4]
        ↓
Lookup: Row 3 nikalo, Row 4 nikalo
        ↓
Output: [[0.2, 0.1, ...512 numbers...],    ← "hello"
         [0.3, 0.5, ...512 numbers...]]    ← "world"

Shape: (2, 512) = (seq_len, d_model)
```

---

## Visualize: Embedding as Table Lookup

```
Token ID = 3 ("hello")
                ↓
    ┌─────────────────────────────┐
    │  Embedding Matrix           │
    │  (30,000 rows × 512 cols)   │
    ├─────────────────────────────┤
Row 0 │ [0.1, 0.2, 0.3, ...]       │ ← <pad>
Row 1 │ [0.4, 0.5, 0.6, ...]       │ ← <sos>
Row 2 │ [0.7, 0.8, 0.9, ...]       │ ← <eos>
Row 3 │ [0.2, 0.1, 0.4, ...] ◄────│ ← "hello" (YE NIKALO!)
Row 4 │ [0.3, 0.5, 0.2, ...]       │ ← "world"
    │  ...                        │
    └─────────────────────────────┘
```

---

## Dimensions Samjho

| Term | Value | Meaning |
|------|-------|---------|
| vocab_size | 30,000 | Total unique words |
| d_model | 512 | Each word's vector size |
| seq_len | 100 | Sentence mein kitne words |
| batch_size | 32 | Kitne sentences ek saath |

### Shape Flow:

```
Input tokens:     (batch, seq_len)          = (32, 100)
                         ↓ Embedding lookup
Output vectors:   (batch, seq_len, d_model) = (32, 100, 512)
```

---

## d_model = 512 Kyun?

**512 dimensions = 512 features jo word describe karte hain**

Imagine each dimension captures something:

```
Dimension 1:  Living ←――――→ Non-living
Dimension 2:  Male ←――――→ Female
Dimension 3:  Singular ←――――→ Plural
Dimension 4:  Positive ←――――→ Negative
...
Dimension 512: (some abstract feature)
```

Reality mein ye interpretable nahi hote, but model automatically meaningful patterns seekhta hai.

---

## Embeddings Kaise Seekhte Hain?

### Initially (Random):
```
"king"  → [0.52, -0.31, 0.87, ...]  (random numbers)
"queen" → [-0.12, 0.45, 0.23, ...]  (random numbers)
```

### After Training:
```
"king"  → [0.8, 0.2, 0.9, -0.1, ...]
"queen" → [0.7, 0.8, 0.9, -0.1, ...]
           ↑    ↑
         Close! Similar meaning

"king" - "man" + "woman" ≈ "queen"  ← Famous example!
```

Training mein backpropagation se embedding matrix ke values update hote hain.

---

## Transformer Paper: Scaling by √d_model

Paper mein likha hai:
```
Embedding output = Embedding(x) × √d_model
```

### Kyun?

```
Embedding values: typically small (-1 to 1 range)
Positional Encoding values: also -1 to 1 range

Problem: Embedding values bahut chhote ho sakte hain
Solution: √512 ≈ 22.6 se multiply → values balanced

Embedding + Positional Encoding = dono ka contribution equal
```

---

## Complete Picture: Token → Embedding → Positional → Encoder

```
"I love AI"
     ↓
[5, 127, 893]              ← Token IDs
     ↓
┌─────────────┐
│  Embedding  │            ← Lookup table
│   Matrix    │
└─────────────┘
     ↓
(3, 512) × √512            ← Scale karo
     ↓
    (+)
     ↓
┌─────────────┐
│ Positional  │            ← Position info add
│  Encoding   │
└─────────────┘
     ↓
(3, 512)                   ← Ready for Encoder!
```

---

## Key Takeaways

| Concept | Summary |
|---------|---------|
| Embedding | Word → Dense vector (lookup table) |
| vocab_size | Total unique tokens (30k-50k typical) |
| d_model | Vector dimension (512 in base Transformer) |
| Learning | Backpropagation se values update |
| Scaling | × √d_model for balance with positional encoding |
| Output shape | (batch, seq_len, d_model) |

---

## Questions to Think About

1. Agar do words similar context mein use hote hain, unke embeddings similar kyun honge?

2. Subword tokenization (BPE) mein "playing" → ["play", "##ing"] - dono ke alag embeddings hain. Final meaning kaise milta hai?

3. Embedding matrix mein 30,000 × 512 = 15 million parameters hain. Ye trainable hain!

---

## Connection to Next Topics

| Current | Next |
|---------|------|
| Embedding gives meaning | But NO position info! |
| "I love you" = "you love I" | Same embeddings, different meaning |
| Solution? | **Positional Encoding** |

---

*Document Created: 2026-01-18*

*Updated: 2026-01-19*
- Reorganized (Mathematics First)
- Added: Euclidean vs Dot Product vs Cosine comparison
- Added: Weight Initialization
- Added: Special Tokens (<PAD>, <UNK>, <SOS>, <EOS>, etc.)
- Added: OOV Problem
- Added: Subword Tokenization (BPE, WordPiece)
- Added: Batch Processing + Padding
- Added: Padding Mask (Critical!)
- Added: Weight Tying/Sharing
- Added: Pre-trained vs Train from Scratch
- Added: Memory/Computation Cost

*Part of: Transformer Implementation Learning Series*

*Total Steps: 20 (Mathematics) + Conceptual Understanding*

---

## Document Table of Contents

### PART 1: Mathematics
| Step | Topic |
|------|-------|
| 1 | Vector Basics |
| 2 | Vector as Point |
| 3 | Embedding Matrix |
| 4 | Lookup = Row Selection |
| 5 | One-Hot × Matrix = Lookup |
| 6 | Euclidean Distance |
| 7 | Dot Product |
| 8 | Cosine Similarity |
| 8.1 | **Euclidean vs Dot Product vs Cosine** |
| 9 | Word Analogy Mathematics |
| 10 | Training Mathematics |
| - | Formula Reference Table |
| 11 | 512D Visualization (PCA, t-SNE, UMAP) |
| 12 | Weight Initialization |
| 13 | **Special Tokens** |
| 14 | OOV Problem |
| 15 | Subword Tokenization |
| 16 | Batch Processing + Padding |
| 17 | **Padding Mask** |
| 18 | Weight Tying/Sharing |
| 19 | Pre-trained vs Train from Scratch |
| 20 | Memory/Computation Cost |

### PART 2: Conceptual
| Topic |
|-------|
| Problem Statement |
| One-Hot vs Embeddings |
| How Embedding Works |
| Dimensions Explained |
| How Embeddings Learn |
| Scaling by √d_model |
| Complete Picture |
| Key Takeaways |
