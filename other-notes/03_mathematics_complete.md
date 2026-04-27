# TRANSFORMER MATHEMATICS - COMPLETE GUIDE
# From Zero to Hero: Sab Kuch Jo Aapko Chahiye

---

> **Target:** Koi bhi padh sake - 10th pass se lekar B.Tech tak
> **Language:** Hindi-English Mix (Hinglish)
> **Style:** Pehle KYU, phir KYA, phir KAISE
> **Goal:** Transformer samajhne ke liye COMPLETE mathematics

---

# TABLE OF CONTENTS

```
PART 0:  Introduction & Roadmap
PART 1:  Numbers & Basic Operations
PART 2:  Algebra Basics
PART 3:  Vectors
PART 4:  Matrices
PART 5:  Matrix Decomposition (Eigen, PCA, SVD)
PART 6:  Calculus - Derivatives
PART 7:  Calculus - Optimization
PART 8:  Probability Basics
PART 9:  Probability Distributions
PART 10: Information Theory
PART 11: Special Functions (Activations, Norms)
PART 12: Putting It All Together
```

---

# =====================================================
# PART 0: INTRODUCTION & ROADMAP
# =====================================================

---

## Yeh Document Kyun?

```
Situation:
- Aap AI/ML seekhna chahte ho
- Transformer (ChatGPT ka base) samajhna chahte ho
- But math weak hai ya basics bhool gaye

Problem:
- Online resources ya toh bohot simple hain (sirf intuition)
- Ya bohot complex hain (sirf formulas)
- Koi PROPERLY nahi samjhata

Solution:
- Yeh document EVERYTHING cover karega
- Step by step, with examples
- Numbers se pehle, formulas baad mein
```

---

## Transformer Kya Hai? (1 Minute Mein)

```
Transformer = Ek AI architecture

Input:  "The cat sat on the ___"
Output: "mat" (most probable next word)

Kaise karta hai?
1. Har word ko numbers mein convert karta hai (Embedding)
2. Words ek dusre ko "dekhte" hain (Attention)
3. Patterns seekhta hai (Training)
4. Next word predict karta hai (Output)

Yeh sab MATH se hota hai!
```

---

## Math Kyun Zaroori Hai?

```
Bina math ke:
- "Attention" = Black box (pata nahi kya ho raha)
- "Training" = Magic (samajh nahi aata)
- "Loss" = Random word (meaning unclear)

Math ke saath:
- "Attention" = Dot product + Softmax (crystal clear!)
- "Training" = Gradient descent (step by step samajh)
- "Loss" = Cross-entropy (exactly pata hai kya measure ho raha)
```

---

## Prerequisites (Pehle Se Kya Aana Chahiye)

```
✅ Basic arithmetic (+, -, ×, ÷)
✅ Tables (2 se 10 tak)
✅ Basic fractions (1/2, 3/4, etc.)
✅ Percentage ka idea
✅ Simple equations (2x + 3 = 7 solve karna)

❌ Calculus (yahan se seekhenge)
❌ Linear Algebra (yahan se seekhenge)
❌ Probability (yahan se seekhenge)
❌ Programming (not required!)
```

---

## Kaise Padhein?

```
Option 1: Sequential (Recommended for beginners)
         Part 0 → Part 1 → Part 2 → ... → Part 12

Option 2: Jump to needed topic (If you know basics)
         Direct Part 3 (Vectors) ya Part 6 (Calculus)

Option 3: Reference mode (For revision)
         Jab zaroorat ho, specific section dekho

Har part ke end mein:
- Summary hoga
- Practice problems honge
- Next part ka connection hoga
```

---

## Time Estimate

```
Part 0:  30 min (Introduction)
Part 1:  2 hours (Numbers - revision)
Part 2:  3 hours (Algebra)
Part 3:  4 hours (Vectors) ⭐ Important
Part 4:  5 hours (Matrices) ⭐ Important
Part 5:  4 hours (Decomposition)
Part 6:  5 hours (Derivatives) ⭐ Important
Part 7:  4 hours (Optimization) ⭐ Important
Part 8:  3 hours (Probability basics)
Part 9:  4 hours (Distributions) ⭐ Important
Part 10: 3 hours (Information theory)
Part 11: 4 hours (Special functions) ⭐ Important
Part 12: 3 hours (Integration)

Total: ~45 hours (self-paced)
```

---

## Symbols Used in This Document

```
★      = Important point
⭐     = Very important section
✓      = Correct
✗      = Wrong/Incorrect
→      = Leads to / Results in
↑      = Increases
↓      = Decreases
≈      = Approximately equal
∴      = Therefore
∵      = Because
```

---

# =====================================================
# PART 1: NUMBERS & BASIC OPERATIONS
# =====================================================

---

## Why This Part?

```
Transformer mein har cheez NUMBER hai:
- Words → Numbers (Embeddings)
- Attention → Numbers (Scores)
- Output → Numbers (Probabilities)

Agar numbers ki understanding strong nahi, toh aage sab weak rahega.

Is part mein:
- Different types of numbers
- Operations on numbers
- Special operations (exponents, logs)
- Transformer mein kahan use hota hai
```

---

# Section 1.1: Types of Numbers

---

## 1.1.1 Natural Numbers (N)

### Real Life Example
```
Counting karte waqt jo numbers use karte ho:
"1 apple, 2 apples, 3 apples..."

Yeh natural numbers hain.
```

### Definition
```
N = {1, 2, 3, 4, 5, 6, 7, ...}

Properties:
- Start from 1
- No end (infinite)
- No fractions
- No negative
- No zero (traditionally)
```

### Transformer Connection
```
Token IDs natural numbers hain!

Vocabulary:
  "the"  → Token ID: 1
  "cat"  → Token ID: 2
  "sat"  → Token ID: 3
  ...
  "hello" → Token ID: 50257

GPT-2 vocabulary: 50,257 tokens
GPT-4 vocabulary: ~100,000 tokens
```

---

## 1.1.2 Whole Numbers (W)

### Real Life Example
```
Natural numbers + Zero

"Kitne apples hain?"
"Zero apples" - yeh bhi valid answer hai!
```

### Definition
```
W = {0, 1, 2, 3, 4, 5, ...}

W = N ∪ {0}
```

### Transformer Connection
```
Padding token often has ID = 0

Sentence: "Hello world"
With padding: [Hello, world, PAD, PAD, PAD]
Token IDs:   [5765,  995,   0,   0,   0]

Zero important hai padding ke liye!
```

---

## 1.1.3 Integers (Z)

### Real Life Example
```
Temperature:
  +30°C (garam)
   0°C  (freezing)
  -10°C (bahut thanda)

Bank account:
  +5000 (credit)
  -2000 (debit/loan)
```

### Definition
```
Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}

Properties:
- Negative numbers included
- Zero included
- No fractions
- Extends infinitely in both directions
```

### Visual
```
        ←───────────────────────────────────→
        -5  -4  -3  -2  -1   0   1   2   3   4   5
                            │
                         Origin
```

### Transformer Connection
```
Relative Position Encoding uses integers!

Sentence: "The cat sat"
Position:   0    1   2

Relative position from "cat" (position 1):
  "The" is at: 0 - 1 = -1 (ek position peeche)
  "cat" is at: 1 - 1 =  0 (same position)
  "sat" is at: 2 - 1 = +1 (ek position aage)

Negative positions are valid!
```

---

## 1.1.4 Rational Numbers (Q)

### Real Life Example
```
Pizza sharing:
  "4 logon mein 1 pizza baanto"
  Har person ko: 1/4 pizza

Percentages:
  "75% marks" = 75/100 = 3/4
```

### Definition
```
Q = {p/q : p, q ∈ Z, q ≠ 0}

Examples:
  1/2, 3/4, -5/3, 7/1, 0/5

Properties:
- Can be written as fraction
- Decimal representation either terminates OR repeats
  1/4 = 0.25 (terminates)
  1/3 = 0.333... (repeats)
```

### Transformer Connection
```
Attention weights are often rational-like!

Attention distribution:
  Word 1: 0.25 (25%)
  Word 2: 0.50 (50%)
  Word 3: 0.25 (25%)
  Total:  1.00 (100%)

Probabilities are always between 0 and 1.
```

---

## 1.1.5 Real Numbers (R)

### Real Life Example
```
Measurements jo exactly fraction mein nahi aa sakte:

Circle ka circumference:
  C = π × diameter
  π = 3.14159265358979...

  π is IRRATIONAL (never repeats, never ends)

Square ka diagonal:
  Side = 1
  Diagonal = √2 = 1.41421356...

  √2 is IRRATIONAL
```

### Definition
```
R = All numbers on the number line

R = Q ∪ Irrational numbers

Includes:
- All integers (..., -2, -1, 0, 1, 2, ...)
- All fractions (1/2, 3/4, -5/7, ...)
- All irrational numbers (π, √2, e, ...)
```

### Visual
```
Real Number Line:

←─────────────────────────────────────────────→
   -π    -1   -1/2   0   1/2   1   √2   π   e
                     │
                  Origin

Har point ek real number hai!
```

### Transformer Connection
```
⭐ TRANSFORMER MEIN SAB KUCH REAL NUMBERS HAIN! ⭐

Embeddings:      [0.23, -1.45, 0.78, ...] ← Real numbers
Weights:         [[0.12, -0.34], [0.56, 0.78]] ← Real numbers
Attention scores: [0.1, 0.7, 0.2] ← Real numbers
Gradients:       [-0.001, 0.003, -0.002] ← Real numbers

Deep Learning = Real Number Manipulation
```

---

## 1.1.6 Number Types Summary

```
N ⊂ W ⊂ Z ⊂ Q ⊂ R

Natural ⊂ Whole ⊂ Integer ⊂ Rational ⊂ Real

Visual:
┌─────────────────────────────────────────────────┐
│ Real Numbers (R)                                │
│  ┌───────────────────────────────────────────┐  │
│  │ Rational Numbers (Q)                      │  │
│  │  ┌─────────────────────────────────────┐  │  │
│  │  │ Integers (Z)                        │  │  │
│  │  │  ┌───────────────────────────────┐  │  │  │
│  │  │  │ Whole Numbers (W)             │  │  │  │
│  │  │  │  ┌─────────────────────────┐  │  │  │  │
│  │  │  │  │ Natural Numbers (N)     │  │  │  │  │
│  │  │  │  │ 1, 2, 3, 4, 5, ...      │  │  │  │  │
│  │  │  │  └─────────────────────────┘  │  │  │  │
│  │  │  │ + 0                           │  │  │  │
│  │  │  └───────────────────────────────┘  │  │  │
│  │  │ + negative integers (-1, -2, ...)   │  │  │
│  │  └─────────────────────────────────────┘  │  │
│  │ + fractions (1/2, 3/4, ...)               │  │
│  └───────────────────────────────────────────┘  │
│ + irrational (π, √2, e, ...)                    │
└─────────────────────────────────────────────────┘
```

---

# Section 1.2: Basic Operations

---

## 1.2.1 Addition (+)

### Real Life
```
3 apples + 2 apples = 5 apples
```

### Properties
```
1. Commutative: a + b = b + a
   3 + 5 = 5 + 3 = 8

2. Associative: (a + b) + c = a + (b + c)
   (2 + 3) + 4 = 2 + (3 + 4) = 9

3. Identity: a + 0 = a
   7 + 0 = 7
```

### Transformer Connection
```
Residual Connection = Addition!

Original input:    x = [0.5, 0.3, 0.2]
After attention:   a = [0.1, 0.4, 0.1]

Residual output:   x + a = [0.6, 0.7, 0.3]

Why add?
- Original information preserve hoti hai
- Gradient flow better hota hai
- Training stable hoti hai
```

---

## 1.2.2 Subtraction (−)

### Real Life
```
Had 10 rupees, spent 3 rupees
Remaining: 10 - 3 = 7 rupees
```

### Properties
```
1. NOT Commutative: a - b ≠ b - a
   5 - 3 = 2
   3 - 5 = -2

2. NOT Associative: (a - b) - c ≠ a - (b - c)
   (10 - 5) - 2 = 3
   10 - (5 - 2) = 7
```

### Transformer Connection
```
Mean Centering (PCA mein dekha tha):

Original:  [4, 2, 1]
Mean:      [2.5, 2.5, 0.5]

Centered:  [4-2.5, 2-2.5, 1-0.5]
         = [1.5, -0.5, 0.5]

Layer Normalization mein bhi subtraction hota hai:
  x_normalized = (x - mean) / std
```

---

## 1.2.3 Multiplication (×)

### Real Life
```
3 packets, each has 4 chocolates
Total: 3 × 4 = 12 chocolates

Repeated addition:
3 × 4 = 4 + 4 + 4 = 12
```

### Properties
```
1. Commutative: a × b = b × a
   3 × 4 = 4 × 3 = 12

2. Associative: (a × b) × c = a × (b × c)
   (2 × 3) × 4 = 2 × (3 × 4) = 24

3. Identity: a × 1 = a
   7 × 1 = 7

4. Zero property: a × 0 = 0
   100 × 0 = 0

5. Distributive: a × (b + c) = a×b + a×c
   2 × (3 + 4) = 2×3 + 2×4 = 14
```

### Transformer Connection
```
⭐ MULTIPLICATION IS EVERYWHERE IN TRANSFORMERS! ⭐

1. Scaling:
   Attention score = (Q · K) / √d

   √d se divide = 1/√d se multiply

2. Learning rate:
   new_weight = old_weight - learning_rate × gradient

3. Element-wise multiplication:
   Gating mechanisms mein use hota hai
```

---

## 1.2.4 Division (÷)

### Real Life
```
12 chocolates, 4 friends mein baanto
Each gets: 12 ÷ 4 = 3 chocolates
```

### Properties
```
1. NOT Commutative: a ÷ b ≠ b ÷ a
   12 ÷ 4 = 3
   4 ÷ 12 = 0.333...

2. NOT Associative: (a ÷ b) ÷ c ≠ a ÷ (b ÷ c)

3. Division by zero: UNDEFINED!
   5 ÷ 0 = ??? (not allowed)
```

### Why Division by Zero is Undefined
```
Question: 6 ÷ 2 = ?
Answer:   3, because 3 × 2 = 6

Question: 6 ÷ 0 = ?
Answer:   ?, because ? × 0 = 6
          But anything × 0 = 0, never 6!
          So no answer exists.
```

### Transformer Connection
```
Softmax mein division hota hai:

Softmax(xᵢ) = eˣⁱ / Σⱼ eˣʲ

Example:
  x = [2, 1, 0]
  eˣ = [e², e¹, e⁰] = [7.39, 2.72, 1]
  Sum = 7.39 + 2.72 + 1 = 11.11

  Softmax = [7.39/11.11, 2.72/11.11, 1/11.11]
          = [0.665, 0.245, 0.090]

Division se normalization hota hai (sum = 1)
```

---

# Section 1.3: Exponents (Powers)

---

## 1.3.1 What is an Exponent?

### Real Life Example
```
Population doubling:
  Year 0: 1000 people
  Year 1: 1000 × 2 = 2000
  Year 2: 2000 × 2 = 4000
  Year 3: 4000 × 2 = 8000

After n years: 1000 × 2ⁿ

2ⁿ = "2 raised to the power n"
   = 2 multiplied by itself n times
```

### Definition
```
aⁿ = a × a × a × ... × a (n times)

Examples:
  2³ = 2 × 2 × 2 = 8
  5² = 5 × 5 = 25
  10⁴ = 10 × 10 × 10 × 10 = 10000
```

### Visual
```
Powers of 2:
2¹ = 2
2² = 4
2³ = 8        ★ Exponential growth!
2⁴ = 16
2⁵ = 32
2⁶ = 64
2⁷ = 128
2⁸ = 256
2⁹ = 512
2¹⁰ = 1024
```

---

## 1.3.2 Special Exponents

### Zero Exponent
```
a⁰ = 1 (for any a ≠ 0)

Why?
Pattern:
  2⁴ = 16
  2³ = 8  (÷2)
  2² = 4  (÷2)
  2¹ = 2  (÷2)
  2⁰ = 1  (÷2)

Proof:
  aⁿ ÷ aⁿ = aⁿ⁻ⁿ = a⁰
  But aⁿ ÷ aⁿ = 1
  ∴ a⁰ = 1
```

### One Exponent
```
a¹ = a

Examples:
  5¹ = 5
  100¹ = 100
```

### Negative Exponent
```
a⁻ⁿ = 1/aⁿ

Examples:
  2⁻¹ = 1/2 = 0.5
  2⁻² = 1/4 = 0.25
  10⁻³ = 1/1000 = 0.001

Pattern:
  2³ = 8
  2² = 4
  2¹ = 2
  2⁰ = 1
  2⁻¹ = 0.5
  2⁻² = 0.25
  2⁻³ = 0.125
```

### Fractional Exponent
```
a^(1/n) = ⁿ√a (nth root of a)

Examples:
  4^(1/2) = √4 = 2
  8^(1/3) = ³√8 = 2
  16^(1/4) = ⁴√16 = 2

a^(m/n) = ⁿ√(aᵐ) = (ⁿ√a)ᵐ

Example:
  8^(2/3) = (³√8)² = 2² = 4
```

---

## 1.3.3 Exponent Rules

### Rule 1: Multiplication (Same Base)
```
aᵐ × aⁿ = aᵐ⁺ⁿ

Example:
  2³ × 2⁴ = 2³⁺⁴ = 2⁷ = 128

Verify:
  2³ × 2⁴ = 8 × 16 = 128 ✓
```

### Rule 2: Division (Same Base)
```
aᵐ ÷ aⁿ = aᵐ⁻ⁿ

Example:
  2⁵ ÷ 2² = 2⁵⁻² = 2³ = 8

Verify:
  2⁵ ÷ 2² = 32 ÷ 4 = 8 ✓
```

### Rule 3: Power of Power
```
(aᵐ)ⁿ = aᵐˣⁿ

Example:
  (2³)² = 2³ˣ² = 2⁶ = 64

Verify:
  (2³)² = 8² = 64 ✓
```

### Rule 4: Power of Product
```
(ab)ⁿ = aⁿ × bⁿ

Example:
  (2 × 3)² = 2² × 3² = 4 × 9 = 36

Verify:
  (2 × 3)² = 6² = 36 ✓
```

### Rule 5: Power of Quotient
```
(a/b)ⁿ = aⁿ/bⁿ

Example:
  (4/2)³ = 4³/2³ = 64/8 = 8

Verify:
  (4/2)³ = 2³ = 8 ✓
```

---

## 1.3.4 The Special Number 'e'

### What is e?
```
e = 2.718281828459045...

Called: Euler's number
       Natural base

e is IRRATIONAL (never ends, never repeats)
```

### Where does e come from?
```
Compound Interest Problem:

₹1 invest karo, 100% interest, 1 year

Compounded yearly:     (1 + 1)¹ = 2
Compounded half-yearly: (1 + 0.5)² = 2.25
Compounded quarterly:  (1 + 0.25)⁴ = 2.44
Compounded monthly:    (1 + 1/12)¹² = 2.61
Compounded daily:      (1 + 1/365)³⁶⁵ = 2.714
Compounded continuously: e = 2.71828...

Formula: e = lim(n→∞) (1 + 1/n)ⁿ
```

### Why is e Important?
```
Special Property:
  d/dx (eˣ) = eˣ

Derivative of eˣ is eˣ itself!
No other function has this property.

This makes calculus much easier.
```

---

## 1.3.5 Transformer Connection: Exponential

```
⭐ SOFTMAX USES EXPONENTIAL! ⭐

Softmax formula:
  Softmax(xᵢ) = eˣⁱ / Σⱼ eˣʲ

Example:
  Attention scores: x = [3, 1, 0.5]

  Step 1: Calculate eˣ
    e³ = 20.09
    e¹ = 2.72
    e⁰·⁵ = 1.65

  Step 2: Sum
    20.09 + 2.72 + 1.65 = 24.46

  Step 3: Divide
    [20.09/24.46, 2.72/24.46, 1.65/24.46]
    = [0.82, 0.11, 0.07]

Result: Probabilities that sum to 1!
```

### Why Exponential in Softmax?
```
Properties we need:
1. Always positive (eˣ > 0 for all x) ✓
2. Preserves order (if a > b, then eᵃ > eᵇ) ✓
3. Amplifies differences (bade ko aur bada, chhote ko aur chhota) ✓
4. Differentiable (for backpropagation) ✓

eˣ satisfies all!
```

---

# Section 1.4: Logarithms

---

## 1.4.1 What is a Logarithm?

### Real Life Example
```
Question: 2 ko kitni baar multiply karein ki 8 aaye?
Answer:   3 baar (2 × 2 × 2 = 8)

This is: log₂(8) = 3

"Log base 2 of 8 equals 3"
```

### Definition
```
If aˣ = b, then logₐ(b) = x

"a to the power x equals b"
"log base a of b equals x"

These are INVERSE operations:
  Exponent: Given base and power, find result
  Logarithm: Given base and result, find power
```

### Visual Understanding
```
Exponent direction:
  2³ = ?
  2³ = 8  (2 ko 3 baar multiply = 8)

Logarithm direction:
  2^? = 8
  ? = log₂(8) = 3  (2 ko kitni baar multiply karein = 3)
```

---

## 1.4.2 Common Logarithms

### Log Base 10 (Common Log)
```
log₁₀(x) often written as log(x)

Examples:
  log(10) = 1      because 10¹ = 10
  log(100) = 2     because 10² = 100
  log(1000) = 3    because 10³ = 1000
  log(1) = 0       because 10⁰ = 1
  log(0.1) = -1    because 10⁻¹ = 0.1
```

### Log Base e (Natural Log)
```
logₑ(x) written as ln(x)

Examples:
  ln(e) = 1        because e¹ = e
  ln(e²) = 2       because e² = e²
  ln(1) = 0        because e⁰ = 1
  ln(e⁻¹) = -1     because e⁻¹ = e⁻¹
```

### Log Base 2 (Binary Log)
```
log₂(x) often used in computer science

Examples:
  log₂(2) = 1
  log₂(4) = 2
  log₂(8) = 3
  log₂(16) = 4
  log₂(1024) = 10
```

---

## 1.4.3 Logarithm Rules

### Rule 1: Log of 1
```
logₐ(1) = 0 (for any base a)

Because: a⁰ = 1
```

### Rule 2: Log of Base
```
logₐ(a) = 1

Because: a¹ = a
```

### Rule 3: Product Rule
```
logₐ(xy) = logₐ(x) + logₐ(y)

Example:
  log(100 × 1000) = log(100) + log(1000)
                  = 2 + 3
                  = 5

Verify: log(100000) = 5 ✓
```

### Rule 4: Quotient Rule
```
logₐ(x/y) = logₐ(x) - logₐ(y)

Example:
  log(1000/10) = log(1000) - log(10)
               = 3 - 1
               = 2

Verify: log(100) = 2 ✓
```

### Rule 5: Power Rule
```
logₐ(xⁿ) = n × logₐ(x)

Example:
  log(10³) = 3 × log(10)
           = 3 × 1
           = 3

Verify: log(1000) = 3 ✓
```

### Rule 6: Change of Base
```
logₐ(x) = logᵦ(x) / logᵦ(a)

Example:
  log₂(8) = ln(8) / ln(2)
          = 2.079 / 0.693
          = 3 ✓
```

---

## 1.4.4 Important Relationship

```
eˡⁿ⁽ˣ⁾ = x    and    ln(eˣ) = x

Exponential and Natural Log are INVERSES!

Visual:
  x → ln → y → exp → x
  x → exp → y → ln → x

Example:
  ln(e⁵) = 5
  eˡⁿ⁽⁷⁾ = 7
```

---

## 1.4.5 Transformer Connection: Logarithm

```
⭐ CROSS-ENTROPY LOSS USES LOGARITHM! ⭐

Cross-Entropy Loss:
  L = -Σ yᵢ × log(ŷᵢ)

Where:
  yᵢ = True label (0 or 1)
  ŷᵢ = Predicted probability

Example:
  True label: "cat" (index 2)
  y = [0, 0, 1, 0, 0]

  Predicted probabilities:
  ŷ = [0.1, 0.1, 0.7, 0.05, 0.05]

  Loss = -[0×log(0.1) + 0×log(0.1) + 1×log(0.7) + ...]
       = -log(0.7)
       = -(-0.357)
       = 0.357
```

### Why Logarithm in Loss?

```
Property 1: Penalizes wrong predictions heavily

If predicted probability for correct class:
  ŷ = 0.9  → -log(0.9) = 0.105  (small loss)
  ŷ = 0.5  → -log(0.5) = 0.693  (medium loss)
  ŷ = 0.1  → -log(0.1) = 2.303  (large loss!)
  ŷ = 0.01 → -log(0.01) = 4.605 (very large loss!)

Graph:
        Loss
          │
     4.6  │     ★ (0.01, 4.6)
          │
     2.3  │        ★ (0.1, 2.3)
          │
     0.7  │              ★ (0.5, 0.7)
          │                    ★ (0.9, 0.1)
     0    └─────────────────────────→ Predicted probability
          0    0.2   0.4   0.6   0.8   1.0

Jitna confident galat, utna zyada penalty!
```

---

# Section 1.5: Roots

---

## 1.5.1 What is a Root?

### Real Life Example
```
Question: Kaun sa number khud se multiply ho ke 9 de?
Answer:   3 (because 3 × 3 = 9)

√9 = 3

"Square root of 9 is 3"
```

### Definition
```
If x² = a, then √a = x (for x ≥ 0)

ⁿ√a = a^(1/n)

Examples:
  √4 = 2     because 2² = 4
  √9 = 3     because 3² = 9
  √16 = 4    because 4² = 16
  ³√8 = 2    because 2³ = 8
  ³√27 = 3   because 3³ = 27
```

---

## 1.5.2 Important Square Roots

```
Perfect Squares:
  √1 = 1
  √4 = 2
  √9 = 3
  √16 = 4
  √25 = 5
  √36 = 6
  √49 = 7
  √64 = 8
  √81 = 9
  √100 = 10

Common non-perfect:
  √2 ≈ 1.414
  √3 ≈ 1.732
  √5 ≈ 2.236
  √10 ≈ 3.162
```

---

## 1.5.3 Transformer Connection: Square Root

```
⭐ ATTENTION SCALING USES SQUARE ROOT! ⭐

Scaled Dot-Product Attention:
  Attention(Q, K, V) = softmax(QKᵀ / √dₖ) × V

Why divide by √dₖ?

Problem without scaling:
  If dₖ = 512, then Q·K can be very large
  Large values → Softmax becomes very peaked
  Very peaked → Gradients become very small
  Small gradients → Learning stops!

Solution:
  Divide by √512 ≈ 22.6
  This keeps values in reasonable range
  Softmax stays smooth
  Gradients stay healthy!

Example:
  dₖ = 64
  √dₖ = √64 = 8

  If Q·K = 40:
    Without scaling: softmax(40) ≈ 1.0 (too peaked!)
    With scaling: softmax(40/8) = softmax(5) ≈ 0.73 (better!)
```

---

# Section 1.6: Absolute Value

---

## 1.6.1 Definition

```
|x| = x    if x ≥ 0
|x| = -x   if x < 0

"Distance from zero"

Examples:
  |5| = 5
  |-5| = 5
  |0| = 0
  |-100| = 100
```

### Visual
```
Number line:

        ←────────────────────────────→
        -5   -3   -1   0   1   3   5

|−3| = distance from -3 to 0 = 3
|3|  = distance from 3 to 0 = 3
```

---

## 1.6.2 Properties

```
1. Always non-negative: |x| ≥ 0

2. |x| = 0 only when x = 0

3. |xy| = |x| × |y|
   |(-3)(4)| = |-12| = 12
   |-3| × |4| = 3 × 4 = 12 ✓

4. |x + y| ≤ |x| + |y| (Triangle inequality)
   |3 + (-5)| = |-2| = 2
   |3| + |-5| = 3 + 5 = 8
   2 ≤ 8 ✓
```

---

## 1.6.3 Transformer Connection

```
L1 Loss (Mean Absolute Error):
  L1 = (1/n) × Σ|yᵢ - ŷᵢ|

Example:
  True values:      y = [3, 5, 2, 8]
  Predicted values: ŷ = [2.5, 5.5, 3, 7]

  Differences: [0.5, -0.5, -1, 1]
  Absolute:    [0.5, 0.5, 1, 1]

  L1 = (0.5 + 0.5 + 1 + 1) / 4 = 0.75

L1 Regularization:
  Penalty = λ × Σ|wᵢ|

  Encourages sparse weights (some weights become exactly 0)
```

---

# Section 1.7: Summation Notation (Σ)

---

## 1.7.1 What is Sigma?

### Without Sigma
```
Add first 5 natural numbers:
  1 + 2 + 3 + 4 + 5 = 15

Add squares of first 4 numbers:
  1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
```

### With Sigma
```
Σᵢ₌₁⁵ i = 1 + 2 + 3 + 4 + 5 = 15

Σᵢ₌₁⁴ i² = 1² + 2² + 3² + 4² = 30

Reading:
  "Sigma i equals 1 to 5 of i"
  "Sum of i, where i goes from 1 to 5"
```

---

## 1.7.2 Anatomy of Sigma

```
    Upper limit (ending value)
         ↓
         5
         Σ   i
        i=1
         ↑   ↑
         │   └── Expression to sum
         │
    Lower limit (starting value + variable name)
```

---

## 1.7.3 Examples

### Example 1
```
Σᵢ₌₁³ i = 1 + 2 + 3 = 6
```

### Example 2
```
Σⱼ₌₂⁴ j² = 2² + 3² + 4² = 4 + 9 + 16 = 29
```

### Example 3
```
Σₖ₌₀³ 2ᵏ = 2⁰ + 2¹ + 2² + 2³ = 1 + 2 + 4 + 8 = 15
```

### Example 4: With constants
```
Σᵢ₌₁⁴ 3 = 3 + 3 + 3 + 3 = 12 = 4 × 3
```

### Example 5: Double sum
```
Σᵢ₌₁² Σⱼ₌₁³ (i + j)

i=1: Σⱼ₌₁³ (1+j) = (1+1) + (1+2) + (1+3) = 2 + 3 + 4 = 9
i=2: Σⱼ₌₁³ (2+j) = (2+1) + (2+2) + (2+3) = 3 + 4 + 5 = 12

Total: 9 + 12 = 21
```

---

## 1.7.4 Sigma Properties

```
1. Constant factor:
   Σᵢ₌₁ⁿ c × aᵢ = c × Σᵢ₌₁ⁿ aᵢ

   Example:
   Σᵢ₌₁³ 2i = 2×1 + 2×2 + 2×3 = 12
            = 2 × (1 + 2 + 3) = 2 × 6 = 12 ✓

2. Sum of sums:
   Σᵢ₌₁ⁿ (aᵢ + bᵢ) = Σᵢ₌₁ⁿ aᵢ + Σᵢ₌₁ⁿ bᵢ

3. Constant sum:
   Σᵢ₌₁ⁿ c = n × c
```

---

## 1.7.5 Common Formulas

```
1. Sum of first n natural numbers:
   Σᵢ₌₁ⁿ i = n(n+1)/2

   Example: Σᵢ₌₁¹⁰⁰ i = 100×101/2 = 5050

2. Sum of squares:
   Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6

3. Sum of cubes:
   Σᵢ₌₁ⁿ i³ = [n(n+1)/2]²

4. Geometric series:
   Σᵢ₌₀ⁿ rⁱ = (1 - rⁿ⁺¹)/(1 - r)  for r ≠ 1
```

---

## 1.7.6 Transformer Connection

```
⭐ SIGMA IS EVERYWHERE IN TRANSFORMERS! ⭐

1. Mean calculation:
   μ = (1/n) × Σᵢ₌₁ⁿ xᵢ

2. Variance calculation:
   σ² = (1/n) × Σᵢ₌₁ⁿ (xᵢ - μ)²

3. Dot product:
   a · b = Σᵢ₌₁ⁿ aᵢ × bᵢ

4. Softmax denominator:
   Σⱼ₌₁ⁿ eˣʲ

5. Cross-entropy loss:
   L = -Σᵢ₌₁ⁿ yᵢ × log(ŷᵢ)

6. Attention output:
   Output = Σⱼ₌₁ⁿ attention_weightⱼ × Vⱼ
```

---

# Section 1.8: Product Notation (Π)

---

## 1.8.1 What is Pi Notation?

```
Π = Product (multiply all terms)

Πᵢ₌₁⁵ i = 1 × 2 × 3 × 4 × 5 = 120

This is 5! (5 factorial)
```

---

## 1.8.2 Examples

```
Example 1:
  Πᵢ₌₁⁴ i = 1 × 2 × 3 × 4 = 24 = 4!

Example 2:
  Πᵢ₌₁³ i² = 1² × 2² × 3² = 1 × 4 × 9 = 36

Example 3:
  Πᵢ₌₂⁴ (i+1) = 3 × 4 × 5 = 60
```

---

## 1.8.3 Transformer Connection

```
Chain of probabilities:

P(sentence) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ...
            = Πᵢ₌₁ⁿ P(wᵢ | w₁, ..., wᵢ₋₁)

Example:
  P("The cat sat") = P("The") × P("cat"|"The") × P("sat"|"The cat")
                   = 0.1 × 0.05 × 0.2
                   = 0.001
```

---

# Section 1.9: Factorial

---

## 1.9.1 Definition

```
n! = n × (n-1) × (n-2) × ... × 2 × 1

Examples:
  1! = 1
  2! = 2 × 1 = 2
  3! = 3 × 2 × 1 = 6
  4! = 4 × 3 × 2 × 1 = 24
  5! = 5 × 4 × 3 × 2 × 1 = 120

Special case:
  0! = 1 (by definition)
```

---

## 1.9.2 Real Life Meaning

```
"How many ways to arrange n items?"

Example: 3 books (A, B, C) ko shelf pe arrange karo
  ABC, ACB, BAC, BCA, CAB, CBA

  Total arrangements = 3! = 6

First position: 3 choices
Second position: 2 choices (one used)
Third position: 1 choice (two used)
Total: 3 × 2 × 1 = 6
```

---

## 1.9.3 Factorial Growth

```
n     n!
1     1
2     2
3     6
4     24
5     120
6     720
7     5,040
8     40,320
9     362,880
10    3,628,800
20    2,432,902,008,176,640,000

★ Factorial grows EXTREMELY fast!
```

---

## 1.9.4 Transformer Connection

```
Permutation in attention:

Self-attention mein, n tokens ke beech n² pairs bante hain.

But full permutation consideration would be n! combinations
This is why attention is O(n²), not O(n!)
Otherwise computationally impossible!

For n = 100 tokens:
  n² = 10,000 (manageable)
  n! = 9.33 × 10¹⁵⁷ (impossible!)
```

---

# PART 1: SUMMARY

```
Numbers in Transformers:
┌─────────────────────────────────────────────────────┐
│ Concept          │ Use in Transformers              │
├─────────────────────────────────────────────────────┤
│ Natural numbers  │ Token IDs                        │
│ Integers         │ Position indices (can be -ve)    │
│ Real numbers     │ Everything else!                 │
│ Exponents        │ Softmax (eˣ)                     │
│ Logarithms       │ Cross-entropy loss               │
│ Square root      │ Attention scaling (√d)           │
│ Sigma (Σ)        │ Mean, sum, normalization         │
│ Product (Π)      │ Probability chains               │
└─────────────────────────────────────────────────────┘
```

