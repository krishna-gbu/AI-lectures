# PCA Complete Example: 3D → 2D

> Yeh document Transformer_Mathematics.md ka supplement hai. PCA ka har step detail mein explain kiya gaya hai.

---

# PART 1: THEORY (KYU Kar Rahe Hain?)

---

## Problem: 512 Dimensions Visualize Nahi Ho Sakte

```
Human brain: Maximum 3D samajh sakta hai (x, y, z)

Embedding:   512 dimensions hai

Problem:     512D ko paper pe kaise dikhayein?
```

**Goal:** 512D → 2D convert karo **WITHOUT losing important information**

---

## Core Theory: VARIANCE = INFORMATION

**Key Insight:** Jis direction mein data ZYADA spread hai, woh direction ZYADA important hai.

```
Example: Class mein students ke marks

Subject 1 (Math):    Sab ke marks: 85, 86, 84, 85, 87
                     Range: 84-87 (sirf 3 marks difference)
                     Variance: LOW
                     Information: LESS (sab same hain!)

Subject 2 (English): Sab ke marks: 45, 92, 30, 78, 65
                     Range: 30-92 (62 marks difference!)
                     Variance: HIGH
                     Information: MORE (difference dikhai de raha hai)
```

**Conclusion:** High variance = High information = Important direction

---

## Theory Step 1: KYU Mean Subtract Karte Hain?

**Problem:** Data center pe nahi hai

```
Example:
Original data:     [100, 101, 102, 103]
Mean:              101.5

Agar directly use karein:
  - Numbers bade hain (100+)
  - But actual variation sirf 3 hai!
  - Scale confuse karega
```

**Solution:** Data ko origin (0,0) pe lao

```
After centering:   [100-101.5, 101-101.5, 102-101.5, 103-101.5]
                 = [-1.5, -0.5, 0.5, 1.5]

Ab:
  - Mean = 0
  - Sirf variation dikhai de rahi hai
  - Scale correct hai
```

**Theory:** Centering removes the "location" and keeps only the "spread"

---

## Theory Step 2: KYU Covariance Matrix?

**Question:** Kaun si direction mein data sabse zyada spread hai?

**Problem:** 512 dimensions hain - manually check karna impossible!

**Solution:** Covariance Matrix automatically bata deta hai

```
Covariance Matrix ka meaning:

C[i][j] = How much dimension i and dimension j move TOGETHER

C = [C₁₁  C₁₂  C₁₃]
    [C₂₁  C₂₂  C₂₃]
    [C₃₁  C₃₂  C₃₃]

C₁₁ = Variance of dimension 1 (how much dim 1 spreads)
C₂₂ = Variance of dimension 2 (how much dim 2 spreads)
C₁₂ = Covariance of dim 1 & 2 (do they move together?)
```

**Example:**

```
Height aur Weight:
  - Tall people generally heavy hote hain
  - Short people generally light hote hain
  - Height ↑ toh Weight ↑
  - Covariance: POSITIVE (move together)

Age aur Hair count:
  - Age ↑ toh Hair ↓ (generally)
  - Covariance: NEGATIVE (opposite direction)

Shoe size aur IQ:
  - No relation
  - Covariance: NEAR ZERO (independent)
```

---

## Theory Step 3: KYU Eigenvectors?

**Yeh sabse important theory hai!**

### Eigenvector Kya Hai?

```
Normal vector:   Matrix multiply karo → Direction CHANGE ho jaati hai
Eigenvector:     Matrix multiply karo → Direction SAME rehti hai, sirf stretch hota hai

C × v = λ × v

Matlab: Covariance matrix v ko multiply karo
        Result: Same direction, but λ times stretched
```

### KYU Eigenvector Best Direction Hai?

**Geometric Intuition:**

```
Imagine data ek ELLIPSE (anda shape) hai 2D mein:

        *  *  *
     *          *
    *            *
     *          *
        *  *  *

Ellipse ke 2 axes hain:
  - Long axis (major) → Maximum spread
  - Short axis (minor) → Minimum spread
```

**Eigenvectors = Ellipse ke axes!**

```
λ₁ (large eigenvalue) → v₁ points along LONG axis → Maximum variance
λ₂ (small eigenvalue) → v₂ points along SHORT axis → Minimum variance
```

