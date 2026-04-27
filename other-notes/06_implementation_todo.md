# Transformer Implementation - TODO Checklist

> Complete roadmap from Basic to Advanced. Check items as you complete them!

---

## HOW TO USE THIS DOCUMENT

```
□ = Not started
◐ = In progress
✓ = Completed
✗ = Skipped (optional items)

Update status as you progress!
```

---

# PHASE 0: PREREQUISITES

## 0.1 Python Basics ✅ DONE
| Status | Task | Notes |
|--------|------|-------|
| ✓ | Lists, Dictionaries mastery | Config patterns, vocab storage |
| ✓ | Functions and Classes (OOP) | nn.Module pattern seekha |
| ✓ | List comprehensions | Batch creation |
| ✓ | File handling | Dataset loading |

### 🚀 Fast-Track Python for Transformers (2 hours total)

> **Pro Strategy:** Learn only what you'll actually use. Read real code + Google what you don't understand = High retention in less time.

#### 1. Lists & Dictionaries (30 mins) ⭐⭐
```python
# Lists - for sequences, batches
tokens = [101, 2054, 2003, 102]
tokens.append(103)
tokens[:5]  # slicing
len(tokens)

# Dictionaries - vocab, configs
vocab = {"hello": 1, "world": 2}
vocab["new"] = 3
vocab.get("unknown", 0)  # default value

# Config pattern (everywhere in ML)
config = {"d_model": 512, "n_heads": 8, "n_layers": 6}
```
**Practice:** Create a word→id vocabulary from a sentence.

#### 2. Functions & Classes (45 mins) ⭐⭐⭐ MOST IMPORTANT
```python
# The ONLY pattern you need - every Transformer component uses this:
class AttentionHead:
    def __init__(self, d_model, d_k):  # constructor
        self.d_k = d_k

    def forward(self, x):  # main logic
        return x

    def __call__(self, x):  # makes object callable
        return self.forward(x)
```
**Practice:** Write a simple `Calculator` class with `add()` and `multiply()` methods.

#### 3. List Comprehensions (15 mins) ⭐
```python
# Instead of loop:
result = [i * 2 for i in range(10)]

# With condition:
even = [i for i in range(10) if i % 2 == 0]

# Nested (for batches):
batch = [[j for j in range(5)] for i in range(3)]
```
**Practice:** Convert a list of words to lowercase in one line.

#### 4. File Handling (15 mins) ⭐
```python
# Reading (datasets)
with open("data.txt", "r") as f:
    lines = f.readlines()

# Writing (logs)
with open("log.txt", "w") as f:
    f.write("epoch 1: loss 0.5")
```
Note: PyTorch handles model saving with `torch.save()`.

#### Time Summary
| Task | Time | Priority |
|------|------|----------|
| Lists, Dicts | 30 min | ⭐⭐ |
| **Classes (OOP)** | 45 min | ⭐⭐⭐ |
| List comprehensions | 15 min | ⭐ |
| File handling | 15 min | ⭐ |

### 🎯 Practice Problems: Functions & Classes

---

#### Level 1: Basic Class ✓ DONE

**Kya banana hai:** Ek simple `Token` class jo word aur uska ID store kare.

```python
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def info(self):
        return f'Token(type={self.type}, value={self.value})'

# Test:
t = Token("word", "hello")
print(t.info())  # Token(type=word, value=hello)
```

**Kya seekha:**
- `class` = ek blueprint/template hai object banane ke liye
- `__init__` = constructor, jab object banta hai tab run hota hai
- `self` = current object ko refer karta hai ("main khud")
- `def` keyword har method ke aage lagana zaroori hai!

---

#### Level 2: Class with Computation ✓ DONE

**Kya banana hai:** Ek `Scaler` class jo number ko multiply kare stored factor se.

```python
class Scaler:
    def __init__(self, factor):
        self.factor = factor

    def scale(self, x):
        return x * self.factor

# Test:
s = Scaler(0.5)
print(s.scale(10))   # 5.0
print(s.scale(100))  # 50.0
```

**Kya seekha:**
- `factor` = temporary variable, sirf `__init__` mein exist karta hai
- `self.factor` = permanent storage, poori class mein kahin bhi access kar sakte ho
- Socho `self` = class ka dimaag, `self.factor` = dimaag mein factor yaad rakh

**Example:**
```python
s1 = Scaler(2)   # s1 ka dimaag: factor = 2
s2 = Scaler(10)  # s2 ka dimaag: factor = 10
s1.scale(5)  # 10 (apna factor 2 use kiya)
s2.scale(5)  # 50 (apna factor 10 use kiya)
```

---

#### Level 3: The __call__ Pattern ✓ DONE

**Kya banana hai:** Ek `Multiplier` class jo object ko function jaisa use karne de.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def forward(self, x):
        return x * self.factor

    def __call__(self, x):
        return self.forward(x)

# Test:
m = Multiplier(3)
print(m(7))   # 21
```

**Kya seekha:**

`__call__` ek magic method hai. Isse object ko directly call kar sakte ho jaise function!

```
m(7)
  ↓ Python internally
m.__call__(7)
  ↓ humne likha hai
self.forward(7)
  ↓ calculation
7 * 3 = 21
```

**Bina `__call__`:**
```python
m.forward(7)  # ✅ kaam karega
m(7)          # ❌ ERROR: object is not callable
```

**`__call__` ke saath:**
```python
m.forward(7)  # ✅ kaam karega
m(7)          # ✅ ye bhi kaam karega! Short aur clean
```

**PyTorch mein yahi hota hai:**
```python
model = Transformer()
output = model(input)  # internally model.forward(input) call hota hai
```

| Method | Kab run hota hai |
|--------|------------------|
| `__init__` | Object banate waqt: `m = Multiplier(3)` |
| `forward` | Jab tum khud call karo: `m.forward(7)` |
| `__call__` | Jab object ko function jaisa call karo: `m(7)` |

---

#### Level 4: Real Transformer Pattern ✓ DONE

**Kya banana hai:** `SimpleAttention` class - Transformer ka actual pattern!

```python
import math

class SimpleAttention:
    def __init__(self, d_model):
        self.d_model = d_model
        self.scale = math.sqrt(d_model)  # √d_model calculate karke store

    def forward(self, x):
        return x / self.scale  # scaling operation

    def __call__(self, x):
        return self.forward(x)