---

# PART 1: PRACTICE PROBLEMS

```
Q1. Calculate: 2⁴ × 2³
    Answer: 2⁴⁺³ = 2⁷ = 128

Q2. Simplify: log₂(32)
    Answer: log₂(2⁵) = 5

Q3. Calculate: Σᵢ₌₁⁵ 2i
    Answer: 2(1) + 2(2) + 2(3) + 2(4) + 2(5)
          = 2 + 4 + 6 + 8 + 10 = 30

Q4. If attention score = 64, and d = 64, what is scaled score?
    Answer: 64 / √64 = 64 / 8 = 8

Q5. Calculate: e^(ln(7))
    Answer: 7 (inverse functions)

Q6. Calculate: -log(0.5)
    Answer: -(-0.693) = 0.693

Q7. Calculate: |3 - 8|
    Answer: |-5| = 5

Q8. Calculate: 5!
    Answer: 5 × 4 × 3 × 2 × 1 = 120
```

---

*End of Part 1*
*Next: Part 2 - Algebra Basics*

---

# =====================================================
# PART 2: ALGEBRA BASICS
# =====================================================

---

## Why This Part?

```
Algebra = Math with symbols (x, y, z instead of numbers)

In Transformers:
- Weights are unknown (we learn them)
- Formulas use symbols: Q, K, V, W, b
- Equations describe relationships

Without algebra:
  "Weight matrix multiply input" = meaningless

With algebra:
  y = Wx + b (now you understand!)
```

---

# Section 2.1: Variables & Constants

---

## 2.1.1 What is a Variable?

### Real Life Example
```
"Aaj mausam ka temperature ___ degree hai"

Yeh blank har din alag hota hai:
- Monday: 30°
- Tuesday: 32°
- Wednesday: 28°

We can write: temperature = x
Where x changes (varies) → VARIABLE
```

### Definition
```
Variable = Symbol that can take different values
         = Unknown or changing quantity

Common variable names:
  x, y, z (general)
  t (time)
  n (count)
  i, j, k (indices)
  θ (theta - angles)
  α, β (alpha, beta - parameters)
```

### Transformer Connection
```
In Transformers, variables include:

W = Weight matrix (LEARNABLE - changes during training)
b = Bias vector (LEARNABLE)
x = Input (changes for each sentence)
Q, K, V = Query, Key, Value (computed from input)
α = Attention weights (computed)
θ = Model parameters (collective)

Initially random → After training → Optimal values
```

---

## 2.1.2 What is a Constant?

### Real Life Example
```
π = 3.14159... (never changes)
e = 2.71828... (never changes)
Speed of light = 3×10⁸ m/s (never changes)
```

### Definition
```
Constant = Fixed value that doesn't change

In math:
  π, e, 0, 1, 2, ...

In Transformers:
  d_model = 512 (fixed architecture choice)
  n_heads = 8 (fixed)
  learning_rate = 0.001 (fixed during training)
```

---

## 2.1.3 Variable vs Constant: Quick Check

```
┌──────────────────────────────────────────────────┐
│ Example                    │ Variable or Constant │
├──────────────────────────────────────────────────┤
│ π                          │ Constant             │
│ Your age                   │ Variable (changes!)  │
│ Number of days in a week   │ Constant (7)         │
│ Stock price                │ Variable             │
│ √2                         │ Constant             │
│ Model weights              │ Variable (learnable) │
│ Embedding dimension (512)  │ Constant (fixed)     │
└──────────────────────────────────────────────────┘
```

---

# Section 2.2: Expressions & Equations

---

## 2.2.1 What is an Expression?

### Definition
```
Expression = Combination of numbers, variables, and operations
           = Recipe / Formula

Examples:
  3x + 5
  x² + 2x + 1
  (a + b)²
  Wx + b
```

### Not an Expression
```
3x + 5 = 11     ← This is an EQUATION (has = sign)
x > 5           ← This is an INEQUALITY
```

### Transformer Example
```
Expression for Linear Layer:

  Wx + b

Where:
  W = weight matrix
  x = input vector
  b = bias vector

This is an EXPRESSION (no = sign)
No specific values, just a formula.
```

---

## 2.2.2 Evaluating Expressions

### Example 1
```
Expression: 3x + 5
Evaluate at x = 4:

  3(4) + 5
  = 12 + 5
  = 17
```

### Example 2
```
Expression: x² - 2x + 1
Evaluate at x = 3:

  (3)² - 2(3) + 1
  = 9 - 6 + 1
  = 4
```

### Example 3: Transformer-style
```
Expression: Softmax(x) = eˣ / Σeˣ

Evaluate at x = [2, 1, 0]:

  e² = 7.39
  e¹ = 2.72
  e⁰ = 1.00
  Sum = 11.11

  Softmax = [7.39/11.11, 2.72/11.11, 1/11.11]
          = [0.665, 0.245, 0.090]
```

---

## 2.2.3 What is an Equation?

### Definition
```
Equation = Two expressions connected by = sign
         = Statement that two things are equal

Examples:
  3x + 5 = 11
  x² = 16
  y = mx + c
  Loss = -log(p)
```

### Parts of an Equation
```
      Left Hand Side    Right Hand Side
            ↓                  ↓
          3x + 5      =       11
                      ↑
                  Equal sign
```

---

## 2.2.4 Solving Equations

### Goal
```
Find the value of variable that makes equation TRUE
```

### Example 1: Linear Equation
```
Solve: 3x + 5 = 11

Step 1: Subtract 5 from both sides
        3x + 5 - 5 = 11 - 5
        3x = 6

Step 2: Divide both sides by 3
        3x/3 = 6/3
        x = 2

Check: 3(2) + 5 = 6 + 5 = 11 ✓
```

### Example 2: Quadratic Equation
```
Solve: x² = 16

Take square root of both sides:
  x = ±√16
  x = ±4

So x = 4 or x = -4

Check: (4)² = 16 ✓
       (-4)² = 16 ✓
```

### Example 3: With Two Variables
```
y = 2x + 3

This has INFINITE solutions!
  x = 0 → y = 3
  x = 1 → y = 5
  x = 2 → y = 7
  ...

Each (x, y) pair is a solution.
All solutions form a LINE.
```

---

## 2.2.5 Transformer Connection: Equations

```
Forward Pass Equation:

  y = Softmax(Wx + b)

This is the fundamental equation of a neural network layer!

Given:
  - Input x (known)
  - Weights W (learned)
  - Bias b (learned)

Output:
  - y = predicted values
```

---

# Section 2.3: Functions

---

## 2.3.1 What is a Function?

### Real Life Example
```
Vending Machine:
  - Put ₹10 → Get 1 chips packet
  - Put ₹20 → Get 2 chips packets
  - Put ₹50 → Get 5 chips packets

Input: Money
Output: Chips
Rule: 1 packet per ₹10

This is a FUNCTION!
```

### Definition
```
Function = Rule that assigns EXACTLY ONE output to each input

Function notation:
  f(x) = output

  f(x) = 2x + 3

  Read as: "f of x equals 2x plus 3"
```

### Visual
```
    Input           Function            Output
      x      →      f(x) = 2x + 3   →    y

      1      →      2(1) + 3        →    5
      2      →      2(2) + 3        →    7
      3      →      2(3) + 3        →    9
```

---

## 2.3.2 Function Notation

```
f(x) = x²

Means:
  "Take input x, square it, that's the output"

Evaluating:
  f(3) = 3² = 9
  f(-2) = (-2)² = 4
  f(a) = a²
  f(x+1) = (x+1)²
```

### Multiple Inputs
```
f(x, y) = x + y

f(3, 5) = 3 + 5 = 8
f(a, b) = a + b
```

### Transformer Example
```
Attention function:

Attention(Q, K, V) = Softmax(QKᵀ/√d) × V

Three inputs: Q, K, V
One output: Attended values

This is a function of THREE variables!
```

---

## 2.3.3 Domain & Range

### Domain
```
Domain = Set of all valid INPUTS

Example: f(x) = √x
  Domain: x ≥ 0 (can't take √ of negative)

Example: f(x) = 1/x
  Domain: x ≠ 0 (can't divide by zero)

Example: f(x) = x²
  Domain: All real numbers (any x works)
```

### Range
```
Range = Set of all possible OUTPUTS

Example: f(x) = x²
  Range: y ≥ 0 (squares are never negative)

Example: f(x) = eˣ
  Range: y > 0 (exponential is always positive)

Example: Softmax
  Range: (0, 1) for each element
```

---

## 2.3.4 Types of Functions

### Linear Function
```
f(x) = mx + c

  m = slope (steepness)
  c = y-intercept (where line crosses y-axis)

Graph: Straight line

Example: f(x) = 2x + 1

  x │ f(x)
  ──┼─────
  0 │  1
  1 │  3
  2 │  5
  3 │  7

        y
        │     ╱
        │   ╱
        │ ╱
        │╱
    ────┼────→ x
       ╱│
```

### Quadratic Function
```
f(x) = ax² + bx + c

Graph: Parabola (U-shape or ∩-shape)

Example: f(x) = x²

        y
        │    ╲   ╱
        │     ╲ ╱
        │      ╲
        │
    ────┼────→ x
```

### Exponential Function
```
f(x) = aˣ (where a > 0)

Most common: f(x) = eˣ

Graph: Rapid growth

        y
        │       ╱
        │     ╱
        │   ╱
        │ ╱
    ────┴─────→ x
```

### Logarithmic Function
```
f(x) = log(x)

Graph: Rapid at first, then slow

        y
        │         ────
        │      ╱
        │    ╱
        │  ╱
    ────┼────→ x
        │╱
```

---

## 2.3.5 Transformer Connection: Functions

```
Transformers = Composition of MANY Functions

Layer 1:   h₁ = f₁(x)
Layer 2:   h₂ = f₂(h₁)
Layer 3:   h₃ = f₃(h₂)
...
Output:    y = fₙ(hₙ₋₁)

Each layer is a function!
Whole network is a BIG function:

  y = fₙ(fₙ₋₁(...f₂(f₁(x))...))
```

---

# Section 2.4: Linear Functions (IMPORTANT!)

---

## 2.4.1 Definition

```
Linear Function: f(x) = mx + c

Where:
  m = slope (rate of change)
  c = intercept (starting value)
```

### Real Life Example
```
Taxi Fare:
  Base fare: ₹50 (intercept)
  Per km: ₹10 (slope)

  Fare = 10 × distance + 50
  f(d) = 10d + 50

  For 5 km: f(5) = 10(5) + 50 = ₹100
```

---

## 2.4.2 Slope

### What is Slope?
```
Slope = Rise / Run
      = Change in y / Change in x
      = How steep the line is

        y
        │      ╱ (m > 0: rising)
        │    ╱
    ────┼──────→ x
        │

        y
        │
    ────┼──────→ x
        │╲
        │  ╲ (m < 0: falling)

        y
        │
    ────┼───────→ x (m = 0: flat)
```

### Calculating Slope
```
Given two points (x₁, y₁) and (x₂, y₂):

  m = (y₂ - y₁) / (x₂ - x₁)

Example:
  Points: (1, 3) and (4, 9)

  m = (9 - 3) / (4 - 1)
    = 6 / 3
    = 2

  Line rises 2 units for every 1 unit right.
```

---

## 2.4.3 Linear Function in Transformer

```
Linear Layer (Dense Layer / Fully Connected):

  y = Wx + b

  W = Weight matrix (like slope, but matrix!)
  b = Bias vector (like intercept, but vector!)
  x = Input vector
  y = Output vector

This is the FUNDAMENTAL building block!
```

### Why "Linear"?
```
Property 1: f(ax) = a × f(x)  (scaling)
Property 2: f(x + y) = f(x) + f(y)  (additivity)

If BOTH properties hold → Function is LINEAR

For y = Wx:
  W(ax) = a(Wx) ✓
  W(x + y) = Wx + Wy ✓

Linear!

Note: y = Wx + b is called "affine" (linear + translation)
      But we often just say "linear layer"
```

---

# Section 2.5: Polynomials

---

## 2.5.1 Definition

```
Polynomial = Sum of terms with non-negative integer powers

General form:
  f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀

Examples:
  f(x) = 3x + 2         (degree 1: linear)
  f(x) = x² + 2x + 1    (degree 2: quadratic)
  f(x) = x³ - x         (degree 3: cubic)
```

### Degree
```
Degree = Highest power of x

  3x + 2         → degree 1
  x² + 2x + 1    → degree 2
  5x⁷ - 3x² + 1  → degree 7
  5              → degree 0 (constant)
```

---

## 2.5.2 Important Identity: (a + b)²

```
(a + b)² = a² + 2ab + b²

Proof:
  (a + b)² = (a + b)(a + b)
           = a(a + b) + b(a + b)
           = a² + ab + ba + b²
           = a² + 2ab + b²
```

### Visual Proof
```
Square with side (a + b):

┌─────────┬─────┐
│         │     │
│   a²    │ ab  │  ← height a
│         │     │
├─────────┼─────┤
│         │     │
│   ab    │ b²  │  ← height b
│         │     │
└─────────┴─────┘
  width a   width b

Total area = a² + ab + ab + b² = a² + 2ab + b²
```

---

## 2.5.3 Other Important Identities

```
1. (a + b)² = a² + 2ab + b²

2. (a - b)² = a² - 2ab + b²

3. (a + b)(a - b) = a² - b²

4. (a + b)³ = a³ + 3a²b + 3ab² + b³

5. (a - b)³ = a³ - 3a²b + 3ab² - b³
```

---

## 2.5.4 Transformer Connection

```
Variance formula uses (a - b)²:

  Variance = (1/n) × Σ(xᵢ - μ)²

Expanding:
  = (1/n) × Σ(xᵢ² - 2xᵢμ + μ²)
  = (1/n) × [Σxᵢ² - 2μΣxᵢ + nμ²]
  = (1/n)Σxᵢ² - 2μ(1/n)Σxᵢ + μ²
  = (1/n)Σxᵢ² - 2μ×μ + μ²
  = (1/n)Σxᵢ² - μ²

So: Var(x) = E[x²] - (E[x])²
    "Mean of squares minus square of mean"
```

---

# Section 2.6: Inequalities

---

## 2.6.1 Symbols

```
<   less than           5 < 7  (5 is less than 7)
>   greater than        7 > 5  (7 is greater than 5)
≤   less than or equal  5 ≤ 5  (5 equals 5, so true)
≥   greater than or equal
≠   not equal
```

---

## 2.6.2 Properties

```
1. If a < b, then a + c < b + c
   5 < 7 → 5 + 3 < 7 + 3 → 8 < 10 ✓

2. If a < b and c > 0, then ac < bc
   5 < 7 → 5×2 < 7×2 → 10 < 14 ✓

3. If a < b and c < 0, then ac > bc (FLIP!)
   5 < 7 → 5×(-2) > 7×(-2) → -10 > -14 ✓

★ Multiplying/dividing by NEGATIVE flips the inequality!
```

---

## 2.6.3 Transformer Connection

```
Probabilities have constraints:

  0 ≤ P(x) ≤ 1

  For all outputs of softmax:
    - Each value ≥ 0
    - Each value ≤ 1
    - Sum = 1

ReLU Activation:
  ReLU(x) = max(0, x)

  If x < 0 → output = 0
  If x ≥ 0 → output = x

  Output is always ≥ 0
```

---

# Section 2.7: Absolute Value in Algebra

---

## 2.7.1 Equations with Absolute Value

```
Solve: |x| = 5

Two cases:
  Case 1: x = 5
  Case 2: x = -5

Solution: x = ±5
```

```
Solve: |x - 3| = 7

Two cases:
  Case 1: x - 3 = 7  →  x = 10
  Case 2: x - 3 = -7 →  x = -4

Solution: x = 10 or x = -4
```

---

## 2.7.2 Inequalities with Absolute Value

```
|x| < 5 means: -5 < x < 5
  (x is WITHIN 5 units of 0)

|x| > 5 means: x < -5 OR x > 5
  (x is MORE THAN 5 units from 0)
```

---

# Section 2.8: Exponent Rules in Algebra

---

## 2.8.1 Rules with Variables

```
All rules work with variables too!

1. xᵃ × xᵇ = xᵃ⁺ᵇ

2. xᵃ ÷ xᵇ = xᵃ⁻ᵇ

3. (xᵃ)ᵇ = xᵃᵇ

4. (xy)ᵃ = xᵃyᵃ

5. x⁻ᵃ = 1/xᵃ

6. x^(1/n) = ⁿ√x
```

---

## 2.8.2 Examples

```
Simplify: x³ × x⁴
  = x³⁺⁴ = x⁷

Simplify: (x²)³
  = x²ˣ³ = x⁶

Simplify: x⁵/x²
  = x⁵⁻² = x³

Simplify: (2x)³
  = 2³ × x³ = 8x³
```

---

# Section 2.9: Logarithm Rules in Algebra

---

## 2.9.1 Rules with Variables

```
1. log(xy) = log(x) + log(y)

2. log(x/y) = log(x) - log(y)

3. log(xⁿ) = n × log(x)

4. logₐ(a) = 1

5. logₐ(1) = 0

6. a^(logₐ(x)) = x

7. logₐ(aˣ) = x
```

---

## 2.9.2 Transformer Connection: Log-Sum-Exp

```
Computing log of sum of exponentials:

log(Σᵢ eˣⁱ)

Problem: eˣ can be very large, causing overflow!

Solution: Log-Sum-Exp trick

log(Σᵢ eˣⁱ) = M + log(Σᵢ e^(xᵢ-M))

Where M = max(xᵢ)

This prevents overflow because xᵢ - M ≤ 0
So e^(xᵢ-M) ≤ 1, manageable!
```

---

# Section 2.10: Systems of Equations

---

## 2.10.1 What is a System?

```
Multiple equations with multiple unknowns:

  x + y = 5
  x - y = 1

Goal: Find x and y that satisfy BOTH equations
```

---

## 2.10.2 Solving Methods

### Method 1: Substitution
```
  x + y = 5  ... (1)
  x - y = 1  ... (2)

From (1): x = 5 - y

Substitute in (2):
  (5 - y) - y = 1
  5 - 2y = 1
  -2y = -4
  y = 2

Back-substitute:
  x = 5 - 2 = 3

Solution: x = 3, y = 2
```

### Method 2: Elimination
```
  x + y = 5  ... (1)
  x - y = 1  ... (2)

Add (1) and (2):
  2x = 6
  x = 3

Subtract (2) from (1):
  2y = 4
  y = 2

Solution: x = 3, y = 2
```

---

## 2.10.3 Types of Solutions

```
1. Unique solution (one intersection point)
   ┌─────────┐
   │   ╲ ╱   │
   │    ╳    │  One point
   │   ╱ ╲   │
   └─────────┘

2. No solution (parallel lines)
   ┌─────────┐
   │  ╱   ╱  │
   │ ╱   ╱   │  Never meet
   │╱   ╱    │
   └─────────┘

3. Infinite solutions (same line)
   ┌─────────┐
   │     ╱   │
   │    ╱    │  Overlap completely
   │   ╱     │
   └─────────┘
```

---

## 2.10.4 Transformer Connection

```
Training finds W and b such that:

For input x₁: Wx₁ + b ≈ y₁
For input x₂: Wx₂ + b ≈ y₂
For input x₃: Wx₃ + b ≈ y₃
...
For input xₙ: Wxₙ + b ≈ yₙ

This is a HUGE system of equations!

Usually more equations than unknowns
→ No exact solution
→ Find BEST APPROXIMATE solution
→ This is what training does!
```

---

# Section 2.11: Proportions & Ratios

---

## 2.11.1 Ratio

```
Ratio = Comparison of two quantities

Boys : Girls = 3 : 2
Means: For every 3 boys, there are 2 girls

Can write as:
  3 : 2
  3/2
  3 to 2
```

---

## 2.11.2 Proportion

```
Proportion = Two ratios are equal

a : b = c : d
OR
a/b = c/d

Cross multiplication:
  a × d = b × c
```

---

## 2.11.3 Direct & Inverse Proportion

```
Direct Proportion:
  As x increases, y increases
  y = kx (k is constant)

  Example: Distance = Speed × Time
           More time → More distance

Inverse Proportion:
  As x increases, y decreases
  y = k/x

  Example: Workers × Days = Constant
           More workers → Less days
```

---

## 2.11.4 Transformer Connection

```
Attention weights are proportional to similarity:

weight ∝ similarity(Query, Key)

Higher similarity → Higher attention weight
This is DIRECT proportion!

Scaled attention:
weight ∝ (Q · K) / √d

Division by √d keeps proportions balanced.
```

---

# PART 2: SUMMARY

```
Algebra in Transformers:
┌─────────────────────────────────────────────────────┐
│ Concept          │ Use in Transformers              │
├─────────────────────────────────────────────────────┤
│ Variables        │ Learnable weights W, b           │
│ Constants        │ Architecture params (d=512)      │
│ Expressions      │ Wx + b                           │
│ Functions        │ Every layer is a function        │
│ Linear functions │ Linear/Dense layers              │
│ Systems of eqns  │ Training problem                 │
│ Inequalities     │ Probability constraints          │
│ Proportions      │ Attention weights                │
└─────────────────────────────────────────────────────┘
```

---

# PART 2: PRACTICE PROBLEMS

```
Q1. Evaluate f(x) = 3x² - 2x + 1 at x = 2
    Answer: 3(4) - 2(2) + 1 = 12 - 4 + 1 = 9

Q2. Solve: 5x - 3 = 12
    Answer: 5x = 15, x = 3

Q3. Simplify: x⁴ × x³
    Answer: x⁷

Q4. Expand: (x + 3)²
    Answer: x² + 6x + 9

Q5. Solve the system:
    2x + y = 7
    x - y = 2

    Answer: Add equations: 3x = 9, x = 3
            From eq 2: y = x - 2 = 1
            Solution: x = 3, y = 1

Q6. If f(x) = log(x), find f(100)
    Answer: log(100) = 2

Q7. Simplify: log(x³)
    Answer: 3log(x)

Q8. What is the slope of y = 4x - 7?
    Answer: 4
```

---

*End of Part 2*
*Next: Part 3 - Vectors*

---

# =====================================================
# PART 3: VECTORS (⭐ VERY IMPORTANT!)
# =====================================================

---

## Why This Part?

```
⭐ VECTORS ARE THE HEART OF TRANSFORMERS! ⭐

Every word in a Transformer = VECTOR
Every layer's input/output = VECTOR
Attention = VECTOR operations

Without vectors:
  "king" = ? (can't represent)
  Similarity = ? (can't measure)
  Attention = ? (can't compute)

With vectors:
  "king" = [0.2, -0.5, 0.8, ...] (512 numbers)
  Similarity = dot product (one formula)
  Attention = softmax of dot products (clear!)
```

---

# Section 3.1: What is a Vector?

---

## 3.1.1 Real Life Examples

### Example 1: Shopping List
```
Shopping list:
  Apples: 3
  Bananas: 2
  Oranges: 5

As a vector: [3, 2, 5]

Order matters!
  [3, 2, 5] = 3 apples, 2 bananas, 5 oranges
  [2, 5, 3] = 2 apples, 5 bananas, 3 oranges (different!)
```

### Example 2: Location
```
Your location:
  From starting point:
    - 3 km East
    - 4 km North

As a vector: [3, 4]

This is a 2D vector (2 dimensions)
```

### Example 3: RGB Color
```
Color = combination of Red, Green, Blue

Pure Red:   [255, 0, 0]
Pure Green: [0, 255, 0]
Pure Blue:  [0, 0, 255]
Yellow:     [255, 255, 0]
White:      [255, 255, 255]
Black:      [0, 0, 0]

Each color is a 3D vector!
```

---

## 3.1.2 Definition

```
Vector = Ordered list of numbers

v = [v₁, v₂, v₃, ..., vₙ]

Where:
  v₁, v₂, ... = components/elements
  n = dimension (number of components)
```

### Notation
```
Column vector (vertical):     Row vector (horizontal):

    [v₁]
v = [v₂]                      v = [v₁, v₂, v₃]
    [v₃]

Both represent the same vector, just different writing style.
```

---

## 3.1.3 Vector Dimensions

```
1D vector (scalar):    [5]
2D vector:             [3, 4]
3D vector:             [1, 2, 3]
4D vector:             [1, 2, 3, 4]
...
512D vector:           [0.1, -0.3, 0.5, ..., 0.2]  ← Transformer embedding!

Dimension = How many numbers in the vector
```

---

## 3.1.4 Transformer Connection: Word Embeddings

```
In Transformers:

Each word → 512-dimensional vector (typically)

"king"  = [0.23, -0.45, 0.12, 0.89, ..., -0.34]  (512 numbers)
"queen" = [0.21, -0.42, 0.15, 0.91, ..., -0.31]  (512 numbers)
"apple" = [0.78, 0.23, -0.56, 0.11, ..., 0.67]  (512 numbers)

Notice:
  - "king" and "queen" vectors are SIMILAR (royalty)
  - "apple" vector is DIFFERENT (not royalty)

This is the POWER of embeddings!
```

---

# Section 3.2: Vector Operations

---

## 3.2.1 Vector Addition

### Real Life Example
```
Day 1: Walk 3 km East, 2 km North → [3, 2]
Day 2: Walk 1 km East, 4 km North → [1, 4]

Total: [3+1, 2+4] = [4, 6]
       4 km East, 6 km North
```

### Formula
```
If a = [a₁, a₂, a₃] and b = [b₁, b₂, b₃]

a + b = [a₁+b₁, a₂+b₂, a₃+b₃]
```

### Example
```
a = [1, 2, 3]
b = [4, 5, 6]

a + b = [1+4, 2+5, 3+6]
      = [5, 7, 9]
```

### Visual (2D)
```
        y
        │
      6 ┼─────────────────★ [4, 6] = a + b
        │               ╱│
        │             ╱  │
      4 ┼───────★ b=[1,4]│
        │     ╱ │        │
      2 ┼─★ a=[3,2]      │
        │╱   │           │
        └────┼───────────┼──→ x
           3            4

Vector a + Vector b = Diagonal of parallelogram
```

### Transformer Connection
```
Residual Connection = Vector Addition!

x = input embedding
a = attention output

output = x + a  (element-wise addition)

Example:
  x = [0.5, 0.3, 0.2]
  a = [0.1, 0.4, 0.1]

  output = [0.6, 0.7, 0.3]
```

---

## 3.2.2 Vector Subtraction

### Formula
```
a - b = [a₁-b₁, a₂-b₂, a₃-b₃]
```

### Example
```
a = [5, 8, 3]
b = [2, 3, 1]

a - b = [5-2, 8-3, 3-1]
      = [3, 5, 2]
```

### Transformer Connection
```
Finding direction from one word to another:

"king" = [0.8, 0.2, 0.5]
"man"  = [0.3, 0.2, 0.1]

"king" - "man" = [0.5, 0.0, 0.4]

This difference vector represents "ROYALTY"!

Famous example:
  king - man + woman ≈ queen

The math:
  [0.8, 0.2, 0.5] - [0.3, 0.2, 0.1] + [0.35, 0.25, 0.05]
= [0.5, 0.0, 0.4] + [0.35, 0.25, 0.05]
= [0.85, 0.25, 0.45]
≈ queen vector!
```

---

## 3.2.3 Scalar Multiplication

### Definition
```
Scalar = Single number (not a vector)

Scalar × Vector = Multiply each component by the scalar
```

### Formula
```
If c is a scalar and v = [v₁, v₂, v₃]

c × v = [c×v₁, c×v₂, c×v₃]
```

### Example
```
v = [2, 3, 4]
c = 3

3 × v = [3×2, 3×3, 3×4]
      = [6, 9, 12]
```

### Visual (2D)
```
        y
        │
        │        ★ 2v = [4, 6]
      6 ┼       ╱
        │     ╱
        │   ╱
      3 ┼─★ v = [2, 3]
        │╱
        │
        └───┼───┼───→ x
            2   4

2 × v = Same direction, but TWICE as long
```

### Special Cases
```
c = 2:   2v = stretch to double length
c = 0.5: 0.5v = shrink to half length
c = -1:  -v = flip direction (opposite)
c = 0:   0v = zero vector [0, 0, 0]
```

### Transformer Connection
```
1. Scaling in Attention:
   score = (Q · K) / √d

   Division by √d = multiplication by 1/√d
   This is scalar multiplication!

2. Learning rate in training:
   weight_update = learning_rate × gradient

   learning_rate = 0.001 (scalar)
   gradient = [0.5, -0.3, 0.2] (vector)

   update = [0.0005, -0.0003, 0.0002]
```

---

## 3.2.4 Dot Product (⭐ MOST IMPORTANT!)

### Real Life Example
```
Shopping:
  Quantities: q = [3, 2, 5]      (3 apples, 2 bananas, 5 oranges)
  Prices:     p = [10, 20, 15]   (₹10, ₹20, ₹15 each)

  Total bill = 3×10 + 2×20 + 5×15
             = 30 + 40 + 75
             = ₹145

  This is: q · p = 145 (dot product!)
```

### Formula
```
If a = [a₁, a₂, ..., aₙ] and b = [b₁, b₂, ..., bₙ]

a · b = a₁×b₁ + a₂×b₂ + ... + aₙ×bₙ
      = Σᵢ aᵢ × bᵢ

Result: Single number (scalar), not a vector!
```

### Example 1
```
a = [1, 2, 3]
b = [4, 5, 6]

a · b = 1×4 + 2×5 + 3×6
      = 4 + 10 + 18
      = 32
```

### Example 2
```
a = [2, -1, 3]
b = [1, 2, -1]

a · b = 2×1 + (-1)×2 + 3×(-1)
      = 2 - 2 - 3
      = -3
```

---

## 3.2.5 Dot Product = Similarity Measure

### Geometric Interpretation
```
a · b = |a| × |b| × cos(θ)

Where:
  |a| = length of vector a
  |b| = length of vector b
  θ = angle between a and b

Implications:
  θ = 0°   → cos(0°) = 1    → a · b = |a||b| (maximum, same direction)
  θ = 90°  → cos(90°) = 0   → a · b = 0 (perpendicular, no similarity)
  θ = 180° → cos(180°) = -1 → a · b = -|a||b| (opposite directions)
```

### Visual
```
                    a · b > 0
                    (similar)
                       ↗ a
                      ╱
                     ╱ θ < 90°
        ────────────●────────────
                     ╲
                      ╲ θ > 90°
                       ↘ b
                    a · b < 0
                    (dissimilar)

If θ = 90°: a · b = 0 (orthogonal/perpendicular)
```

---

## 3.2.6 Transformer Connection: Attention Score

```
⭐ ATTENTION = DOT PRODUCT! ⭐

Query: Q = [0.5, 0.3, 0.2]
Key:   K = [0.4, 0.3, 0.3]

Attention score = Q · K
                = 0.5×0.4 + 0.3×0.3 + 0.2×0.3
                = 0.2 + 0.09 + 0.06
                = 0.35

Higher dot product = More attention!

Why dot product for attention?
  - Similar vectors → High dot product → Pay more attention
  - Dissimilar vectors → Low dot product → Pay less attention

"How much should I look at this word?"
  = "How similar is my query to this key?"
  = Dot product!
```

---

# Section 3.3: Vector Length (Norm)

---

## 3.3.1 What is Vector Length?

### Real Life Example
```
You walk: 3 km East, 4 km North
Vector: v = [3, 4]

How far from start?

Using Pythagoras:
  distance² = 3² + 4²
  distance² = 9 + 16 = 25
  distance = √25 = 5 km

This is the LENGTH (or NORM) of vector v.
```

### Visual
```
        y
        │
      4 ┼───────★ v = [3, 4]
        │      ╱│
        │    ╱  │  length = 5
        │  ╱    │
        │╱      │
        └───────┼───→ x
              3

Pythagoras: 3² + 4² = 5²
```

---

## 3.3.2 Formula (L2 Norm / Euclidean Norm)

```
For v = [v₁, v₂, ..., vₙ]

||v|| = √(v₁² + v₂² + ... + vₙ²)
      = √(Σᵢ vᵢ²)

Also written as: |v| or ‖v‖₂
```

### Example
```
v = [3, 4]
||v|| = √(3² + 4²) = √(9 + 16) = √25 = 5

v = [1, 2, 2]
||v|| = √(1² + 2² + 2²) = √(1 + 4 + 4) = √9 = 3

v = [1, 1, 1, 1]
||v|| = √(1 + 1 + 1 + 1) = √4 = 2
```

---

## 3.3.3 Other Norms

### L1 Norm (Manhattan Distance)
```
||v||₁ = |v₁| + |v₂| + ... + |vₙ|

Example:
  v = [3, -4]
  ||v||₁ = |3| + |-4| = 3 + 4 = 7

Called "Manhattan" because:
  Like walking in NYC grid - only horizontal/vertical
```

### L∞ Norm (Maximum Norm)
```
||v||∞ = max(|v₁|, |v₂|, ..., |vₙ|)

Example:
  v = [3, -4, 2]
  ||v||∞ = max(3, 4, 2) = 4
```

### Comparison
```
v = [3, 4]

L2 (Euclidean): √(9 + 16) = 5
L1 (Manhattan): 3 + 4 = 7
L∞ (Maximum):   max(3, 4) = 4
```

---

## 3.3.4 Transformer Connection

```
Layer Normalization uses L2 norm:

Given vector x = [x₁, x₂, ..., xₙ]

Step 1: Mean
  μ = (1/n) × Σxᵢ

Step 2: Variance
  σ² = (1/n) × Σ(xᵢ - μ)²

Step 3: Normalize
  x_norm = (x - μ) / σ

This keeps vectors at "reasonable" lengths,
preventing explosion or vanishing during training.
```

---

# Section 3.4: Unit Vectors

---

## 3.4.1 Definition

```
Unit vector = Vector with length 1

||u|| = 1
```

### How to Create a Unit Vector
```
Given any vector v, its unit vector û is:

û = v / ||v||

(Divide vector by its length)
```

### Example
```
v = [3, 4]
||v|| = 5

Unit vector:
û = [3/5, 4/5]
  = [0.6, 0.8]

Check:
||û|| = √(0.6² + 0.8²) = √(0.36 + 0.64) = √1 = 1 ✓
```

---

## 3.4.2 Standard Basis Vectors

```
In 2D:
  î = [1, 0]  (unit vector along x-axis)
  ĵ = [0, 1]  (unit vector along y-axis)

In 3D:
  î = [1, 0, 0]  (x-direction)
  ĵ = [0, 1, 0]  (y-direction)
  k̂ = [0, 0, 1]  (z-direction)

Any vector can be written using these:
  [3, 4] = 3î + 4ĵ
         = 3[1, 0] + 4[0, 1]
         = [3, 0] + [0, 4]
         = [3, 4] ✓
```

---

## 3.4.3 Why Unit Vectors Matter

```
Unit vectors preserve DIRECTION, remove MAGNITUDE

When comparing directions:
  v₁ = [100, 0]
  v₂ = [1, 0]

  Both point in same direction (East)
  But v₁ is 100× longer

  Unit vectors:
  û₁ = [1, 0]
  û₂ = [1, 0]

  Now both are identical! Same direction = Same unit vector
```