**Mathematical Proof (simplified):**

```
Question: Kaun si direction mein variance maximum hai?

Maximize:  Variance along direction v
           = vᵀ × C × v

Constraint: v ka length = 1 (unit vector)
           ||v|| = 1

Solution (Lagrange multiplier):
           C × v = λ × v

Yeh eigenvector equation hai!

Conclusion: Maximum variance direction = Eigenvector with largest eigenvalue
```

---

## Theory Step 4: KYU Eigenvalue = Variance?

```
Eigenvalue λ = Variance along that eigenvector direction

λ₁ = 2.5  → Direction v₁ mein variance 2.5 hai
λ₂ = 0.25 → Direction v₂ mein variance 0.25 hai
λ₃ = 0    → Direction v₃ mein variance 0 hai (no information!)
```

**Variance Explained:**

```
Total variance = λ₁ + λ₂ + λ₃ = 2.5 + 0.25 + 0 = 2.75

v₁ explains: 2.5/2.75 = 91% of total variance
v₂ explains: 0.25/2.75 = 9% of total variance
v₃ explains: 0/2.75 = 0% of total variance

Top 2 directions: 91% + 9% = 100% information captured!
```

---

## Theory Step 5: KYU Projection?

**Projection = Shadow dalna**

```
3D object hai, 2D paper pe shadow daalo

        ☀️ (Light source)
         |
         ▼
    [3D Object]
         |
         ▼
    ═══════════ (2D Paper)
      Shadow
```

**Mathematical Projection:**

```
Original point: x = [x₁, x₂, x₃] (3D)

Direction v₁ = [a, b, c]

Projection on v₁ = x · v₁ = x₁×a + x₂×b + x₃×c (1 number)

Yeh number batata hai: "v₁ direction mein kitna door hai?"
```

**Why project on eigenvectors?**

```
Because eigenvectors are ORTHOGONAL (90° angle)

v₁ ⊥ v₂ ⊥ v₃

No information overlap!
Each eigenvector captures UNIQUE information.
```

---

## Complete Theory Summary

| Step | Kya Karte Hain | Kyun Karte Hain |
|------|----------------|-----------------|
| **Mean subtract** | Data ko center pe lao | Location hatao, sirf spread rakho |
| **Covariance Matrix** | Dimensions ka relationship nikalo | Automatically find karo kahan spread hai |
| **Eigenvalues** | Har direction ki variance nikalo | Rank karo - kaunsi direction important |
| **Eigenvectors** | Best directions nikalo | Maximum information wali directions |
| **Sort by λ** | Bade eigenvalue pehle | Important directions pehle |
| **Project** | Data ko new directions pe daalo | 512D → 2D without losing info |

---

## Intuitive Analogy: Photography

```
Situation: 3D statue hai, 2D photo leni hai

Bad photographer:
  - Random angle se photo li
  - Statue ka sirf side dikha
  - Information lost!

Good photographer (PCA):
  - Pehle statue ghoom ke dekha
  - Best angle dhundha (maximum features dikhein)
  - Woh angle se photo li
  - Maximum information captured!

PCA = Finding the BEST ANGLE to view high-dimensional data
```

---

## Why Covariance Matrix Symmetric Hai?

```
C[i][j] = C[j][i]

Because:
  Covariance(X, Y) = Covariance(Y, X)

  "X aur Y saath move karte hain" = "Y aur X saath move karte hain"

Symmetric matrix ka property:
  - Eigenvalues always REAL numbers (no imaginary)
  - Eigenvectors always ORTHOGONAL (90° angle)
```

---

## Why Eigenvectors Orthogonal Hote Hain?

```
Symmetric matrix ka mathematical property:

If C is symmetric, then:
  v₁ · v₂ = 0 (perpendicular)

Intuition:
  - v₁ captures maximum variance
  - v₂ captures maximum REMAINING variance
  - v₂ cannot overlap with v₁
  - So v₂ must be perpendicular to v₁

Like building axes:
  X-axis ⊥ Y-axis ⊥ Z-axis
  Each axis captures independent information
```

---

## PCA Theory in One Line

```
"Find the directions where data varies the most,
 and project data onto those directions"

512D → 2D:
  - Find 2 directions with maximum variance (eigenvectors)
  - Project all points onto those 2 directions
  - Result: 2D representation with maximum preserved information
```