# Test:
attn = SimpleAttention(64)
print(attn(128))  # 16.0 (128 / √64 = 128/8 = 16)
```

**Math samjho:**
```
d_model = 64
scale = √64 = 8
input = 128
output = 128 / 8 = 16.0
```

**Ye scaling kyun zaroori hai?**

Transformer paper mein attention formula hai:
```
Attention = softmax(QK^T / √d_k) × V
                    ↑
            yahi scaling hai!
```

- Bina scaling ke dot products bahut bade ho jaate hain
- Bade numbers → softmax extreme values deta hai (0 ya 1)
- Scaling se numbers controlled rehte hain → softmax stable
- Stable softmax = better learning!

**Ye THE pattern hai:** Transformer ke har component (Attention, FFN, Encoder, Decoder) mein yahi structure milega!

## 0.2 NumPy ✅ DONE
| Status | Task | Notes |
|--------|------|-------|
| ✓ | Array creation (zeros, ones, random) | Weight initialization |
| ✓ | Reshaping (reshape, transpose, squeeze) | Multi-head reshape |
| ✓ | Matrix multiplication (np.matmul, @) | Q @ K, Attention @ V |
| ✓ | Broadcasting rules | Bias addition |
| ✓ | Indexing and slicing | Batch processing |
| ✓ | **Practice:** Multiply two matrices | Done |

### 🚀 Fast-Track NumPy for Transformers (~35 mins total)

**Kyun zaroori hai?**
```
Transformer = Matrix operations ka game
- Q, K, V = matrices
- Attention = matrix multiplication
- All weights = matrices
```
PyTorch internally NumPy jaisa hi kaam karta hai, so NumPy samjho = PyTorch samjho!

---

#### 1. Array Creation (5 mins) ⭐

```python
import numpy as np

# Zeros - initialize weights
zeros = np.zeros((3, 4))        # 3x4 matrix of 0s

# Ones
ones = np.ones((2, 3))          # 2x3 matrix of 1s

# Random - weight initialization
random = np.random.randn(3, 4)  # 3x4 random values (normal distribution)

# Arange - position indices
positions = np.arange(100)       # [0, 1, 2, ..., 99]
```

---

#### 2. Reshaping (10 mins) ⭐⭐⭐ MOST IMPORTANT

```python
x = np.arange(12)   # [0,1,2,3,4,5,6,7,8,9,10,11]

# Reshape - change dimensions
x.reshape(3, 4)     # 3 rows, 4 columns
x.reshape(2, 2, 3)  # 2 batches, 2 rows, 3 cols
x.reshape(-1)       # flatten, -1 = "figure it out"

# Transpose - swap dimensions
x = np.array([[1,2,3], [4,5,6]])  # (2, 3)
x.T                                # (3, 2) - rows↔cols swap

# Squeeze - remove dimension of size 1
x = np.zeros((1, 3, 1))  # shape: (1, 3, 1)
x.squeeze()               # shape: (3,)
```

**Transformer mein:** Multi-head attention mein `(batch, seq, d_model)` → `(batch, heads, seq, d_k)` reshape hota hai!

**Rule:** Total elements same rehne chahiye!
```
(3, 4) = 12 elements
Can reshape to: (12,), (6, 2), (2, 6), (2, 2, 3), (1, 12), etc.
Cannot reshape to: (5, 3) = 15 ❌
```

---

#### 📌 Shape Samjho - Bahut Important!

```python
# (12,) = 1D array - just a line of numbers
a = np.arange(12)         # [ 0  1  2  3 ... 11]

# (12, 1) = 2D - 12 rows, 1 column (COLUMN vector)
b = a.reshape(12, 1)      # [[0], [1], [2], ... [11]]

# (1, 12) = 2D - 1 row, 12 columns (ROW vector)
c = a.reshape(1, 12)      # [[0, 1, 2, 3 ... 11]]
```

**Visual:**
```
(12,)    →  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]   (1D line)

(12, 1)  →  [[0],       (Column - 12 rows, 1 col)
             [1],
             ...
             [11]]

(1, 12)  →  [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]  (Row - 1 row, 12 cols)
```

**Shape Guide:**
| Shape | Dimensions | Meaning |
|-------|------------|---------|
| `(12,)` | 1D | Sirf 12 elements, ek line |
| `(12, 1)` | 2D | 12 rows × 1 col |
| `(1, 12)` | 2D | 1 row × 12 cols |
| `(3, 4)` | 2D | 3 rows × 4 cols |
| `(2, 3, 4)` | 3D | 2 batches × 3 rows × 4 cols |

> **Tip:** Trailing comma `(12,)` indicates tuple with single element = 1D array!

---

#### 3. Matrix Multiplication (10 mins) ⭐⭐⭐

```python
A = np.array([[1, 2], [3, 4]])  # (2, 2)
B = np.array([[5, 6], [7, 8]])  # (2, 2)

# Two ways - same result:
C = np.matmul(A, B)
C = A @ B          # @ operator - cleaner!

# Rule: (m, n) @ (n, p) = (m, p)
# Inner dimensions must match!
```

**Transformer mein:**
```python
# Attention scores
scores = Q @ K.T     # (seq, d_k) @ (d_k, seq) = (seq, seq)

# Attention output
output = scores @ V  # (seq, seq) @ (seq, d_k) = (seq, d_k)
```

---

#### 4. Broadcasting (5 mins) ⭐⭐

```python
# Smaller array automatically expands
A = np.array([[1, 2, 3],
              [4, 5, 6]])     # (2, 3)
b = np.array([10, 20, 30])    # (3,)

A + b  # b becomes [[10,20,30], [10,20,30]] automatically!
# Result: [[11, 22, 33],
#          [14, 25, 36]]
```

**Transformer mein:** Bias add karte waqt broadcasting hota hai.

---

#### 5. Indexing & Slicing (5 mins) ⭐⭐

```python
x = np.arange(12).reshape(3, 4)
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]

x[0]        # First row: [0, 1, 2, 3]
x[:, 0]     # First column: [0, 4, 8]
x[1:3, 2:4] # Slice: [[6, 7], [10, 11]]
x[:, -1]    # Last column: [3, 7, 11]
```

---

#### Time Summary
| Task | Time | Priority |
|------|------|----------|
| Array creation | 5 min | ⭐ |
| **Reshaping** | 10 min | ⭐⭐⭐ |
| **Matrix multiplication** | 10 min | ⭐⭐⭐ |
| Broadcasting | 5 min | ⭐⭐ |
| Indexing | 5 min | ⭐⭐ |

---

### 📊 Complete Array Visualization Guide

#### 1D Array: `(6,)` - Ek Line
```python
x = np.arange(6)  # [0, 1, 2, 3, 4, 5]
```
```
Index:   0   1   2   3   4   5
       ┌───┬───┬───┬───┬───┬───┐
       │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
       └───┴───┴───┴───┴───┴───┘