---

## 3.4.4 Transformer Connection

```
Normalized Embeddings:

Some models normalize word vectors to unit length.

Before: "king" = [2.3, -1.5, 0.8, ...]
        ||"king"|| = 3.2

After:  "king" = [0.72, -0.47, 0.25, ...]
        ||"king"|| = 1

Why?
  - Removes effect of "how strong" the embedding is
  - Keeps only "what direction" (meaning)
  - Makes cosine similarity = dot product (simpler!)
```

---

# Section 3.5: Cosine Similarity

---

## 3.5.1 Definition

```
Cosine Similarity = cos(θ) = (a · b) / (||a|| × ||b||)

Where θ is the angle between vectors a and b

Range: -1 to +1
  +1 = Same direction (identical)
   0 = Perpendicular (unrelated)
  -1 = Opposite direction (opposite meaning)
```

---

## 3.5.2 Formula Breakdown

```
cosine_similarity(a, b) = (a · b) / (||a|| × ||b||)

                        = Σᵢ aᵢbᵢ
                          ─────────────────
                          √(Σᵢ aᵢ²) × √(Σᵢ bᵢ²)
```

---

## 3.5.3 Example

```
a = [1, 2, 3]
b = [2, 4, 6]

Step 1: Dot product
  a · b = 1×2 + 2×4 + 3×6 = 2 + 8 + 18 = 28

Step 2: Lengths
  ||a|| = √(1 + 4 + 9) = √14 ≈ 3.74
  ||b|| = √(4 + 16 + 36) = √56 ≈ 7.48

Step 3: Cosine similarity
  cos(θ) = 28 / (3.74 × 7.48)
         = 28 / 28
         = 1.0

Result: Perfect similarity! (b = 2×a, same direction)
```

---

## 3.5.4 Another Example

```
a = [1, 0, 0]
b = [0, 1, 0]

Step 1: Dot product
  a · b = 1×0 + 0×1 + 0×0 = 0

Step 2: Lengths
  ||a|| = 1
  ||b|| = 1

Step 3: Cosine similarity
  cos(θ) = 0 / (1 × 1) = 0

Result: Zero similarity! (perpendicular/orthogonal)
```

---

## 3.5.5 Transformer Connection

```
⭐ WORD SIMILARITY = COSINE SIMILARITY ⭐

"king"  = [0.8, 0.2, 0.3]
"queen" = [0.75, 0.25, 0.32]
"apple" = [0.1, 0.9, 0.1]

Similarity("king", "queen"):
  dot = 0.8×0.75 + 0.2×0.25 + 0.3×0.32 = 0.6 + 0.05 + 0.096 = 0.746
  ||king|| = √(0.64 + 0.04 + 0.09) = √0.77 = 0.88
  ||queen|| = √(0.56 + 0.06 + 0.10) = √0.72 = 0.85

  cosine = 0.746 / (0.88 × 0.85) = 0.746 / 0.748 = 0.997

  Almost 1! Very similar! ✓

Similarity("king", "apple"):
  dot = 0.8×0.1 + 0.2×0.9 + 0.3×0.1 = 0.08 + 0.18 + 0.03 = 0.29
  ||apple|| = √(0.01 + 0.81 + 0.01) = √0.83 = 0.91

  cosine = 0.29 / (0.88 × 0.91) = 0.29 / 0.80 = 0.36

  Low similarity! Different concepts! ✓
```

---

# Section 3.6: Orthogonal Vectors

---

## 3.6.1 Definition

```
Two vectors are ORTHOGONAL (perpendicular) if:

  a · b = 0

They form a 90° angle.
```

---

## 3.6.2 Examples

```
a = [1, 0]
b = [0, 1]

a · b = 1×0 + 0×1 = 0 ✓

These are orthogonal (x-axis ⟂ y-axis)
```

```
a = [3, 4]
b = [4, -3]

a · b = 3×4 + 4×(-3) = 12 - 12 = 0 ✓

Orthogonal! (not obvious, but math confirms)
```

```
a = [1, 2, 3]
b = [1, 1, -1]

a · b = 1×1 + 2×1 + 3×(-1) = 1 + 2 - 3 = 0 ✓

Orthogonal in 3D!
```

---

## 3.6.3 Why Orthogonality Matters

```
Orthogonal vectors = INDEPENDENT information

If a ⊥ b:
  - Knowing a tells you NOTHING about b
  - They capture DIFFERENT aspects of data

In PCA:
  - Eigenvectors are orthogonal
  - Each captures UNIQUE variance
  - No redundancy!

In Transformer Multi-Head Attention:
  - Different heads learn different patterns
  - Ideally somewhat orthogonal
  - Each head contributes unique information
```

---

# Section 3.7: Vector Projection

---

## 3.7.1 What is Projection?

### Real Life Example
```
Sun shining from above creates shadows.

3D object → 2D shadow on ground

This is PROJECTION!
```

---

## 3.7.2 Projecting a onto b

```
"How much of a lies in the direction of b?"

        a
       ╱│
      ╱ │
     ╱  │
    ╱   │
   ●────┴────→ b
   └──────┘
   projection of a onto b
```

### Formula
```
proj_b(a) = [(a · b) / (b · b)] × b

Or equivalently:

proj_b(a) = [(a · b) / ||b||²] × b

Scalar projection (just the length):
comp_b(a) = (a · b) / ||b||
```

---

## 3.7.3 Example

```
a = [3, 4]
b = [1, 0]  (x-axis)

Projection of a onto b:

a · b = 3×1 + 4×0 = 3
b · b = 1×1 + 0×0 = 1

proj_b(a) = (3/1) × [1, 0] = [3, 0]

The projection of [3, 4] onto x-axis is [3, 0].
(The "shadow" on the x-axis)
```

---

## 3.7.4 Transformer Connection: PCA

```
PCA = Projecting high-dimensional data onto principal components

512D embedding → Project onto top 2 eigenvectors → 2D visualization

Projection formula:
  x_projected = (x · v₁) × v₁ + (x · v₂) × v₂

Where v₁, v₂ are the principal component directions.

Each dot product tells us:
"How much does this word lie in this direction?"
```

---

# Section 3.8: Linear Combinations

---

## 3.8.1 Definition

```
Linear combination = Weighted sum of vectors

c₁v₁ + c₂v₂ + ... + cₙvₙ

Where c₁, c₂, ... are scalars (weights)
```

---

## 3.8.2 Example

```
v₁ = [1, 0]
v₂ = [0, 1]

Linear combination: 3v₁ + 2v₂
  = 3[1, 0] + 2[0, 1]
  = [3, 0] + [0, 2]
  = [3, 2]

Any 2D vector can be written as linear combination of v₁ and v₂!
```

---

## 3.8.3 Transformer Connection: Attention Output

```
⭐ ATTENTION OUTPUT = LINEAR COMBINATION OF VALUES ⭐

Values:   V₁ = [0.5, 0.3]
          V₂ = [0.2, 0.8]
          V₃ = [0.1, 0.4]

Attention weights: α = [0.7, 0.2, 0.1]

Output = 0.7×V₁ + 0.2×V₂ + 0.1×V₃
       = 0.7×[0.5, 0.3] + 0.2×[0.2, 0.8] + 0.1×[0.1, 0.4]
       = [0.35, 0.21] + [0.04, 0.16] + [0.01, 0.04]
       = [0.40, 0.41]

The output is a WEIGHTED AVERAGE of value vectors!
Weights come from attention scores (after softmax).
```

---

# Section 3.9: Span and Basis

---

## 3.9.1 Span

```
Span of vectors = All vectors you can create using linear combinations

Span({v₁, v₂}) = {c₁v₁ + c₂v₂ : c₁, c₂ ∈ R}

Example:
  v₁ = [1, 0]
  v₂ = [0, 1]

  Span({v₁, v₂}) = All of 2D space!
  Any [a, b] = a×[1, 0] + b×[0, 1]
```

---

## 3.9.2 Basis

```
Basis = Minimal set of vectors that spans the whole space

For 2D: Any 2 non-parallel vectors form a basis
For 3D: Any 3 non-coplanar vectors form a basis
For nD: Need exactly n independent vectors

Standard basis for 3D:
  {[1,0,0], [0,1,0], [0,0,1]}
```

---

## 3.9.3 Linear Independence

```
Vectors are LINEARLY INDEPENDENT if:
  None can be written as linear combination of others

v₁ = [1, 0]
v₂ = [0, 1]
v₃ = [2, 0]  ← This is 2×v₁, so NOT independent!

Independent: {v₁, v₂}
Dependent: {v₁, v₂, v₃}
```

---

## 3.9.4 Transformer Connection

```
Embedding dimension = 512

This means word vectors live in 512-dimensional space.

A basis for this space has 512 vectors.

Ideally, different "features" are independent:
  - Direction 1: Royalty vs Common
  - Direction 2: Male vs Female
  - Direction 3: Animate vs Inanimate
  - ...
  - Direction 512: Some other feature

PCA finds the most important basis directions!
```

---

# Section 3.10: Outer Product

---

## 3.10.1 Definition

```
Inner product: a · b = scalar
Outer product: a ⊗ b = MATRIX

If a = [a₁, a₂] and b = [b₁, b₂, b₃]

a ⊗ b = [a₁] × [b₁, b₂, b₃]
        [a₂]

      = [a₁b₁  a₁b₂  a₁b₃]
        [a₂b₁  a₂b₂  a₂b₃]

Result: 2×3 matrix!
```

---

## 3.10.2 Example

```
a = [2, 3]
b = [1, 4, 5]

a ⊗ b = [2] × [1, 4, 5]
        [3]

      = [2×1  2×4  2×5]
        [3×1  3×4  3×5]

      = [2   8  10]
        [3  12  15]
```

---

## 3.10.3 Transformer Connection

```
In PCA (covariance matrix):

C = (1/n) × Σ xᵢ ⊗ xᵢ

Each xᵢ ⊗ xᵢ creates a matrix.
Sum them up → Covariance matrix!

Already saw this in PCA_Complete_Example.md!
```

---

# PART 3: SUMMARY

```
Vectors in Transformers:
┌──────────────────────────────────────────────────────┐
│ Concept            │ Use in Transformers             │
├──────────────────────────────────────────────────────┤
│ Vector             │ Word embedding (512D)           │
│ Addition           │ Residual connections            │
│ Subtraction        │ Word analogies (king-man+woman) │
│ Scalar multiply    │ Attention scaling, learning rate│
│ Dot product ⭐      │ Attention scores (Q·K)         │
│ Length (norm)      │ Normalization                   │
│ Unit vectors       │ Normalized embeddings           │
│ Cosine similarity  │ Word similarity                 │
│ Orthogonal         │ Independent features            │
│ Projection         │ PCA dimensionality reduction    │
│ Linear combination │ Attention output (Σ αᵢVᵢ)      │
│ Outer product      │ Covariance matrix               │
└──────────────────────────────────────────────────────┘
```

---

# PART 3: KEY FORMULAS

```
1. Dot Product:
   a · b = Σᵢ aᵢbᵢ

2. Vector Length:
   ||v|| = √(Σᵢ vᵢ²)

3. Cosine Similarity:
   cos(θ) = (a · b) / (||a|| × ||b||)

4. Unit Vector:
   û = v / ||v||

5. Projection:
   proj_b(a) = [(a · b) / ||b||²] × b

6. Orthogonality Test:
   a ⊥ b ⟺ a · b = 0
```

---

# PART 3: PRACTICE PROBLEMS

```
Q1. Calculate: [1, 2, 3] + [4, 5, 6]
    Answer: [5, 7, 9]

Q2. Calculate: 3 × [2, -1, 4]
    Answer: [6, -3, 12]

Q3. Calculate dot product: [1, 2] · [3, 4]
    Answer: 1×3 + 2×4 = 3 + 8 = 11

Q4. Find length: ||[3, 4]||
    Answer: √(9 + 16) = √25 = 5

Q5. Find unit vector of [6, 8]
    Answer: ||v|| = 10, so û = [0.6, 0.8]

Q6. Are [1, 2] and [2, -1] orthogonal?
    Answer: 1×2 + 2×(-1) = 2 - 2 = 0. Yes! ✓

Q7. Cosine similarity of [1, 0] and [1, 1]
    Answer: dot = 1, ||a|| = 1, ||b|| = √2
            cos = 1/(1×√2) = 1/√2 ≈ 0.707

Q8. If attention weights are [0.5, 0.3, 0.2] and values are
    V₁=[1,0], V₂=[0,1], V₃=[1,1], find output.

    Answer: 0.5×[1,0] + 0.3×[0,1] + 0.2×[1,1]
          = [0.5, 0] + [0, 0.3] + [0.2, 0.2]
          = [0.7, 0.5]
```

---

*End of Part 3*
*Next: Part 4 - Matrices*

---

# =====================================================
# PART 4: MATRICES (⭐ VERY IMPORTANT!)
# =====================================================

---

## Why This Part?

```
⭐ MATRICES ARE THE COMPUTATIONAL BACKBONE OF TRANSFORMERS! ⭐

Every operation in Transformer = Matrix operation
- Embedding lookup = Matrix multiplication
- Attention = Matrix multiplication
- Feed-forward = Matrix multiplication
- Output = Matrix multiplication

Without matrices:
  Processing 1000 words = 1000 separate calculations (slow!)

With matrices:
  Processing 1000 words = 1 matrix calculation (fast! parallel!)
```

---

# Section 4.1: What is a Matrix?

---

## 4.1.1 Real Life Examples

### Example 1: Spreadsheet
```
Excel sheet with exam marks:

         Math  Science  English
Student1  85     90       78
Student2  92     88       95
Student3  76     84       80

This is a MATRIX (3×3):
[85  90  78]
[92  88  95]
[76  84  80]
```

### Example 2: Image
```
A grayscale image = Matrix of pixel values

[0   50  100 150]
[50  100 150 200]
[100 150 200 255]

Each number = brightness (0=black, 255=white)
```

### Example 3: Connections
```
Social network (who follows whom):

         Alice Bob Carol
Alice    [0    1   1]     Alice follows Bob and Carol
Bob      [1    0   0]     Bob follows Alice
Carol    [0    1   0]     Carol follows Bob

This is an ADJACENCY matrix!
```

---

## 4.1.2 Definition

```
Matrix = 2D array of numbers arranged in rows and columns

A = [a₁₁  a₁₂  a₁₃]
    [a₂₁  a₂₂  a₂₃]

Notation:
  - aᵢⱼ = element in row i, column j
  - A is m×n matrix = m rows, n columns

Size:
  [a  b  c]
  [d  e  f]  → 2 rows, 3 columns → 2×3 matrix
```

---

## 4.1.3 Special Matrices

### Square Matrix
```
Same number of rows and columns

[1  2  3]
[4  5  6]  → 3×3 (square)
[7  8  9]
```

### Row Vector
```
Matrix with 1 row
[1  2  3]  → 1×3 matrix
```

### Column Vector
```
Matrix with 1 column
[1]
[2]  → 3×1 matrix
[3]
```

### Zero Matrix
```
All elements are 0
[0  0  0]
[0  0  0]
```

### Identity Matrix (I)
```
1s on diagonal, 0s elsewhere

I = [1  0  0]
    [0  1  0]
    [0  0  1]

Special property: AI = IA = A (like multiplying by 1!)
```

### Diagonal Matrix
```
Non-zero elements only on diagonal

D = [3  0  0]
    [0  5  0]
    [0  0  2]
```

---

## 4.1.4 Transformer Connection

```
Weight Matrix W in Linear Layer:

If input dimension = 3
And output dimension = 2

W is a 2×3 matrix:

W = [w₁₁  w₁₂  w₁₃]
    [w₂₁  w₂₂  w₂₃]

These weights are LEARNED during training!

In GPT-2 (d_model = 768):
  Attention W_Q: 768×768 = 589,824 parameters
  Attention W_K: 768×768 = 589,824 parameters
  Attention W_V: 768×768 = 589,824 parameters

  Just attention has ~1.7 million parameters!
```

---

# Section 4.2: Matrix Operations

---

## 4.2.1 Matrix Addition

### Rule
```
Add corresponding elements
Matrices must be SAME SIZE!
```

### Example
```
A = [1  2]    B = [5  6]
    [3  4]        [7  8]

A + B = [1+5  2+6]   = [6   8]
        [3+7  4+8]     [10  12]
```

### Transformer Connection
```
Residual connection with layer output:

x = [0.5, 0.3, 0.2]  (input)
h = [0.1, 0.4, 0.1]  (layer output)

output = x + h = [0.6, 0.7, 0.3]

This is element-wise addition!
```

---

## 4.2.2 Scalar Multiplication

### Rule
```
Multiply every element by the scalar
```

### Example
```
A = [1  2]
    [3  4]

3 × A = [3×1  3×2]  = [3   6]
        [3×3  3×4]    [9  12]
```

### Transformer Connection
```
Learning rate application:

gradient = [[0.01, -0.02],
            [0.03, -0.01]]

learning_rate = 0.001

weight_update = 0.001 × gradient
             = [[0.00001, -0.00002],
                [0.00003, -0.00001]]
```

---

## 4.2.3 Matrix Multiplication (⭐ MOST IMPORTANT!)

### Real Life Analogy
```
Scenario: 3 factories, 2 products

Factory production (units/day):
         Product A  Product B
Factory1 [  10        20    ]
Factory2 [  15        25    ]
Factory3 [  20        30    ]

Profit per unit:
Product A: ₹5
Product B: ₹3

Daily profit per factory:
Factory1: 10×5 + 20×3 = 50 + 60 = ₹110
Factory2: 15×5 + 25×3 = 75 + 75 = ₹150
Factory3: 20×5 + 30×3 = 100 + 90 = ₹190

This is MATRIX MULTIPLICATION!
```

### Rule
```
A (m×n) × B (n×p) = C (m×p)

IMPORTANT: Inner dimensions must match!
  A is m×n
  B is n×p
       ↑ these must be equal!

Result: m×p matrix
```

### Formula
```
C[i][j] = Σₖ A[i][k] × B[k][j]

In words:
  Element at row i, column j of result =
  Dot product of (row i of A) and (column j of B)
```

### Step-by-Step Example
```
A = [1  2  3]     B = [7   8]
    [4  5  6]         [9  10]
                      [11 12]

A is 2×3, B is 3×2 → Result will be 2×2

C[1,1] = Row 1 of A · Column 1 of B
       = [1, 2, 3] · [7, 9, 11]
       = 1×7 + 2×9 + 3×11
       = 7 + 18 + 33
       = 58

C[1,2] = Row 1 of A · Column 2 of B
       = [1, 2, 3] · [8, 10, 12]
       = 1×8 + 2×10 + 3×12
       = 8 + 20 + 36
       = 64

C[2,1] = Row 2 of A · Column 1 of B
       = [4, 5, 6] · [7, 9, 11]
       = 4×7 + 5×9 + 6×11
       = 28 + 45 + 66
       = 139

C[2,2] = Row 2 of A · Column 2 of B
       = [4, 5, 6] · [8, 10, 12]
       = 4×8 + 5×10 + 6×12
       = 32 + 50 + 72
       = 154

Result:
C = [58   64]
    [139  154]
```

---

## 4.2.4 Matrix Multiplication is NOT Commutative!

```
⚠️ IMPORTANT: A × B ≠ B × A (generally)

Example:
A = [1  2]    B = [5  6]
    [3  4]        [7  8]

A × B = [1×5+2×7  1×6+2×8]  = [19  22]
        [3×5+4×7  3×6+4×8]    [43  50]

B × A = [5×1+6×3  5×2+6×4]  = [23  34]
        [7×1+8×3  7×2+8×4]    [31  46]

A × B ≠ B × A !!!

Order matters in matrix multiplication!
```

---

## 4.2.5 Transformer Connection: Linear Layer

```
⭐ LINEAR LAYER = MATRIX MULTIPLICATION ⭐

Input: x = [x₁, x₂, x₃] (1×3)

Weight matrix: W = [w₁₁  w₁₂]
                   [w₂₁  w₂₂]
                   [w₃₁  w₃₂]  (3×2)

Output: y = x × W

y = [x₁, x₂, x₃] × [w₁₁  w₁₂]
                    [w₂₁  w₂₂]
                    [w₃₁  w₃₂]

y = [x₁w₁₁ + x₂w₂₁ + x₃w₃₁,  x₁w₁₂ + x₂w₂₂ + x₃w₃₂]

Output is 1×2 vector!

This transforms 3D input to 2D output.
```

---

## 4.2.6 Batch Processing with Matrices

```
Processing multiple inputs at once:

Input batch (4 sentences, each 3D):
X = [sentence1]     [x₁₁  x₁₂  x₁₃]
    [sentence2]  =  [x₂₁  x₂₂  x₂₃]
    [sentence3]     [x₃₁  x₃₂  x₃₃]
    [sentence4]     [x₄₁  x₄₂  x₄₃]

X is 4×3 matrix

Weight: W (3×2 matrix)

Output: Y = X × W

Y is 4×2 matrix (4 outputs, each 2D)

ALL 4 sentences processed in ONE matrix multiplication!
This is why GPUs are so fast for deep learning.
```

---

# Section 4.3: Matrix Transpose

---

## 4.3.1 Definition

```
Transpose = Flip rows and columns

If A = [a  b  c]
       [d  e  f]

Then Aᵀ = [a  d]
          [b  e]
          [c  f]

Row i of A becomes Column i of Aᵀ
```

### Example
```
A = [1  2  3]
    [4  5  6]

A is 2×3

Aᵀ = [1  4]
     [2  5]
     [3  6]

Aᵀ is 3×2
```

---

## 4.3.2 Properties

```
1. (Aᵀ)ᵀ = A (double transpose = original)

2. (A + B)ᵀ = Aᵀ + Bᵀ

3. (cA)ᵀ = c(Aᵀ)

4. (AB)ᵀ = BᵀAᵀ (order reverses!)
```

---

## 4.3.3 Transformer Connection: Attention

```
⭐ Kᵀ IN ATTENTION FORMULA ⭐

Attention(Q, K, V) = Softmax(QKᵀ/√d) × V

Why Kᵀ?

Q has shape: (seq_len, d_k)
K has shape: (seq_len, d_k)

For Q × K, dimensions don't match!
  (seq_len × d_k) × (seq_len × d_k) = ERROR!

But Q × Kᵀ works:
  (seq_len × d_k) × (d_k × seq_len) = (seq_len × seq_len) ✓

Result: Attention matrix (seq_len × seq_len)
  Shows how much each word attends to every other word!
```

---

# Section 4.4: Element-wise Operations

---

## 4.4.1 Hadamard Product (⊙)

```
Element-wise multiplication (NOT matrix multiplication!)

A = [1  2]    B = [5  6]
    [3  4]        [7  8]

A ⊙ B = [1×5  2×6]  = [5   12]
        [3×7  4×8]    [21  32]

Multiply corresponding elements.
```

---

## 4.4.2 Transformer Connection: Gating

```
Some architectures use element-wise multiplication for "gating":

gate = σ(Wg × x)   # sigmoid → values between 0 and 1
value = f(x)

output = gate ⊙ value

If gate[i] ≈ 1: let value[i] through
If gate[i] ≈ 0: block value[i]

This is like a "switch" for each dimension!
```

---

# Section 4.5: Inverse Matrix

---

## 4.5.1 Definition

```
A × A⁻¹ = A⁻¹ × A = I (Identity matrix)

A⁻¹ is the INVERSE of A

Analogy:
  5 × (1/5) = 1
  A × A⁻¹ = I
```

---

## 4.5.2 When Does Inverse Exist?

```
A⁻¹ exists if and only if:
  1. A is SQUARE (m×m)
  2. det(A) ≠ 0 (determinant not zero)

If det(A) = 0, A is "singular" and has no inverse.
```

---

## 4.5.3 2×2 Inverse Formula

```
A = [a  b]
    [c  d]

A⁻¹ = (1/det) × [d   -b]
                [-c   a]

Where det = ad - bc
```

### Example
```
A = [4  7]
    [2  6]

det = 4×6 - 7×2 = 24 - 14 = 10

A⁻¹ = (1/10) × [6   -7]
               [-2   4]

    = [0.6   -0.7]
      [-0.2   0.4]

Verify: A × A⁻¹
= [4  7] × [0.6   -0.7]
  [2  6]   [-0.2   0.4]

= [4×0.6 + 7×(-0.2)    4×(-0.7) + 7×0.4]
  [2×0.6 + 6×(-0.2)    2×(-0.7) + 6×0.4]

= [2.4 - 1.4    -2.8 + 2.8]
  [1.2 - 1.2    -1.4 + 2.4]

= [1  0]  = I ✓
  [0  1]
```

---

## 4.5.4 Transformer Connection

```
Inverse matrices are rarely used directly in Transformers.

Why?
  1. Computing inverse is expensive: O(n³)
  2. Numerical instability issues
  3. Gradient computation is complicated

Instead:
  - Use iterative methods
  - Use pseudo-inverse for non-square matrices
  - Design architectures that avoid needing inverse
```

---

# Section 4.6: Determinant

---

## 4.6.1 What is Determinant?

```
Determinant = Single number that captures matrix properties

det(A) or |A|

Geometric meaning:
  2×2: Area scaling factor
  3×3: Volume scaling factor
```

---

## 4.6.2 2×2 Determinant

```
A = [a  b]
    [c  d]

det(A) = ad - bc

Example:
A = [3  2]
    [1  4]

det(A) = 3×4 - 2×1 = 12 - 2 = 10
```

---

## 4.6.3 3×3 Determinant

```
A = [a  b  c]
    [d  e  f]
    [g  h  i]

det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)

Or use "Rule of Sarrus" (diagonal method)
```

### Example (from PCA document)
```
C = [2.25   0      0.75]
    [0      0.25   0   ]
    [0.75   0      0.25]

Using cofactor expansion along row 2 (has zeros):

det = 0×(...) - 0.25×M₂₂ + 0×(...)
    = -0.25 × M₂₂

M₂₂ = det([2.25   0.75])
          ([0.75   0.25])
    = 2.25×0.25 - 0.75×0.75
    = 0.5625 - 0.5625
    = 0

Wait, this gives 0! Let me recalculate...

Actually for the characteristic equation det(C - λI),
we get a polynomial in λ, not just a number.
```

---

## 4.6.4 Properties of Determinant

```
1. det(I) = 1

2. det(Aᵀ) = det(A)

3. det(AB) = det(A) × det(B)

4. det(A⁻¹) = 1/det(A)

5. If any row/column is all zeros: det = 0

6. If two rows/columns are identical: det = 0

7. det(cA) = cⁿ × det(A) for n×n matrix
```

---

## 4.6.5 Transformer Connection

```
Determinant in eigenvalue calculation:

To find eigenvalues:
  det(A - λI) = 0

This is the "characteristic equation"

Already saw this in PCA!
  det(C - λI) = 0
  Solve for λ → Get eigenvalues
```

---

# Section 4.7: Eigenvalues and Eigenvectors (Preview)

---

## 4.7.1 Definition

```
For matrix A, if:
  A × v = λ × v

Then:
  v is an EIGENVECTOR of A
  λ is the corresponding EIGENVALUE

Meaning:
  Multiply A by v → Get same direction, scaled by λ
```

---

## 4.7.2 Geometric Intuition

```
Most vectors change direction when multiplied by A.

But eigenvectors are SPECIAL:
  They only get stretched (or shrunk), not rotated!

        Regular vector:
            A          ↗ Av (different direction!)
          ↗ v
        ●

        Eigenvector:
            A          ——→ λv (same direction, just scaled!)
          ——→ v
        ●
```

---

## 4.7.3 Transformer Connection

```
Eigenvalues/eigenvectors are crucial for:

1. PCA (dimensionality reduction)
   - Eigenvectors = Principal components
   - Eigenvalues = Variance explained

2. Understanding matrix behavior
   - Large eigenvalue = Strong transformation in that direction
   - Small eigenvalue = Weak transformation

3. Numerical stability analysis
   - Condition number = ratio of largest to smallest eigenvalue
   - Large ratio = Potentially unstable

We'll cover this in detail in Part 5!
```

---

# Section 4.8: Special Matrix Types

---

## 4.8.1 Symmetric Matrix

```
A = Aᵀ (matrix equals its transpose)

Example:
A = [1  2  3]
    [2  5  6]
    [3  6  9]

Properties:
- Eigenvalues are always REAL
- Eigenvectors are ORTHOGONAL
- Important for covariance matrices!
```

---

## 4.8.2 Orthogonal Matrix

```
Q × Qᵀ = Qᵀ × Q = I

Also: Q⁻¹ = Qᵀ (inverse equals transpose!)

Properties:
- Columns are orthonormal (perpendicular unit vectors)
- Preserves lengths: ||Qx|| = ||x||
- Preserves angles
- det(Q) = ±1

Geometric meaning:
- Orthogonal matrix = Rotation (and/or reflection)
- No stretching or skewing!
```

### Transformer Connection
```
Some weight initializations use orthogonal matrices
for better training stability.
```

---

## 4.8.3 Positive Definite Matrix

```
A matrix A is positive definite if:
  xᵀAx > 0 for all non-zero vectors x

Properties:
- All eigenvalues are positive
- Covariance matrices are positive semi-definite
- Hessian being positive definite = local minimum!
```

---

# Section 4.9: Matrix Rank

---

## 4.9.1 Definition

```
Rank = Number of linearly independent rows (or columns)

Rank tells you the "effective dimension" of the matrix.
```

### Example
```
A = [1  2  3]
    [2  4  6]     ← Row 2 = 2 × Row 1 (dependent!)
    [1  0  1]

Row 1 and Row 3 are independent.
Row 2 depends on Row 1.

Rank(A) = 2 (only 2 independent rows)
```

---

## 4.9.2 Properties

```
1. rank(A) ≤ min(m, n) for m×n matrix

2. rank(AB) ≤ min(rank(A), rank(B))

3. rank(A) = rank(Aᵀ)

4. Full rank: rank = min(m, n)
```

---

## 4.9.3 Transformer Connection

```
Low-Rank Approximation:

Original weight matrix W: 768×768 = 590,000 parameters

Low-rank approximation: W ≈ U × V
  U: 768×64 = 49,152 parameters
  V: 64×768 = 49,152 parameters
  Total: ~98,000 parameters

Same effect, 6× fewer parameters!

This is used in:
- LoRA (Low-Rank Adaptation) for fine-tuning
- Model compression
- Efficient transformers
```

---

# Section 4.10: Matrix as Linear Transformation

---

## 4.10.1 Concept

```
Every matrix represents a LINEAR TRANSFORMATION

A × x = y

Input vector x → Transform by A → Output vector y

Matrix A defines HOW the transformation happens:
- Rotation
- Scaling
- Shearing
- Projection
- Any combination!
```

---

## 4.10.2 Examples of Transformations

### Scaling Matrix
```
A = [2  0]
    [0  3]

Effect: Scale x by 2, scale y by 3

[2  0] × [1]   [2]
[0  3]   [1] = [3]

Point (1,1) → (2,3)
```

### Rotation Matrix
```
Rotate by angle θ:

R = [cos(θ)  -sin(θ)]
    [sin(θ)   cos(θ)]

For θ = 90°:
R = [0  -1]
    [1   0]

[0  -1] × [1]   [-1]
[1   0]   [0] = [1]

(1,0) rotates to (0,1) → 90° counterclockwise!
```

### Projection Matrix
```
Project onto x-axis:

P = [1  0]
    [0  0]

[1  0] × [3]   [3]
[0  0]   [4] = [0]

Point (3,4) → (3,0) (shadow on x-axis)
```

---

## 4.10.3 Transformer Connection

```
Weight matrices in Transformers = Learned transformations

W_Q: Transform embedding → Query space
W_K: Transform embedding → Key space
W_V: Transform embedding → Value space

These transformations are LEARNED to:
- Make similar words have similar queries/keys
- Separate different concepts
- Enable meaningful attention patterns

The network learns WHAT transformation is useful!
```

---

# PART 4: SUMMARY

```
Matrices in Transformers:
┌────────────────────────────────────────────────────────────┐
│ Concept               │ Use in Transformers               │
├────────────────────────────────────────────────────────────┤
│ Matrix                │ Weight storage, batch data        │
│ Addition              │ Residual connections, bias add    │
│ Multiplication ⭐      │ Linear layers, attention         │
│ Transpose             │ Kᵀ in attention (QKᵀ)            │
│ Element-wise ops      │ Gating, masking                  │
│ Identity matrix       │ Residual: x + f(x) = Ix + f(x)   │
│ Determinant           │ Eigenvalue computation           │
│ Inverse               │ (Rarely used directly)           │
│ Symmetric             │ Covariance matrices              │
│ Orthogonal            │ Weight initialization            │
│ Rank                  │ LoRA, model compression          │
│ Linear transformation │ Learned transformations          │
└────────────────────────────────────────────────────────────┘
```

---

# PART 4: KEY FORMULAS

```
1. Matrix Multiplication:
   C[i][j] = Σₖ A[i][k] × B[k][j]

2. Transpose:
   (Aᵀ)[i][j] = A[j][i]

3. 2×2 Determinant:
   det([a b; c d]) = ad - bc

4. 2×2 Inverse:
   A⁻¹ = (1/det) × [d -b; -c a]

5. Attention formula:
   Attention = Softmax(QKᵀ/√d) × V

6. Linear layer:
   y = Wx + b
```

---

# PART 4: PRACTICE PROBLEMS

```
Q1. Add matrices:
    [1 2] + [5 6]
    [3 4]   [7 8]

    Answer: [6  8 ]
            [10 12]

Q2. Multiply: 2 × [1 2; 3 4]
    Answer: [2 4; 6 8]

Q3. Matrix multiply:
    [1 2] × [5]
    [3 4]   [6]

    Answer: [1×5 + 2×6]   [17]
            [3×5 + 4×6] = [39]

Q4. Find (AB)ᵀ if A = [1 2; 3 4], B = [5 6; 7 8]
    Answer: (AB)ᵀ = BᵀAᵀ

Q5. Determinant of [3 1; 2 4]
    Answer: 3×4 - 1×2 = 12 - 2 = 10

Q6. Is [1 2; 2 1] symmetric?
    Answer: Yes, A = Aᵀ

Q7. If Q × K has shape (10, 64) × (64, 10), what's the result shape?
    Answer: Wait, (10,64) × (64,10) → (10,10)
    Correction: Usually Q × Kᵀ where K is (10,64)
    So Q(10,64) × Kᵀ(64,10) = (10,10) attention matrix ✓

Q8. Rank of [[1,2,3], [2,4,6]]
    Answer: 1 (row 2 = 2 × row 1)
```

---

*End of Part 4*
*Next: Part 5 - Matrix Decomposition (Eigen, PCA, SVD)*

---

# =====================================================
# PART 5: MATRIX DECOMPOSITION (Eigen, PCA, SVD)
# =====================================================

---

## Why This Part?

```
Matrix Decomposition = Matrix ko simple pieces mein todna

Like factoring numbers:
  12 = 4 × 3 = 2 × 2 × 3

For matrices:
  A = U × Σ × Vᵀ (SVD)
  A = Q × Λ × Q⁻¹ (Eigendecomposition)

Why decompose?
1. Understand matrix structure
2. Simplify computations
3. Dimensionality reduction (PCA!)
4. Find important patterns
```