---

# PART 2: MATHEMATICS (Step-by-Step Example)

---

## Step 0: Data

4 words ke 3D embeddings:

```
"king"  = [4, 2, 1]
"queen" = [4, 3, 1]
"man"   = [1, 2, 0]
"woman" = [1, 3, 0]
```

---

## Step 1: Mean Nikalo

**Formula:** μ = (1/n) × Σ xᵢ

```
n = 4 (4 words hain)

Sum = [4, 2, 1] + [4, 3, 1] + [1, 2, 0] + [1, 3, 0]

Dimension 1: 4 + 4 + 1 + 1 = 10
Dimension 2: 2 + 3 + 2 + 3 = 10
Dimension 3: 1 + 1 + 0 + 0 = 2

Sum = [10, 10, 2]

μ = [10, 10, 2] / 4
μ = [10/4, 10/4, 2/4]
μ = [2.5, 2.5, 0.5]
```

---

## Step 2: Mean Subtract Karo (Centering)

**Formula:** xᵢ_centered = xᵢ - μ

**"king":**
```
[4, 2, 1] - [2.5, 2.5, 0.5]
= [4-2.5, 2-2.5, 1-0.5]
= [1.5, -0.5, 0.5]
```

**"queen":**
```
[4, 3, 1] - [2.5, 2.5, 0.5]
= [4-2.5, 3-2.5, 1-0.5]
= [1.5, 0.5, 0.5]
```

**"man":**
```
[1, 2, 0] - [2.5, 2.5, 0.5]
= [1-2.5, 2-2.5, 0-0.5]
= [-1.5, -0.5, -0.5]
```

**"woman":**
```
[1, 3, 0] - [2.5, 2.5, 0.5]
= [1-2.5, 3-2.5, 0-0.5]
= [-1.5, 0.5, -0.5]
```

**Centered Data:**
```
"king"  = [1.5, -0.5, 0.5]
"queen" = [1.5, 0.5, 0.5]
"man"   = [-1.5, -0.5, -0.5]
"woman" = [-1.5, 0.5, -0.5]
```

---

## Step 3: Covariance Matrix Banao

**Formula:** C = (1/n) × Σ (xᵢ)(xᵢ)ᵀ

**Outer product kya hai?**

```
Vector x = [a, b, c]

x × xᵀ = [a]             [a×a  a×b  a×c]
         [b] × [a b c] = [b×a  b×b  b×c]
         [c]             [c×a  c×b  c×c]
```

---

### "king" = [1.5, -0.5, 0.5]

```
[1.5 ]
[-0.5] × [1.5  -0.5  0.5]
[0.5 ]

Row 1: [1.5×1.5,   1.5×(-0.5),   1.5×0.5  ]
     = [2.25,      -0.75,        0.75     ]

Row 2: [(-0.5)×1.5,  (-0.5)×(-0.5),  (-0.5)×0.5]
     = [-0.75,       0.25,           -0.25     ]

Row 3: [0.5×1.5,   0.5×(-0.5),   0.5×0.5]
     = [0.75,      -0.25,        0.25   ]

Matrix_king = [2.25   -0.75   0.75]
              [-0.75   0.25  -0.25]
              [0.75   -0.25   0.25]
```

---

### "queen" = [1.5, 0.5, 0.5]

```
[1.5]
[0.5] × [1.5  0.5  0.5]
[0.5]

Row 1: [1.5×1.5,   1.5×0.5,   1.5×0.5]
     = [2.25,      0.75,      0.75   ]

Row 2: [0.5×1.5,   0.5×0.5,   0.5×0.5]
     = [0.75,      0.25,      0.25   ]

Row 3: [0.5×1.5,   0.5×0.5,   0.5×0.5]
     = [0.75,      0.25,      0.25   ]

Matrix_queen = [2.25   0.75   0.75]
               [0.75   0.25   0.25]
               [0.75   0.25   0.25]
```

---

### "man" = [-1.5, -0.5, -0.5]