```

#### 2D Array: `(3, 4)` - Ek Table/Page
```python
x = np.arange(12).reshape(3, 4)
```
```
              col 0   col 1   col 2   col 3
            ┌───────┬───────┬───────┬───────┐
    row 0   │   0   │   1   │   2   │   3   │
            ├───────┼───────┼───────┼───────┤
    row 1   │   4   │   5   │   6   │   7   │
            ├───────┼───────┼───────┼───────┤
    row 2   │   8   │   9   │  10   │  11   │
            └───────┴───────┴───────┴───────┘

x[1, 2] = 6  (row 1, col 2)
```

#### 3D Array: `(2, 3, 4)` - Stack of Pages
```python
x = np.arange(24).reshape(2, 3, 4)
```
```
Page 0:                    Page 1:
┌──┬──┬──┬──┐             ┌──┬──┬──┬──┐
│0 │1 │2 │3 │             │12│13│14│15│
├──┼──┼──┼──┤             ├──┼──┼──┼──┤
│4 │5 │6 │7 │             │16│17│18│19│
├──┼──┼──┼──┤             ├──┼──┼──┼──┤
│8 │9 │10│11│             │20│21│22│23│
└──┴──┴──┴──┘             └──┴──┴──┴──┘

x[0]       = Page 0 (shape: 3, 4)
x[1, 2]    = Page 1, Row 2 = [20, 21, 22, 23]
x[1, 2, 3] = 23
```

#### 4D Array: `(2, 3, 3, 4)` - Books with Pages
```python
x = np.arange(72).reshape(2, 3, 3, 4)
# (2 books, 3 pages each, 3 rows, 4 cols)
```
```
📚 Book 0                    📚 Book 1
├── 📄 Page 0               ├── 📄 Page 0
│   [0-11]                  │   [36-47]
├── 📄 Page 1               ├── 📄 Page 1
│   [12-23]                 │   [48-59]
├── 📄 Page 2               ├── 📄 Page 2
│   [24-35]                 │   [60-71]

x[0]          = Book 0 (shape: 3, 3, 4)
x[0, 1]       = Book 0, Page 1 (shape: 3, 4)
x[0, 1, 2]    = Row = [20, 21, 22, 23]
x[0, 1, 2, 3] = Single number = 23
```

#### Quick Reference:
| Shape | Visualization | Indexing | Transformer Use |
|-------|--------------|----------|-----------------|
| `(6,)` | Line | `x[i]` | - |
| `(3, 4)` | Table | `x[row, col]` | Single sequence |
| `(2, 3, 4)` | Stack of tables | `x[page, row, col]` | (batch, seq, d_model) |
| `(2, 3, 3, 4)` | Books of stacks | `x[book, page, row, col]` | (batch, heads, seq, d_k) |

#### Transformer Shapes याद रखो:
```
(32, 100, 512)     = (batch, seq, d_model)
                      32 sentences, 100 words each, 512-dim vectors

(32, 8, 100, 64)   = (batch, heads, seq, d_k)
                      32 sentences, 8 attention heads, 100 words, 64-dim per head
```

## 0.3 PyTorch Basics ✅ DONE (2026-01-18)
| Status | Task | Notes |
|--------|------|-------|
| ✓ | Tensor creation and operations | NumPy jaisa hi |
| ✓ | torch.nn.Module class | __call__ → forward pattern |
| ✓ | Forward pass concept | Data flow through layers |
| ✓ | Loss functions (MSE) | ((pred - true)²).mean() |
| ✓ | Optimizers (Adam, SGD) | Adam = best, auto weight update |
| ✓ | Backpropagation (loss.backward()) | Gradient calculation |
| ✓ | nn.Parameter | Learnable weights, tracked by PyTorch |
| ✓ | Save/Load model | state_dict(), load_state_dict() |
| ✓ | **Practice:** Linear Regression (y=mx+c) | 1model/ folder complete |

### 🚀 Fast-Track PyTorch for Transformers (~45 mins total)

**Good news:** NumPy seekh liya = 80% PyTorch already done!

```python
# NumPy                    # PyTorch (almost same!)
import numpy as np         import torch

np.array([1,2,3])          torch.tensor([1,2,3])
np.zeros((3,4))            torch.zeros(3,4)
np.random.randn(3,4)       torch.randn(3,4)
x.reshape(2,6)             x.view(2,6)  # or x.reshape(2,6)
x.T                        x.T
A @ B                      A @ B
```

---

#### 1. Tensors = NumPy Arrays with Superpowers (5 mins) ⭐

```python
import torch

# Creation - NumPy jaisa hi!
x = torch.tensor([1, 2, 3])           # from list
x = torch.zeros(3, 4)                  # 3x4 zeros
x = torch.ones(3, 4)                   # 3x4 ones
x = torch.randn(3, 4)                  # random normal
x = torch.arange(12)                   # [0, 1, 2, ..., 11]

# NumPy ↔ PyTorch conversion
numpy_arr = x.numpy()                  # tensor → numpy
tensor = torch.from_numpy(numpy_arr)   # numpy → tensor

# Shape operations - same!
x.shape                                # shape dekho
x.view(4, 3)                          # reshape (PyTorch style)
x.reshape(4, 3)                        # reshape (also works)
x.T                                    # transpose
```

---

#### 2. nn.Module - THE Pattern (10 mins) ⭐⭐⭐ MOST IMPORTANT

```python
import torch.nn as nn

# Har PyTorch model aise banta hai:
class MyModel(nn.Module):           # nn.Module inherit karo
    def __init__(self):
        super().__init__()          # parent ko call karo (ZAROORI!)
        self.linear = nn.Linear(512, 256)

    def forward(self, x):           # forward pass
        return self.linear(x)

# Use:
model = MyModel()
output = model(input)   # internally model.forward(input) call hota hai
```

**Yaad hai Level 3 ka `__call__` pattern?** nn.Module already `__call__` provide karta hai!

**Flow:**
```
model(x) → nn.Module.__call__(x) → self.forward(x) → result
```

**Visual:**
```
┌─────────────────────────────────────────────────┐
│  nn.Module (Parent class)                       │
│  ┌───────────────────────────────────────────┐  │
│  │  def __call__(self, x):                   │  │
│  │      return self.forward(x)  ◄── defined  │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
                      ▲
                      │ inherit (super().__init__())
┌─────────────────────────────────────────────────┐
│  MyModel (Tera class)                           │
│  ┌───────────────────────────────────────────┐  │
│  │  def forward(self, x):       ◄── tu likhe │  │
│  │      return self.linear(x)                │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