---

# Section 5.1: Eigenvalues & Eigenvectors (Full Detail)

---

## 5.1.1 The Big Idea

### Analogy
```
Imagine a transformation (matrix A) that stretches space.

Most directions: Both direction AND length change
Special directions: Only LENGTH changes, direction stays same!

These special directions = EIGENVECTORS
How much length changes = EIGENVALUE
```

### Visual
```
Matrix A transforms the plane:

Before:                After A:
    │ ↗                    │    ↗ (rotated & stretched)
    │╱                     │   ╱
────●────              ────●────
    │                      │
    │                      │

But eigenvector v:
    │                      │
    │——→ v                │————————→ λv (same direction!)
────●────              ────●────
    │                      │

Eigenvector only gets SCALED, not rotated!
```

---

## 5.1.2 Mathematical Definition

```
A × v = λ × v

Where:
  A = Square matrix (n×n)
  v = Eigenvector (non-zero!)
  λ = Eigenvalue (can be any number, even 0 or negative)

Reading:
  "A times v equals lambda times v"
  "Multiplying A by v just scales v by lambda"
```

---

## 5.1.3 Finding Eigenvalues

### Step 1: Set up characteristic equation
```
A × v = λ × v

Rearrange:
A × v - λ × v = 0
A × v - λ × I × v = 0
(A - λI) × v = 0

For non-zero v to exist:
det(A - λI) = 0

This is the CHARACTERISTIC EQUATION
```

### Step 2: Solve for λ
```
det(A - λI) = 0 gives a polynomial in λ

For 2×2 matrix: quadratic equation
For 3×3 matrix: cubic equation
For n×n matrix: degree-n polynomial

Roots of this polynomial = Eigenvalues
```

---

## 5.1.4 Complete Example: 2×2 Matrix

```
A = [4  1]
    [2  3]

Step 1: A - λI
[4  1]   [λ  0]   [4-λ   1 ]
[2  3] - [0  λ] = [2    3-λ]

Step 2: Determinant = 0
det([4-λ   1 ]) = 0
    [2    3-λ]

(4-λ)(3-λ) - (1)(2) = 0

12 - 4λ - 3λ + λ² - 2 = 0

λ² - 7λ + 10 = 0

Step 3: Solve quadratic
λ = (7 ± √(49-40)) / 2
λ = (7 ± √9) / 2
λ = (7 ± 3) / 2

λ₁ = (7+3)/2 = 5
λ₂ = (7-3)/2 = 2

Eigenvalues: λ₁ = 5, λ₂ = 2
```

---

## 5.1.5 Finding Eigenvectors

### For λ₁ = 5:
```
(A - 5I) × v = 0

[4-5   1 ] [v₁]   [0]
[2    3-5] [v₂] = [0]

[-1   1] [v₁]   [0]
[2   -2] [v₂] = [0]

Row 1: -v₁ + v₂ = 0 → v₂ = v₁

Choose v₁ = 1:
v₂ = 1

Eigenvector for λ₁ = 5:  v₁ = [1, 1]

Normalized: v₁ = [1/√2, 1/√2] ≈ [0.707, 0.707]
```

### For λ₂ = 2:
```
(A - 2I) × v = 0

[4-2   1 ] [v₁]   [0]
[2    3-2] [v₂] = [0]

[2   1] [v₁]   [0]
[2   1] [v₂] = [0]

Row 1: 2v₁ + v₂ = 0 → v₂ = -2v₁

Choose v₁ = 1:
v₂ = -2

Eigenvector for λ₂ = 2:  v₂ = [1, -2]

Normalized: v₂ = [1/√5, -2/√5] ≈ [0.447, -0.894]
```

---

## 5.1.6 Verification

```
Check: A × v₁ = λ₁ × v₁

[4  1] × [1]   [4×1 + 1×1]   [5]
[2  3]   [1] = [2×1 + 3×1] = [5]

λ₁ × v₁ = 5 × [1, 1] = [5, 5] ✓

Check: A × v₂ = λ₂ × v₂

[4  1] × [1 ]   [4×1 + 1×(-2)]   [2 ]
[2  3]   [-2] = [2×1 + 3×(-2)] = [-4]

λ₂ × v₂ = 2 × [1, -2] = [2, -4] ✓
```

---

## 5.1.7 Properties of Eigenvalues

```
1. Sum of eigenvalues = Trace of matrix
   λ₁ + λ₂ = 5 + 2 = 7
   trace(A) = 4 + 3 = 7 ✓

2. Product of eigenvalues = Determinant
   λ₁ × λ₂ = 5 × 2 = 10
   det(A) = 4×3 - 1×2 = 12 - 2 = 10 ✓

3. n×n matrix has n eigenvalues (counting multiplicity)

4. Real symmetric matrix → Real eigenvalues, orthogonal eigenvectors
```

---

## 5.1.8 Transformer Connection

```
Why eigenvalues matter in ML:

1. PCA: Eigenvalues = Variance explained
   Large λ → Important direction
   Small λ → Unimportant direction

2. Covariance matrix analysis:
   Eigenvalues tell you data spread in each direction

3. Stability analysis:
   |λ| < 1 → Stable
   |λ| > 1 → Potentially unstable (exploding gradients!)

4. Learning rate selection:
   Optimal learning rate related to eigenvalues of Hessian
```

---

# Section 5.2: Eigendecomposition

---

## 5.2.1 Definition

```
If A has n linearly independent eigenvectors:

A = Q × Λ × Q⁻¹

Where:
  Q = Matrix of eigenvectors (columns)
  Λ = Diagonal matrix of eigenvalues
  Q⁻¹ = Inverse of Q
```

---

## 5.2.2 Example

```
A = [4  1]
    [2  3]

Eigenvalues: λ₁ = 5, λ₂ = 2
Eigenvectors: v₁ = [1, 1], v₂ = [1, -2]

Q = [1   1]  (eigenvectors as columns)
    [1  -2]

Λ = [5  0]  (eigenvalues on diagonal)
    [0  2]

Q⁻¹ = ?

det(Q) = 1×(-2) - 1×1 = -3

Q⁻¹ = (1/-3) × [-2  -1]   [2/3   1/3]
               [-1   1] = [1/3  -1/3]

Verify: A = Q × Λ × Q⁻¹

[1   1] × [5  0] × [2/3   1/3]
[1  -2]   [0  2]   [1/3  -1/3]

= [5   2] × [2/3   1/3]
  [5  -4]   [1/3  -1/3]

= [5×2/3 + 2×1/3    5×1/3 + 2×(-1/3)]
  [5×2/3 + (-4)×1/3  5×1/3 + (-4)×(-1/3)]

= [10/3 + 2/3    5/3 - 2/3]
  [10/3 - 4/3    5/3 + 4/3]

= [12/3   3/3]   [4  1]
  [6/3    9/3] = [2  3] ✓
```

---

## 5.2.3 Why Eigendecomposition is Useful

```
Powers of matrix become easy:

A² = (QΛQ⁻¹)(QΛQ⁻¹) = QΛ(Q⁻¹Q)ΛQ⁻¹ = QΛ²Q⁻¹
A³ = QΛ³Q⁻¹
Aⁿ = QΛⁿQ⁻¹

Λⁿ is easy to compute (just raise diagonal elements to power n):

Λⁿ = [λ₁ⁿ   0 ]
     [0    λ₂ⁿ]

This is used in analyzing recurrent networks!
```

---

# Section 5.3: Symmetric Matrices (Special Case)

---

## 5.3.1 Properties

```
For symmetric matrix A = Aᵀ:

1. All eigenvalues are REAL (no imaginary numbers)
2. Eigenvectors are ORTHOGONAL
3. A = QΛQᵀ (Q is orthogonal, so Q⁻¹ = Qᵀ)

This is called SPECTRAL DECOMPOSITION
```

---

## 5.3.2 Why This Matters

```
COVARIANCE MATRIX IS SYMMETRIC!

C = (1/n) × XᵀX

C = Cᵀ (always true for covariance)

Therefore:
- Eigenvalues of C are real and non-negative
- Eigenvectors of C are orthogonal
- PCA works perfectly!
```

---

# Section 5.4: PCA (Principal Component Analysis)

---

## 5.4.1 What is PCA?

```
PCA = Find the "best" directions in high-dimensional data

"Best" = Maximum variance directions

512D data → Find top 2 directions → 2D visualization
```

---

## 5.4.2 PCA Algorithm

```
Step 1: Center the data
  X_centered = X - mean(X)

Step 2: Compute covariance matrix
  C = (1/n) × X_centeredᵀ × X_centered

Step 3: Find eigenvalues and eigenvectors of C
  Eigenvalues: λ₁ ≥ λ₂ ≥ ... ≥ λₙ
  Eigenvectors: v₁, v₂, ..., vₙ

Step 4: Select top k eigenvectors
  P = [v₁ | v₂ | ... | vₖ]

Step 5: Project data
  X_reduced = X_centered × P
```

---

## 5.4.3 PCA Example (from your document)

```
Data:
  "king"  = [4, 2, 1]
  "queen" = [4, 3, 1]
  "man"   = [1, 2, 0]
  "woman" = [1, 3, 0]

Step 1: Mean
  μ = [2.5, 2.5, 0.5]

Step 2: Center
  "king"  → [1.5, -0.5, 0.5]
  "queen" → [1.5, 0.5, 0.5]
  "man"   → [-1.5, -0.5, -0.5]
  "woman" → [-1.5, 0.5, -0.5]

Step 3: Covariance matrix
  C = [2.25   0      0.75]
      [0      0.25   0   ]
      [0.75   0      0.25]

Step 4: Eigenvalues
  λ₁ = 2.5, λ₂ = 0.25, λ₃ = 0

Step 5: Eigenvectors (normalized)
  v₁ = [0.95, 0, 0.32]    (for λ₁ = 2.5)
  v₂ = [0, 1, 0]          (for λ₂ = 0.25)
  v₃ = [-0.32, 0, 0.95]   (for λ₃ = 0)

Step 6: Variance explained
  Total = 2.5 + 0.25 + 0 = 2.75
  v₁ explains: 2.5/2.75 = 91%
  v₂ explains: 0.25/2.75 = 9%

Step 7: Project onto v₁, v₂
  "king"  → [1.585, -0.5]
  "queen" → [1.585, 0.5]
  "man"   → [-1.585, -0.5]
  "woman" → [-1.585, 0.5]
```

---

## 5.4.4 What PCA Discovered

```
        Dim 2 (Gender)
            ↑
       +0.5 │  woman    queen
            │    ★        ★
            │
  ──────────┼──────────────→ Dim 1 (Royalty)
            │
       -0.5 │  man      king
            │    ★        ★

Dim 1: Separates royalty (positive) from commoners (negative)
Dim 2: Separates female (positive) from male (negative)

PCA found these MEANINGFUL directions automatically!
```

---

## 5.4.5 Transformer Connection: Embedding Visualization

```
Word embeddings are 512D (or more).

To visualize:
1. Take embedding vectors for many words
2. Apply PCA: 512D → 2D
3. Plot on 2D graph
4. Similar words cluster together!

This is how we CREATE those famous word embedding plots
showing king-queen-man-woman relationships.
```

---

# Section 5.5: SVD (Singular Value Decomposition)

---

## 5.5.1 What is SVD?

```
SVD = Decompose ANY matrix (not just square!)

A = U × Σ × Vᵀ

Where:
  A = m×n matrix (any size!)
  U = m×m orthogonal matrix (left singular vectors)
  Σ = m×n diagonal matrix (singular values)
  Vᵀ = n×n orthogonal matrix (right singular vectors)
```

---

## 5.5.2 SVD vs Eigendecomposition

```
Eigendecomposition:
  - Only for SQUARE matrices
  - A = QΛQ⁻¹
  - Eigenvectors might not be orthogonal (unless symmetric)

SVD:
  - Works for ANY matrix (rectangular too!)
  - A = UΣVᵀ
  - U and V are always orthogonal
  - More general and numerically stable
```

---

## 5.5.3 Geometric Interpretation

```
Any linear transformation can be decomposed as:

1. Rotate (Vᵀ)
2. Scale along axes (Σ)
3. Rotate again (U)

A = U × Σ × Vᵀ

    Input    →    Vᵀ     →     Σ      →     U     → Output
    space       (rotate)    (scale)     (rotate)     space
```

---

## 5.5.4 SVD Example

```
A = [3  2]
    [2  3]
    [2  1]

A is 3×2 (not square!)

SVD gives:
  U (3×3)
  Σ (3×2) with diagonal values
  Vᵀ (2×2)

Singular values (σ): found by √(eigenvalues of AᵀA)

AᵀA = [3 2 2] × [3  2]   [17  13]
      [2 3 1]   [2  3] = [13  14]
                [2  1]

Eigenvalues of AᵀA: λ₁ ≈ 28.5, λ₂ ≈ 2.5

Singular values: σ₁ = √28.5 ≈ 5.34, σ₂ = √2.5 ≈ 1.58
```

---

## 5.5.5 Low-Rank Approximation with SVD

```
SVD enables data compression!

Full SVD:
A = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + ... + σₙuₙvₙᵀ

Keep only top k terms:
A_k = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + ... + σₖuₖvₖᵀ

A_k is the BEST rank-k approximation of A!
(Best in terms of Frobenius norm)
```

---

## 5.5.6 Transformer Connection: LoRA

```
LoRA (Low-Rank Adaptation) uses this idea!

Original weight matrix W: 768×768 = 590,000 parameters

Instead of fine-tuning full W:
  W_new = W + ΔW
  ΔW = A × B  (low-rank!)

Where:
  A: 768×16 = 12,288 parameters
  B: 16×768 = 12,288 parameters
  Total: 24,576 parameters (96% reduction!)

Same idea as truncated SVD for compression.
```

---

# Section 5.6: Relationship Between Methods

---

## 5.6.1 Comparison Table

```
┌─────────────────┬────────────────┬────────────────────────────┐
│ Method          │ Input          │ Output                     │
├─────────────────┼────────────────┼────────────────────────────┤
│ Eigendecomp     │ Square matrix  │ Eigenvalues, eigenvectors  │
│ Spectral decomp │ Symmetric mat  │ Real eigenval, ortho eigvec│
│ PCA             │ Data matrix    │ Principal components       │
│ SVD             │ Any matrix     │ U, Σ, V                    │
└─────────────────┴────────────────┴────────────────────────────┘
```

---

## 5.6.2 PCA via SVD

```
PCA can be computed using SVD!

1. Center data: X_centered

2. SVD of X_centered:
   X_centered = UΣVᵀ

3. Principal components = columns of V

4. Variance explained = σᵢ² / Σσⱼ²

This is often more numerically stable than
computing eigenvalues of covariance matrix!
```

---

# Section 5.7: QR Decomposition (Brief)

---

## 5.7.1 Definition

```
A = Q × R

Where:
  Q = Orthogonal matrix
  R = Upper triangular matrix

Used for:
  - Solving linear systems
  - Computing eigenvalues (iteratively)
  - Least squares problems
```

---

## 5.7.2 Gram-Schmidt Process

```
QR decomposition can be computed using Gram-Schmidt:

Given vectors a₁, a₂, ..., aₙ

1. u₁ = a₁
   e₁ = u₁ / ||u₁||

2. u₂ = a₂ - (a₂·e₁)e₁
   e₂ = u₂ / ||u₂||

3. u₃ = a₃ - (a₃·e₁)e₁ - (a₃·e₂)e₂
   e₃ = u₃ / ||u₃||

...and so on

Result: e₁, e₂, ... are orthonormal
Q = [e₁ | e₂ | ...]
```

---

# PART 5: SUMMARY

```
Matrix Decomposition in ML/Transformers:
┌────────────────────────────────────────────────────────────────┐
│ Method              │ Use in ML/Transformers                  │
├────────────────────────────────────────────────────────────────┤
│ Eigendecomposition  │ PCA, covariance analysis               │
│ Spectral decomp     │ Graph neural networks, kernels         │
│ PCA                 │ Visualization, dimensionality reduction│
│ SVD                 │ LoRA, model compression, LSA           │
│ QR decomposition    │ Solving linear systems, stability      │
└────────────────────────────────────────────────────────────────┘
```

---

# PART 5: KEY FORMULAS

```
1. Eigenvalue equation:
   Av = λv

2. Characteristic equation:
   det(A - λI) = 0

3. Eigendecomposition:
   A = QΛQ⁻¹

4. Spectral decomposition (symmetric):
   A = QΛQᵀ

5. SVD:
   A = UΣVᵀ

6. Covariance matrix:
   C = (1/n) × XᵀX

7. Variance explained:
   λᵢ / Σλⱼ
```

---

# PART 5: PRACTICE PROBLEMS

```
Q1. Find eigenvalues of A = [2 1; 1 2]
    Answer: det(A - λI) = (2-λ)² - 1 = 0
            λ² - 4λ + 3 = 0
            λ = 3 or λ = 1

Q2. Verify: eigenvalues sum = trace
    Answer: 3 + 1 = 4, trace = 2 + 2 = 4 ✓

Q3. Verify: eigenvalues product = det
    Answer: 3 × 1 = 3, det = 4 - 1 = 3 ✓

Q4. If λ₁ = 5, λ₂ = 1, which explains more variance?
    Answer: λ₁ = 5 (larger eigenvalue = more variance)

Q5. Can [1 2; 3 4] be decomposed as QΛQᵀ?
    Answer: No, because it's not symmetric.
            Need general eigendecomposition QΛQ⁻¹

Q6. What does SVD allow that eigendecomposition doesn't?
    Answer: SVD works on ANY matrix (including rectangular)

Q7. In PCA, if top 2 eigenvalues are 8 and 2 out of total 10,
    how much variance do top 2 components explain?
    Answer: (8+2)/10 = 100%

Q8. LoRA uses A×B with A(768×16) and B(16×768).
    What's the rank of A×B?
    Answer: At most 16 (the inner dimension)
```

---

*End of Part 5*
*Next: Part 6 - Calculus (Derivatives)*

---

# =====================================================
# PART 6: CALCULUS - DERIVATIVES (⭐ CRITICAL!)
# =====================================================

---

## Why This Part?

```
⭐ DERIVATIVES = HOW DEEP LEARNING LEARNS! ⭐

Without derivatives:
  - Can't compute gradients
  - Can't do backpropagation
  - Can't train neural networks
  - No Transformers!

Derivative answers: "How much does output change when input changes?"

Training = Adjusting weights to reduce loss
         = Need to know: "How does loss change when weights change?"
         = Need derivatives!
```

---

# Section 6.1: What is a Derivative?

---

## 6.1.1 Real Life Example

```
Car speedometer problem:

Position at time t: s(t) = t² km

At t=0: s(0) = 0 km
At t=1: s(1) = 1 km
At t=2: s(2) = 4 km
At t=3: s(3) = 9 km

Speed = Rate of change of position
      = How fast position changes
      = DERIVATIVE of position!

From t=1 to t=2:
  Distance = 4 - 1 = 3 km
  Time = 2 - 1 = 1 hour
  Average speed = 3 km/h

From t=2 to t=3:
  Distance = 9 - 4 = 5 km
  Time = 3 - 2 = 1 hour
  Average speed = 5 km/h

Speed is INCREASING! (accelerating)
```

---

## 6.1.2 Graphical Understanding

```
Derivative = SLOPE of the curve at a point

        y
        │
        │         ╱
        │       ╱   (steep slope = large derivative)
        │     ╱
        │   ╱
        │ ╱   (gentle slope = small derivative)
    ────┴─────────→ x

Slope = Rise / Run = Δy / Δx

At any point, derivative tells you the instantaneous slope.
```

---

## 6.1.3 Mathematical Definition

```
Derivative of f(x) at point x:

f'(x) = lim    f(x + h) - f(x)
       h→0    ─────────────────
                     h

Notations for derivative:
  f'(x)     (Lagrange notation)
  df/dx     (Leibniz notation)
  Df(x)     (Euler notation)
  ḟ         (Newton notation - for time derivatives)

All mean the same thing!
```

---

## 6.1.4 Simple Example

```
f(x) = x²

Using definition:
f'(x) = lim    (x + h)² - x²
       h→0    ─────────────
                    h

     = lim    x² + 2xh + h² - x²
       h→0    ───────────────────
                      h

     = lim    2xh + h²
       h→0    ─────────
                  h

     = lim    h(2x + h)
       h→0    ─────────
                  h

     = lim    (2x + h)
       h→0

     = 2x

So: d/dx(x²) = 2x

At x = 3: f'(3) = 2×3 = 6
The slope of x² at x=3 is 6.
```

---

# Section 6.2: Derivative Rules

---

## 6.2.1 Constant Rule

```
If f(x) = c (constant):
  f'(x) = 0

Example:
  f(x) = 5
  f'(x) = 0

Why? A horizontal line has zero slope!
```

---

## 6.2.2 Power Rule (MOST USED!)

```
If f(x) = xⁿ:
  f'(x) = n × xⁿ⁻¹

Examples:
  d/dx(x²) = 2x¹ = 2x
  d/dx(x³) = 3x²
  d/dx(x⁴) = 4x³
  d/dx(x¹) = 1x⁰ = 1
  d/dx(x⁰) = 0×x⁻¹ = 0 (constant!)
  d/dx(x⁻¹) = -1×x⁻² = -1/x²
  d/dx(√x) = d/dx(x^0.5) = 0.5×x^(-0.5) = 1/(2√x)
```

---

## 6.2.3 Constant Multiple Rule

```
If f(x) = c × g(x):
  f'(x) = c × g'(x)

Example:
  f(x) = 5x³
  f'(x) = 5 × 3x² = 15x²
```

---

## 6.2.4 Sum Rule

```
If f(x) = g(x) + h(x):
  f'(x) = g'(x) + h'(x)

Example:
  f(x) = x² + x³
  f'(x) = 2x + 3x²
```

---

## 6.2.5 Difference Rule

```
If f(x) = g(x) - h(x):
  f'(x) = g'(x) - h'(x)

Example:
  f(x) = x³ - 2x
  f'(x) = 3x² - 2
```

---

## 6.2.6 Product Rule

```
If f(x) = g(x) × h(x):
  f'(x) = g'(x)×h(x) + g(x)×h'(x)

"First × derivative of second + Second × derivative of first"

Example:
  f(x) = x² × (x + 1)

  g(x) = x²,       g'(x) = 2x
  h(x) = x + 1,    h'(x) = 1

  f'(x) = 2x × (x+1) + x² × 1
        = 2x² + 2x + x²
        = 3x² + 2x

Verify by expanding first:
  f(x) = x³ + x²
  f'(x) = 3x² + 2x ✓
```

---

## 6.2.7 Quotient Rule

```
If f(x) = g(x) / h(x):
  f'(x) = [g'(x)×h(x) - g(x)×h'(x)] / [h(x)]²

"(Low × d-High - High × d-Low) / Low²"

Example:
  f(x) = x² / (x + 1)

  g(x) = x²,      g'(x) = 2x
  h(x) = x + 1,   h'(x) = 1

  f'(x) = [2x×(x+1) - x²×1] / (x+1)²
        = [2x² + 2x - x²] / (x+1)²
        = [x² + 2x] / (x+1)²
        = x(x + 2) / (x+1)²
```

---

## 6.2.8 Chain Rule (⭐ MOST IMPORTANT FOR DL!)

```
If f(x) = g(h(x)):
  f'(x) = g'(h(x)) × h'(x)

"Derivative of outer × Derivative of inner"

Example:
  f(x) = (2x + 3)⁵

  Outer: g(u) = u⁵,        g'(u) = 5u⁴
  Inner: h(x) = 2x + 3,    h'(x) = 2

  f'(x) = 5(2x + 3)⁴ × 2
        = 10(2x + 3)⁴
```

### Why Chain Rule Matters for Deep Learning

```
Neural Network = Composition of functions!

Layer 1: h₁ = f₁(x)
Layer 2: h₂ = f₂(h₁)
Layer 3: y = f₃(h₂)

y = f₃(f₂(f₁(x)))

To find dy/dx:
  dy/dx = dy/dh₂ × dh₂/dh₁ × dh₁/dx

This is BACKPROPAGATION!
Chain rule applied through all layers.
```

---

# Section 6.3: Derivatives of Special Functions

---

## 6.3.1 Exponential Functions

```
d/dx(eˣ) = eˣ  ← Magical! Derivative equals itself!

d/dx(aˣ) = aˣ × ln(a)

Example:
  d/dx(e³ˣ) = e³ˣ × 3 = 3e³ˣ  (chain rule)
  d/dx(2ˣ) = 2ˣ × ln(2)
```

### Transformer Connection
```
Softmax uses eˣ:
  Softmax(xᵢ) = eˣⁱ / Σⱼ eˣʲ

Derivative of eˣ is easy, which makes softmax gradient tractable!
```

---

## 6.3.2 Logarithmic Functions

```
d/dx(ln(x)) = 1/x

d/dx(logₐ(x)) = 1/(x × ln(a))

Example:
  d/dx(ln(2x)) = (1/2x) × 2 = 1/x  (chain rule)
```

### Transformer Connection
```
Cross-entropy loss uses log:
  Loss = -log(p)

d/dp(-log(p)) = -1/p

If p → 0 (very wrong prediction): derivative → -∞ (strong signal!)
If p → 1 (correct prediction): derivative → -1 (mild signal)
```

---

## 6.3.3 Trigonometric Functions

```
d/dx(sin(x)) = cos(x)
d/dx(cos(x)) = -sin(x)
d/dx(tan(x)) = sec²(x) = 1/cos²(x)
```

### Transformer Connection
```
Positional Encoding uses sin and cos:
  PE(pos, 2i) = sin(pos / 10000^(2i/d))
  PE(pos, 2i+1) = cos(pos / 10000^(2i/d))

Why sin/cos? They have bounded derivatives, periodic nature.
```

---

# Section 6.4: Higher-Order Derivatives

---

## 6.4.1 Second Derivative

```
f''(x) = d/dx(f'(x)) = d²f/dx²

First derivative: Rate of change
Second derivative: Rate of change of rate of change!

Example:
  f(x) = x³
  f'(x) = 3x²
  f''(x) = 6x
  f'''(x) = 6
  f''''(x) = 0
```

---

## 6.4.2 Physical Meaning

```
Position: s(t)
Velocity: s'(t) = v(t)      (first derivative)
Acceleration: s''(t) = a(t) (second derivative)

s(t) = t³
v(t) = 3t²
a(t) = 6t
```

---

## 6.4.3 Curvature and Optimization

```
At critical point (where f'(x) = 0):

f''(x) > 0 → Local MINIMUM (curve is concave up ∪)
f''(x) < 0 → Local MAXIMUM (curve is concave down ∩)
f''(x) = 0 → Need more analysis (could be inflection point)
```

---

## 6.4.4 Transformer Connection

```
Second derivative → Hessian matrix

The Hessian tells us about loss surface curvature.

If loss surface is very curved (large second derivative):
  → Need smaller learning rate
  → Gradient descent might oscillate

If loss surface is flat (small second derivative):
  → Can use larger learning rate
  → But gradient signal is weak

This is why adaptive optimizers (Adam) are useful!
```

---

# Section 6.5: Partial Derivatives

---

## 6.5.1 Functions of Multiple Variables

```
f(x, y) = x² + xy + y²

Two inputs: x and y
One output: f

How does f change when:
  - Only x changes? → Partial derivative with respect to x
  - Only y changes? → Partial derivative with respect to y
```

---

## 6.5.2 Notation

```
Partial derivative of f with respect to x:
  ∂f/∂x  or  fₓ  or  ∂ₓf

The symbol ∂ (partial) indicates we hold other variables constant.
```

---

## 6.5.3 Computing Partial Derivatives

```
f(x, y) = x² + xy + y²

∂f/∂x: Treat y as constant, differentiate w.r.t. x
  = 2x + y + 0
  = 2x + y

∂f/∂y: Treat x as constant, differentiate w.r.t. y
  = 0 + x + 2y
  = x + 2y
```

---

## 6.5.4 Another Example

```
f(x, y, z) = x²y + yz² + xz

∂f/∂x = 2xy + 0 + z = 2xy + z

∂f/∂y = x² + z² + 0 = x² + z²

∂f/∂z = 0 + 2yz + x = 2yz + x
```

---

## 6.5.5 Transformer Connection

```
Loss function has MILLIONS of parameters!

L(w₁, w₂, w₃, ..., wₙ)

To train, we need:
  ∂L/∂w₁
  ∂L/∂w₂
  ∂L/∂w₃
  ...
  ∂L/∂wₙ

Each tells us: "How does loss change when this weight changes?"
Update each weight based on its partial derivative!
```

---

# Section 6.6: Gradient

---

## 6.6.1 Definition

```
Gradient = Vector of all partial derivatives

∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

For f(x, y) = x² + y²:

∇f = [∂f/∂x, ∂f/∂y]
   = [2x, 2y]
```

---

## 6.6.2 Gradient Properties

```
1. Points in direction of STEEPEST INCREASE

2. Magnitude = Rate of steepest increase

3. Perpendicular to level curves

4. NEGATIVE gradient points toward steepest DECREASE
   → This is why we use gradient DESCENT!
```

---

## 6.6.3 Visual

```
For f(x, y) = x² + y² (paraboloid):

        ↑
       ╱│╲         ← gradient vectors point outward and up
      ╱ │ ╲
     ╱  │  ╲
    ╱   ●   ╲      ← minimum at origin
   ╱    │    ╲
  ───────────────
       x, y

At point (1, 1):
  ∇f = [2, 2]
  Points toward "uphill" direction
```

---

## 6.6.4 Transformer Connection

```
Training = Gradient Descent

1. Compute loss L
2. Compute gradient ∇L (all partial derivatives)
3. Update weights: w = w - α × ∇L

α = learning rate

We move in NEGATIVE gradient direction (downhill!)
to minimize loss.
```

---

# Section 6.7: Chain Rule for Multivariable Functions

---

## 6.7.1 Single Path

```
If z = f(y) and y = g(x):

dz/dx = dz/dy × dy/dx

Example:
  y = x²
  z = eʸ = eˣ²

  dz/dx = dz/dy × dy/dx
        = eʸ × 2x
        = eˣ² × 2x
        = 2xeˣ²
```

---

## 6.7.2 Multiple Paths

```
If z = f(x, y) and both x and y depend on t:

dz/dt = ∂z/∂x × dx/dt + ∂z/∂y × dy/dt

Sum over all paths from t to z!
```

---

## 6.7.3 Computational Graph

```
Backpropagation uses computational graphs:

    x ──→ [×2] ──→ a ──→ [+3] ──→ b ──→ [²] ──→ c

x = 2
a = 2×2 = 4
b = 4+3 = 7
c = 7² = 49

Forward pass: Compute outputs
Backward pass: Compute derivatives using chain rule

dc/dx = dc/db × db/da × da/dx
      = 2b × 1 × 2
      = 2×7 × 1 × 2
      = 28
```

---

# Section 6.8: Jacobian Matrix

---

## 6.8.1 Definition

```
For vector function f: Rⁿ → Rᵐ

f(x) = [f₁(x₁,...,xₙ)]
       [f₂(x₁,...,xₙ)]
       [    ...      ]
       [fₘ(x₁,...,xₙ)]

Jacobian J:

J = [∂f₁/∂x₁  ∂f₁/∂x₂  ...  ∂f₁/∂xₙ]
    [∂f₂/∂x₁  ∂f₂/∂x₂  ...  ∂f₂/∂xₙ]
    [  ...      ...    ...    ...   ]
    [∂fₘ/∂x₁  ∂fₘ/∂x₂  ...  ∂fₘ/∂xₙ]

J[i][j] = ∂fᵢ/∂xⱼ
```

---

## 6.8.2 Example

```
f(x, y) = [x² + y  ]
          [xy      ]

f₁ = x² + y
f₂ = xy

J = [∂f₁/∂x  ∂f₁/∂y]   [2x  1]
    [∂f₂/∂x  ∂f₂/∂y] = [y   x]

At (1, 2):
J = [2  1]
    [2  1]
```

---

## 6.8.3 Transformer Connection

```
Each layer in a neural network is a vector function.

Layer: f(x) where x is n-dimensional, f(x) is m-dimensional

The Jacobian tells us how ALL outputs change with respect to ALL inputs.

For backpropagation through a layer:
  Gradient of loss w.r.t. input = Jᵀ × Gradient of loss w.r.t. output
```

---

# Section 6.9: Hessian Matrix

---

## 6.9.1 Definition

```
Hessian = Matrix of second partial derivatives

For f(x₁, x₂, ..., xₙ):

H = [∂²f/∂x₁²      ∂²f/∂x₁∂x₂  ...  ∂²f/∂x₁∂xₙ]
    [∂²f/∂x₂∂x₁    ∂²f/∂x₂²    ...  ∂²f/∂x₂∂xₙ]
    [    ...          ...      ...      ...    ]
    [∂²f/∂xₙ∂x₁    ∂²f/∂xₙ∂x₂  ...  ∂²f/∂xₙ²  ]
```

---

## 6.9.2 Example

```
f(x, y) = x² + 3xy + y²

First derivatives:
∂f/∂x = 2x + 3y
∂f/∂y = 3x + 2y

Second derivatives:
∂²f/∂x² = 2
∂²f/∂y² = 2
∂²f/∂x∂y = 3
∂²f/∂y∂x = 3

H = [2  3]
    [3  2]
```

---

## 6.9.3 Properties

```
1. Hessian is symmetric: H = Hᵀ
   (if f has continuous second derivatives)

2. Eigenvalues of H tell about curvature:
   - All positive eigenvalues → local minimum
   - All negative eigenvalues → local maximum
   - Mixed signs → saddle point

3. Large eigenvalues → Sharp curvature → Need small learning rate
   Small eigenvalues → Flat regions → Slow learning
```

---

## 6.9.4 Transformer Connection

```
Second-order optimization (Newton's method):

Update: x_new = x - H⁻¹ × ∇f

Uses both gradient AND Hessian.

Problem: Computing H is O(n²) memory, O(n³) computation
For millions of parameters → IMPOSSIBLE!

Solution: Approximate methods (Adam, etc.)
```

---

# Section 6.10: Automatic Differentiation

---

## 6.10.1 The Problem

```
Manual derivative calculation is:
1. Error-prone
2. Tedious
3. Specific to each function

We need AUTOMATIC computation of derivatives!
```

---

## 6.10.2 Forward Mode vs Reverse Mode

```
Forward Mode:
  - Compute derivatives as you compute function
  - Good when: few inputs, many outputs

Reverse Mode (Backpropagation):
  - Compute function first, then derivatives backward
  - Good when: many inputs, few outputs
  - PERFECT for neural networks!
    (millions of inputs/weights, one loss output)
```

---

## 6.10.3 Computational Graph Example

```
f(x, y) = (x + y) × (x × y)

Graph:
     x ───┬──→ [+] ──→ a ──┐
          │              ├──→ [×] ──→ f
     y ───┼──→ [×] ──→ b ──┘
          │
          └──┘

Where:
  a = x + y
  b = x × y
  f = a × b

Forward: x=2, y=3
  a = 2 + 3 = 5
  b = 2 × 3 = 6
  f = 5 × 6 = 30

Backward: df/df = 1
  df/da = b = 6
  df/db = a = 5

  da/dx = 1,  da/dy = 1
  db/dx = y = 3,  db/dy = x = 2

  df/dx = df/da × da/dx + df/db × db/dx
        = 6 × 1 + 5 × 3
        = 6 + 15
        = 21

  df/dy = df/da × da/dy + df/db × db/dy
        = 6 × 1 + 5 × 2
        = 6 + 10
        = 16
```