```
[-1.5]
[-0.5] × [-1.5  -0.5  -0.5]
[-0.5]

Row 1: [(-1.5)×(-1.5),  (-1.5)×(-0.5),  (-1.5)×(-0.5)]
     = [2.25,           0.75,           0.75         ]

Row 2: [(-0.5)×(-1.5),  (-0.5)×(-0.5),  (-0.5)×(-0.5)]
     = [0.75,           0.25,           0.25         ]

Row 3: [(-0.5)×(-1.5),  (-0.5)×(-0.5),  (-0.5)×(-0.5)]
     = [0.75,           0.25,           0.25         ]

Matrix_man = [2.25   0.75   0.75]
             [0.75   0.25   0.25]
             [0.75   0.25   0.25]
```

---

### "woman" = [-1.5, 0.5, -0.5]

```
[-1.5]
[0.5 ] × [-1.5  0.5  -0.5]
[-0.5]

Row 1: [(-1.5)×(-1.5),  (-1.5)×0.5,  (-1.5)×(-0.5)]
     = [2.25,          -0.75,        0.75         ]

Row 2: [0.5×(-1.5),  0.5×0.5,  0.5×(-0.5)]
     = [-0.75,       0.25,     -0.25     ]

Row 3: [(-0.5)×(-1.5),  (-0.5)×0.5,  (-0.5)×(-0.5)]
     = [0.75,          -0.25,        0.25         ]

Matrix_woman = [2.25   -0.75   0.75]
               [-0.75   0.25  -0.25]
               [0.75   -0.25   0.25]
```

---

### Sum of All 4 Matrices

```
Matrix_king  = [2.25   -0.75   0.75]
               [-0.75   0.25  -0.25]
               [0.75   -0.25   0.25]

Matrix_queen = [2.25   0.75   0.75]
               [0.75   0.25   0.25]
               [0.75   0.25   0.25]

Matrix_man   = [2.25   0.75   0.75]
               [0.75   0.25   0.25]
               [0.75   0.25   0.25]

Matrix_woman = [2.25   -0.75   0.75]
               [-0.75   0.25  -0.25]
               [0.75   -0.25   0.25]
```

**Position (1,1):** 2.25 + 2.25 + 2.25 + 2.25 = 9.0
**Position (1,2):** -0.75 + 0.75 + 0.75 + (-0.75) = 0.0
**Position (1,3):** 0.75 + 0.75 + 0.75 + 0.75 = 3.0
**Position (2,1):** -0.75 + 0.75 + 0.75 + (-0.75) = 0.0
**Position (2,2):** 0.25 + 0.25 + 0.25 + 0.25 = 1.0
**Position (2,3):** -0.25 + 0.25 + 0.25 + (-0.25) = 0.0
**Position (3,1):** 0.75 + 0.75 + 0.75 + 0.75 = 3.0
**Position (3,2):** -0.25 + 0.25 + 0.25 + (-0.25) = 0.0
**Position (3,3):** 0.25 + 0.25 + 0.25 + 0.25 = 1.0

```
Sum = [9.0   0.0   3.0]
      [0.0   1.0   0.0]
      [3.0   0.0   1.0]
```

---

### Divide by n = 4

```
C = Sum / 4

C = [9.0/4   0.0/4   3.0/4]
    [0.0/4   1.0/4   0.0/4]
    [3.0/4   0.0/4   1.0/4]

C = [2.25   0.0    0.75]
    [0.0    0.25   0.0 ]
    [0.75   0.0    0.25]
```

**Yeh hai Covariance Matrix!**

---

## Step 4: Eigenvalues Nikalo

**Formula:** det(C - λI) = 0

**Identity Matrix I:**
```
I = [1  0  0]
    [0  1  0]
    [0  0  1]
```

**λI:**
```
λI = [λ  0  0]
     [0  λ  0]
     [0  0  λ]
```

**C - λI:**
```
C - λI = [2.25-λ   0       0.75  ]
         [0        0.25-λ  0     ]
         [0.75     0       0.25-λ]
```

---

### Determinant Nikalo

**3×3 determinant formula (middle row expansion - kyunki zeros hain):**

```
det = a₂₁ × M₂₁ - a₂₂ × M₂₂ + a₂₃ × M₂₃

Where:
a₂₁ = 0
a₂₂ = (0.25-λ)
a₂₃ = 0
```

Using cofactor expansion along row 2:

```
det = a₂₂ × C₂₂
det = (0.25-λ) × M₂₂
```

**M₂₂ = Minor at position (2,2):**