**Important:**
- `forward` naam **fix** hai - change nahi kar sakte
- `super().__init__()` **zaroori** hai - isse `__call__`, GPU support, parameter tracking milta hai

**Additional helper functions bana sakte ho:**
```python
class Transformer(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = Encoder()
        self.decoder = Decoder()

    def encode(self, src):              # ← helper function
        return self.encoder(src)

    def decode(self, tgt, memory):      # ← helper function
        return self.decoder(tgt, memory)

    def forward(self, src, tgt):        # ← main entry (ZAROORI)
        memory = self.encode(src)
        output = self.decode(tgt, memory)
        return output

# Use:
output = model(src, tgt)         # forward call
memory = model.encode(src)       # direct helper call
```

---

#### 3. Common Layers (5 mins) ⭐⭐

```python
# Linear layer (fully connected)
nn.Linear(512, 256)         # 512 → 256

# Embedding (word → vector)
nn.Embedding(10000, 512)    # 10k words → 512-dim vectors

# LayerNorm (Transformer mein use hota hai)
nn.LayerNorm(512)

# Dropout (regularization)
nn.Dropout(p=0.1)           # 10% neurons randomly off

# Softmax
nn.Softmax(dim=-1)          # last dimension pe softmax

# ReLU activation
nn.ReLU()
```

---

#### 📌 nn.Linear Deep Dive

**nn.Linear(512, 256) ka matlab:**
```
nn.Linear(512, 256)
          ↓    ↓
       input  output    (rows/cols NAHI!)
       size   size

512 numbers input → 256 numbers output
```

**Matrix Operation:**
```
y = x @ W.T + b

Input x     Weight W.T      Bias b      Output y
(1, 512) @ (512, 256)   +  (256,)   =  (1, 256)
```

**Visual:**
```
         512 input features
         ↓
    ┌─────────┐
    │  Matrix │ ← (512 × 256) = 131,072 weights
    │  Magic  │   + 256 biases
    └─────────┘   = 131,328 parameters
         ↓
    256 output features
```

**Ek output element kaise banta hai:**
```
y1 = (x1 × w1) + (x2 × w2) + ... + (x512 × w512) + b1
     ────────────────────────────────────────────────
              512 multiplications + 1 bias
```

**256 kaun decide karta hai? TU! (Programmer)**

| Situation | Output size | Reason |
|-----------|-------------|--------|
| Compression | 512 → 256 | Information compress |
| Expansion | 512 → 2048 | More capacity |
| Classification | 512 → 10 | 10 classes predict |
| Binary | 512 → 1 | Yes/No predict |

**Transformer mein Linear layers:**
```python
nn.Linear(512, 512)    # Q, K, V projections
nn.Linear(512, 2048)   # FFN layer 1 (expand 4x)
nn.Linear(2048, 512)   # FFN layer 2 (back)
nn.Linear(512, 30000)  # output to vocab
```

**Tips:**
- Powers of 2 use karo (64, 128, 256...) - GPU efficient
- Gradually decrease/increase karo
- Last layer = task ke according (10 classes = 10)

---

#### 📌 Bias kya hai?

**Bias = ek extra number jo har output mein add hota hai**

```
y = x × weight + bias
        ↑          ↑
     slope      shift/offset
```

**Without vs With Bias:**
```
Without bias:              With bias (b = 2):
y = 3x                     y = 3x + 2

x=0 → y=0 (always!)        x=0 → y=2 (flexible!)

Line origin se guzregi     Line kahi bhi ho sakti
```

**Kyun zaroori hai?**
- Without bias: Model sirf origin se patterns seekh sakta
- With bias: Model kisi bhi position pe fit ho sakta

**Code mein:**
```python
linear = nn.Linear(512, 256)
print(linear.weight.shape)  # (256, 512) - slopes
print(linear.bias.shape)    # (256,) - shifts

# Calculation:
# y[i] = (x[0]×w[i,0] + x[1]×w[i,1] + ... + x[511]×w[i,511]) + bias[i]
```

**Analogy:**
```
Temperature prediction:
predicted = weather_data × weights + baseline_temp(25°C)
                                     ↑
                                    bias = reasonable starting point
```

---

#### 4. Forward Pass Example (5 mins) ⭐⭐

```python
class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(784, 256)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.layer1(x)    # 784 → 256
        x = self.relu(x)       # activation
        x = self.layer2(x)    # 256 → 10
        return x

# Data flow:
# Input(784) → Linear → ReLU → Linear → Output(10)
```

---

#### 5. Loss Functions (3 mins) ⭐⭐

```python
# Classification (Transformer mein bhi!)
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(logits, target)   # logits: (batch, classes), target: (batch,)

# Regression
loss_fn = nn.MSELoss()
```

---

#### 6. Optimizer (3 mins) ⭐⭐

```python
# Adam - Transformer paper bhi use karta hai
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# SGD - basic
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

---

#### 7. Training Loop - Core Pattern (10 mins) ⭐⭐⭐

```python
model = MyModel()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(num_epochs):
    for batch_x, batch_y in dataloader:

        # 1. Forward pass
        predictions = model(batch_x)

        # 2. Loss calculate
        loss = loss_fn(predictions, batch_y)

        # 3. Backward pass
        optimizer.zero_grad()   # purane gradients clear
        loss.backward()         # naye gradients calculate

        # 4. Update weights
        optimizer.step()

# Yaad rakho: Forward → Loss → Zero Grad → Backward → Step
```

---

#### 📌 Gradient & Learning Rate Explained

**Gradient kya hai?**

Gradient = **Direction + Magnitude** (kis taraf jaana hai aur kitna)

Socho tum ek **pahad pe ho** aur neeche jaana hai (lowest point = minimum loss):

```
     You are here
          ↓
         /\
        /  \
       /    \
      /      \
     /________\  ← Lowest point (minimum loss)
```

**Gradient batata hai:**
- Kis direction mein slope hai (+ ya -)
- Kitna steep hai slope (bada ya chhota number)

---

**Learning Rate kya hai?**

Learning rate = **Step size** (ek baar mein kitna move karna hai)

```
learning_rate = 0.01  (chhota step)
learning_rate = 0.1   (bada step)
learning_rate = 1.0   (bahut bada step)
```

**Problem with wrong learning rate:**

```
Too Small (0.0001):          Too Large (1.0):
     /\                           /\
    /  \                         /  \
   /    \                       /    \ ↗ JUMP!
  / ↓↓↓  \  (bahut slow)       /      X (miss kar diya!)