---

# PART 6: SUMMARY

```
Calculus in Transformers:
┌──────────────────────────────────────────────────────────────┐
│ Concept              │ Use in Transformers                   │
├──────────────────────────────────────────────────────────────┤
│ Derivative           │ Rate of change, slopes                │
│ Chain rule ⭐         │ Backpropagation through layers       │
│ d/dx(eˣ) = eˣ       │ Softmax gradients                     │
│ d/dx(ln(x)) = 1/x   │ Cross-entropy loss gradients          │
│ Partial derivative   │ Gradient w.r.t. each weight           │
│ Gradient             │ Direction for weight updates          │
│ Jacobian             │ Layer-wise backprop                   │
│ Hessian              │ Curvature (for advanced optimizers)   │
│ Auto-diff            │ PyTorch/TensorFlow automatic gradients│
└──────────────────────────────────────────────────────────────┘
```

---

# PART 6: KEY FORMULAS

```
1. Power rule:      d/dx(xⁿ) = nxⁿ⁻¹
2. Chain rule:      d/dx(f(g(x))) = f'(g(x)) × g'(x)
3. Product rule:    d/dx(fg) = f'g + fg'
4. Quotient rule:   d/dx(f/g) = (f'g - fg') / g²
5. Exponential:     d/dx(eˣ) = eˣ
6. Logarithm:       d/dx(ln(x)) = 1/x
7. Gradient:        ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]
```

---

# PART 6: PRACTICE PROBLEMS

```
Q1. d/dx(3x⁴ - 2x² + 5)
    Answer: 12x³ - 4x

Q2. d/dx(e²ˣ)
    Answer: 2e²ˣ (chain rule)

Q3. d/dx(ln(x²))
    Answer: (1/x²) × 2x = 2/x

Q4. d/dx((x+1)³)
    Answer: 3(x+1)² × 1 = 3(x+1)²

Q5. For f(x,y) = x²y + y³, find ∂f/∂x and ∂f/∂y
    Answer: ∂f/∂x = 2xy
            ∂f/∂y = x² + 3y²

Q6. Find gradient of f(x,y) = x² + y² at point (3, 4)
    Answer: ∇f = [2x, 2y] = [6, 8]

Q7. If y = f(g(h(x))) and we know f'=2, g'=3, h'=4,
    what is dy/dx?
    Answer: 2 × 3 × 4 = 24 (chain rule)

Q8. Why is reverse mode autodiff better for neural networks?
    Answer: Many inputs (weights), one output (loss).
            Reverse mode computes all gradients in one pass.
```

---

*End of Part 6*
*Next: Part 7 - Calculus (Optimization)*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 7: CALCULUS - OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│                    PART 7: OPTIMIZATION                         │
│                    "Learning = Finding the Best"                │
│                                                                 │
│  Gradient hum ne Part 6 mein nikaal liya                       │
│  Ab gradient se OPTIMIZE kaise karein? 🎯                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why This Part?

```
Neural network ka sara kaam hai:
  LOSS FUNCTION ko MINIMIZE karna!

Loss kam → Model better
Loss zyada → Model worse

Optimization = Loss kam karne ka tarika

Transformer mein optimization:
  - 100+ million parameters
  - Har parameter ko adjust karna hai
  - Loss kam hota rahe

Kaise? GRADIENT DESCENT! ⬇️
```

---

# 7.1 The Mountain Analogy (पहाड़ की कहानी)

---

## 7.1.1 Finding the Lowest Point

```
Situation:
  Aap ek पहाड़ पर हो।
  रात का अंधेरा है।
  आपको सबसे नीची जगह (valley) जाना है।
  आप देख नहीं सकते!

Strategy?
  1. जहाँ खड़े हो, feel करो slope
  2. जो direction सबसे steep DOWN हो, उधर जाओ
  3. छोटा कदम लो
  4. फिर से slope feel करो
  5. Repeat...

Eventually: LOWEST POINT! ✓

This is GRADIENT DESCENT!
```

---

## 7.1.2 Mathematical Version

```
Mountain = Loss function L(w)
Your position = Weights w
Slope = Gradient ∇L(w)
Step = Weight update

Algorithm:
  w_new = w_old - η × ∇L(w_old)

Where:
  η (eta) = Step size = Learning rate
  ∇L = Gradient (which way is UP)
  -∇L = Which way is DOWN (we want to go DOWN!)
```

---

# 7.2 Gradient Descent Algorithm

---

## 7.2.1 The Core Formula

```
┌───────────────────────────────────────────────────────────┐
│          w_new = w_old - η × ∇L(w)                        │
│                                                           │
│  w_new  = Updated weights                                 │
│  w_old  = Current weights                                 │
│  η      = Learning rate (small number like 0.001)         │
│  ∇L(w)  = Gradient of Loss w.r.t. weights                 │
└───────────────────────────────────────────────────────────┘

MINUS sign kyun?
  ∇L points UPHILL (increasing loss direction)
  We want DOWNHILL (decreasing loss direction)
  So we go OPPOSITE = MINUS!
```

---

## 7.2.2 Step-by-Step Example

```
Problem: Minimize f(x) = x²

We know: Minimum is at x = 0

Start: x = 4
Learning rate: η = 0.1

Gradient: df/dx = 2x

Iteration 1:
  x = 4
  gradient = 2(4) = 8
  x_new = 4 - 0.1 × 8 = 4 - 0.8 = 3.2

Iteration 2:
  x = 3.2
  gradient = 2(3.2) = 6.4
  x_new = 3.2 - 0.1 × 6.4 = 3.2 - 0.64 = 2.56

Iteration 3:
  x = 2.56
  gradient = 2(2.56) = 5.12
  x_new = 2.56 - 0.1 × 5.12 = 2.56 - 0.512 = 2.048

...continuing...

Iteration 10:
  x ≈ 0.43

Iteration 20:
  x ≈ 0.047

Iteration 30:
  x ≈ 0.005

Converging to 0! ✓
```

---

## 7.2.3 2D Example (Two Variables)

```
Minimize: f(x, y) = x² + y²
(A paraboloid - bowl shape)

Minimum at (0, 0)

Start: (x, y) = (4, 3)
η = 0.1

Gradient: ∇f = [2x, 2y]

Iteration 1:
  gradient = [8, 6]
  x_new = 4 - 0.1 × 8 = 3.2
  y_new = 3 - 0.1 × 6 = 2.4
  New position: (3.2, 2.4)

Iteration 2:
  gradient = [6.4, 4.8]
  x_new = 3.2 - 0.64 = 2.56
  y_new = 2.4 - 0.48 = 1.92
  New position: (2.56, 1.92)

Iteration 3:
  gradient = [5.12, 3.84]
  x_new = 2.56 - 0.512 = 2.048
  y_new = 1.92 - 0.384 = 1.536
  New position: (2.048, 1.536)

Pattern: (x, y) × 0.8 each step!
Converging to (0, 0) ✓
```

---

# 7.3 Learning Rate (η) - The Step Size

---

## 7.3.1 Why Learning Rate Matters

```
Learning rate = कदम का size

Too SMALL (η = 0.0001):
  - बहुत धीरे converge होगा
  - Years लग जाएंगे training में

  x → 3.999 → 3.998 → 3.997 ... (forever!)

Too LARGE (η = 2):
  - Overshoot हो जाएगा!
  - Diverge कर जाएगा (blow up)

  x = 4 → -4 → 4 → -4 ... (oscillating!)
  or
  x = 4 → -12 → 36 → -108 ... (exploding!)

Just RIGHT (η = 0.1):
  - Smooth convergence
  - Not too slow, not too fast
```

---

## 7.3.2 Learning Rate Visual

```
Loss Landscape (imagine a bowl):

η too small:          η just right:          η too large:
   ╲                      ╲                      ╲  ╱
    ╲                      ╲                    ╱  ╲
     ╲                      ╲                  ╱    ╲
      ╲                      ↘               ↙      ↘
       ↘                      ↘             ↗
        ↘                      ↘          ↙
         ↘                      •        DIVERGE!
          ↘                   (found it!)
           ↘
            (taking forever...)

Common learning rates:
  - 0.1     (aggressive)
  - 0.01    (common starting point)
  - 0.001   (safe default)
  - 0.0001  (fine-tuning)
  - 1e-5    (very careful fine-tuning)
```

---

## 7.3.3 Example: Effect of Learning Rate

```
Function: f(x) = x²
Start: x = 4

η = 0.01 (too small):
  Step 1: x = 4 - 0.01×8 = 3.92
  Step 10: x ≈ 3.27
  Step 100: x ≈ 0.54
  Step 500: x ≈ 0.00005
  (Slow but converges)

η = 0.5 (just right for this function):
  Step 1: x = 4 - 0.5×8 = 0
  DONE IN 1 STEP! (Lucky case)

η = 1.0 (too large):
  Step 1: x = 4 - 1×8 = -4
  Step 2: x = -4 - 1×(-8) = 4
  Step 3: x = 4 - 8 = -4
  (Oscillating forever!)

η = 1.5 (way too large):
  Step 1: x = 4 - 1.5×8 = -8
  Step 2: x = -8 - 1.5×(-16) = 16
  Step 3: x = 16 - 1.5×32 = -32
  (EXPLODING! 💥)
```

---

# 7.4 Types of Gradient Descent

---

## 7.4.1 Batch Gradient Descent

```
BATCH = Use ALL data at once

Algorithm:
  1. Take ALL training examples
  2. Compute gradient using ALL of them
  3. Update weights ONCE
  4. Repeat

Loss = (1/N) × Σ L(xᵢ, yᵢ)

Example:
  Dataset: 1000 images

  Each update step:
    - Forward pass: ALL 1000 images
    - Compute loss: Average of 1000 losses
    - Backward pass: Gradient from all 1000
    - Update weights: ONE update

Pros:
  ✓ Stable gradient (accurate direction)
  ✓ Clean convergence path

Cons:
  ✗ SLOW (big datasets = too much computation)
  ✗ Memory hungry (all data in memory)
  ✗ Can get stuck in local minima
```

---

## 7.4.2 Stochastic Gradient Descent (SGD)

```
STOCHASTIC = Use ONE example at a time

Algorithm:
  1. Take ONE random training example
  2. Compute gradient using that ONE example
  3. Update weights
  4. Repeat with next example

Loss = L(x₁, y₁) for just example 1

Example:
  Dataset: 1000 images

  Step 1: Use image #472
    - Forward pass: 1 image
    - Compute loss: 1 loss
    - Update weights

  Step 2: Use image #891
    - Forward pass: 1 image
    - Compute loss: 1 loss
    - Update weights

  ... (1000 steps = 1 "epoch")

Pros:
  ✓ FAST updates
  ✓ Low memory
  ✓ Noise helps escape local minima!

Cons:
  ✗ Noisy gradient (wrong direction possible)
  ✗ Jumpy convergence
```

---

## 7.4.3 Mini-Batch Gradient Descent (⭐ MOST USED!)

```
MINI-BATCH = Use SOME examples (not all, not one)

Algorithm:
  1. Split data into batches of size B
  2. For each batch:
     - Compute gradient using batch
     - Update weights
  3. Repeat

Typical batch sizes: 16, 32, 64, 128, 256, 512

Example:
  Dataset: 1000 images
  Batch size: 100
  Batches per epoch: 1000/100 = 10

  Batch 1: Images 1-100
    - Forward pass: 100 images
    - Compute average loss
    - Update weights

  Batch 2: Images 101-200
    - Forward pass: 100 images
    - Compute average loss
    - Update weights

  ... (10 batches = 1 epoch)

Pros:
  ✓ Best of both worlds!
  ✓ Stable enough gradient
  ✓ Fast enough updates
  ✓ Fits GPU memory well
  ✓ Some noise (helps generalization)

This is what everyone uses in practice!
```

---

## 7.4.4 Comparison Visual

```
                    Convergence Path to Minimum ★

Batch GD:            Mini-batch GD:          Stochastic GD:
    ↘                    ↘                       ↙
     ↘                    ↘                     ↗
      ↘                    ↙                   ↙
       ↘                  ↓                   ↗
        ↘                ↘                  ↙
         ↘                ★                ↘
          ↘                                 ↗
           ★                                ★

Clean path           Slightly noisy       Very noisy
(smooth)             (practical)          (zigzag)

Transformer Training:
  - Batch size: 32 to 2048 (depends on GPU memory)
  - Larger batch → More stable but needs more memory
  - GPT-3 used batch size ~3 million tokens!
```

---

# 7.5 Momentum

---

## 7.5.1 The Problem with Vanilla GD

```
Problem: Ravines (लम्बी narrow valleys)

Imagine loss surface like this (top view):

        ─────────────────
       │                 │
       │   ★             │  (narrow valley)
       │                 │
        ─────────────────
          ↑
          Goal here

Normal gradient descent:
   ↙ ↗ ↙ ↗ ↙ ↗ ↙ (oscillates side to side!)

It oscillates across the narrow dimension
but makes slow progress along the valley!
```

---

## 7.5.2 Momentum Solution

```
Idea: Remember previous direction!

Real-life analogy:
  गेंद पहाड़ से नीचे लुढ़क रही है
  गेंद को MOMENTUM है
  छोटी bumps को ignore करती है
  बड़ी direction में smoothly जाती है

Formula:
  v = β × v_prev + ∇L(w)      ← velocity
  w = w - η × v                ← update

Where:
  v = velocity (accumulated gradient)
  β = momentum coefficient (usually 0.9)
  v_prev = previous velocity

With momentum:
  - Accumulate gradients from past
  - Smooth out oscillations
  - Faster convergence!
```

---

## 7.5.3 Momentum Example

```
1D Example: Gradient descent with momentum

Start: x = 10, v = 0
η = 0.1, β = 0.9
Function: f(x) = x²
Gradient: 2x

Without Momentum:
  x1 = 10 - 0.1×20 = 8
  x2 = 8 - 0.1×16 = 6.4
  x3 = 6.4 - 0.1×12.8 = 5.12
  ...

With Momentum:
  Step 1:
    gradient = 20
    v1 = 0.9×0 + 20 = 20
    x1 = 10 - 0.1×20 = 8

  Step 2:
    gradient = 16
    v2 = 0.9×20 + 16 = 18 + 16 = 34
    x2 = 8 - 0.1×34 = 4.6

  Step 3:
    gradient = 9.2
    v3 = 0.9×34 + 9.2 = 30.6 + 9.2 = 39.8
    x3 = 4.6 - 0.1×39.8 = 0.62

Faster convergence! (reached ~0 in 3 steps vs many more without momentum)
```

---

## 7.5.4 Momentum Visual

```
Without Momentum:
  ↘ ↗ ↙ ↗ ↙ (oscillating, slow progress)
       ↘
        ↘
         ★

With Momentum:
  ↘
    ↘
      ↘
        ↘
          ★ (smooth, fast!)

Ball analogy:
  Without momentum: Ball stops at each point
  With momentum: Ball rolls with inertia
```

---

# 7.6 Advanced Optimizers

---

## 7.6.1 Problems to Solve

```
Different parameters need different learning rates!

Example:
  - Frequent words (common parameters): Need small updates
  - Rare words (rare parameters): Need larger updates

One learning rate for all? Not optimal!

Idea: ADAPTIVE learning rates
  - Each parameter gets its own learning rate
  - Automatically adjusted based on history
```

---

## 7.6.2 AdaGrad (Adaptive Gradient)

```
Idea: Decrease learning rate for frequently updated parameters

Formula:
  G += gradient²                    ← accumulate squared gradients
  w = w - (η / √(G + ε)) × gradient  ← adaptive update

ε = small number (1e-8) to avoid division by zero

Problem:
  G keeps growing forever
  Eventually η/√G becomes tiny
  Learning STOPS!

Not used much anymore, but led to better methods...
```

---

## 7.6.3 RMSprop (Root Mean Square Propagation)

```
Fix AdaGrad's problem: Use MOVING AVERAGE instead!

Formula:
  G = β × G_prev + (1-β) × gradient²    ← exponential moving average
  w = w - (η / √(G + ε)) × gradient

β typically = 0.99

This way:
  - G doesn't grow forever
  - Recent gradients matter more
  - Old gradients fade away

Better than AdaGrad!
```

---

## 7.6.4 Adam (Adaptive Moment Estimation) ⭐⭐⭐

```
THE KING OF OPTIMIZERS! 👑
Most used in modern deep learning!

Combines: Momentum + RMSprop

Formula:
  m = β₁ × m_prev + (1-β₁) × gradient       ← 1st moment (mean)
  v = β₂ × v_prev + (1-β₂) × gradient²      ← 2nd moment (variance)

  m̂ = m / (1 - β₁ᵗ)                         ← bias correction
  v̂ = v / (1 - β₂ᵗ)                         ← bias correction

  w = w - η × m̂ / (√v̂ + ε)                  ← update

Default hyperparameters:
  β₁ = 0.9      (momentum term)
  β₂ = 0.999    (RMSprop term)
  ε = 1e-8      (numerical stability)
  η = 0.001     (learning rate)

Why bias correction?
  m and v start at 0
  Early values are biased toward 0
  Divide by (1 - βᵗ) to correct this
```

---

## 7.6.5 Adam Step-by-Step Example

```
Minimize f(x) = x², start at x = 10

Parameters: β₁=0.9, β₂=0.999, η=0.1, ε=1e-8
Initial: m=0, v=0

Step 1 (t=1):
  gradient = 2×10 = 20

  m = 0.9×0 + 0.1×20 = 2
  v = 0.999×0 + 0.001×400 = 0.4

  m̂ = 2 / (1 - 0.9¹) = 2 / 0.1 = 20
  v̂ = 0.4 / (1 - 0.999¹) = 0.4 / 0.001 = 400

  x = 10 - 0.1 × 20 / (√400 + 1e-8)
  x = 10 - 0.1 × 20 / 20
  x = 10 - 0.1 = 9.9

Step 2 (t=2):
  gradient = 2×9.9 = 19.8

  m = 0.9×2 + 0.1×19.8 = 1.8 + 1.98 = 3.78
  v = 0.999×0.4 + 0.001×392.04 = 0.3996 + 0.392 = 0.7916

  m̂ = 3.78 / (1 - 0.9²) = 3.78 / 0.19 = 19.89
  v̂ = 0.7916 / (1 - 0.999²) = 0.7916 / 0.001999 = 396

  x = 9.9 - 0.1 × 19.89 / (√396 + 1e-8)
  x = 9.9 - 0.1 × 19.89 / 19.9
  x = 9.9 - 0.1 ≈ 9.8

Continues smoothly toward 0!
```

---

## 7.6.6 Optimizer Comparison

```
┌────────────────────────────────────────────────────────────────────────┐
│ Optimizer    │ Pros                      │ Cons                       │
├────────────────────────────────────────────────────────────────────────┤
│ SGD          │ Simple, generalizes well  │ Slow, sensitive to η       │
│ SGD+Momentum │ Faster, smoother          │ Still need good η          │
│ AdaGrad      │ Adaptive learning rate    │ Learning rate goes to 0    │
│ RMSprop      │ Fixes AdaGrad             │ Still hyperparameters      │
│ Adam ⭐       │ Best of all, fast, stable │ Can overfit, memory heavy  │
│ AdamW        │ Adam + better weight decay│ Standard for transformers  │
└────────────────────────────────────────────────────────────────────────┘

For Transformers:
  - AdamW is most commonly used
  - Adam with weight decay (regularization)
  - β₁ = 0.9, β₂ = 0.98 or 0.999
  - Learning rate with warmup + decay
```

---

# 7.7 Learning Rate Scheduling

---

## 7.7.1 Why Schedule Learning Rate?

```
Fixed learning rate is not optimal!

Start of training:
  - Far from optimum
  - Need BIG steps to make progress
  - Higher learning rate OK

End of training:
  - Close to optimum
  - Need SMALL steps for fine adjustment
  - Lower learning rate needed

Solution: CHANGE learning rate during training!
```

---

## 7.7.2 Common Schedules

```
1. STEP DECAY
   η starts at 0.1
   Every 30 epochs: η = η × 0.1

   Epochs 1-30:   η = 0.1
   Epochs 31-60:  η = 0.01
   Epochs 61-90:  η = 0.001

   Visual:
   η
   │░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
   │                              ░░░░░░░░░░░░░░░
   │                                             ░░░░░
   └──────────────────────────────────────────────────→ epochs

2. EXPONENTIAL DECAY
   η = η₀ × γᵗ  where γ < 1 (like 0.95)

   Smoothly decreases each step

   Visual:
   η
   │░
   │ ░░
   │   ░░░
   │      ░░░░
   │          ░░░░░░
   │                 ░░░░░░░░░░░░░░
   └──────────────────────────────────────────────────→ epochs

3. COSINE ANNEALING
   η = η_min + 0.5 × (η_max - η_min) × (1 + cos(πt/T))

   Smooth cosine curve from max to min

   Visual:
   η
   │░░
   │   ░░
   │     ░░
   │       ░░░
   │          ░░░░
   │              ░░░░░░░░░
   └──────────────────────────────────────────────────→ epochs
```

---

## 7.7.3 Warmup (⭐ Important for Transformers!)

```
WARMUP = Start with very small η, gradually increase

Why?
  - Random initialization → unstable gradients
  - Big η at start → exploding updates!
  - Start small, let model stabilize, then increase

Warmup schedule:
  Step 1-1000: η increases from 0 to η_max
  Step 1000+:  η decays from η_max to η_min

Visual:
   η
   │         ░░░░░
   │       ░░     ░░░
   │      ░          ░░░
   │    ░               ░░░░
   │  ░                     ░░░░░░░░░░░
   │░
   └──────────────────────────────────────────────────→ steps
    ↑ warmup ↑     ↑ decay phase ↑

Transformer training:
  - 4000 warmup steps is common
  - Then inverse square root decay
  - Or cosine decay to 0
```

---

## 7.7.4 Original Transformer Schedule

```
From "Attention Is All You Need" paper:

lrate = d_model^(-0.5) × min(step^(-0.5), step × warmup_steps^(-1.5))

Where:
  d_model = 512 (model dimension)
  warmup_steps = 4000

This creates:
  - Linear warmup for first 4000 steps
  - Inverse square root decay after

Example with d_model=512, warmup=4000:

Step 100:    η = 0.044 × min(0.1, 0.000025×100) = 0.044 × 0.0025 = 0.00011
Step 1000:   η = 0.044 × min(0.0316, 0.00025×1000) = 0.044 × 0.025 = 0.0011
Step 4000:   η = 0.044 × min(0.0158, 0.0158) = 0.044 × 0.0158 = 0.0007 (PEAK!)
Step 10000:  η = 0.044 × min(0.01, 0.025) = 0.044 × 0.01 = 0.00044
Step 100000: η = 0.044 × min(0.00316, 0.079) = 0.044 × 0.00316 = 0.00014
```

---

# 7.8 Convexity and Local Minima

---

## 7.8.1 Convex vs Non-Convex

```
CONVEX function: Bowl shape
  - Only ONE minimum (global)
  - Gradient descent ALWAYS finds it
  - Easy!

  Example: f(x) = x²

        ╲       ╱
         ╲     ╱
          ╲   ╱
           ╲ ╱
            • ← only one minimum

NON-CONVEX function: Bumpy landscape
  - MULTIPLE minima
  - Local minima trap!
  - Gradient descent might get stuck

  Example: f(x) = x⁴ - 3x² + 1

        ╱╲     ╱╲
       ╱  ╲   ╱  ╲
      ╱    ╲ ╱    ╲
     ╱      •      ╲
           ↑ local minimum (trap!)
    • global minimum
```

---

## 7.8.2 Neural Networks are Non-Convex!

```
Bad news:
  Neural network loss is NON-CONVEX
  Millions of local minima exist
  Mathematically, finding global minimum is NP-hard!

Good news:
  1. Many local minima are "good enough"
     - They generalize similarly to global minimum

  2. Saddle points are bigger problem than local minima
     - High-dimensional spaces have many saddle points
     - Momentum helps escape them

  3. Techniques help:
     - Random initialization
     - Mini-batch noise
     - Momentum
     - Learning rate schedules

In practice:
  Don't worry about finding THE global minimum
  Find A minimum that generalizes well!
```

---

## 7.8.3 Saddle Points

```
Saddle Point = minimum in some directions, maximum in others

Like a horse saddle:
  - Minimum going front-to-back
  - Maximum going side-to-side

             ╱╲
            ╱  ╲
           ╱    ╲
        ──•──────•──
           ↖    ↗
            ╲  ╱
             ╲╱

In high dimensions:
  - Saddle points are MORE common than local minima!
  - Gradient = 0 at saddle points
  - Plain GD gets stuck!

How to escape:
  - Momentum: accumulated velocity pushes through
  - Noise from mini-batches: random kicks
  - Adam: adaptive learning rates
```

---

# 7.9 Regularization

---

## 7.9.1 The Overfitting Problem

```
Overfitting = Model memorizes training data
              but fails on new data

Like a student who:
  - Memorizes answers from practice tests
  - Fails when questions are slightly different

Visual:

  Training data: •  •  •  •  •

  Good fit:       ────────────  (simple line)
                   •  •  •  •  •

  Overfit:        ╱╲╱╲╱╲╱╲╱╲  (wiggly line)
                  •  •  •  •  •

The wiggly line PERFECTLY fits training data
but will be TERRIBLE on new data!
```

---

## 7.9.2 L2 Regularization (Weight Decay)

```
Idea: Penalize large weights!

Original loss: L(w)
Regularized loss: L(w) + λ × ||w||²

Where:
  ||w||² = sum of squared weights = w₁² + w₂² + ... + wₙ²
  λ = regularization strength (hyperparameter)

Effect:
  - Large weights → large penalty → discouraged
  - Model prefers smaller weights
  - Smaller weights → simpler model → less overfitting

Gradient update becomes:
  w = w - η × (∇L(w) + 2λw)
  w = w × (1 - 2ηλ) - η × ∇L(w)
        ↑
     "Weight decay" - weights shrink each step!
```

---

## 7.9.3 L1 Regularization

```
Loss: L(w) + λ × ||w||₁

||w||₁ = sum of absolute values = |w₁| + |w₂| + ... + |wₙ|

Effect:
  - Encourages SPARSE weights
  - Many weights become exactly 0
  - Feature selection built-in

L1 vs L2:
  L1: Some weights → 0, others stay
  L2: All weights shrink, none exactly 0
```

---

## 7.9.4 Dropout

```
DROPOUT = Randomly turn off neurons during training!

During training:
  - Each neuron has probability p of being "dropped"
  - Set its output to 0
  - Different neurons dropped each batch

During inference:
  - Use ALL neurons
  - Scale outputs by (1-p)

Example (p = 0.5):

  Training batch 1:    Training batch 2:    Inference:
  [a] ○ [c] ○          ○ [b] [c] ○          [a] [b] [c] [d]
   │     │              │   │   │            │   │   │   │
   ↓     ↓              ↓   ↓   ↓            ↓   ↓   ↓   ↓
  (dropped: b, d)      (dropped: a, d)      (all neurons)

Why it works:
  - Neurons can't co-adapt
  - Forces redundancy
  - Like training many different networks!

Transformer uses dropout:
  - After attention
  - After feedforward layers
  - On embeddings
  - Typical: p = 0.1 to 0.3
```

---

# 7.10 Optimization in Transformers

---

## 7.10.1 What Gets Optimized?

```
Transformer parameters to optimize:

1. Embedding matrices:
   - Token embeddings: vocab_size × d_model
   - Position embeddings: max_len × d_model

2. Attention weights (per layer):
   - W_Q: d_model × d_k
   - W_K: d_model × d_k
   - W_V: d_model × d_v
   - W_O: d_v × d_model

3. Feedforward layers (per layer):
   - W_1: d_model × d_ff
   - b_1: d_ff
   - W_2: d_ff × d_model
   - b_2: d_model

4. Layer normalization (per layer):
   - γ (scale): d_model
   - β (shift): d_model

5. Final output:
   - Output projection: d_model × vocab_size

Total for BERT-base:
  ~110 million parameters!

Total for GPT-3:
  ~175 BILLION parameters!
```

---

## 7.10.2 Typical Transformer Training

```
Hyperparameters (BERT-style):

Optimizer: AdamW
  β₁ = 0.9
  β₂ = 0.999
  ε = 1e-6
  weight_decay = 0.01

Learning rate:
  Peak: 1e-4 to 5e-4
  Warmup: 10,000 steps
  Decay: Linear or cosine to 0

Batch size:
  256 to 8192 tokens/batch
  Gradient accumulation if memory limited

Dropout:
  p = 0.1

Training:
  1 million+ steps
  Days to weeks on multiple GPUs

Gradient clipping:
  Clip gradient norm to max 1.0
  Prevents exploding gradients
```

---

## 7.10.3 Training Loop Pseudocode

```python
# Pseudocode for Transformer training

model = Transformer(config)
optimizer = AdamW(model.parameters(), lr=0, betas=(0.9, 0.999))
scheduler = get_warmup_scheduler(warmup_steps=4000)

for step in range(total_steps):
    # Get batch
    batch = dataloader.next_batch()

    # Forward pass
    outputs = model(batch.input_ids)
    loss = cross_entropy(outputs, batch.labels)

    # Backward pass
    loss.backward()                    # Compute gradients

    # Gradient clipping
    clip_grad_norm(model.parameters(), max_norm=1.0)

    # Update weights
    optimizer.step()

    # Update learning rate
    scheduler.step()

    # Clear gradients
    optimizer.zero_grad()

    # Log
    if step % 100 == 0:
        print(f"Step {step}, Loss: {loss.item()}")
```

---

# PART 7: SUMMARY

```
Optimization in Transformers:
┌────────────────────────────────────────────────────────────────────────┐
│ Concept              │ Use in Transformers                             │
├────────────────────────────────────────────────────────────────────────┤
│ Gradient Descent     │ Core algorithm for training                     │
│ Learning Rate        │ Controls step size (crucial hyperparameter!)    │
│ Mini-batch           │ Balance between speed and stability             │
│ Momentum             │ Smooth updates, escape saddle points            │
│ Adam/AdamW ⭐         │ Standard optimizer for transformers            │
│ Warmup               │ Stabilize early training                        │
│ LR Schedule          │ Decay learning rate over time                   │
│ Weight Decay         │ L2 regularization, prevent overfitting          │
│ Dropout              │ Regularization during training                  │
│ Gradient Clipping    │ Prevent exploding gradients                     │
└────────────────────────────────────────────────────────────────────────┘
```

---

# PART 7: KEY FORMULAS

```
1. Gradient Descent:    w = w - η × ∇L(w)

2. Momentum:            v = βv + ∇L(w)
                        w = w - η × v

3. Adam:                m = β₁m + (1-β₁)g
                        v = β₂v + (1-β₂)g²
                        w = w - η × m̂/(√v̂ + ε)

4. Weight Decay:        L_total = L + λ||w||²

5. Warmup Schedule:     η = d^(-0.5) × min(step^(-0.5), step × warmup^(-1.5))

6. Gradient Clipping:   if ||g|| > max_norm: g = g × max_norm/||g||
```

---

# PART 7: PRACTICE PROBLEMS

```
Q1. Given f(x) = x² - 4x + 4, find minimum using gradient descent.
    Start: x = 0, η = 0.1
    Do 5 iterations.

    Answer:
    f'(x) = 2x - 4
    x₀ = 0, f'(0) = -4, x₁ = 0 - 0.1×(-4) = 0.4
    x₁ = 0.4, f'(0.4) = -3.2, x₂ = 0.4 + 0.32 = 0.72
    x₂ = 0.72, f'(0.72) = -2.56, x₃ = 0.72 + 0.256 = 0.976
    x₃ = 0.976, f'(0.976) = -2.048, x₄ = 0.976 + 0.2048 = 1.18
    x₄ = 1.18, f'(1.18) = -1.64, x₅ = 1.18 + 0.164 = 1.344

    Converging to x = 2 (the minimum)

Q2. Why does learning rate too high cause divergence?
    Answer: Updates overshoot the minimum, landing on the other side
    with even larger gradient, causing exponential explosion.

Q3. What's the difference between SGD and mini-batch GD?
    Answer: SGD uses 1 sample per update (noisy, fast)
    Mini-batch uses B samples (balance of noise and stability)

Q4. Why does Adam need bias correction?
    Answer: m and v are initialized to 0, making early estimates
    biased toward 0. Dividing by (1-βᵗ) corrects this.

Q5. What is learning rate warmup and why is it used?
    Answer: Start with low η, gradually increase.
    Prevents unstable updates from random initialization.

Q6. If loss = data_loss + 0.001 × ||w||², what is λ?
    Answer: λ = 0.001 (L2 regularization coefficient)

Q7. With momentum β=0.9, if previous velocity was 10 and current
    gradient is 2, what's the new velocity?
    Answer: v = 0.9 × 10 + 2 = 9 + 2 = 11

Q8. Why is gradient clipping important for transformers?
    Answer: Prevents exploding gradients which can cause
    NaN values and training collapse.
```

---

*End of Part 7*
*Next: Part 8 - Probability Basics*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 8: PROBABILITY BASICS
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│                    PART 8: PROBABILITY                          │
│                    "Uncertainty को समझना"                       │
│                                                                 │
│  Machine Learning = Learning from uncertain data               │
│  Probability = Uncertainty की भाषा                             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why This Part?

```
Transformer probability use करता है EVERYWHERE:

1. Output prediction:
   "The cat sat on the ___"
   mat: 0.4, floor: 0.3, chair: 0.2, dog: 0.1
   ↑ These are PROBABILITIES!

2. Attention weights:
   How much to "attend" to each word
   All weights sum to 1.0 = PROBABILITY distribution!

3. Training (Cross-entropy loss):
   Measures "how wrong" our probability predictions are

4. Sampling:
   Temperature, top-k, top-p = probability manipulation

Without probability → No transformers!
```

---

# 8.1 What is Probability?

---

## 8.1.1 Real-Life Understanding

```
Probability = Chance of something happening

Examples:
  - सिक्के को उछालो → Heads की probability = 0.5 (50%)
  - Dice roll → 6 आने की probability = 1/6 ≈ 0.167 (16.7%)
  - बारिश होगी कल? → 70% chance (weather prediction)

Probability always between 0 and 1:
  0 = Impossible (असंभव)
  1 = Certain (पक्का)
  0.5 = 50-50 chance

All possible outcomes की probability का sum = 1

Dice example:
  P(1) + P(2) + P(3) + P(4) + P(5) + P(6) = 1
  1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6 = 6/6 = 1 ✓
```

---

## 8.1.2 Mathematical Notation

```
P(A) = Probability of event A happening

P(A) ∈ [0, 1]  ← Between 0 and 1

Rules:
  P(certain event) = 1
  P(impossible event) = 0
  P(A or B) = P(A) + P(B) - P(A and B)
  P(not A) = 1 - P(A)

Example:
  Deck of cards (52 cards)
  P(drawing a heart) = 13/52 = 1/4 = 0.25
  P(drawing a king) = 4/52 = 1/13 ≈ 0.077
  P(drawing king of hearts) = 1/52 ≈ 0.019
```