Delete row 2 and column 2:
```
M₂₂ = det([2.25-λ   0.75  ])
          ([0.75     0.25-λ])

M₂₂ = (2.25-λ)(0.25-λ) - (0.75)(0.75)
```

---

### (2.25-λ)(0.25-λ) expand karo

```
(2.25-λ)(0.25-λ)

= 2.25 × 0.25 + 2.25 × (-λ) + (-λ) × 0.25 + (-λ) × (-λ)

= 0.5625 - 2.25λ - 0.25λ + λ²

= λ² - 2.5λ + 0.5625
```

---

### M₂₂ calculate karo

```
M₂₂ = (2.25-λ)(0.25-λ) - (0.75)(0.75)

M₂₂ = λ² - 2.5λ + 0.5625 - 0.5625

M₂₂ = λ² - 2.5λ
```

---

### Full determinant

```
det(C - λI) = (0.25-λ) × M₂₂

= (0.25-λ) × (λ² - 2.5λ)

= (0.25-λ) × λ × (λ - 2.5)
```

---

### Set det = 0

```
(0.25-λ) × λ × (λ - 2.5) = 0
```

**Three solutions:**

```
0.25 - λ = 0  →  λ = 0.25
λ = 0         →  λ = 0
λ - 2.5 = 0   →  λ = 2.5
```

**Eigenvalues (sorted by size):**
```
λ₁ = 2.5    (largest - most important!)
λ₂ = 0.25   (second)
λ₃ = 0      (smallest - least important)
```

---

## Step 5: Eigenvector for λ₁ = 2.5

**Formula:** (C - λI) × v = 0

**C - 2.5I:**
```
[2.25-2.5    0         0.75    ]
[0          0.25-2.5   0       ]
[0.75       0          0.25-2.5]

= [-0.25    0       0.75 ]
  [0       -2.25    0    ]
  [0.75     0      -2.25 ]
```

**Equation:**
```
[-0.25    0       0.75 ] [v₁]   [0]
[0       -2.25    0    ] [v₂] = [0]
[0.75     0      -2.25 ] [v₃]   [0]
```

---

### Row 1 × Vector

```
[-0.25, 0, 0.75] · [v₁, v₂, v₃] = 0

(-0.25) × v₁ + 0 × v₂ + 0.75 × v₃ = 0

-0.25v₁ + 0.75v₃ = 0
```

**Solve for v₁:**
```
-0.25v₁ = -0.75v₃

v₁ = -0.75v₃ / -0.25

v₁ = 0.75v₃ / 0.25

v₁ = 3v₃
```

---

### Row 2 × Vector

```
[0, -2.25, 0] · [v₁, v₂, v₃] = 0

0 × v₁ + (-2.25) × v₂ + 0 × v₃ = 0

-2.25v₂ = 0

v₂ = 0
```

---

### Row 3 × Vector (Verify)

```
[0.75, 0, -2.25] · [v₁, v₂, v₃] = 0

0.75 × v₁ + 0 × v₂ + (-2.25) × v₃ = 0

0.75v₁ - 2.25v₃ = 0

0.75v₁ = 2.25v₃

v₁ = 2.25v₃ / 0.75

v₁ = 3v₃  ✓ (same as Row 1!)
```

---

### Choose v₃ = 1

```
v₃ = 1
v₁ = 3 × v₃ = 3 × 1 = 3
v₂ = 0

Eigenvector = [3, 0, 1]
```

---

### Normalize Eigenvector

**Length nikalo:**
```
||v|| = √(v₁² + v₂² + v₃²)

||v|| = √(3² + 0² + 1²)

||v|| = √(9 + 0 + 1)

||v|| = √10

||v|| = 3.162
```

**Divide each component by length:**
```
v₁_norm = v₁ / ||v|| = 3 / 3.162 = 0.949 ≈ 0.95

v₂_norm = v₂ / ||v|| = 0 / 3.162 = 0

v₃_norm = v₃ / ||v|| = 1 / 3.162 = 0.316 ≈ 0.32
```

**Normalized Eigenvector for λ₁ = 2.5:**
```
v₁ = [0.95, 0, 0.32]
```

---

## Step 6: Eigenvector for λ₂ = 0.25