```

---

**Formula samjho:**

```python
weight = weight - learning_rate * gradient
```

**Example:**
- Current `m = 1.0`
- Gradient = `+0.5` (matlab: m zyada hai, kam karo)
- Learning rate = `0.01`

```
new_m = 1.0 - (0.01 * 0.5)
new_m = 1.0 - 0.005
new_m = 0.995  (thoda kam hua!)
```

---

**Code mein:**
```python
# Manual way (Linear Regression example)
with torch.no_grad():
    model.m -= learning_rate * model.m.grad   # weight update
    model.c -= learning_rate * model.c.grad

# PyTorch automatic way (Optimizer)
optimizer.step()  # internally yahi karta hai!
```

**Key Points:**
| Concept | Meaning | Analogy |
|---------|---------|---------|
| Gradient | Direction + steepness | Pahad ka slope |
| Learning Rate | Step size | Ek kadam kitna bada |
| `loss.backward()` | Gradient calculate | Slope measure karo |
| `optimizer.step()` | Weight update | Ek kadam neeche lo |

---

#### 📌 Gradient Calculation - How It Works

**Model:** `y_pred = m * x + c`
**Loss:** `Loss = mean((y_pred - y_train)²)`

---

**Step 1: Power Rule (2 kahan se aaya?)**

```
d/dx (x²) = 2x    ← Basic calculus rule

Loss = (y_pred - y_train)²
d(Loss)/d(y_pred) = 2 × (y_pred - y_train)
                    ↑
                    2 yahan se aaya!
```

---

**Step 2: Chain Rule**

```
d(Loss)     d(Loss)      d(y_pred)
─────── = ────────── × ──────────
  dm       d(y_pred)       dm

y_pred = m*x + c

d(y_pred)/dm = x      (m ke saath x multiply hai)
d(y_pred)/dc = 1      (c akela hai)
```

---

**Step 3: Final Gradients**

```
d(Loss)/dm = 2 × (y_pred - y_train) × x
d(Loss)/dc = 2 × (y_pred - y_train) × 1
```

---

**Example with Numbers:**

```
m = 1.5, c = 0.5, x = 3, y_train = 6

y_pred = 1.5 × 3 + 0.5 = 5.0
error = y_pred - y_train = 5.0 - 6 = -1.0

d(Loss)/dm = 2 × (-1.0) × 3 = -6.0   → m badhana chahiye
d(Loss)/dc = 2 × (-1.0) × 1 = -2.0   → c badhana chahiye

# Update:
new_m = 1.5 - 0.01 × (-6.0) = 1.56   ← m badha!
new_c = 0.5 - 0.01 × (-2.0) = 0.52   ← c badha!
```

---

**Visual Flow:**

```
Forward:   x ──→ [m*x + c] ──→ y_pred ──→ [Loss] ──→ number
                    ↑                        ↓
Backward:  m.grad ←──────── chain rule ──────┘
           c.grad ←──────── chain rule ──────┘
```

**Note:** `loss.backward()` ye sab automatically calculate karta hai!

---

#### 📌 Training Steps Deep Dive: backward → update → zero_grad

**Step 3: `loss.backward()` - Gradient CALCULATE**

```
Sirf CALCULATE karta hai, weights change NAHI hote:

m = 1.5         →  m = 1.5        (same)
m.grad = ???    →  m.grad = -6.0  (calculated!)
```

---

**Step 4: Update Weights - Actually MOVE karo**

```python
with torch.no_grad():
    model.m.data -= learning_rate * model.m.grad
```

```
m = 1.5 - 0.01 × (-6.0)
  = 1.5 + 0.06
  = 1.56  ← Actually move hua!

Analogy:
backward() = GPS ne bataya "100m left jaao"
update     = Actually 100m left chale
```

---

**Step 5: `zero_grad()` - Clean Slate**

```python
model.m.grad.zero_()
```

**Kyun zaroori hai?** PyTorch gradients ACCUMULATE hote hain!

```python
# WITHOUT zeroing:
Epoch 1: backward() → m.grad = -6.0
Epoch 2: backward() → m.grad = -6.0 + (-5.0) = -11.0  ❌ WRONG!

# WITH zeroing:
Epoch 1: backward() → m.grad = -6.0
         zero_grad() → m.grad = 0
Epoch 2: backward() → m.grad = -5.0  ✅ CORRECT!
```

---

**Visual Timeline:**

```
┌─────────────────────────────────────────────────────┐
│ backward()   │ m.grad = -6.0  │ m = 1.5  (same)     │
├──────────────┼────────────────┼─────────────────────┤
│ update       │ m.grad = -6.0  │ m = 1.56 (moved!)   │
├──────────────┼────────────────┼─────────────────────┤
│ zero_grad()  │ m.grad = 0     │ m = 1.56 (same)     │
└──────────────┴────────────────┴─────────────────────┘
```

---

**Summary Table:**

| Step | Kya karta hai | `.grad` | `.data` |
|------|---------------|---------|---------|
| `backward()` | Gradient calculate | Value aati hai | Same |
| `update` | Weight move | Same | Change |
| `zero_grad()` | Gradient clear | 0 | Same |

---

#### 📌 Manual vs Optimizer - Complete Code Comparison

**Manual Way (Without Optimizer):**

```python
import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.m = nn.Parameter(torch.randn(1))
        self.c = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return self.m * x + self.c

model = LinearRegression()

x_train = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y_train = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])

learning_rate = 0.01
epochs = 100

for epoch in range(epochs):
    # 1. Forward
    y_pred = model(x_train)

    # 2. Loss
    loss = ((y_pred - y_train) ** 2).mean()

    # 3. Backward
    loss.backward()

    # 4. Update (MANUAL - har parameter likhna padta hai)
    with torch.no_grad():
        model.m.data -= learning_rate * model.m.grad
        model.c.data -= learning_rate * model.c.grad

    # 5. Zero grad (MANUAL)
    model.m.grad.zero_()
    model.c.grad.zero_()
```

---

**Optimizer Way (With Adam):**

```python
import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.m = nn.Parameter(torch.randn(1))
        self.c = nn.Parameter(torch.randn(1))

    def forward(self, x):
        return self.m * x + self.c

model = LinearRegression()

x_train = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
y_train = torch.tensor([2.0, 4.0, 6.0, 8.0, 10.0])

learning_rate = 0.01
epochs = 100