---

## 8.1.3 Probability in Language

```
Language is PROBABILISTIC!

"I am going to the ___"
  P(market) = 0.20
  P(school) = 0.15
  P(office) = 0.15
  P(park) = 0.10
  P(mall) = 0.08
  P(bank) = 0.07
  ... (many more possibilities)

Total = 1.0

Transformer learns these probabilities from data!
  - Sees millions of sentences
  - Learns: After "going to the", which words come next?
  - Outputs a probability distribution over ALL words
```

---

# 8.2 Conditional Probability

---

## 8.2.1 The Core Idea

```
Conditional Probability = Probability GIVEN some information

P(A | B) = Probability of A, given that B happened

Read as: "Probability of A given B"

Example:
  सिक्का fair है।
  P(Heads) = 0.5

  But अगर मुझे पता है कि पिछले 5 tosses में सब Heads आए...
  P(6th is Heads | first 5 were Heads) = ?

  For fair coin: Still 0.5! (coins have no memory)

Another example:
  P(rain tomorrow) = 0.3 (general)
  P(rain tomorrow | cloudy today) = 0.7 (higher with information!)

New information CHANGES probabilities!
```

---

## 8.2.2 The Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│             P(A and B)                                    │
│  P(A | B) = ──────────                                   │
│               P(B)                                        │
│                                                           │
└───────────────────────────────────────────────────────────┘

Meaning:
  P(A | B) = P(A and B) / P(B)

  "Probability of A given B"
  = "Probability of both A and B"
    divided by
    "Probability of B"

Example:
  Deck of 52 cards
  P(King | Heart) = ?
  "If I draw a heart, what's probability it's a king?"

  P(King and Heart) = 1/52  (only king of hearts)
  P(Heart) = 13/52 = 1/4

  P(King | Heart) = (1/52) / (1/4) = (1/52) × (4/1) = 4/52 = 1/13

  Verification: 13 hearts में से 1 king है → 1/13 ✓
```

---

## 8.2.3 Conditional Probability in Transformers

```
Language model = Conditional probability machine!

P(next word | previous words)

Example:
  Input: "The cat sat on the"

  Model computes:
  P(mat | The cat sat on the) = 0.35
  P(floor | The cat sat on the) = 0.20
  P(couch | The cat sat on the) = 0.15
  P(table | The cat sat on the) = 0.08
  ...

Full sentence probability:
  P("The cat sat on the mat")
  = P(The) × P(cat|The) × P(sat|The cat) × P(on|The cat sat) × ...

Chain rule of probability!
```

---

# 8.3 Chain Rule of Probability

---

## 8.3.1 The Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  P(A, B, C, ...) = P(A) × P(B|A) × P(C|A,B) × ...        │
│                                                           │
└───────────────────────────────────────────────────────────┘

Joint probability = Product of conditional probabilities

Example with 3 events:
  P(A, B, C) = P(A) × P(B|A) × P(C|A,B)

For sentence "I love math":
  P("I love math")
  = P("I") × P("love" | "I") × P("math" | "I love")
```

---

## 8.3.2 Autoregressive Language Models

```
GPT/Transformer LM uses chain rule!

Generate sentence word by word:

Step 1: P(w₁)
  Sample first word

Step 2: P(w₂ | w₁)
  Given first word, sample second

Step 3: P(w₃ | w₁, w₂)
  Given first two, sample third

...and so on

Example generation:
  P("The") = 0.08 → Sample "The"
  P("cat" | "The") = 0.05 → Sample "cat"
  P("sat" | "The cat") = 0.12 → Sample "sat"
  P("on" | "The cat sat") = 0.25 → Sample "on"
  P("the" | "The cat sat on") = 0.40 → Sample "the"
  P("mat" | "The cat sat on the") = 0.35 → Sample "mat"

Full probability:
  P("The cat sat on the mat")
  = 0.08 × 0.05 × 0.12 × 0.25 × 0.40 × 0.35
  = 0.0000168 (small number, but highest among alternatives!)
```

---

# 8.4 Bayes' Theorem

---

## 8.4.1 The Most Famous Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│              P(B|A) × P(A)                                │
│  P(A|B) = ─────────────────                              │
│                P(B)                                       │
│                                                           │
└───────────────────────────────────────────────────────────┘

In words:
  P(A|B) = P(B|A) × P(A) / P(B)

  Posterior = (Likelihood × Prior) / Evidence

This lets us REVERSE conditional probability!
  If we know P(B|A), we can find P(A|B)
```

---

## 8.4.2 Real-World Example

```
Medical test example:

Disease affects 1% of population: P(Disease) = 0.01

Test accuracy:
  - If you have disease, test positive 99% time: P(+|D) = 0.99
  - If you don't have disease, test positive 5% time: P(+|~D) = 0.05

Question: You test positive. What's P(Disease | +)?

Using Bayes:
  P(D|+) = P(+|D) × P(D) / P(+)

First, find P(+):
  P(+) = P(+|D)×P(D) + P(+|~D)×P(~D)
  P(+) = 0.99×0.01 + 0.05×0.99
  P(+) = 0.0099 + 0.0495
  P(+) = 0.0594

Now apply Bayes:
  P(D|+) = (0.99 × 0.01) / 0.0594
  P(D|+) = 0.0099 / 0.0594
  P(D|+) ≈ 0.167 = 16.7%

Surprising! Positive test → only 16.7% chance of disease!
(Because disease is rare, false positives dominate)
```

---

## 8.4.3 Bayes in Machine Learning

```
Bayesian perspective on learning:

Prior: P(θ)
  - What we believe about parameters BEFORE seeing data
  - "Initial guess"

Likelihood: P(data | θ)
  - How likely is this data IF these are the true parameters?

Posterior: P(θ | data)
  - Updated belief AFTER seeing data
  - This is what we want!

P(θ | data) = P(data | θ) × P(θ) / P(data)

Neural networks approximate this!
  - Training updates our "beliefs" (weights)
  - Each batch of data updates the posterior
```

---

# 8.5 Independence

---

## 8.5.1 What is Independence?

```
Two events are INDEPENDENT if:
  Knowing one tells you NOTHING about the other

Mathematically:
  P(A and B) = P(A) × P(B)

Or equivalently:
  P(A | B) = P(A)  (B doesn't change A's probability)

Example of INDEPENDENT events:
  - Coin flip 1 and coin flip 2
  - P(H₁ and H₂) = P(H₁) × P(H₂) = 0.5 × 0.5 = 0.25

Example of DEPENDENT events:
  - Drawing cards without replacement
  - P(2nd is Ace | 1st was Ace) ≠ P(2nd is Ace)
  - 3/51 ≠ 4/52
```

---

## 8.5.2 Independence Assumption

```
Naive Bayes Classifier assumes independence:

P(spam | words) ∝ P(spam) × P(w₁|spam) × P(w₂|spam) × ...

Assumes words are independent given class!
  - "free" and "money" independent? NO! (But we pretend yes)

This is why it's called "Naive"

Transformers DON'T make this assumption!
  - Attention captures word dependencies
  - "free" and "money" together = more spam-like
  - Context matters!
```

---

## 8.5.3 Conditional Independence

```
A and B are conditionally independent given C if:
  P(A and B | C) = P(A|C) × P(B|C)

Example:
  A = "Person has flu symptoms"
  B = "Person's coworker has flu symptoms"
  C = "Flu season is happening"

Without knowing C:
  A and B are dependent (if one has flu, other might too)

Given C (knowing it's flu season):
  A and B become more independent
  (Both explained by the season, not each other)
```

---

# 8.6 Expected Value (E[X])

---

## 8.6.1 The Concept

```
Expected Value = "Average" in the long run

If you repeat an experiment many times,
expected value is the average outcome.

Notation: E[X] or μ (mu)

Formula (discrete):
  E[X] = Σ xᵢ × P(xᵢ)
       = x₁×P(x₁) + x₂×P(x₂) + ... + xₙ×P(xₙ)

"Sum of (each value × its probability)"
```

---

## 8.6.2 Examples

```
Example 1: Fair die roll
  Values: 1, 2, 3, 4, 5, 6
  Each probability: 1/6

  E[X] = 1×(1/6) + 2×(1/6) + 3×(1/6) + 4×(1/6) + 5×(1/6) + 6×(1/6)
       = (1+2+3+4+5+6)/6
       = 21/6
       = 3.5

  Average roll = 3.5 (even though you can never roll 3.5!)

Example 2: Weighted die (6 appears more)
  P(1) = P(2) = P(3) = P(4) = P(5) = 0.1
  P(6) = 0.5

  E[X] = 1×0.1 + 2×0.1 + 3×0.1 + 4×0.1 + 5×0.1 + 6×0.5
       = 0.1 + 0.2 + 0.3 + 0.4 + 0.5 + 3.0
       = 4.5

  Higher expected value because 6 is more likely!

Example 3: Lottery
  Win $1,000,000 with probability 0.000001
  Lose $1 (ticket cost) with probability 0.999999

  E[gain] = 1,000,000 × 0.000001 + (-1) × 0.999999
          = 1 - 0.999999
          = 0.000001

  Expected gain ≈ $0 (actually slightly negative with real lotteries)
```

---

## 8.6.3 Expected Value in ML

```
Loss function = Expected loss over data

L = E[ℓ(prediction, truth)]
  = Σ ℓ(predᵢ, truthᵢ) × P(data point i)

With uniform data distribution:
  L = (1/N) × Σ ℓ(predᵢ, truthᵢ)

This is just AVERAGE loss over all training examples!

Training goal:
  Minimize E[Loss]
  = Minimize expected loss
  = Minimize average loss
```

---

# 8.7 Variance and Standard Deviation

---

## 8.7.1 Variance

```
Variance = "How spread out" are the values?

Var(X) = E[(X - μ)²]
       = E[X²] - (E[X])²

Alternative formula:
  Var(X) = Σ (xᵢ - μ)² × P(xᵢ)

Notation: Var(X) or σ²

Low variance = Values clustered near mean
High variance = Values spread out
```

---

## 8.7.2 Variance Examples

```
Example 1: Fair die
  μ = E[X] = 3.5

  Var(X) = E[X²] - (E[X])²

  E[X²] = 1²×(1/6) + 2²×(1/6) + 3²×(1/6) + 4²×(1/6) + 5²×(1/6) + 6²×(1/6)
        = (1+4+9+16+25+36)/6
        = 91/6
        ≈ 15.17

  Var(X) = 15.17 - 3.5²
         = 15.17 - 12.25
         = 2.92

Example 2: Constant (always 5)
  E[X] = 5
  E[X²] = 25
  Var(X) = 25 - 25 = 0

  No spread → zero variance!

Example 3: Two extreme values
  X = 0 with P = 0.5
  X = 10 with P = 0.5

  E[X] = 0×0.5 + 10×0.5 = 5
  E[X²] = 0×0.5 + 100×0.5 = 50
  Var(X) = 50 - 25 = 25

  High spread → high variance!
```

---

## 8.7.3 Standard Deviation

```
Standard Deviation = √Variance

σ = √(Var(X))

Why square root?
  - Variance is in "squared units"
  - Dice variance = 2.92 "squared points" (?)
  - Standard deviation = √2.92 ≈ 1.71 points (same units!)

For die: σ ≈ 1.71
  Meaning: Typical deviation from mean (3.5) is about 1.7

Rule of thumb (for normal distribution):
  - 68% of values within 1σ of mean
  - 95% of values within 2σ of mean
  - 99.7% of values within 3σ of mean
```

---

## 8.7.4 Variance in Deep Learning

```
Variance matters in neural networks:

1. Weight initialization:
   - Variance too high → gradients explode
   - Variance too low → gradients vanish
   - Xavier/He initialization: Set variance = 2/n

2. Batch normalization:
   - Normalize to zero mean, unit variance
   - Var(normalized) = 1

3. Attention scores:
   - Scaled dot-product divides by √d_k
   - Why? To control variance!
   - Var(q·k) ≈ d_k for unit variance q, k
   - After scaling: Var(q·k/√d_k) ≈ 1
```

---

# 8.8 Probability Distributions

---

## 8.8.1 What is a Distribution?

```
Probability Distribution = Complete description of all probabilities

Discrete distribution: List all values and their probabilities
  Die: {(1, 1/6), (2, 1/6), (3, 1/6), (4, 1/6), (5, 1/6), (6, 1/6)}

Continuous distribution: Probability density function (PDF)
  Can't list all values (infinite!)
  Instead: P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx

Key property:
  Sum (discrete) or integral (continuous) over all values = 1
```

---

## 8.8.2 Uniform Distribution

```
UNIFORM = All values equally likely

Discrete uniform (dice):
  P(X = k) = 1/n for k = 1, 2, ..., n

Continuous uniform [a, b]:
  f(x) = 1/(b-a) for a ≤ x ≤ b

Example: Random number between 0 and 1
  f(x) = 1 for 0 ≤ x ≤ 1
  P(0.3 ≤ X ≤ 0.7) = 0.7 - 0.3 = 0.4

Properties:
  E[X] = (a + b) / 2   (midpoint)
  Var(X) = (b - a)² / 12
```

---

## 8.8.3 Categorical Distribution

```
CATEGORICAL = Generalized coin flip (multiple outcomes)

Each outcome has its own probability:
  P(X = k) = pₖ where Σpₖ = 1

Example: Word prediction
  P("mat") = 0.35
  P("floor") = 0.20
  P("chair") = 0.15
  P("table") = 0.10
  P("other") = 0.20

  Sum = 1.0 ✓

THIS IS WHAT SOFTMAX OUTPUTS!

Softmax creates a categorical distribution:
  - n possible words
  - Each has probability pᵢ
  - Sum to 1
```

---

## 8.8.4 Multinomial Distribution

```
MULTINOMIAL = Multiple categorical trials

Roll a k-sided die n times
Count how many times each side appeared

Example: Roll loaded die 100 times
  Side 1 appeared 10 times
  Side 2 appeared 15 times
  ...
  Side 6 appeared 30 times

Probability of specific count vector:
  P(counts = [n₁, n₂, ..., nₖ]) = (n! / n₁!n₂!...nₖ!) × p₁^n₁ × p₂^n₂ × ... × pₖ^nₖ

In NLP:
  - Document = multiple word samples
  - "Bag of words" model
  - Counts how many times each word appears
```

---

# 8.9 Sampling

---

## 8.9.1 What is Sampling?

```
Sampling = Randomly picking values according to distribution

Given probability distribution, GENERATE values

Example: Sample from die distribution
  Run 1: 3
  Run 2: 6
  Run 3: 1
  Run 4: 4
  ...

Over many samples, frequencies ≈ probabilities
  ~16.7% will be 1s, ~16.7% will be 2s, etc.

In Python:
  import numpy as np
  np.random.choice([1,2,3,4,5,6], p=[1/6]*6)
```

---

## 8.9.2 Sampling in Transformers

```
Text generation = Sampling from word distribution!

Input: "The cat sat on the"

Model outputs:
  P("mat") = 0.35
  P("floor") = 0.20
  P("chair") = 0.15
  ...

Greedy decoding:
  Always pick highest probability
  → Always "mat"
  → Boring, repetitive text!

Random sampling:
  Sample according to probabilities
  → Sometimes "mat" (35%), sometimes "floor" (20%), etc.
  → More diverse text!
```

---

## 8.9.3 Temperature Sampling

```
TEMPERATURE = Controls randomness

softmax_with_temperature:
  pᵢ = exp(logitᵢ / T) / Σ exp(logitⱼ / T)

T = 1.0: Normal softmax
T → 0: More deterministic (sharpen distribution)
T → ∞: More random (flatten distribution)

Example logits: [2.0, 1.0, 0.5]

T = 1.0:
  exp([2.0, 1.0, 0.5]) = [7.39, 2.72, 1.65]
  probs = [0.63, 0.23, 0.14]

T = 0.5 (sharper):
  exp([4.0, 2.0, 1.0]) = [54.6, 7.39, 2.72]
  probs = [0.84, 0.11, 0.04]
  (First option dominates more)

T = 2.0 (flatter):
  exp([1.0, 0.5, 0.25]) = [2.72, 1.65, 1.28]
  probs = [0.48, 0.29, 0.23]
  (More uniform)
```

---

## 8.9.4 Top-k and Top-p Sampling

```
TOP-K: Only sample from top k most likely words

Example (k=3):
  Original: mat=0.35, floor=0.20, chair=0.15, table=0.10, ...
  Keep only top 3: mat, floor, chair
  Renormalize: mat=0.50, floor=0.29, chair=0.21
  Sample from these 3 only

TOP-P (Nucleus Sampling): Keep words until cumulative P ≥ p

Example (p=0.7):
  Sorted: mat=0.35, floor=0.20, chair=0.15, table=0.10, ...
  Cumulative: 0.35, 0.55, 0.70, 0.80, ...
  Stop at 0.70: Keep mat, floor, chair
  Sample from these

Why top-p is better:
  - Adapts to distribution shape
  - If one word has P=0.9, only sample that word
  - If distribution is flat, keep many words
```

---

# 8.10 Joint and Marginal Probability

---

## 8.10.1 Joint Probability

```
JOINT PROBABILITY = Probability of multiple events together

P(X=x, Y=y) = Probability that X=x AND Y=y simultaneously

Example: Two dice rolls
  P(first=3, second=5) = 1/6 × 1/6 = 1/36

Joint distribution table:
  X = {0, 1}, Y = {0, 1}

       Y=0    Y=1
  X=0  0.2    0.3   | 0.5
  X=1  0.1    0.4   | 0.5
       ─────────────
       0.3    0.7   | 1.0

  P(X=0, Y=0) = 0.2
  P(X=0, Y=1) = 0.3
  P(X=1, Y=0) = 0.1
  P(X=1, Y=1) = 0.4
```

---

## 8.10.2 Marginal Probability

```
MARGINAL = Probability of one variable (ignoring others)

"Sum out" the other variable

P(X=x) = Σᵧ P(X=x, Y=y)

From above table:
  P(X=0) = P(X=0,Y=0) + P(X=0,Y=1) = 0.2 + 0.3 = 0.5
  P(X=1) = P(X=1,Y=0) + P(X=1,Y=1) = 0.1 + 0.4 = 0.5

  P(Y=0) = P(X=0,Y=0) + P(X=1,Y=0) = 0.2 + 0.1 = 0.3
  P(Y=1) = P(X=0,Y=1) + P(X=1,Y=1) = 0.3 + 0.4 = 0.7

These are the row/column sums in the table!
(Written in "margins" of the table → "marginal")
```

---

## 8.10.3 In NLP

```
Word co-occurrence = Joint probability

P(word₁="machine", word₂="learning")
  Higher than
P(word₁="machine", word₂="banana")

Embedding models learn to capture joint probabilities!

Word2Vec objective:
  P(context word | target word)
  Related to joint distribution of word pairs
```

---

# PART 8: SUMMARY

```
Probability in Transformers:
┌────────────────────────────────────────────────────────────────────────┐
│ Concept              │ Use in Transformers                             │
├────────────────────────────────────────────────────────────────────────┤
│ Probability P(X)     │ Softmax outputs, attention weights             │
│ Conditional P(A|B)   │ P(next word | context) - core of LM!           │
│ Chain Rule           │ Autoregressive generation                       │
│ Bayes' Theorem       │ Posterior updating, some model variants        │
│ Independence         │ Attention learns dependencies (no assumption)   │
│ Expected Value       │ Loss = expected loss over data                  │
│ Variance             │ Scaled attention (÷√d_k), initialization       │
│ Categorical dist.    │ Softmax output distribution                     │
│ Sampling             │ Text generation (temperature, top-k, top-p)    │
│ Joint probability    │ Word co-occurrence, relationships               │
└────────────────────────────────────────────────────────────────────────┘
```

---

# PART 8: KEY FORMULAS

```
1. Conditional probability:  P(A|B) = P(A,B) / P(B)

2. Chain rule:              P(A,B,C) = P(A) × P(B|A) × P(C|A,B)

3. Bayes' theorem:          P(A|B) = P(B|A) × P(A) / P(B)

4. Independence:            P(A,B) = P(A) × P(B)

5. Expected value:          E[X] = Σ xᵢ × P(xᵢ)

6. Variance:                Var(X) = E[X²] - (E[X])²

7. Temperature softmax:     pᵢ = exp(zᵢ/T) / Σ exp(zⱼ/T)
```

---

# PART 8: PRACTICE PROBLEMS

```
Q1. A bag has 3 red and 7 blue balls. Pick one.
    What is P(red)?
    Answer: 3/10 = 0.3

Q2. Roll two dice. What is P(sum = 7)?
    Answer: Outcomes summing to 7: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1)
    = 6 outcomes out of 36 = 6/36 = 1/6 ≈ 0.167

Q3. P(A) = 0.4, P(B) = 0.5, P(A|B) = 0.6
    Find P(A and B).
    Answer: P(A|B) = P(A,B)/P(B)
    0.6 = P(A,B)/0.5
    P(A,B) = 0.3

Q4. Are A and B in Q3 independent?
    Answer: If independent, P(A,B) = P(A)×P(B) = 0.4×0.5 = 0.2
    But P(A,B) = 0.3 ≠ 0.2
    NOT independent!

Q5. E[X] = 5, E[X²] = 30. Find Var(X).
    Answer: Var(X) = E[X²] - (E[X])² = 30 - 25 = 5

Q6. Softmax outputs: [0.6, 0.3, 0.1]
    You sample 1000 times. Approximately how many times
    will you get the first option?
    Answer: 0.6 × 1000 = 600 times (approximately)

Q7. Why does lower temperature make text generation more deterministic?
    Answer: Lower T sharpens the distribution, making the highest
    probability word much more likely to be sampled.

Q8. In P(next|context), what is P(mat|"The cat sat on the") = 0.4?
    Answer: Given the context "The cat sat on the", there is a
    40% probability that the next word is "mat".
```

---

*End of Part 8*
*Next: Part 9 - Probability Distributions*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 9: PROBABILITY DISTRIBUTIONS (ADVANCED)
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│                  PART 9: DISTRIBUTIONS                          │
│                  "Data के Patterns"                              │
│                                                                 │
│  Different types of randomness have different shapes           │
│  Understanding shapes = Understanding data                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why This Part?

```
Distributions appear EVERYWHERE in deep learning:

1. Weight initialization: Gaussian distribution
2. Dropout: Bernoulli distribution
3. Batch statistics: Sample from data distribution
4. Output layer: Categorical (softmax)
5. VAE: Gaussian latent space
6. Noise injection: Various distributions

Knowing distributions = Knowing how to:
  - Initialize weights properly
  - Understand model uncertainty
  - Design loss functions
  - Sample from models
```

---

# 9.1 Normal (Gaussian) Distribution ⭐⭐⭐

---

## 9.1.1 The Bell Curve

```
THE most important distribution in all of ML!

                        ╱╲
                      ╱    ╲
                    ╱        ╲
                  ╱            ╲
                ╱                ╲
              ╱                    ╲
           ╱                          ╲
       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    μ (mean)

Named after Carl Friedrich Gauss
Also called "Normal" because it appears SO often in nature
```

---

## 9.1.2 The Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│             1              -(x-μ)²                        │
│  f(x) = ───────── × exp(─────────)                       │
│         σ√(2π)             2σ²                           │
│                                                           │
└───────────────────────────────────────────────────────────┘

Parameters:
  μ (mu) = Mean (center of the bell)
  σ (sigma) = Standard deviation (width of the bell)
  σ² = Variance

Notation: X ~ N(μ, σ²)
Read as: "X follows Normal distribution with mean μ and variance σ²"

Standard Normal: μ = 0, σ = 1
  X ~ N(0, 1)
```

---

## 9.1.3 Properties

```
Properties of Normal Distribution:

1. Symmetric around mean
   P(X < μ - a) = P(X > μ + a)

2. 68-95-99.7 Rule:
   - 68% of data within 1σ of mean
   - 95% of data within 2σ of mean
   - 99.7% of data within 3σ of mean

   │       ╱╲
   │     ╱    ╲
   │   ╱   68%  ╲
   │ ╱    ├──┤    ╲
   │╱  95% │    │  ╲
   ├──────┴────┴──────
        μ-σ  μ  μ+σ

3. Mean = Median = Mode (all at center)

4. Tails extend to ±∞ (but probability becomes tiny)

5. Sum of normals is normal:
   X ~ N(μ₁, σ₁²), Y ~ N(μ₂, σ₂²)
   X + Y ~ N(μ₁ + μ₂, σ₁² + σ₂²)
```

---

## 9.1.4 Why Normal Appears Everywhere

```
Central Limit Theorem (CLT):

Sum of MANY independent random variables → Normal!

Example:
  Roll 1 die: Uniform {1,2,3,4,5,6}
  Roll 2 dice, add: Triangular shape
  Roll 10 dice, add: Almost normal!
  Roll 100 dice, add: Very normal!

This is why normal appears in nature:
  - Heights = sum of many genetic factors
  - Measurement errors = sum of many small errors
  - Neural network outputs = sum of many weighted inputs!

Weight initialization:
  Output = w₁x₁ + w₂x₂ + ... + wₙxₙ
  Sum of many terms → approximately Normal
  So we initialize weights from Normal distribution!
```

---

## 9.1.5 Normal in Neural Networks

```
1. Weight Initialization:
   W ~ N(0, σ²)

   Xavier init: σ² = 1/n_in
   He init: σ² = 2/n_in (for ReLU)

   Why?
   - Keep variance stable across layers
   - Prevent exploding/vanishing gradients

2. Batch Normalization:
   Normalize activations to N(0, 1)
   Then scale/shift: γ×normalized + β

3. Gaussian Noise:
   Add noise during training: x + ε where ε ~ N(0, σ²)
   Regularization effect

4. VAE Latent Space:
   Encode to N(μ, σ²)
   Sample using reparameterization: z = μ + σ × ε, ε ~ N(0,1)
```

---

## 9.1.6 Multivariate Normal

```
Normal in multiple dimensions:

Univariate: Single variable X ~ N(μ, σ²)
Multivariate: Vector X ~ N(μ, Σ)

Where:
  μ = Mean vector [μ₁, μ₂, ..., μₙ]
  Σ = Covariance matrix (n × n)

Formula:
  f(x) = (1 / √((2π)ⁿ|Σ|)) × exp(-½(x-μ)ᵀΣ⁻¹(x-μ))

2D example:
  μ = [0, 0]
  Σ = [[1, 0],
       [0, 1]]

  This is 2D standard normal (uncorrelated)

  Σ = [[1, 0.8],
       [0.8, 1]]

  This has correlation 0.8 (tilted ellipse)

Embeddings often assumed to be multivariate normal!
```

---

# 9.2 Bernoulli Distribution

---

## 9.2.1 The Simplest Distribution

```
Bernoulli = Coin flip (success/failure, yes/no, 0/1)

X ∈ {0, 1}

P(X = 1) = p
P(X = 0) = 1 - p = q

Formula:
  P(X = x) = pˣ × (1-p)^(1-x)

  x = 1: p¹ × (1-p)⁰ = p
  x = 0: p⁰ × (1-p)¹ = 1-p

Properties:
  E[X] = p
  Var(X) = p(1-p)

Maximum variance at p = 0.5:
  Var = 0.5 × 0.5 = 0.25
```

---

## 9.2.2 Bernoulli in Deep Learning

```
1. DROPOUT:
   Each neuron: Keep with probability p, drop with probability 1-p
   Mask ~ Bernoulli(p)

   mask = [1, 0, 1, 1, 0, 1, ...]  (sampled)
   output = activation × mask

2. Binary Classification:
   Output: P(class = 1) = σ(logit) = p
   True label: y ∈ {0, 1}

   Loss = -[y×log(p) + (1-y)×log(1-p)]
   This is Bernoulli negative log-likelihood!

3. Binary Cross-Entropy:
   Same as above!
   BCE is the natural loss for Bernoulli outcomes
```

---

# 9.3 Binomial Distribution

---

## 9.3.1 Multiple Bernoulli Trials

```
Binomial = Number of successes in n independent Bernoulli trials

X = number of heads in n coin flips

X ~ Binomial(n, p)

Formula:
  P(X = k) = C(n,k) × pᵏ × (1-p)^(n-k)

Where:
  C(n,k) = n! / (k!(n-k)!)  (combinations)
  k = number of successes
  n = total trials
  p = success probability

Example: 10 coin flips, P(exactly 6 heads)?
  P(X = 6) = C(10,6) × 0.5⁶ × 0.5⁴
           = 210 × 0.0156 × 0.0625
           = 0.205 (about 20.5%)

Properties:
  E[X] = np
  Var(X) = np(1-p)
```

---

## 9.3.2 Binomial Approaches Normal

```
When n is large, Binomial ≈ Normal!

Binomial(n, p) ≈ N(np, np(1-p))

Example: 1000 coin flips
  E[heads] = 1000 × 0.5 = 500
  Var = 1000 × 0.5 × 0.5 = 250
  σ = √250 ≈ 15.8

  P(between 470 and 530 heads) ≈ 95%
  (within 2σ of mean)

This is CLT in action again!
```

---

# 9.4 Categorical and Multinomial

---

## 9.4.1 Categorical Distribution

```
Categorical = Generalized Bernoulli (more than 2 outcomes)

X ∈ {1, 2, 3, ..., k}
P(X = i) = pᵢ where Σpᵢ = 1

Example: Die roll
  k = 6
  P(X = i) = 1/6 for all i (fair die)

One-hot encoding:
  X = 3 → [0, 0, 1, 0, 0, 0]

THIS IS SOFTMAX OUTPUT!

Softmax converts logits to categorical probabilities:
  logits = [2.0, 1.0, 0.5, 0.1, -0.5, -1.0]
  probs = softmax(logits) = [0.41, 0.15, 0.09, 0.06, 0.03, 0.02]
  Sum = 1.0 ✓
```

---

## 9.4.2 Multinomial Distribution

```
Multinomial = Multiple categorical trials

Roll die n times, count each outcome

X = [n₁, n₂, n₃, n₄, n₅, n₆] where Σnᵢ = n

P(X = [n₁,...,nₖ]) = (n! / Π nᵢ!) × Π pᵢ^nᵢ

Example: Roll fair die 12 times
  Expected count per side = 12/6 = 2

In NLP:
  Document = Bag of words
  Each word is a "die roll"
  Multinomial models word frequency
```

---

# 9.5 Exponential Family

---

## 9.5.1 What is Exponential Family?

```
Many distributions share a common form:

f(x; θ) = h(x) × exp(η(θ)ᵀT(x) - A(θ))

Members:
  - Normal
  - Bernoulli
  - Binomial
  - Poisson
  - Exponential
  - Gamma
  - Beta
  - Categorical
  - and more!

Why care?
  - Nice mathematical properties
  - Easy to find maximum likelihood
  - Generalized Linear Models (GLM)
  - Natural for neural network outputs
```

---

## 9.5.2 Softmax is Exponential Family!

```
Categorical distribution in exponential family form:

P(X = k) = exp(θₖ) / Σ exp(θⱼ)

This IS softmax!

Properties from exponential family:
  - Gradient of log-partition = expected value
  - Second derivative = variance
  - Convex log-likelihood (nice for optimization)

Cross-entropy loss comes from:
  - Negative log-likelihood of categorical distribution
  - Natural loss for softmax outputs
```

---

# 9.6 Maximum Likelihood Estimation (MLE)

---

## 9.6.1 The Core Idea

```
MLE = Find parameters that make observed data most likely

Given: Data points x₁, x₂, ..., xₙ
Find: Parameters θ that maximize P(data | θ)

Likelihood:
  L(θ) = P(x₁, x₂, ..., xₙ | θ)

Assuming independence:
  L(θ) = P(x₁|θ) × P(x₂|θ) × ... × P(xₙ|θ)
       = Π P(xᵢ|θ)

Log-likelihood (easier to work with):
  ℓ(θ) = log L(θ) = Σ log P(xᵢ|θ)

MLE: θ* = argmax ℓ(θ)
```

---

## 9.6.2 MLE Example: Coin Flips

```
Data: 7 heads, 3 tails in 10 flips
Find: Best estimate of P(heads) = p

Likelihood:
  L(p) = p⁷ × (1-p)³

Log-likelihood:
  ℓ(p) = 7×log(p) + 3×log(1-p)

To maximize, take derivative and set to 0:
  dℓ/dp = 7/p - 3/(1-p) = 0
  7(1-p) = 3p
  7 - 7p = 3p
  7 = 10p
  p = 0.7

MLE estimate: p̂ = 7/10 = 0.7

Intuitive! Best estimate of P(heads) = observed frequency
```

---

## 9.6.3 MLE for Normal Distribution

```
Data: x₁, x₂, ..., xₙ from N(μ, σ²)
Find: Best μ and σ²

Log-likelihood:
  ℓ(μ, σ²) = -n/2 × log(2πσ²) - 1/(2σ²) × Σ(xᵢ - μ)²

Maximizing:
  μ̂ = (1/n) × Σxᵢ = sample mean
  σ̂² = (1/n) × Σ(xᵢ - μ̂)² = sample variance

MLE says: Best estimates are sample statistics!
```

---

## 9.6.4 MLE is Neural Network Training!

```
Neural network training IS maximum likelihood!

Model outputs: P(y | x; θ)
Data: (x₁,y₁), (x₂,y₂), ..., (xₙ,yₙ)

Log-likelihood:
  ℓ(θ) = Σ log P(yᵢ | xᵢ; θ)

MAXIMIZING log-likelihood = MINIMIZING negative log-likelihood

Loss = -ℓ(θ) = -Σ log P(yᵢ | xᵢ; θ)

For classification with softmax:
  P(y=k | x) = softmax(z)_k
  -log P(y=k | x) = Cross-entropy loss!

SO:
  Cross-entropy loss = Negative log-likelihood
  Training = Maximum likelihood estimation!
```

---

# 9.7 KL Divergence Preview

---

## 9.7.1 Comparing Distributions

```
Given two distributions P and Q, how different are they?

KL Divergence:
  D_KL(P || Q) = Σ P(x) × log(P(x) / Q(x))

Properties:
  - D_KL ≥ 0 always
  - D_KL = 0 iff P = Q
  - NOT symmetric! D_KL(P||Q) ≠ D_KL(Q||P)

In ML:
  P = true distribution (data)
  Q = model distribution (predictions)

Minimizing KL divergence = Making Q match P
```

---

## 9.7.2 KL and Cross-Entropy

```
Cross-entropy:
  H(P, Q) = -Σ P(x) × log Q(x)

Entropy:
  H(P) = -Σ P(x) × log P(x)

Relationship:
  H(P, Q) = H(P) + D_KL(P || Q)

Since H(P) is constant (data doesn't change):
  Minimizing cross-entropy = Minimizing KL divergence!

This is why cross-entropy loss works:
  It pushes model distribution toward true distribution!
```

---

# 9.8 Softmax as Distribution

---

## 9.8.1 Softmax Creates Probability