**C - 0.25I:**
```
[2.25-0.25    0          0.75     ]
[0           0.25-0.25   0        ]
[0.75        0           0.25-0.25]

= [2.0    0    0.75]
  [0      0    0   ]
  [0.75   0    0   ]
```

**Equation:**
```
[2.0    0    0.75] [v₁]   [0]
[0      0    0   ] [v₂] = [0]
[0.75   0    0   ] [v₃]   [0]
```

---

### Row 1 × Vector

```
2.0v₁ + 0v₂ + 0.75v₃ = 0

2.0v₁ + 0.75v₃ = 0

2.0v₁ = -0.75v₃

v₁ = -0.375v₃
```

---

### Row 2 × Vector

```
0v₁ + 0v₂ + 0v₃ = 0

0 = 0  (always true - no constraint on v₂!)
```

**v₂ can be anything!** This means v₂ is free.

---

### Row 3 × Vector

```
0.75v₁ + 0v₂ + 0v₃ = 0

0.75v₁ = 0

v₁ = 0
```

---

### Combine Results

From Row 3: v₁ = 0
From Row 1: v₁ = -0.375v₃

```
0 = -0.375v₃
v₃ = 0
```

So: v₁ = 0, v₃ = 0, v₂ = free

**Choose v₂ = 1:**
```
Eigenvector = [0, 1, 0]
```

**Already normalized** (length = 1):
```
||v|| = √(0² + 1² + 0²) = √1 = 1 ✓

v₂ = [0, 1, 0]
```

---

## Step 7: Eigenvector for λ₃ = 0

**C - 0I = C:**
```
[2.25   0.0    0.75]
[0.0    0.25   0.0 ]
[0.75   0.0    0.25]
```

**Equation:**
```
[2.25   0.0    0.75] [v₁]   [0]
[0.0    0.25   0.0 ] [v₂] = [0]
[0.75   0.0    0.25] [v₃]   [0]
```

---

### Row 2 × Vector

```
0v₁ + 0.25v₂ + 0v₃ = 0

0.25v₂ = 0

v₂ = 0
```

---

### Row 1 × Vector

```
2.25v₁ + 0v₂ + 0.75v₃ = 0

2.25v₁ + 0.75v₃ = 0

2.25v₁ = -0.75v₃

v₁ = -0.75v₃ / 2.25

v₁ = -v₃/3

v₁ = -0.333v₃
```

---

### Row 3 × Vector (Verify)

```
0.75v₁ + 0v₂ + 0.25v₃ = 0

0.75v₁ + 0.25v₃ = 0

0.75v₁ = -0.25v₃

v₁ = -0.25v₃ / 0.75

v₁ = -v₃/3

v₁ = -0.333v₃  ✓ (same!)
```

---

### Choose v₃ = 1

```
v₃ = 1
v₁ = -0.333 × 1 = -0.333
v₂ = 0

Eigenvector = [-0.333, 0, 1]
```

---

### Normalize

**Length:**
```
||v|| = √((-0.333)² + 0² + 1²)

||v|| = √(0.111 + 0 + 1)

||v|| = √1.111

||v|| = 1.054
```

**Normalize:**
```
v₁_norm = -0.333 / 1.054 = -0.316 ≈ -0.32

v₂_norm = 0 / 1.054 = 0

v₃_norm = 1 / 1.054 = 0.949 ≈ 0.95
```

**Normalized Eigenvector for λ₃ = 0:**
```
v₃ = [-0.32, 0, 0.95]
```

---

## Step 8: Summary of Eigenvalues & Eigenvectors

```
λ₁ = 2.5    →  v₁ = [0.95,  0,  0.32]   ← Most important (highest variance)
λ₂ = 0.25   →  v₂ = [0,     1,  0   ]   ← Second important
λ₃ = 0      →  v₃ = [-0.32, 0,  0.95]   ← Least important (zero variance)
```

**Variance explained:**
```
Total variance = λ₁ + λ₂ + λ₃ = 2.5 + 0.25 + 0 = 2.75

λ₁ explains: 2.5 / 2.75 = 90.9%
λ₂ explains: 0.25 / 2.75 = 9.1%
λ₃ explains: 0 / 2.75 = 0%

Top 2 components explain: 90.9% + 9.1% = 100%!
```

---

## Step 9: Create Projection Matrix (3D → 2D)

**Select top 2 eigenvectors:**