# Optimizer (define ONCE before loop)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    # 1. Forward
    y_pred = model(x_train)

    # 2. Loss
    loss = ((y_pred - y_train) ** 2).mean()

    # 3. Backward + Update (3 lines only!)
    optimizer.zero_grad()   # Clear gradients
    loss.backward()         # Calculate gradients
    optimizer.step()        # Update ALL weights automatically
```

---

**Key Differences:**

| Aspect | Manual | Optimizer |
|--------|--------|-----------|
| Lines of code | 6+ | 3 |
| Per parameter | Likhna padta hai | Automatic |
| Features | Basic | Momentum, Adaptive LR |
| Production use | ❌ | ✅ |

---

**Popular Optimizers:**

| Optimizer | Code | Use Case |
|-----------|------|----------|
| SGD | `torch.optim.SGD(params, lr=0.01)` | Basic |
| SGD+Momentum | `torch.optim.SGD(params, lr=0.01, momentum=0.9)` | Faster |
| Adam | `torch.optim.Adam(params, lr=0.01)` | Best for most cases |

**Adam = Industry standard, Transformer paper bhi use karta hai!**

---

#### 8. GPU Usage (2 mins) ⭐

```python
# Check GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Model + Data dono GPU pe bhejo
model = model.to(device)
input = input.to(device)
target = target.to(device)
```

---

#### Time Summary
| Topic | Time | Priority |
|-------|------|----------|
| Tensors | 5 min | ⭐ |
| **nn.Module** | 10 min | ⭐⭐⭐ |
| Common Layers | 5 min | ⭐⭐ |
| Forward Pass | 5 min | ⭐⭐ |
| Loss Functions | 3 min | ⭐⭐ |
| Optimizer | 3 min | ⭐⭐ |
| **Training Loop** | 10 min | ⭐⭐⭐ |
| GPU | 2 min | ⭐ |

## 0.4 Math Concepts ✅ DONE (2026-02-17)
| Status | Task | Notes |
|--------|------|-------|
| ✓ | Matrix multiplication understand | A @ B, Q @ K.T |
| ✓ | Dot product understand | sum(a * b), scalar result |
| ✓ | Softmax function (formula + intuition) | exp(x) / sum(exp(x)), stable version |
| ✓ | Layer Normalization concept | (x-mean)/sqrt(var+eps), gamma, beta |
| ✓ | Cross-entropy loss | -log(P(correct)), batch version |
| ✓ | **Practice:** Implement softmax manually | math_concepts.py |

---

# PHASE 1: BUILDING BLOCKS

## Step 1: Scaled Dot-Product Attention ⭐ START HERE!

### 1.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Understand Q, K, V concept | Query, Key, Value |
| □ | Understand attention formula | Attention(Q,K,V) = softmax(QK^T/√d_k)V |
| □ | Why scaling by √d_k? | Prevents large dot products |
| □ | What is masking for? | Hide future positions in decoder |

### 1.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create function/class structure | |
| □ | Implement Q @ K.transpose() | Matrix multiplication |
| □ | Implement scaling (/ sqrt(d_k)) | |
| □ | Implement optional masking | masked_fill with -inf |
| □ | Implement softmax | |
| □ | Implement output = weights @ V | |
| □ | Return output and attention weights | |

### 1.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Test with random Q, K, V | |
| □ | Verify output shape | (batch, seq_len, d_v) |
| □ | Verify attention weights sum = 1 | Per row |
| □ | Test masking works | Future positions = 0 |
| □ | Test with different batch sizes | |
| □ | Check no NaN values | |

### 1.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 1:** Scaled Dot-Product Attention COMPLETE | |

---

## Step 2: Multi-Head Attention

### 2.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Why multiple heads? | Different representation subspaces |
| □ | Understand head splitting | d_model → h heads of d_k each |
| □ | Understand concatenation | Combine heads back |
| □ | Parameters: h=8, d_k=64, d_model=512 | |

### 2.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create class structure | |
| □ | Create W_Q linear layer (512→512) | |
| □ | Create W_K linear layer (512→512) | |
| □ | Create W_V linear layer (512→512) | |
| □ | Create W_O linear layer (512→512) | |
| □ | Implement projection of Q, K, V | |
| □ | Implement reshape for multi-head | (batch, seq, 512) → (batch, h, seq, 64) |
| □ | Apply scaled dot-product attention | Use Step 1 |
| □ | Implement concatenation | (batch, h, seq, 64) → (batch, seq, 512) |
| □ | Apply output projection W_O | |

### 2.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Input shape (32, 10, 512) → Output (32, 10, 512) | |
| □ | Test self-attention (Q=K=V) | |
| □ | Test cross-attention (Q≠K,V) | |
| □ | Test with mask | |
| □ | Verify gradient flow | |

### 2.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 2:** Multi-Head Attention COMPLETE | |

---

## Step 3: Positional Encoding

### 3.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Why positional encoding needed? | No recurrence = no position info |
| □ | Understand sin/cos formula | PE(pos,2i) = sin(...), PE(pos,2i+1) = cos(...) |
| □ | Why sin and cos? | Allows learning relative positions |
| □ | Add vs Concatenate? | ADD to embeddings! |

### 3.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create class structure | |
| □ | Create position indices (0 to max_len) | |
| □ | Create dimension indices | |
| □ | Calculate div_term = 10000^(2i/d_model) | |
| □ | Apply sin to even dimensions | |
| □ | Apply cos to odd dimensions | |
| □ | Register as buffer (not parameter) | register_buffer() |
| □ | Implement forward (add to input) | |

### 3.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Output shape (1, max_len, d_model) | |
| □ | Values between -1 and 1 | |
| □ | Each position unique encoding | |
| □ | Visualize as heatmap (optional) | |

### 3.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 3:** Positional Encoding COMPLETE | |

---

## Step 4: Position-wise Feed-Forward Network

### 4.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Structure: Linear → ReLU → Linear | 512 → 2048 → 512 |
| □ | Why expand then contract? | More capacity in hidden layer |
| □ | Applied position-wise (independently) | |

### 4.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create class structure | |
| □ | Create Linear(512, 2048) | |
| □ | Create ReLU activation | |
| □ | Create Linear(2048, 512) | |
| □ | Optional: Add dropout | |
| □ | Implement forward pass | |

### 4.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Input (32, 10, 512) → Output (32, 10, 512) | |
| □ | Count parameters | ~4M parameters |
| □ | Verify gradient flow | |

### 4.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 4:** Feed-Forward Network COMPLETE | |

---

## Step 5: Layer Normalization + Residual Connection

### 5.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Why residual connection? | Gradient flow, skip connection |
| □ | Why layer normalization? | Stabilize training |
| □ | Formula: LayerNorm(x + Sublayer(x)) | |

### 5.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Use nn.LayerNorm(d_model) | Built-in PyTorch |
| □ | Implement sublayer connection | |
| □ | Pattern: norm(x + dropout(sublayer(x))) | |

### 5.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Output shape same as input | |
| □ | Verify residual adds correctly | |

### 5.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 5:** Layer Norm + Residual COMPLETE | |

---

## Step 6: Embeddings

### 6.1 Theory Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | What is embedding? | Token ID → Dense vector |
| □ | Why scale by √d_model? | Balance with positional encoding |
| □ | Weight sharing concept | Input, output, pre-softmax |

### 6.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Use nn.Embedding(vocab_size, d_model) | |
| □ | Implement scaling (* sqrt(d_model)) | |
| □ | Optional: Weight sharing | |

### 6.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Input (batch, seq_len) → Output (batch, seq_len, 512) | |
| □ | Check embedding values | |

### 6.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 6:** Embeddings COMPLETE | |

---

# PHASE 2: ENCODER

## Step 7: Single Encoder Layer

### 7.1 Components Needed
| Status | Component | Notes |
|--------|-----------|-------|
| □ | MultiHeadAttention (from Step 2) | |
| □ | FeedForward (from Step 4) | |
| □ | LayerNorm × 2 | |
| □ | Dropout × 2 | |

### 7.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create EncoderLayer class | |
| □ | Initialize all components | |
| □ | Forward: Self-attention | attn(x, x, x, mask) |
| □ | Forward: Add & Norm 1 | |
| □ | Forward: Feed-forward | |
| □ | Forward: Add & Norm 2 | |

### 7.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Input/Output shape same | (batch, seq, 512) |
| □ | Gradient flow works | |

### 7.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 7:** Single Encoder Layer COMPLETE | |

---

## Step 8: Encoder Stack

### 8.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create Encoder class | |
| □ | Stack N=6 EncoderLayers | nn.ModuleList |
| □ | Add final LayerNorm | |
| □ | Implement forward (loop through layers) | |

### 8.2 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Input/Output shape correct | |
| □ | All 6 layers execute | |
| □ | Memory output correct | |

### 8.3 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 8:** Encoder Stack COMPLETE | |

---

# PHASE 3: DECODER

## Step 9: Causal Mask Creation

### 9.1 Understanding
| Status | Task | Notes |
|--------|------|-------|
| □ | Why causal mask? | Prevent seeing future |
| □ | Lower triangular matrix | |

### 9.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create mask function | |
| □ | torch.tril(torch.ones(size, size)) | |
| □ | Handle batch dimension | |

### 9.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Mask shape correct | |
| □ | Future positions are 0 | |

---

## Step 10: Single Decoder Layer

### 10.1 Components Needed
| Status | Component | Notes |
|--------|-----------|-------|
| □ | MultiHeadAttention × 2 | Self + Cross |
| □ | FeedForward | |
| □ | LayerNorm × 3 | |
| □ | Dropout × 3 | |

### 10.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create DecoderLayer class | |
| □ | Forward: Masked self-attention | With causal mask |
| □ | Forward: Add & Norm 1 | |
| □ | Forward: Cross-attention | Q=decoder, K,V=encoder |
| □ | Forward: Add & Norm 2 | |
| □ | Forward: Feed-forward | |
| □ | Forward: Add & Norm 3 | |

### 10.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Masking works (future hidden) | |
| □ | Cross-attention connects to encoder | |
| □ | Output shape correct | |

### 10.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 9:** Single Decoder Layer COMPLETE | |

---

## Step 11: Decoder Stack

### 11.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create Decoder class | |
| □ | Stack N=6 DecoderLayers | |
| □ | Add final LayerNorm | |
| □ | Pass memory (encoder output) to each layer | |

### 11.2 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | All 6 layers execute | |
| □ | Memory used in cross-attention | |

### 11.3 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 10:** Decoder Stack COMPLETE | |

---

# PHASE 4: COMPLETE TRANSFORMER

## Step 12: Full Transformer Model

### 12.1 Components Needed
| Status | Component | Notes |
|--------|-----------|-------|
| □ | Source Embedding | |
| □ | Target Embedding | |
| □ | Positional Encoding | |
| □ | Encoder Stack | |
| □ | Decoder Stack | |
| □ | Final Linear (d_model → vocab_size) | |

### 12.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create Transformer class | |
| □ | Initialize all components | |
| □ | Forward: Embed + PosEnc source | |
| □ | Forward: Embed + PosEnc target | |
| □ | Forward: Encoder(src) → memory | |
| □ | Forward: Decoder(tgt, memory) | |
| □ | Forward: Linear → logits | |
| □ | Create mask generation methods | |

### 12.3 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Forward pass without error | Random src, tgt |
| □ | Output shape (batch, tgt_len, vocab_size) | |
| □ | Gradient flow through entire model | |
| □ | Parameter count reasonable | ~65M for base |

### 12.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 11:** Full Transformer COMPLETE | |

---

# PHASE 5: DATA PREPARATION

## Step 13: Tokenization

### 13.1 Setup
| Status | Task | Notes |
|--------|------|-------|
| □ | Choose tokenizer (BPE/WordPiece) | Or use existing |
| □ | Build vocabulary | |
| □ | Define special tokens | <pad>, <sos>, <eos>, <unk> |

### 13.2 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Text → Token IDs function | |
| □ | Token IDs → Text function | |
| □ | Handle unknown words | |

---

## Step 14: Dataset & DataLoader

### 14.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create Dataset class | |
| □ | Load source-target pairs | |
| □ | Tokenize on-the-fly or pre-tokenize | |
| □ | Implement __getitem__ | |
| □ | Implement __len__ | |

### 14.2 Batching
| Status | Task | Notes |
|--------|------|-------|
| □ | Implement padding (same length) | |
| □ | Create collate_fn | |
| □ | Create DataLoader | |
| □ | Sort by length (optional, efficiency) | |

### 14.3 Mask Creation
| Status | Task | Notes |
|--------|------|-------|
| □ | Source padding mask | |
| □ | Target padding mask | |
| □ | Target causal mask | |
| □ | Combine masks properly | |

### 14.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 12:** Data Pipeline COMPLETE | |

---

# PHASE 6: TRAINING

## Step 15: Loss Function

### 15.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | CrossEntropyLoss | |
| □ | Set ignore_index for padding | |
| □ | Optional: Label smoothing (ε=0.1) | |

---

## Step 16: Optimizer & Scheduler

### 16.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Adam optimizer | β1=0.9, β2=0.98, ε=1e-9 |
| □ | Warmup scheduler | |
| □ | Implement lr formula | d^(-0.5) * min(step^(-0.5), step*warmup^(-1.5)) |
| □ | warmup_steps = 4000 | |

---

## Step 17: Training Loop

### 17.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Create training function | |
| □ | Forward pass | |
| □ | Loss calculation | |
| □ | Backward pass | |
| □ | Gradient clipping (optional) | |
| □ | Optimizer step | |
| □ | Scheduler step | |
| □ | Logging (loss, lr, step) | |
| □ | Checkpoint saving | |

### 17.2 Validation Loop
| Status | Task | Notes |
|--------|------|-------|
| □ | Create validation function | |
| □ | No gradient computation | torch.no_grad() |
| □ | Calculate validation loss | |

### 17.3 Training Script
| Status | Task | Notes |
|--------|------|-------|
| □ | Epoch loop | |
| □ | Train + Validate each epoch | |
| □ | Early stopping (optional) | |
| □ | Best model saving | |

### 17.4 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 13:** Training Loop COMPLETE | |

---

## Step 18: Overfit Test

### 18.1 Critical Test!
| Status | Task | Notes |
|--------|------|-------|
| □ | Take 5-10 examples only | |
| □ | Train until loss → 0 | |
| □ | Model should MEMORIZE | |
| □ | If not overfitting, there's a BUG! | |

### 18.2 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 14:** Overfit Test PASSED | |

---

# PHASE 7: INFERENCE

## Step 19: Greedy Decoding

### 19.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Encode source → memory | |
| □ | Start with <sos> token | |
| □ | Loop: predict next token | |
| □ | Append predicted token | |
| □ | Stop at <eos> or max_len | |
| □ | Return generated sequence | |

### 19.2 Testing
| Status | Task | Notes |
|--------|------|-------|
| □ | Generates valid tokens | |
| □ | Stops correctly | |
| □ | On overfit data, reproduces target | |

### 19.3 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 15:** Greedy Decoding COMPLETE | |

---

## Step 20: Beam Search (Advanced)

### 20.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Maintain beam_size candidates | |
| □ | Score = log probability | |
| □ | Expand each candidate | |
| □ | Keep top beam_size | |
| □ | Length penalty (optional) | |
| □ | Return best sequence | |

### 20.2 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 16:** Beam Search COMPLETE | |

---

# PHASE 8: EVALUATION

## Step 21: BLEU Score

### 21.1 Implementation
| Status | Task | Notes |
|--------|------|-------|
| □ | Use sacrebleu or nltk | |
| □ | Generate translations for test set | |
| □ | Calculate BLEU score | |

### 21.2 Milestone
| Status | Milestone | Notes |
|--------|-----------|-------|
| □ | **MILESTONE 17:** BLEU Evaluation COMPLETE | |

---

# PHASE 9: IMPROVEMENTS (Advanced)

## Optional Enhancements
| Status | Task | Notes |
|--------|------|-------|
| □ | Mixed precision training (fp16) | |
| □ | Gradient accumulation | |
| □ | Learning rate finder | |
| □ | Attention visualization | |
| □ | Model parallelism | |
| □ | Larger dataset training | |

---

# FINAL MILESTONES SUMMARY

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Scaled Dot-Product Attention | □ |
| 2 | Multi-Head Attention | □ |
| 3 | Positional Encoding | □ |
| 4 | Feed-Forward Network | □ |
| 5 | Layer Norm + Residual | □ |
| 6 | Embeddings | □ |
| 7 | Single Encoder Layer | □ |
| 8 | Encoder Stack | □ |
| 9 | Single Decoder Layer | □ |
| 10 | Decoder Stack | □ |
| 11 | Full Transformer | □ |
| 12 | Data Pipeline | □ |
| 13 | Training Loop | □ |
| 14 | Overfit Test | □ |
| 15 | Greedy Decoding | □ |
| 16 | Beam Search | □ |
| 17 | BLEU Evaluation | □ |

---

# DEBUGGING CHECKLIST

## When Something Goes Wrong:

### Shape Errors
| Check | Status |
|-------|--------|
| □ | Print shapes at each step | |
| □ | Verify batch dimension | |
| □ | Check transpose dimensions | |
| □ | Verify mask shape | |

### NaN Loss
| Check | Status |
|-------|--------|
| □ | Check for division by zero | |
| □ | Verify softmax input not too large | |
| □ | Check learning rate not too high | |
| □ | Add gradient clipping | |

### Loss Not Decreasing
| Check | Status |
|-------|--------|
| □ | Learning rate too low? | |
| □ | Learning rate too high? | |
| □ | Data loading correct? | |
| □ | Labels shifted correctly? | |
| □ | Mask applied correctly? | |

### Model Not Learning
| Check | Status |
|-------|--------|
| □ | Gradients flowing? (param.grad) | |
| □ | Parameters updating? | |
| □ | Try overfitting small data | |
| □ | Check loss function | |

---

# PROGRESS TRACKER

## Daily Progress Log

| Date | What I Did | Issues Faced | Resolved? |
|------|------------|--------------|-----------|
| 2026-01-18 | Linear Regression complete (y=mx+c) | Loss high with lr=0.01 | ✅ lr=0.1 |
| 2026-01-18 | Manual gradient descent implemented | - | ✅ |
| 2026-01-18 | Adam optimizer implemented | - | ✅ |
| 2026-01-18 | Save/Load model working | state_dict empty | ✅ nn.Parameter |
| 2026-01-18 | 1model folder setup complete | - | ✅ |
| | | | |

---

# NOTES

## Important Learnings:
```
1. nn.Parameter vs torch.randn - Parameter is tracked by PyTorch for save/load

2. Gradient = direction + magnitude, Learning Rate = step size

3. loss.backward() sirf calculate karta hai, optimizer.step() actually update karta hai

4. Gradients accumulate hote hain - zero_grad() zaroori hai!

5. Adam optimizer = best for most cases, Transformer bhi use karta hai
```

## Questions to Explore:
```
1. How does Adam internally adjust learning rate?

2. What is momentum in SGD?

3. When to use SGD vs Adam?
```

## Resources Used:
```
1. PyTorch documentation

2. Transformer Paper (Attention Is All You Need)

3. Claude Code learning sessions
```

---

*Last Updated: 2026-01-18*

*Current Phase: Phase 0.3 PyTorch Basics ✅ COMPLETE*

*Phase 0.4 Math Concepts ✅ DONE (2026-02-17) - math_concepts.py*
*Next Step: Phase 1 - Scaled Dot-Product Attention*