```
Softmax converts any real numbers to valid probability distribution

Input: logits z = [z₁, z₂, ..., zₖ] (any real numbers)
Output: probs p = [p₁, p₂, ..., pₖ] (valid probabilities)

Formula:
  pᵢ = exp(zᵢ) / Σ exp(zⱼ)

Properties guaranteed:
  1. pᵢ > 0 for all i (exponential is always positive)
  2. Σpᵢ = 1 (normalization)
  3. Larger zᵢ → Larger pᵢ (order preserved)
```

---

## 9.8.2 Softmax Example

```
Logits: z = [2.0, 1.0, 0.1]

Step 1: Exponentiate
  exp(z) = [e², e¹, e^0.1]
         = [7.39, 2.72, 1.11]

Step 2: Sum
  Σ = 7.39 + 2.72 + 1.11 = 11.22

Step 3: Normalize
  p = [7.39/11.22, 2.72/11.22, 1.11/11.22]
    = [0.659, 0.242, 0.099]

Check: 0.659 + 0.242 + 0.099 = 1.0 ✓

Interpretation:
  Class 1: 66% probability
  Class 2: 24% probability
  Class 3: 10% probability
```

---

## 9.8.3 Softmax Numerical Stability

```
Problem: exp(large number) = ∞ (overflow!)

z = [1000, 1001, 1002]
exp(z) = [e^1000, e^1001, e^1002] = [∞, ∞, ∞]

Solution: Subtract maximum before exponentiating

z' = z - max(z) = [1000-1002, 1001-1002, 1002-1002]
                = [-2, -1, 0]

exp(z') = [0.135, 0.368, 1.0]
sum = 1.503
p = [0.09, 0.24, 0.67]

SAME result as unstable version (mathematically)!

softmax(z) = softmax(z - c) for any constant c

All libraries do this automatically!
```

---

## 9.8.4 Log-Softmax

```
Often need log(softmax(z)) for cross-entropy

Naive: log(softmax(z))
Problem: If softmax is tiny → log(tiny) = -∞

Better: Compute directly!

log(softmax(z))ᵢ = log(exp(zᵢ) / Σexp(zⱼ))
                 = zᵢ - log(Σexp(zⱼ))
                 = zᵢ - logsumexp(z)

Where logsumexp is computed stably:
  logsumexp(z) = max(z) + log(Σexp(z - max(z)))

PyTorch:
  F.log_softmax(z, dim=-1)  # Stable and fast!
```

---

# 9.9 Mixture Models

---

## 9.9.1 Gaussian Mixture Model (GMM)

```
Single Gaussian: One bell curve
Mixture: Multiple bell curves combined!

P(x) = Σ πₖ × N(x; μₖ, σₖ²)

Where:
  πₖ = mixture weight (probability of component k)
  Σπₖ = 1
  N(x; μₖ, σₖ²) = Gaussian with mean μₖ, variance σₖ²

Example: Heights of population
  - Men: N(175cm, 7²)
  - Women: N(162cm, 6²)
  - Mixed: 0.5×N(175, 49) + 0.5×N(162, 36)

Visual:
      ╱╲            ╱╲
    ╱    ╲        ╱    ╲
  ╱        ╲    ╱        ╲
 ╱          ╲  ╱          ╲
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Women       Men

Combined gives bimodal distribution!
```

---

## 9.9.2 GMM in Deep Learning

```
Mixture Density Networks:
  - Output is GMM parameters
  - Predict mean, variance, mixture weights
  - Good for multi-modal predictions

Example: Predicting where someone will go
  - Home? Work? Gym?
  - Single prediction fails
  - GMM can represent all options!

VAE with GMM prior:
  - Instead of single Gaussian latent space
  - Use mixture of Gaussians
  - More expressive representations
```

---

# PART 9: SUMMARY

```
Distributions in Transformers:
┌────────────────────────────────────────────────────────────────────────┐
│ Distribution       │ Use in Transformers                               │
├────────────────────────────────────────────────────────────────────────┤
│ Normal (Gaussian)  │ Weight init, batch norm, noise, VAE               │
│ Bernoulli          │ Dropout masks, binary classification              │
│ Categorical        │ Softmax output (next word prediction)             │
│ Multinomial        │ Bag-of-words, document modeling                   │
│ MLE                │ Training = maximizing likelihood                   │
│ Softmax            │ Converts logits to categorical distribution       │
│ Temperature        │ Controls softmax sharpness                        │
│ Mixture models     │ Multi-modal predictions                           │
└────────────────────────────────────────────────────────────────────────┘
```

---

# PART 9: KEY FORMULAS

```
1. Normal:          f(x) = (1/σ√2π) × exp(-(x-μ)²/2σ²)

2. Bernoulli:       P(X=x) = pˣ(1-p)^(1-x)

3. Binomial:        P(X=k) = C(n,k) × pᵏ(1-p)^(n-k)

4. Categorical:     P(X=k) = pₖ where Σpₖ = 1

5. Softmax:         pᵢ = exp(zᵢ) / Σexp(zⱼ)

6. MLE:             θ* = argmax Σ log P(xᵢ|θ)

7. KL Divergence:   D_KL(P||Q) = Σ P(x) log(P(x)/Q(x))

8. Cross-entropy:   H(P,Q) = -Σ P(x) log Q(x)
```

---

# PART 9: PRACTICE PROBLEMS

```
Q1. X ~ N(100, 25). What is P(X < 90)?
    Answer: σ = 5, z = (90-100)/5 = -2
    P(Z < -2) ≈ 0.023 (2.3%)

Q2. Dropout p=0.2. Expected number of neurons dropped from 100?
    Answer: E[dropped] = 100 × 0.2 = 20 neurons

Q3. Fair coin, 10 flips. P(exactly 5 heads)?
    Answer: C(10,5) × 0.5^5 × 0.5^5 = 252 × 0.03125 = 0.246

Q4. Softmax([3, 1, 1]). Find probabilities.
    Answer: exp([3,1,1]) = [20.09, 2.72, 2.72]
    sum = 25.53
    probs = [0.787, 0.107, 0.107]

Q5. Data: 8 heads, 2 tails. MLE for p?
    Answer: p̂ = 8/10 = 0.8

Q6. Why is softmax(z) = softmax(z - max(z))?
    Answer: softmax(z-c)ᵢ = exp(zᵢ-c)/Σexp(zⱼ-c)
            = exp(zᵢ)×exp(-c) / Σexp(zⱼ)×exp(-c)
            = exp(zᵢ)/Σexp(zⱼ) = softmax(z)ᵢ
    Exponential of constant cancels!

Q7. What does minimizing cross-entropy achieve?
    Answer: Makes model distribution Q approach true distribution P
    (Equivalent to minimizing KL divergence)

Q8. Xavier initialization uses variance = 1/n. Why?
    Answer: Keeps output variance ≈ input variance,
    preventing gradients from exploding/vanishing through layers.
```

---

*End of Part 9*
*Next: Part 10 - Information Theory*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 10: INFORMATION THEORY
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│                PART 10: INFORMATION THEORY                      │
│                "Surprise को नापना"                               │
│                                                                 │
│  How much information is in a message?                         │
│  How surprised should we be?                                    │
│  Foundation of modern ML loss functions!                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why This Part?

```
Information theory is ESSENTIAL for understanding:

1. Cross-entropy loss:
   - THE loss function for classification
   - THE loss function for language models
   - Based on information theory!

2. KL divergence:
   - Measures "distance" between distributions
   - Used in VAE, knowledge distillation
   - Regularization in many models

3. Attention mechanism:
   - Information flow between tokens
   - Which tokens are "informative"

4. Compression and embeddings:
   - Efficient representation = compression
   - Embeddings compress meaning

Claude Shannon invented this field in 1948!
```

---

# 10.1 Information and Surprise

---

## 10.1.1 The Core Intuition

```
INFORMATION = SURPRISE

Low probability event → High surprise → High information
High probability event → Low surprise → Low information

Examples:
  "Sun rose today" → P ≈ 1 → No surprise → No information
  "Alien landed in Delhi" → P ≈ 0 → High surprise → High information

More formally:
  If event has probability p:
  Information = -log(p)

Why log?
  - Makes information additive
  - Two independent events: I(A,B) = I(A) + I(B)
  - log(p₁ × p₂) = log(p₁) + log(p₂)
```

---

## 10.1.2 Information Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  I(x) = -log₂(P(x))    (in bits)                         │
│                                                           │
│  I(x) = -ln(P(x))      (in nats)                         │
│                                                           │
└───────────────────────────────────────────────────────────┘

Examples (using log₂):

  Event              Probability    Information
  ─────────────────────────────────────────────
  Fair coin heads    0.5            -log₂(0.5) = 1 bit
  Roll 6 on die      1/6 ≈ 0.167    -log₂(0.167) ≈ 2.58 bits
  Specific card      1/52 ≈ 0.019   -log₂(0.019) ≈ 5.7 bits
  Win lottery        10⁻⁸           -log₂(10⁻⁸) ≈ 26.6 bits

Less likely = More bits needed to describe it!
```

---

## 10.1.3 Why Bits?

```
1 bit = Information needed to distinguish 2 equally likely outcomes

Coin flip:
  Heads or Tails? → 1 bit (yes/no question)

2 bits = 4 outcomes
  Two coin flips: HH, HT, TH, TT

3 bits = 8 outcomes
  Three coin flips: 2³ = 8 possibilities

n bits = 2ⁿ outcomes

To identify 1 out of N equally likely options:
  Need log₂(N) bits

Examples:
  N = 8 → 3 bits
  N = 1024 → 10 bits
  N = 50,000 (vocab size) → ~15.6 bits
```

---

# 10.2 Entropy

---

## 10.2.1 Average Information

```
ENTROPY = Expected (average) information

H(X) = E[I(X)] = E[-log P(X)]
     = -Σ P(x) × log P(x)

Entropy measures:
  - Average surprise
  - Uncertainty in the distribution
  - How "spread out" the distribution is
```

---

## 10.2.2 Entropy Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  H(X) = -Σ P(x) × log P(x)                               │
│                                                           │
│  (Sum over all possible values of X)                     │
│                                                           │
└───────────────────────────────────────────────────────────┘

Convention: 0 × log(0) = 0
(Because lim p→0 of p×log(p) = 0)
```

---

## 10.2.3 Entropy Examples

```
Example 1: Fair coin
  P(H) = 0.5, P(T) = 0.5

  H = -[0.5×log₂(0.5) + 0.5×log₂(0.5)]
    = -[0.5×(-1) + 0.5×(-1)]
    = -[-0.5 - 0.5]
    = 1 bit

  Maximum entropy for binary outcome!

Example 2: Biased coin (P(H) = 0.9)
  H = -[0.9×log₂(0.9) + 0.1×log₂(0.1)]
    = -[0.9×(-0.152) + 0.1×(-3.322)]
    = -[-0.137 - 0.332]
    = 0.469 bits

  Less entropy! (More predictable)

Example 3: Certain outcome (P(H) = 1)
  H = -[1×log₂(1) + 0×log₂(0)]
    = -[1×0 + 0]
    = 0 bits

  Zero entropy! (No uncertainty)
```

---

## 10.2.4 Entropy Properties

```
Properties:
  1. H(X) ≥ 0 always (non-negative)

  2. H(X) = 0 iff X is deterministic
     (Only one outcome has P = 1)

  3. Maximum entropy when uniform:
     H_max = log(n) for n outcomes
     Fair die: H = log₂(6) ≈ 2.58 bits

  4. Adding more probable outcomes → more entropy

Visual intuition:
  Low entropy: Sharp peak (predictable)
       │
       ██
       ██
   ────██────

  High entropy: Flat (unpredictable)
       │
   ████████
   ████████
   ────────
```

---

## 10.2.5 Entropy in NLP

```
Language has entropy!

P(next word | context) = distribution over vocabulary

High entropy context:
  "The ___"
  Could be: cat, dog, house, man, woman, tree, ...
  High uncertainty → High entropy

Low entropy context:
  "The cat sat on the ___"
  Likely: mat, floor, chair, couch, bed
  Lower uncertainty → Lower entropy

  "2 + 2 = ___"
  Almost certainly: 4
  Very low entropy

Transformer learns to REDUCE entropy:
  Given context → Predict next word with low entropy
  Good model → Confident predictions → Low entropy
```

---

# 10.3 Cross-Entropy

---

## 10.3.1 The Core Idea

```
CROSS-ENTROPY = Information needed when using wrong distribution

Scenario:
  True distribution: P
  Model distribution: Q

If we use Q to encode messages that actually come from P:
  How many bits on average?

H(P, Q) = -Σ P(x) × log Q(x)

Cross-entropy is ALWAYS ≥ Entropy:
  H(P, Q) ≥ H(P)

Equality only when P = Q (model is perfect!)
```

---

## 10.3.2 Cross-Entropy Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  H(P, Q) = -Σ P(x) × log Q(x)                            │
│                                                           │
│  P = true distribution (data)                            │
│  Q = model distribution (predictions)                    │
│                                                           │
└───────────────────────────────────────────────────────────┘

For single example with one-hot label:
  True: P = [0, 0, 1, 0, 0]  (class 3 is correct)
  Model: Q = [0.1, 0.1, 0.6, 0.1, 0.1]

  H(P, Q) = -[0×log(0.1) + 0×log(0.1) + 1×log(0.6) + 0×log(0.1) + 0×log(0.1)]
          = -log(0.6)
          = 0.51 nats (or 0.74 bits)

Only the TRUE class contributes!
  H(P, Q) = -log(Q_true_class)
```

---

## 10.3.3 Cross-Entropy Loss

```
THIS IS THE LOSS FUNCTION FOR CLASSIFICATION!

Single example:
  Loss = -log(predicted probability of correct class)
       = -log(P_model(y_true | x))

Batch of examples:
  Loss = -(1/N) × Σ log(P_model(yᵢ | xᵢ))

Why this works:
  - Model predicts wrong? → Low probability for true class → High loss
  - Model predicts right? → High probability for true class → Low loss
  - Minimizing cross-entropy → Making predictions confident AND correct

Example:
  True class: 2
  Model outputs: [0.1, 0.7, 0.2]  (Class 1 predicted highest!)
  Loss = -log(0.2) = 1.61 (high!)

  Model outputs: [0.05, 0.05, 0.9]  (Class 2 predicted highest!)
  Loss = -log(0.9) = 0.11 (low!)
```

---

## 10.3.4 Cross-Entropy in Language Models

```
Language model loss = Cross-entropy over words

For sequence "The cat sat":
  P("The") → Loss₁ = -log P("The")
  P("cat" | "The") → Loss₂ = -log P("cat" | "The")
  P("sat" | "The cat") → Loss₃ = -log P("sat" | "The cat")

Total loss = (Loss₁ + Loss₂ + Loss₃) / 3

Per-token cross-entropy!

Perplexity = 2^(cross-entropy)
  - "How many words is the model confused between?"
  - Perplexity 100 ≈ Choosing from 100 equally likely words
  - Lower perplexity = Better model

GPT-3: ~20 perplexity (very good!)
Random: ~50,000 perplexity (vocab size, very bad)
```

---

# 10.4 KL Divergence

---

## 10.4.1 Measuring Distribution Difference

```
KL DIVERGENCE = Extra bits needed due to wrong distribution

D_KL(P || Q) = H(P, Q) - H(P)
             = "Cross-entropy" - "Entropy"
             = "Bits with Q" - "Bits with P"
             = "Wasted bits due to using Q instead of P"
```

---

## 10.4.2 KL Divergence Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  D_KL(P || Q) = Σ P(x) × log(P(x) / Q(x))                │
│                                                           │
│              = Σ P(x) × [log P(x) - log Q(x)]            │
│                                                           │
└───────────────────────────────────────────────────────────┘

Alternative form:
  D_KL(P || Q) = -H(P) + H(P, Q)

Properties:
  - D_KL ≥ 0 always (Gibbs' inequality)
  - D_KL = 0 iff P = Q
  - NOT symmetric: D_KL(P||Q) ≠ D_KL(Q||P) generally
```

---

## 10.4.3 KL Divergence Example

```
P = [0.5, 0.5]  (fair coin)
Q = [0.9, 0.1]  (biased coin)

D_KL(P || Q) = 0.5×log(0.5/0.9) + 0.5×log(0.5/0.1)
             = 0.5×log(0.556) + 0.5×log(5)
             = 0.5×(-0.587) + 0.5×(1.609)
             = -0.294 + 0.805
             = 0.511 nats

D_KL(Q || P) = 0.9×log(0.9/0.5) + 0.1×log(0.1/0.5)
             = 0.9×log(1.8) + 0.1×log(0.2)
             = 0.9×(0.588) + 0.1×(-1.609)
             = 0.529 - 0.161
             = 0.368 nats

Different! KL is asymmetric!
```

---

## 10.4.4 Why KL is Asymmetric

```
D_KL(P || Q): Using Q to approximate P

  P has mass where Q doesn't? → BIG penalty!
  Q has mass where P doesn't? → No penalty (P×log term is 0)

  "Mode-seeking" behavior

D_KL(Q || P): Using P to approximate Q

  Q has mass where P doesn't? → BIG penalty!
  P has mass where Q doesn't? → No penalty

  "Mean-seeking" behavior

In ML:
  Usually D_KL(P_data || Q_model)
  = We want model to cover all modes of data
  = Cross-entropy loss is equivalent!
```

---

## 10.4.5 KL in Deep Learning

```
1. VAE (Variational Autoencoder):
   Loss = Reconstruction + β × D_KL(q(z|x) || p(z))
   Push encoder distribution toward prior!

2. Knowledge Distillation:
   Student learns from teacher:
   Loss = D_KL(P_teacher || P_student)
   Match teacher's probability distribution!

3. Policy Gradient (RL):
   Constrain policy updates:
   D_KL(π_old || π_new) < ε
   Don't change too fast!

4. Information Bottleneck:
   Compress while preserving information
   Balance D_KL terms
```

---