```
v₁ = [0.95,  0,  0.32]
v₂ = [0,     1,  0   ]
```

**Projection Matrix P (3×2):**

```
P = [v₁ | v₂]

    [0.95   0]
P = [0      1]
    [0.32   0]
```

---

## Step 10: Project Centered Data

**Formula:** x_2D = x_3D × P

---

### "king" = [1.5, -0.5, 0.5]

```
[1.5, -0.5, 0.5] × [0.95   0]
                   [0      1]
                   [0.32   0]

Dimension 1:
= 1.5 × 0.95 + (-0.5) × 0 + 0.5 × 0.32
= 1.425 + 0 + 0.16
= 1.585

Dimension 2:
= 1.5 × 0 + (-0.5) × 1 + 0.5 × 0
= 0 + (-0.5) + 0
= -0.5

"king" in 2D = [1.585, -0.5]
```

---

### "queen" = [1.5, 0.5, 0.5]

```
[1.5, 0.5, 0.5] × [0.95   0]
                  [0      1]
                  [0.32   0]

Dimension 1:
= 1.5 × 0.95 + 0.5 × 0 + 0.5 × 0.32
= 1.425 + 0 + 0.16
= 1.585

Dimension 2:
= 1.5 × 0 + 0.5 × 1 + 0.5 × 0
= 0 + 0.5 + 0
= 0.5

"queen" in 2D = [1.585, 0.5]
```

---

### "man" = [-1.5, -0.5, -0.5]

```
[-1.5, -0.5, -0.5] × [0.95   0]
                     [0      1]
                     [0.32   0]

Dimension 1:
= (-1.5) × 0.95 + (-0.5) × 0 + (-0.5) × 0.32
= -1.425 + 0 + (-0.16)
= -1.585

Dimension 2:
= (-1.5) × 0 + (-0.5) × 1 + (-0.5) × 0
= 0 + (-0.5) + 0
= -0.5

"man" in 2D = [-1.585, -0.5]
```

---

### "woman" = [-1.5, 0.5, -0.5]

```
[-1.5, 0.5, -0.5] × [0.95   0]
                    [0      1]
                    [0.32   0]

Dimension 1:
= (-1.5) × 0.95 + 0.5 × 0 + (-0.5) × 0.32
= -1.425 + 0 + (-0.16)
= -1.585

Dimension 2:
= (-1.5) × 0 + 0.5 × 1 + (-0.5) × 0
= 0 + 0.5 + 0
= 0.5

"woman" in 2D = [-1.585, 0.5]
```

---

## Final Result: 2D Coordinates

```
Word      3D (centered)         2D (projected)
────────────────────────────────────────────────
"king"    [1.5, -0.5, 0.5]  →  [1.585,  -0.5]
"queen"   [1.5,  0.5, 0.5]  →  [1.585,   0.5]
"man"     [-1.5, -0.5, -0.5] → [-1.585, -0.5]
"woman"   [-1.5,  0.5, -0.5] → [-1.585,  0.5]
```

---

## Visualization

```
                    Dim 2 (Gender)
                        ↑
                   +0.5 │  woman              queen
                        │    ★                  ★
                        │
         ───────────────┼───────────────────────→ Dim 1 (Royalty)
                        │
                   -0.5 │  man                 king
                        │    ★                  ★
                        │
                     -1.585                  +1.585
```

---

## What PCA Discovered

**Dimension 1 (v₁):** Separates Royalty
- Positive: king, queen (royalty)
- Negative: man, woman (commoners)

**Dimension 2 (v₂):** Separates Gender
- Positive: queen, woman (female)
- Negative: king, man (male)

**PCA automatically found these meaningful directions without being told!**

---

## Complete Formula Summary

```
1. Mean:           μ = (1/n) × Σ xᵢ

2. Center:         xᵢ_centered = xᵢ - μ

3. Covariance:     C = (1/n) × Σ (xᵢ_centered)(xᵢ_centered)ᵀ

4. Eigenvalues:    det(C - λI) = 0

5. Eigenvectors:   (C - λI) × v = 0

6. Normalize:      v_norm = v / ||v||

7. Project:        x_2D = x_centered × [v₁ | v₂]
```

---

*Document Created: 2026-01-19*

*This is a supplement to Transformer_Mathematics.md - Step 11 (PCA Visualization)*