# 10.5 Relationship: Entropy, Cross-Entropy, KL

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    H(P, Q) = H(P) + D_KL(P || Q)                           │
│                                                             │
│    Cross-entropy = Entropy + KL Divergence                 │
│                                                             │
│    ┌──────────┐   ┌─────────┐   ┌───────────────┐         │
│    │H(P,Q)    │ = │ H(P)    │ + │ D_KL(P||Q)   │         │
│    │Cross-ent.│   │ Entropy │   │ KL Div.      │         │
│    └──────────┘   └─────────┘   └───────────────┘         │
│                                                             │
│  Total bits     = Minimum bits + Wasted bits               │
│  needed           possible        (wrong model)            │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Since H(P) is constant (data doesn't change):
  Minimizing cross-entropy H(P,Q)
  = Minimizing KL divergence D_KL(P||Q)
  = Making Q match P!

THIS IS WHY CROSS-ENTROPY LOSS WORKS!
```

---

# 10.6 Mutual Information

---

## 10.6.1 Shared Information

```
MUTUAL INFORMATION = Information shared between two variables

I(X; Y) = How much does knowing X tell us about Y?

If X and Y are independent:
  I(X; Y) = 0 (knowing one tells nothing about other)

If X determines Y completely:
  I(X; Y) = H(Y) (knowing X tells everything about Y)
```

---

## 10.6.2 Mutual Information Formula

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  I(X; Y) = H(X) + H(Y) - H(X, Y)                         │
│                                                           │
│         = H(X) - H(X | Y)                                │
│                                                           │
│         = D_KL(P(X,Y) || P(X)P(Y))                       │
│                                                           │
└───────────────────────────────────────────────────────────┘

Properties:
  - I(X; Y) = I(Y; X) (symmetric!)
  - I(X; Y) ≥ 0
  - I(X; X) = H(X) (information with self = entropy)
```

---

## 10.6.3 Mutual Information Visual

```
Venn diagram view:

   ┌─────────────────────────────────────┐
   │           H(X,Y)                    │
   │   ┌───────────────────────┐        │
   │   │        ┌─────────────┐│        │
   │   │  H(X)  │   I(X;Y)    ││  H(Y)  │
   │   │        │   (shared)  ││        │
   │   │        └─────────────┘│        │
   │   └───────────────────────┘        │
   └─────────────────────────────────────┘

H(X) = Uncertainty in X
H(Y) = Uncertainty in Y
I(X;Y) = Shared uncertainty (overlap)
H(X,Y) = Total uncertainty
H(X|Y) = Uncertainty in X after knowing Y = H(X) - I(X;Y)
```

---

## 10.6.4 Mutual Information in NLP

```
Word relationships = Mutual information

I(word₁; word₂) = How often do they co-occur vs. random?

High mutual information pairs:
  - "machine" ↔ "learning"
  - "New" ↔ "York"
  - "ice" ↔ "cream"

Low mutual information pairs:
  - "the" ↔ "quantum" (both common, but unrelated)
  - "pizza" ↔ "algorithm"

Pointwise Mutual Information (PMI):
  PMI(x, y) = log(P(x,y) / (P(x)P(y)))

Used in:
  - Word embeddings (GloVe is related to PMI)
  - Collocation detection
  - Feature selection
```

---

# 10.7 Information Theory in Attention

---

## 10.7.1 Attention as Information Selection

```
Attention = Selecting informative tokens

Query asks: "What information do I need?"
Keys answer: "Here's what I have"
Values provide: "Here's the actual information"

Attention weights = Information relevance scores

High attention weight = High information content for query
Low attention weight = Low information content for query
```

---

## 10.7.2 Entropy of Attention Distribution

```
Attention weights form a probability distribution!

α = softmax(QKᵀ/√d_k) = [α₁, α₂, ..., αₙ]
Sum to 1 ✓

Entropy of attention:
  H(α) = -Σ αᵢ × log(αᵢ)

High entropy attention:
  - Weights spread across many tokens
  - "Looking at everything"
  - Diffuse attention

Low entropy attention:
  - Weights concentrated on few tokens
  - "Focusing on specific words"
  - Sharp attention

Different heads learn different entropy patterns!
  Some: Sharp focus (syntax, specific relations)
  Some: Broad attention (context, global meaning)
```

---

## 10.7.3 Information Bottleneck Perspective

```
Transformer as information compressor:

Input: Many tokens, high-dimensional embeddings
Output: Compressed representation for task

Goal: Keep task-relevant information, discard noise

I(Input; Representation) → Minimize (compression)
I(Representation; Output) → Maximize (relevance)

Trade-off! Can't compress too much or lose signal.

Attention helps:
  - Select relevant information (high I with output)
  - Ignore irrelevant tokens (low I with noise)
```

---

# 10.8 Bits-per-Character and Perplexity

---

## 10.8.1 Bits-per-Character (BPC)

```
BPC = Cross-entropy in bits at character level

Lower BPC = Better compression = Better model

Example:
  Model gives 0.8 BPC on English text
  Meaning: On average, each character takes 0.8 bits to encode

Theoretical minimum:
  English text entropy ≈ 1-1.5 bits per character
  (Calculated by Shannon using human experiments!)

GPT-level models achieve ~0.9-1.0 BPC
  Almost optimal compression of English!
```

---

## 10.8.2 Perplexity

```
PERPLEXITY = 2^(cross-entropy in bits)
           = e^(cross-entropy in nats)

Interpretation: "Effective vocabulary size"
  - Perplexity 10 ≈ Choosing from 10 equally likely words
  - Perplexity 100 ≈ Choosing from 100 equally likely words

Formula:
  PPL = exp(-(1/N) × Σ log P(wᵢ | context))

Lower perplexity = Better model

Benchmarks:
  - Random: ~Vocab size (50,000)
  - N-gram models: ~100-200
  - LSTM: ~50-80
  - GPT-2: ~20-30
  - GPT-3/4: ~10-20
```

---

## 10.8.3 Why Perplexity Matters

```
Perplexity directly measures:
  "How well does the model predict the next word?"

Connection to loss:
  Loss = -log P(correct word)
  Average loss = Cross-entropy
  Perplexity = exp(Average loss)

Example:
  Average loss = 3.0 nats
  Perplexity = e³ ≈ 20

  Model is as confused as choosing among 20 equally likely words

In practice:
  Report perplexity on held-out test set
  Compare models fairly
  Lower perplexity = Better language understanding
```

---

# PART 10: SUMMARY

```
Information Theory in Transformers:
┌────────────────────────────────────────────────────────────────────────┐
│ Concept           │ Use in Transformers                                │
├────────────────────────────────────────────────────────────────────────┤
│ Information       │ Surprise = -log(p), rare events = more info       │
│ Entropy H(X)      │ Uncertainty in predictions                         │
│ Cross-entropy     │ THE loss function! -Σp×log(q)                      │
│ KL Divergence     │ VAE, distillation, policy constraints             │
│ Mutual Information│ Word relationships, feature selection             │
│ Perplexity        │ Model evaluation metric = 2^(cross-entropy)       │
│ Attention entropy │ Sharp vs. diffuse attention patterns              │
│ Info bottleneck   │ Compression-relevance trade-off                   │
└────────────────────────────────────────────────────────────────────────┘
```

---

# PART 10: KEY FORMULAS

```
1. Information:     I(x) = -log P(x)

2. Entropy:         H(X) = -Σ P(x) log P(x)

3. Cross-entropy:   H(P,Q) = -Σ P(x) log Q(x)

4. KL Divergence:   D_KL(P||Q) = Σ P(x) log(P(x)/Q(x))

5. Relationship:    H(P,Q) = H(P) + D_KL(P||Q)

6. Mutual Info:     I(X;Y) = H(X) + H(Y) - H(X,Y)

7. Perplexity:      PPL = exp(cross-entropy) = 2^(cross-entropy in bits)

8. CE Loss:         Loss = -log P_model(y_true | x)
```

---

# PART 10: PRACTICE PROBLEMS

```
Q1. P(x) = 0.01. How many bits of information?
    Answer: I(x) = -log₂(0.01) = -log₂(1/100) = log₂(100) ≈ 6.64 bits

Q2. Fair die entropy?
    Answer: H = -6 × (1/6)×log₂(1/6) = -6 × (1/6)×(-2.58) = 2.58 bits

Q3. Model predicts P(correct) = 0.9. What is cross-entropy loss?
    Answer: Loss = -log(0.9) = 0.105 nats (or -log₂(0.9) = 0.152 bits)

Q4. Cross-entropy loss = 4.6 nats. What is perplexity?
    Answer: PPL = e^4.6 ≈ 100

Q5. Model A: perplexity 50. Model B: perplexity 25.
    Which is better?
    Answer: Model B (lower perplexity = better predictions)

Q6. Why is cross-entropy loss equivalent to minimizing KL divergence?
    Answer: H(P,Q) = H(P) + D_KL(P||Q)
    H(P) is constant (data entropy), so minimizing H(P,Q)
    equals minimizing D_KL(P||Q)

Q7. Attention weights: [0.9, 0.05, 0.05]. Calculate entropy.
    Answer: H = -[0.9×log(0.9) + 0.05×log(0.05) + 0.05×log(0.05)]
             = -[0.9×(-0.105) + 0.05×(-3) + 0.05×(-3)]
             = -[-0.095 - 0.15 - 0.15]
             = 0.395 nats (low entropy = sharp attention)

Q8. What does perplexity = vocab_size mean?
    Answer: Random guessing! Model has no better prediction than
    uniform distribution over all words.
```

---

*End of Part 10*
*Next: Part 11 - Special Functions (Activation, Normalization)*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 11: SPECIAL FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│               PART 11: SPECIAL FUNCTIONS                        │
│               "Transformer के Special Tools"                    │
│                                                                 │
│  Activation functions, Normalization, Softmax                  │
│  These make neural networks actually WORK!                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Why This Part?

```
Without these functions, neural networks are JUST linear!

y = W₂(W₁x) = (W₂W₁)x = Wx

Just a single linear transformation!
No matter how many layers!

Special functions add:
  1. Non-linearity (activation functions)
  2. Stability (normalization)
  3. Probability (softmax)
  4. Position awareness (positional encoding)
```

---

# 11.1 Activation Functions

---

## 11.1.1 Why Non-linearity?

```
Without non-linearity:
  Layer 1: y₁ = W₁x
  Layer 2: y₂ = W₂y₁ = W₂W₁x
  Layer 3: y₃ = W₃y₂ = W₃W₂W₁x = Wx

  Just ONE matrix! Useless deep network.

With non-linearity:
  Layer 1: y₁ = σ(W₁x)      ← non-linear function σ
  Layer 2: y₂ = σ(W₂y₁)
  Layer 3: y₃ = σ(W₃y₂)

  Can't collapse! Each layer adds capacity.

Non-linearity lets networks learn complex patterns!
```

---

## 11.1.2 Sigmoid

```
┌───────────────────────────────────────────────────────────┐
│                        1                                  │
│  σ(x) = ─────────────                                    │
│         1 + e^(-x)                                       │
└───────────────────────────────────────────────────────────┘

Output range: (0, 1)

Shape:
            1 ──────────────────────────•
              │                      ╱
              │                    ╱
          0.5 │─────────────────•─────────
              │              ╱
              │            ╱
            0 │•──────────────────────────
             -∞            0             +∞

Properties:
  σ(0) = 0.5
  σ(∞) → 1
  σ(-∞) → 0
  σ'(x) = σ(x)(1 - σ(x))  ← Derivative

Problems:
  1. Vanishing gradient: σ'(x) ≤ 0.25 always!
     Deep networks → gradient → 0
  2. Not zero-centered
  3. exp() is expensive

Used in:
  - Binary classification output
  - Gates in LSTM/GRU
  - NOT in transformer hidden layers
```

---

## 11.1.3 Tanh

```
┌───────────────────────────────────────────────────────────┐
│           e^x - e^(-x)                                    │
│  tanh(x) = ────────────                                  │
│           e^x + e^(-x)                                   │
└───────────────────────────────────────────────────────────┘

Output range: (-1, 1)

Shape:
            1 ──────────────────────────•
              │                      ╱
              │                   ╱
            0 │─────────────────•─────────
              │              ╱
              │           ╱
           -1 │•──────────────────────────
             -∞            0             +∞

Properties:
  tanh(0) = 0  (zero-centered! Better than sigmoid)
  tanh'(x) = 1 - tanh²(x)

Better than sigmoid:
  - Zero-centered output
  - Stronger gradients

Still has vanishing gradient problem!

Used in:
  - RNN hidden states (traditional)
  - Some attention mechanisms
```

---

## 11.1.4 ReLU (Rectified Linear Unit) ⭐

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  ReLU(x) = max(0, x)                                     │
│                                                           │
└───────────────────────────────────────────────────────────┘

Shape:
              │              ╱
              │            ╱
              │          ╱
              │        ╱
            0 │──────•─────────────────
              │      0
             -∞

Properties:
  ReLU(x < 0) = 0
  ReLU(x ≥ 0) = x
  ReLU'(x < 0) = 0
  ReLU'(x > 0) = 1

Advantages:
  ✓ Simple and fast (just max operation)
  ✓ No vanishing gradient for positive values
  ✓ Sparse activation (many zeros → efficiency)
  ✓ Biologically plausible

Problems:
  ✗ "Dead neurons": If always x < 0, neuron dies
     Gradient = 0, never updates!
  ✗ Not zero-centered

THE dominant activation for CNNs and some transformers!
```

---

## 11.1.5 Leaky ReLU and PReLU

```
LEAKY ReLU:
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  LeakyReLU(x) = max(αx, x)  where α = 0.01 typically     │
│                                                           │
└───────────────────────────────────────────────────────────┘

Shape:
              │              ╱
              │            ╱
              │          ╱
        ╱     │        ╱
    ──────────│──────•─────────────────
    (slope α) │      0

For x < 0: Small slope α instead of 0
Prevents dead neurons!

PReLU (Parametric ReLU):
  α is LEARNED parameter, not fixed!
  Network decides best negative slope.
```

---

## 11.1.6 GELU (Gaussian Error Linear Unit) ⭐⭐⭐

```
THE activation function for Transformers!

┌───────────────────────────────────────────────────────────┐
│                                                           │
│  GELU(x) = x × Φ(x)                                      │
│                                                           │
│  where Φ(x) = CDF of standard normal distribution        │
│             = P(X ≤ x) for X ~ N(0, 1)                   │
│                                                           │
└───────────────────────────────────────────────────────────┘

Approximation (commonly used):
  GELU(x) ≈ 0.5x × (1 + tanh(√(2/π) × (x + 0.044715x³)))

Or simpler:
  GELU(x) ≈ x × σ(1.702x)

Shape:
              │              ╱
              │            ╱
              │         ╱
              │       ╱
    ─────╲____│_____╱──────────────────
              │    0

Key insight:
  - Smooth version of ReLU
  - Small negative values allowed
  - Probabilistic interpretation:
    "Multiply x by probability that x is greater than random normal"

Why it works:
  - Smooth everywhere (good for optimization)
  - Non-zero gradient for negative inputs
  - Empirically best for transformers

Used in: BERT, GPT, most modern transformers!
```

---

## 11.1.7 Swish / SiLU

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  Swish(x) = x × σ(x) = x × (1 / (1 + e^(-x)))           │
│                                                           │
└───────────────────────────────────────────────────────────┘

Shape: Similar to GELU
  - Smooth
  - Self-gated (x gates itself!)
  - Small negative values allowed

Found by neural architecture search (Google)!
Computer discovered this works well.

SiLU = Swish with β=1 (Sigmoid Linear Unit)

Used in: EfficientNet, some transformer variants
```

---

## 11.1.8 Activation Comparison

```
┌──────────────────────────────────────────────────────────────────┐
│ Function │ Formula          │ Output Range │ Transformer Use    │
├──────────────────────────────────────────────────────────────────┤
│ Sigmoid  │ 1/(1+e^-x)       │ (0, 1)       │ Gates, not hidden  │
│ Tanh     │ (e^x-e^-x)/(e^x+e^-x) │ (-1, 1) │ Some attention    │
│ ReLU     │ max(0, x)        │ [0, ∞)       │ Some FFN layers    │
│ GELU ⭐   │ x × Φ(x)         │ (-∞, ∞)      │ BERT, GPT (main!)  │
│ Swish    │ x × σ(x)         │ (-∞, ∞)      │ Some variants      │
│ Softmax  │ exp(x)/Σexp      │ (0, 1)       │ Attention, output  │
└──────────────────────────────────────────────────────────────────┘

Transformer FFN typically uses:
  FFN(x) = GELU(xW₁ + b₁)W₂ + b₂

Or "GLU" variants:
  FFN(x) = (xW₁ ⊙ σ(xV))W₂  (gated linear unit)
```

---

# 11.2 Normalization

---

## 11.2.1 Why Normalize?

```
Problem: Internal covariate shift
  - Layer outputs change distribution during training
  - Later layers constantly adapting to shifting inputs
  - Training becomes unstable and slow

Solution: Normalize activations!
  - Fixed mean and variance
  - Stable inputs to each layer
  - Faster, more stable training
```

---

## 11.2.2 Batch Normalization

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  BN(x) = γ × (x - μ_batch) / √(σ²_batch + ε) + β        │
│                                                           │
└───────────────────────────────────────────────────────────┘

Steps:
  1. Compute mean over BATCH: μ = (1/B) Σᵢ xᵢ
  2. Compute variance over BATCH: σ² = (1/B) Σᵢ (xᵢ - μ)²
  3. Normalize: x̂ = (x - μ) / √(σ² + ε)
  4. Scale and shift: y = γx̂ + β

Parameters:
  γ (gamma) = Learnable scale
  β (beta) = Learnable shift
  ε = Small constant for numerical stability (1e-5)

Why γ and β?
  - Network can learn to undo normalization if needed!
  - γ=σ, β=μ would restore original

Problem for transformers:
  - Needs batch dimension
  - Sequence length varies
  - NOT used in modern transformers!
```

---

## 11.2.3 Layer Normalization ⭐⭐⭐

```
THE normalization for Transformers!

┌───────────────────────────────────────────────────────────┐
│                                                           │
│  LN(x) = γ × (x - μ_layer) / √(σ²_layer + ε) + β        │
│                                                           │
└───────────────────────────────────────────────────────────┘

Key difference from BatchNorm:
  BatchNorm: Normalize over BATCH dimension
  LayerNorm: Normalize over FEATURE dimension

For input x of shape [batch, seq_len, d_model]:
  LayerNorm normalizes over d_model (last dimension)
  Each position normalized independently!

Step-by-step for one vector x = [x₁, x₂, ..., x_d]:
  1. Mean: μ = (1/d) Σᵢ xᵢ
  2. Variance: σ² = (1/d) Σᵢ (xᵢ - μ)²
  3. Normalize: x̂ = (x - μ) / √(σ² + ε)
  4. Scale/shift: y = γ ⊙ x̂ + β

γ, β are vectors of size d_model (element-wise)
```

---

## 11.2.4 Layer Norm Example

```
Input: x = [4, 8, 6, 2]  (d_model = 4)

Step 1: Mean
  μ = (4 + 8 + 6 + 2) / 4 = 20 / 4 = 5

Step 2: Variance
  σ² = ((4-5)² + (8-5)² + (6-5)² + (2-5)²) / 4
     = (1 + 9 + 1 + 9) / 4
     = 20 / 4 = 5

Step 3: Normalize (ε = 0 for simplicity)
  x̂ = (x - 5) / √5
     = [-1/√5, 3/√5, 1/√5, -3/√5]
     = [-0.447, 1.342, 0.447, -1.342]

Step 4: Scale and shift (assume γ=1, β=0)
  y = x̂ = [-0.447, 1.342, 0.447, -1.342]

Check: mean(y) ≈ 0, std(y) ≈ 1 ✓
```

---

## 11.2.5 Pre-LN vs Post-LN

```
Original Transformer (Post-LN):
  x → Attention → Add x → LayerNorm → FFN → Add → LayerNorm
       └────────────────────────────────┘

  x = LayerNorm(x + Attention(x))
  x = LayerNorm(x + FFN(x))

Pre-LN (More common now):
  x → LayerNorm → Attention → Add x → LayerNorm → FFN → Add x
      └────────────────────────────────────────────────┘

  x = x + Attention(LayerNorm(x))
  x = x + FFN(LayerNorm(x))

Why Pre-LN is better:
  - More stable gradients
  - Easier to train deep networks
  - No learning rate warmup needed

GPT-2, GPT-3 use Pre-LN!
```

---

## 11.2.6 RMSNorm (Root Mean Square Normalization)

```
Simpler than LayerNorm - skip the mean!

┌───────────────────────────────────────────────────────────┐
│                                                           │
│  RMSNorm(x) = x / √((1/d) Σᵢ xᵢ²) × γ                   │
│                                                           │
│             = x / RMS(x) × γ                             │
│                                                           │
└───────────────────────────────────────────────────────────┘

No mean subtraction!
  - Simpler computation
  - Fewer parameters (no β needed)
  - Works just as well empirically!

Used in: LLaMA, some efficient transformers

RMS = Root Mean Square = √(mean of squares)

Example:
  x = [3, 4]
  RMS = √((9 + 16)/2) = √12.5 = 3.54
  RMSNorm(x) = [3/3.54, 4/3.54] = [0.85, 1.13]
```

---

# 11.3 Softmax (Deep Dive)

---

## 11.3.1 Softmax Review

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  softmax(z)ᵢ = exp(zᵢ) / Σⱼ exp(zⱼ)                     │
│                                                           │
└───────────────────────────────────────────────────────────┘

Converts any vector to valid probability distribution:
  - All outputs > 0
  - All outputs sum to 1
  - Preserves order (larger input → larger output)
```

---

## 11.3.2 Softmax in Attention

```
Attention formula:
  Attention(Q, K, V) = softmax(QKᵀ / √d_k) × V

Why softmax in attention?

1. Creates probability distribution over keys
   "How much attention to pay to each position?"

2. All attention weights positive
   No negative influence

3. Weights sum to 1
   Output is weighted average of values

4. Differentiable
   Gradients flow through

Numerical stability:
  QKᵀ can have large values
  exp(large) = overflow!

  Solution: Subtract max before softmax
  softmax(z) = softmax(z - max(z))
```

---

## 11.3.3 Softmax Temperature

```
softmax(z/T) where T = temperature

T = 1: Normal softmax
T < 1: Sharper (more confident)
T > 1: Smoother (more uniform)
T → 0: argmax (one-hot)
T → ∞: uniform distribution

Example: z = [2, 1, 0]

T = 1:
  exp([2, 1, 0]) = [7.39, 2.72, 1]
  probs = [0.67, 0.24, 0.09]

T = 0.5 (sharp):
  exp([4, 2, 0]) = [54.6, 7.39, 1]
  probs = [0.87, 0.12, 0.02]

T = 2 (smooth):
  exp([1, 0.5, 0]) = [2.72, 1.65, 1]
  probs = [0.50, 0.31, 0.19]

In attention: √d_k acts as temperature!
  Higher d_k → Cooler temperature → Sharper attention
```

---

## 11.3.4 Softmax Gradient

```
Derivative of softmax:

∂softmax(z)ᵢ / ∂zⱼ = softmax(z)ᵢ × (δᵢⱼ - softmax(z)ⱼ)

Where δᵢⱼ = 1 if i=j, else 0 (Kronecker delta)

For i = j:
  ∂pᵢ/∂zᵢ = pᵢ(1 - pᵢ)

For i ≠ j:
  ∂pᵢ/∂zⱼ = -pᵢpⱼ

In matrix form (Jacobian):
  J = diag(p) - ppᵀ

This is used in backpropagation through attention!
```

---

# 11.4 Positional Encoding

---

## 11.4.1 Why Position Matters

```
Problem: Transformer is permutation invariant!

Self-attention treats all positions equally:
  "cat sat mat" → same attention as "mat sat cat"!

Attention only looks at content, not position.

But position matters!
  "The cat ate the mouse" ≠ "The mouse ate the cat"

Solution: Add position information to embeddings!
```

---

## 11.4.2 Sinusoidal Positional Encoding

```
Original Transformer uses sine/cosine functions:

┌───────────────────────────────────────────────────────────┐
│                                                           │
│  PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))          │
│  PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))          │
│                                                           │
└───────────────────────────────────────────────────────────┘

pos = position in sequence (0, 1, 2, ...)
i = dimension index (0, 1, 2, ..., d_model/2)
d_model = embedding dimension

Even indices: sine
Odd indices: cosine
```

---

## 11.4.3 Sinusoidal Encoding Example

```
Let d_model = 4, pos = 0, 1, 2

PE for position 0:
  PE(0, 0) = sin(0 / 10000^0) = sin(0) = 0
  PE(0, 1) = cos(0 / 10000^0) = cos(0) = 1
  PE(0, 2) = sin(0 / 10000^0.5) = sin(0) = 0
  PE(0, 3) = cos(0 / 10000^0.5) = cos(0) = 1
  PE(0) = [0, 1, 0, 1]

PE for position 1:
  PE(1, 0) = sin(1 / 1) = sin(1) = 0.84
  PE(1, 1) = cos(1 / 1) = cos(1) = 0.54
  PE(1, 2) = sin(1 / 100) = sin(0.01) = 0.01
  PE(1, 3) = cos(1 / 100) = cos(0.01) = 1.00
  PE(1) = [0.84, 0.54, 0.01, 1.00]

PE for position 2:
  PE(2, 0) = sin(2) = 0.91
  PE(2, 1) = cos(2) = -0.42
  PE(2, 2) = sin(0.02) = 0.02
  PE(2, 3) = cos(0.02) = 1.00
  PE(2) = [0.91, -0.42, 0.02, 1.00]
```

---

## 11.4.4 Why Sinusoidal Works

```
Key property: Relative position can be computed!

PE(pos + k) can be written as linear transform of PE(pos)

For any fixed offset k:
  PE(pos + k) = T_k × PE(pos)

Where T_k is a rotation matrix!

This lets attention learn:
  "Word 3 positions before current word"
  Without knowing absolute position!

Also:
  - Generalizes to longer sequences than training
  - No extra parameters to learn
  - Smooth: Nearby positions have similar encodings
```

---

## 11.4.5 Learned Positional Embeddings

```
Alternative: LEARN position embeddings!

Create embedding matrix: PE ∈ ℝ^(max_len × d_model)

Each position has learnable embedding:
  PE[0] = [learnable vector for position 0]
  PE[1] = [learnable vector for position 1]
  ...

Pros:
  + More expressive
  + Can learn task-specific patterns
  + Works well in practice

Cons:
  - Fixed maximum length
  - Doesn't generalize to unseen lengths
  - More parameters

BERT uses learned positional embeddings!
GPT uses learned embeddings too!
```

---

## 11.4.6 Rotary Position Embedding (RoPE)

```
Modern alternative: Rotate embeddings!

┌───────────────────────────────────────────────────────────┐
│                                                           │
│  f(x, m) = Rₘ × x                                        │
│                                                           │
│  Where Rₘ is rotation matrix for position m              │
│                                                           │
└───────────────────────────────────────────────────────────┘

Key insight:
  qᵀk in attention becomes:
  (Rₘq)ᵀ(Rₙk) = qᵀRₘ⁻¹Rₙk = qᵀRₙ₋ₘk

Only depends on RELATIVE position (n-m)!

Advantages:
  - Encodes relative position naturally
  - Works with linear attention
  - Better length generalization
  - Used in LLaMA, GPT-NeoX

Mathematical beauty!
```

---

# 11.5 Other Important Functions

---

## 11.5.1 Dropout

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  Dropout(x, p) = mask × x / (1 - p)                      │
│                                                           │
│  mask ~ Bernoulli(1 - p)                                 │
│                                                           │
└───────────────────────────────────────────────────────────┘

During training:
  - Random elements set to 0 with probability p
  - Remaining elements scaled by 1/(1-p)

During inference:
  - No dropout (use all neurons)
  - No scaling needed

Why it works:
  - Prevents co-adaptation
  - Acts like ensemble of networks
  - Regularization

Transformer dropout locations:
  - After attention
  - After FFN
  - On embeddings
  - Typical p = 0.1
```

---

## 11.5.2 Linear (Fully Connected)

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  Linear(x) = xW + b                                      │
│                                                           │
│  x: [batch, seq_len, d_in]                               │
│  W: [d_in, d_out]                                        │
│  b: [d_out]                                              │
│                                                           │
└───────────────────────────────────────────────────────────┘

The fundamental building block!

Used for:
  - Query, Key, Value projections: d_model → d_k/d_v
  - Output projection: d_v → d_model
  - FFN layers: d_model → d_ff → d_model
  - Final vocabulary projection: d_model → vocab_size
```

---

## 11.5.3 Embedding

```
┌───────────────────────────────────────────────────────────┐
│                                                           │
│  Embedding(token_id) = E[token_id, :]                    │
│                                                           │
│  E: [vocab_size, d_model]                                │
│                                                           │
└───────────────────────────────────────────────────────────┘

Lookup table!
  Input: Integer token ID
  Output: Vector of dimension d_model

Example:
  vocab_size = 50000
  d_model = 768

  E = matrix of shape [50000, 768]

  token_id = 42 → E[42, :] = 768-dim vector

Same matrix often used for:
  1. Input embedding (token → vector)
  2. Output projection (vector → logits over vocab)
     This is called "weight tying"
```

---

# PART 11: SUMMARY

```
Special Functions in Transformers:
┌────────────────────────────────────────────────────────────────────────┐
│ Function           │ Use in Transformers                               │
├────────────────────────────────────────────────────────────────────────┤
│ GELU ⭐             │ Activation in FFN layers                         │
│ ReLU               │ Some FFN variants                                 │
│ Softmax            │ Attention weights, output probabilities          │
│ LayerNorm ⭐        │ Normalize at each sublayer                       │
│ RMSNorm            │ Efficient alternative to LayerNorm               │
│ Sinusoidal PE      │ Position information (original)                  │
│ Learned PE         │ Position information (BERT, GPT)                 │
│ RoPE               │ Rotary position (LLaMA)                          │
│ Dropout            │ Regularization                                    │
│ Linear             │ Projections (Q, K, V, FFN)                       │
│ Embedding          │ Token to vector lookup                           │
└────────────────────────────────────────────────────────────────────────┘
```

---

# PART 11: KEY FORMULAS

```
1. GELU:        GELU(x) = x × Φ(x) ≈ 0.5x(1 + tanh(√(2/π)(x + 0.044715x³)))

2. ReLU:        ReLU(x) = max(0, x)

3. Softmax:     softmax(z)ᵢ = exp(zᵢ) / Σexp(zⱼ)

4. LayerNorm:   LN(x) = γ(x - μ)/√(σ² + ε) + β

5. RMSNorm:     RMSNorm(x) = x / √(mean(x²)) × γ

6. Sin PE:      PE(pos, 2i) = sin(pos / 10000^(2i/d))
                PE(pos, 2i+1) = cos(pos / 10000^(2i/d))

7. Dropout:     Dropout(x) = mask × x / (1-p)

8. Linear:      Linear(x) = xW + b
```

---

# PART 11: PRACTICE PROBLEMS

```
Q1. ReLU([-2, 0, 3, -1, 5])?
    Answer: [0, 0, 3, 0, 5]

Q2. Why is GELU preferred over ReLU in transformers?
    Answer: GELU is smooth (differentiable everywhere),
    has small negative values (not dead neurons),
    and empirically works better for attention-based models.

Q3. LayerNorm of [2, 4, 4, 2] with γ=1, β=0?
    Answer: μ = 3, σ² = ((−1)² + 1² + 1² + (−1)²)/4 = 1
    LN = [−1, 1, 1, −1]

Q4. Why use √d_k in attention softmax?
    Answer: Controls variance of dot products.
    Prevents softmax from becoming too sharp (gradient vanishing).

Q5. Softmax([1, 2, 3]) approximately?
    Answer: exp([1,2,3]) = [2.72, 7.39, 20.09]
    sum = 30.2
    probs ≈ [0.09, 0.24, 0.67]

Q6. Why doesn't transformer use BatchNorm?
    Answer: BatchNorm normalizes over batch dimension,
    problematic with variable sequence lengths and
    doesn't work well at inference with batch_size=1.

Q7. What's the advantage of Pre-LN over Post-LN?
    Answer: More stable gradients, easier to train deep models,
    less need for learning rate warmup.

Q8. If d_model = 512, how many parameters in one LayerNorm?
    Answer: γ and β each have 512 parameters.
    Total = 512 + 512 = 1024 parameters.
```

---

*End of Part 11*
*Next: Part 12 - Putting It All Together*

---

# ═══════════════════════════════════════════════════════════════════════════════
# PART 12: PUTTING IT ALL TOGETHER
# ═══════════════════════════════════════════════════════════════════════════════

```
┌─────────────────────────────────────────────────────────────────┐
│             PART 12: COMPLETE TRANSFORMER                       │
│             "सब कुछ एक साथ"                                      │
│                                                                 │
│  Now you understand EVERY piece of math in transformers!       │
│  Let's see how they all work together! 🚀                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Congratulations!

```
You have learned:

Part 1:  Numbers & Basic Operations    ✓
Part 2:  Algebra Basics               ✓
Part 3:  Vectors                      ✓
Part 4:  Matrices                     ✓
Part 5:  Matrix Decomposition         ✓
Part 6:  Calculus - Derivatives       ✓
Part 7:  Calculus - Optimization      ✓
Part 8:  Probability Basics           ✓
Part 9:  Probability Distributions    ✓
Part 10: Information Theory           ✓
Part 11: Special Functions            ✓

Now let's see the COMPLETE picture!
```

---

# 12.1 The Complete Transformer Architecture

---

## 12.1.1 High-Level View

```
┌─────────────────────────────────────────────────────────────────┐
│                     TRANSFORMER                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Input: "The cat sat"                                          │
│           ↓                                                    │
│  ┌─────────────────┐                                           │
│  │ Token Embedding │  Part 3: Vectors                          │
│  │ + Position Enc  │  Part 11: Positional Encoding             │
│  └────────┬────────┘                                           │
│           ↓                                                    │
│  ┌─────────────────┐                                           │
│  │  Transformer    │  × N layers                               │
│  │    Block        │                                           │
│  │  ┌───────────┐  │                                           │
│  │  │ Attention │  │  Part 4: Matrix multiply                  │
│  │  │ + Add&Norm│  │  Part 11: Softmax, LayerNorm             │
│  │  ├───────────┤  │                                           │
│  │  │    FFN    │  │  Part 11: GELU                           │
│  │  │ + Add&Norm│  │  Part 11: LayerNorm                      │
│  │  └───────────┘  │                                           │
│  └────────┬────────┘                                           │
│           ↓                                                    │
│  ┌─────────────────┐                                           │
│  │ Output Linear  │  Part 4: Matrix multiply                   │
│  │ + Softmax      │  Part 11: Softmax                         │
│  └────────┬────────┘                                           │
│           ↓                                                    │
│  Output: Probabilities over vocabulary                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 12.1.2 Math Components Map

```
EVERY MATH CONCEPT maps to a transformer component:

┌────────────────────────────────────────────────────────────────────┐
│ Math Concept         │ Transformer Component                       │
├────────────────────────────────────────────────────────────────────┤
│ Vectors              │ Embeddings, hidden states                   │
│ Matrices             │ Weight matrices (Q, K, V, FFN)              │
│ Matrix multiply      │ Attention, projections                      │
│ Dot product          │ Attention scores (Q·K)                      │
│ Transpose            │ Kᵀ in attention                             │
│ Softmax              │ Attention weights, output probs             │
│ GELU/ReLU            │ FFN activation                              │
│ LayerNorm            │ After attention, after FFN                  │
│ Residual connection  │ x + Attention(x)                            │
│ Embeddings           │ Token lookup, position lookup               │
│ Chain rule           │ Backpropagation                             │
│ Gradient descent     │ Training (Adam optimizer)                   │
│ Cross-entropy        │ Loss function                               │
│ Probability          │ Output distribution                         │
│ Categorical dist.    │ Next word prediction                        │
└────────────────────────────────────────────────────────────────────┘
```

---

# 12.2 Step-by-Step Forward Pass

---

## 12.2.1 Input Processing

```
Input sentence: "The cat sat"

Step 1: TOKENIZATION (not math, but important)
  "The cat sat" → [464, 3797, 3332]  (token IDs)

Step 2: TOKEN EMBEDDING (Part 3, 11)
  Each token ID → d_model dimensional vector

  E = Embedding matrix [vocab_size × d_model]

  token_464 → E[464, :] = [0.12, -0.34, 0.56, ...] (768 dims)
  token_3797 → E[3797, :] = [0.78, 0.23, -0.11, ...]
  token_3332 → E[3332, :] = [-0.45, 0.67, 0.89, ...]

  Result: X_emb = [3 × 768] matrix

Step 3: POSITIONAL ENCODING (Part 11)
  Add position information:

  PE = [PE(0), PE(1), PE(2)]  (3 × 768)

  X = X_emb + PE

  Each token now knows its position!
```

---

## 12.2.2 Self-Attention Layer

```
Input: X [seq_len × d_model] = [3 × 768]

Step 4: CREATE Q, K, V (Part 4)
  Q = X × W_Q    [3×768] × [768×64] = [3×64]
  K = X × W_K    [3×768] × [768×64] = [3×64]
  V = X × W_V    [3×768] × [768×64] = [3×64]

Step 5: ATTENTION SCORES (Part 4 - Dot product)
  scores = Q × Kᵀ    [3×64] × [64×3] = [3×3]

  scores = ┌                    ┐
           │ q₁·k₁  q₁·k₂  q₁·k₃│  "The" attends to all
           │ q₂·k₁  q₂·k₂  q₂·k₃│  "cat" attends to all
           │ q₃·k₁  q₃·k₂  q₃·k₃│  "sat" attends to all
           └                    ┘

Step 6: SCALE (Part 7, 8 - Variance control)
  scaled_scores = scores / √d_k = scores / √64 = scores / 8

Step 7: SOFTMAX (Part 11)
  attention_weights = softmax(scaled_scores, axis=-1)

  Each row sums to 1!

  weights = ┌                      ┐
            │ 0.8   0.1   0.1     │  "The" mostly self-attends
            │ 0.2   0.5   0.3     │  "cat" attends to self & context
            │ 0.1   0.3   0.6     │  "sat" attends to self & context
            └                      ┘

Step 8: WEIGHTED SUM (Part 4)
  output = attention_weights × V    [3×3] × [3×64] = [3×64]

  Each position gets weighted combination of all values!
```

---

## 12.2.3 Multi-Head Attention

```
Run attention h times in parallel (h=12 typically):

  head_1 = Attention(XW_Q1, XW_K1, XW_V1)  [3×64]
  head_2 = Attention(XW_Q2, XW_K2, XW_V2)  [3×64]
  ...
  head_12 = Attention(XW_Q12, XW_K12, XW_V12)  [3×64]

Concatenate all heads:
  multi_head = [head_1; head_2; ...; head_12]  [3×768]

Project back:
  output = multi_head × W_O    [3×768] × [768×768] = [3×768]

Different heads learn different patterns:
  - Some attend to nearby words
  - Some attend to specific syntax
  - Some attend to semantics
```

---

## 12.2.4 Residual + LayerNorm

```
Step 9: RESIDUAL CONNECTION (Part 6 - Gradient flow)
  X = X + Attention(X)

  Why? Gradients flow directly through!
  Prevents vanishing gradient in deep networks.

Step 10: LAYER NORMALIZATION (Part 11)
  X = LayerNorm(X)

  For each position vector x:
    μ = mean(x)
    σ = std(x)
    x_norm = (x - μ) / σ
    x_out = γ × x_norm + β

  Stabilizes training!
```

---

## 12.2.5 Feedforward Network

```
Step 11: FFN - Expand (Part 4)
  hidden = X × W_1 + b_1    [3×768] × [768×3072] = [3×3072]

  Dimension increases 4×!

Step 12: ACTIVATION (Part 11)
  hidden = GELU(hidden)

  Non-linearity! Network can learn complex functions.

Step 13: FFN - Contract (Part 4)
  output = hidden × W_2 + b_2    [3×3072] × [3072×768] = [3×768]

  Back to original dimension.

Step 14: RESIDUAL + LAYER NORM
  X = LayerNorm(X + output)
```

---

## 12.2.6 Repeat for N Layers

```
┌──────────────────────────────────────────┐
│                                          │
│  for layer in range(N):  # N = 12 or 24 │
│      X = Attention_Block(X)              │
│      X = FFN_Block(X)                    │
│                                          │
└──────────────────────────────────────────┘

Each layer refines the representations!
  Layer 1: Basic patterns
  Layer 6: Syntactic structure
  Layer 12: Deep semantic understanding
```

---

## 12.2.7 Output Layer

```
Step 15: FINAL PROJECTION (Part 4)
  logits = X × W_vocab    [3×768] × [768×50000] = [3×50000]

  Each position gets score for each vocabulary word!

Step 16: SOFTMAX TO PROBABILITIES (Part 8, 9, 11)
  probs = softmax(logits, axis=-1)    [3×50000]

  For position 3 (after "sat"):
    P("on") = 0.15
    P("down") = 0.12
    P("there") = 0.08
    P("the") = 0.05
    ...

Step 17: SAMPLE OR ARGMAX
  next_token = sample(probs[2]) or argmax(probs[2])

  Output: "on" (or whatever is sampled)
```

---

# 12.3 Training: Backward Pass

---

## 12.3.1 Loss Computation

```
Training example:
  Input: "The cat sat"
  Target: "cat sat on"  (shifted by 1)

For each position:
  predicted_probs = softmax(logits)
  target_token = actual next word

CROSS-ENTROPY LOSS (Part 10):
  Loss = -Σ log(P(correct_token))

  Position 1: target="cat", P("cat")=0.8 → -log(0.8) = 0.22
  Position 2: target="sat", P("sat")=0.6 → -log(0.6) = 0.51
  Position 3: target="on", P("on")=0.15 → -log(0.15) = 1.90

  Total Loss = (0.22 + 0.51 + 1.90) / 3 = 0.88
```

---

## 12.3.2 Backpropagation

```
Compute gradients using CHAIN RULE (Part 6):

∂Loss/∂W_vocab = ∂Loss/∂logits × ∂logits/∂W_vocab

∂Loss/∂W_2 = ∂Loss/∂output × ∂output/∂hidden × ∂hidden/∂W_2

...through every layer...

∂Loss/∂W_Q = ∂Loss/∂attn × ∂attn/∂scores × ∂scores/∂Q × ∂Q/∂W_Q

Every matrix has a gradient!
  ∇W_Q, ∇W_K, ∇W_V, ∇W_O
  ∇W_1, ∇W_2
  ∇W_embed
  ∇γ, ∇β (LayerNorm)
```

---

## 12.3.3 Parameter Update

```
ADAM OPTIMIZER (Part 7):

For each parameter W:
  m = β₁ × m + (1-β₁) × ∇W         # Momentum
  v = β₂ × v + (1-β₂) × (∇W)²      # RMSprop

  m̂ = m / (1 - β₁ᵗ)                # Bias correction
  v̂ = v / (1 - β₂ᵗ)

  W = W - η × m̂ / (√v̂ + ε)         # Update

Repeat for millions of batches!
```

---

# 12.4 Parameter Count

---

## 12.4.1 Counting Parameters

```
Let's count for BERT-base:
  d_model = 768
  d_ff = 3072
  h = 12 (heads)
  d_k = d_v = 64
  N = 12 (layers)
  vocab_size = 30522

EMBEDDING:
  Token: vocab × d_model = 30522 × 768 = 23.4M
  Position: max_len × d_model = 512 × 768 = 0.4M
  Segment: 2 × 768 = 1.5K

PER TRANSFORMER LAYER:
  Attention:
    W_Q: d × d = 768 × 768 = 0.59M
    W_K: d × d = 768 × 768 = 0.59M
    W_V: d × d = 768 × 768 = 0.59M
    W_O: d × d = 768 × 768 = 0.59M
    Total attention: 2.36M

  FFN:
    W_1: d × 4d = 768 × 3072 = 2.36M
    W_2: 4d × d = 3072 × 768 = 2.36M
    Total FFN: 4.72M

  LayerNorm (×2):
    γ, β: 2 × 768 × 2 = 3K

  Per layer total: ~7.1M

ALL LAYERS:
  12 × 7.1M = 85.2M

OUTPUT:
  Often tied with embedding = 0 extra

TOTAL: ~23.4M + 0.4M + 85.2M ≈ 109M parameters

That's BERT-base: 110 million parameters!
```

---

## 12.4.2 Model Sizes

```
┌────────────────────────────────────────────────────────────┐
│ Model          │ Parameters  │ Layers │ d_model │ Heads   │
├────────────────────────────────────────────────────────────┤
│ BERT-base      │ 110M        │ 12     │ 768     │ 12      │
│ BERT-large     │ 340M        │ 24     │ 1024    │ 16      │
│ GPT-2          │ 1.5B        │ 48     │ 1600    │ 25      │
│ GPT-3          │ 175B        │ 96     │ 12288   │ 96      │
│ GPT-4          │ ~1.7T       │ ?      │ ?       │ ?       │
│ LLaMA-7B       │ 7B          │ 32     │ 4096    │ 32      │
│ LLaMA-70B      │ 70B         │ 80     │ 8192    │ 64      │
└────────────────────────────────────────────────────────────┘

Scaling laws: Bigger usually = Better!
```

---

# 12.5 The Complete Math Journey

---

## 12.5.1 Math in Order of Appearance

```
When you read "Hello" to a transformer:

1. "Hello" → token_id = 31373
   └── Just lookup (Part 1: numbers)

2. token_id → embedding vector [768 dims]
   └── Matrix row lookup (Part 4)

3. Add positional encoding
   └── sin/cos functions (Part 11)
   └── Vector addition (Part 3)

4. Create Q, K, V
   └── Matrix multiplication (Part 4)

5. Compute attention scores Q·Kᵀ
   └── Dot product (Part 3)
   └── Matrix multiplication (Part 4)

6. Scale by √d_k
   └── Division, square root (Part 1)
   └── Variance control (Part 8)

7. Apply softmax
   └── Exponential function (Part 2)
   └── Probability distribution (Part 8)

8. Weighted sum with V
   └── Matrix multiplication (Part 4)

9. Project output
   └── Matrix multiplication (Part 4)

10. Add residual
    └── Vector addition (Part 3)

11. Layer normalize
    └── Mean, variance (Part 8)
    └── Division, subtraction (Part 1)

12. FFN forward
    └── Matrix multiply (Part 4)
    └── GELU activation (Part 11)

13. Add residual, normalize again

14. Repeat 12× (or more)

15. Final projection to vocabulary
    └── Matrix multiplication (Part 4)

16. Softmax for probabilities
    └── Probability distribution (Part 9)

17. Cross-entropy loss
    └── Log function (Part 2)
    └── Information theory (Part 10)

18. Backpropagation
    └── Chain rule (Part 6)
    └── Partial derivatives (Part 6)

19. Parameter update
    └── Gradient descent (Part 7)
    └── Adam optimizer (Part 7)
```

---

## 12.5.2 One Equation Summary

```
The entire forward pass can be written as:

P(next_word) = softmax(
    LayerNorm(
        Repeat_N(
            FFN(LayerNorm(
                x + MultiHeadAttention(LayerNorm(x))
            ))
        )
    ) × W_vocab
)

Where:
  MultiHeadAttention(x) = Concat(head₁, ..., head_h) × W_O
  head_i = softmax(xW_Qi × (xW_Ki)ᵀ / √d_k) × xW_Vi
  FFN(x) = GELU(xW₁)W₂
```

---

# 12.6 Final Wisdom

---

## 12.6.1 Key Insights

```
1. ATTENTION = Learned weighted average
   - Queries ask, Keys answer, Values provide
   - O(n²) complexity in sequence length

2. FFN = Per-position processing
   - Expand, activate, contract
   - Where knowledge is "stored"

3. RESIDUAL + NORM = Stability
   - Gradients flow
   - Training works at scale

4. EMBEDDINGS = Learned representations
   - Words become vectors
   - Similar meaning → Similar vectors

5. SOFTMAX = Probability
   - Attention weights sum to 1
   - Output is distribution over words

6. CROSS-ENTROPY = Learning signal
   - Minimize surprise
   - Match true distribution
```

---

## 12.6.2 What Makes Transformers Special

```
Before Transformers (RNN/LSTM):
  - Sequential processing
  - Information bottleneck
  - Hard to parallelize
  - Struggle with long sequences

Transformers:
  - Parallel processing
  - Direct connections (attention)
  - Highly parallelizable (GPUs love it!)
  - Constant path length

The magic formula:
  Attention + FFN + Residual + LayerNorm + Scale
  = State-of-the-art on almost everything!
```

---

## 12.6.3 Where to Go From Here

```
You now understand the math!

Next steps:
  1. Implement a transformer from scratch
  2. Read the original "Attention Is All You Need" paper
  3. Experiment with huggingface transformers
  4. Fine-tune models on your tasks
  5. Read about recent advances:
     - Flash Attention (efficient)
     - Mixture of Experts (scale)
     - State Space Models (long sequences)

Resources:
  - "The Illustrated Transformer" (Jay Alammar)
  - "Attention Is All You Need" (Vaswani et al.)
  - Andrej Karpathy's videos
  - This document! 📖
```

---

# 12.7 Complete Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TRANSFORMER MATH CHEAT SHEET                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ATTENTION:                                                         │
│    Attention(Q,K,V) = softmax(QKᵀ/√d_k)V                           │
│                                                                     │
│  MULTI-HEAD:                                                        │
│    MultiHead = Concat(head₁,...,head_h)W_O                         │
│    head_i = Attention(XW_Qi, XW_Ki, XW_Vi)                         │
│                                                                     │
│  FFN:                                                               │
│    FFN(x) = GELU(xW₁ + b₁)W₂ + b₂                                  │
│                                                                     │
│  LAYER NORM:                                                        │
│    LN(x) = γ(x - μ)/σ + β                                          │
│                                                                     │
│  TRANSFORMER BLOCK:                                                 │
│    x = x + MultiHead(LN(x))                                        │
│    x = x + FFN(LN(x))                                              │
│                                                                     │
│  SOFTMAX:                                                           │
│    softmax(z)ᵢ = exp(zᵢ) / Σexp(zⱼ)                               │
│                                                                     │
│  GELU:                                                              │
│    GELU(x) ≈ 0.5x(1 + tanh(√(2/π)(x + 0.044715x³)))               │
│                                                                     │
│  CROSS-ENTROPY LOSS:                                                │
│    L = -Σ log P(correct_token)                                     │
│                                                                     │
│  ADAM UPDATE:                                                       │
│    m = β₁m + (1-β₁)g                                               │
│    v = β₂v + (1-β₂)g²                                              │
│    θ = θ - η × m̂/(√v̂ + ε)                                         │
│                                                                     │
│  POSITIONAL ENCODING:                                               │
│    PE(pos,2i) = sin(pos/10000^(2i/d))                              │
│    PE(pos,2i+1) = cos(pos/10000^(2i/d))                            │
│                                                                     │
│  PERPLEXITY:                                                        │
│    PPL = exp(cross_entropy)                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

# PART 12: FINAL SUMMARY

```
आपने सीखा:

┌──────────────────────────────────────────────────────────────────────┐
│ Part  │ Topic                    │ Key Takeaway                      │
├──────────────────────────────────────────────────────────────────────┤
│ 1     │ Numbers                  │ Foundation of everything          │
│ 2     │ Algebra                  │ Equations and functions           │
│ 3     │ Vectors                  │ Embeddings are vectors!           │
│ 4     │ Matrices                 │ Transformations, projections      │
│ 5     │ Decomposition            │ PCA, understanding structure      │
│ 6     │ Derivatives              │ Rate of change, gradients         │
│ 7     │ Optimization             │ How training actually works       │
│ 8     │ Probability              │ Uncertainty, predictions          │
│ 9     │ Distributions            │ Softmax = categorical dist.       │
│ 10    │ Information Theory       │ Cross-entropy loss explained      │
│ 11    │ Special Functions        │ GELU, LayerNorm, Softmax         │
│ 12    │ Everything Together      │ Complete transformer math!        │
└──────────────────────────────────────────────────────────────────────┘

अब आप Transformer के हर piece of math को समझते हो!

From "1 + 1 = 2" to "GPT generates text"
You've traveled the complete mathematical journey! 🎉
```

---

# CLOSING THOUGHTS

```
"Mathematics is the language in which God has written the universe."
                                        - Galileo Galilei

Transformers are written in this language.
Now you can read it.

Go build something amazing! 🚀

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    THE END
              Transformer Mathematics Complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

*Document Complete*
*Total: 12 Parts covering all mathematics for Transformers and Deep Learning*

---
