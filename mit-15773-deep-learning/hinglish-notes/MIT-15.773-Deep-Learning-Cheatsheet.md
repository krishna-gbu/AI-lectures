# MIT 15.773 Deep Learning Cheatsheet

Ye file `MIT-15.773-Deep-Learning-Hinglish-Notes.md` ka fast-revision companion hai.

Use case:

- exam se pehle ultra-fast revision
- lecture flow ek jagah dekhna
- formulas + architecture + comparisons ek sheet me rakhna
- visual diagram ke saath full course map samajhna

---

## Course Map

```text
Lecture 1   -> NN intuition
Lecture 2   -> Training, loss, gradient, backprop
Lecture 3A  -> Keras/TF structured-data pipeline
Lecture 3B  -> Image basics + Fashion MNIST dense model
Lecture 4   -> CNNs + transfer learning
Lecture 5   -> Text vectorization + Bag-of-Words
Lecture 6   -> Embeddings
Lecture 7   -> Transformer encoder intuition
Lecture 8   -> Full transformer block + HF pipelines
Lecture 9   -> Causal LLMs + decoding + BPE
Lecture 10  -> Instruction tuning + RLHF + RAG
Lecture 10.5 -> Fine-tuning + LoRA
Lecture 11  -> Diffusion + U-Net + CLIP + Stable Diffusion
```

```text
Raw Data
   |
   v
Representation Learning
   |
   v
Prediction / Generation
   |
   v
Loss
   |
   v
Gradient
   |
   v
Update
   |
   v
Better Model
```

---

## Lecture 1: Neural Network Foundations

### Big Picture

```text
AI
 |
 +-- ML
      |
      +-- Deep Learning
             |
             +-- Generative AI
```

- `AI` = intelligent behavior
- `ML` = rules manually mat likho, examples se seekho
- `DL` = features manually mat banao, representations seekho
- `GenAI` = new text/image/audio generate karo

### Structured vs Unstructured

| Type | Example | Notes |
|---|---|---|
| structured | age, income, cholesterol | columns predefined hote hain |
| unstructured | image, audio, text, video | raw signal hota hai, direct columns nahi |

### Human Bottleneck

Old pipeline:

```text
Raw image/audio/text
   |
   v
Human manually features banaye
   |
   v
Model learn kare
```

DL pipeline:

```text
Raw image/audio/text
   |
   v
Deep network khud features seekhe
   |
   v
Prediction / generation
```

### Logistic Regression -> Neural Network

```text
Input x
  |
  v
Weighted sum: z = w.x + b
  |
  v
Activation
  |
  v
Output
```

- ek single-neuron binary classifier = logistic regression mindset
- hidden layers add karo = richer feature composition

### Activation Functions

| Activation | Formula | Best use |
|---|---|---|
| sigmoid | `1 / (1 + e^-x)` | binary output |
| ReLU | `max(0, x)` | hidden layers |

### Critical Idea

- hidden layer = smarter intermediate representation
- nonlinearity = actual power
- all-linear deep net = still effectively linear

### One-line Recall

`Logistic regression + hidden layers + nonlinearity = neural network mindset`

---

## Lecture 2: Training Deep Neural Networks

### Heart Disease Model

```text
29 inputs -> Dense(16, ReLU) -> Dense(1, Sigmoid)
```

- `29 inputs` one-hot encoding ke baad bane
- total params:

```text
(29 x 16) + 16 + (16 x 1) + 1 = 497
```

### Training Objective

```text
Input -> Prediction -> Loss -> Gradient -> Update -> Better weights
```

### Loss Matching

| Problem | Output layer | Loss |
|---|---|---|
| regression | linear | MSE |
| binary classification | sigmoid | binary cross-entropy |
| multi-class classification | softmax | categorical-family cross-entropy |

### BCE Intuition

- correct confident prediction = low loss
- wrong confident prediction = huge loss

### Gradient Descent

```text
w <- w - alpha * grad
```

- `grad` = kis direction me loss badh raha hai
- `-grad` = kis direction me loss ghatega
- `alpha` = step size

### Backpropagation

```text
Output error
   |
   v
Chain rule se hidden layers tak blame bhejo
   |
   v
Har weight ka gradient nikalo
```

- backprop = gradient calculator
- gradient descent / Adam = weight updater

### SGD vs Full GD

| Method | Data per update | Practicality |
|---|---|---|
| full GD | full dataset | expensive |
| minibatch SGD | small batch | practical default |

### Adam

- adaptive learning rates
- past gradient info use karta hai
- strong default optimizer

### One-line Recall

`Loss tells how bad, gradient tells where, learning rate tells how far`

---

## Lecture 3A: Structured Data + Keras/TF

### Training Terms

| Term | Meaning |
|---|---|
| epoch | full pass over training data |
| batch | mini chunk of training data |
| iteration | one weight update |

### Example

```text
194 samples, batch size 32
=> ceil(194/32) = 7 batches per epoch
```

### Overfitting Pattern

```text
Training loss down
Validation loss down initially
Validation loss later up
=> overfitting
```

### Early Stopping

- validation metric monitor karo
- jab improvement ruk jaye, stop karo

### Dropout

```text
Training time:
some neurons randomly off
=> model robust banta hai
```

### TensorFlow vs Keras

| Tool | Role |
|---|---|
| TensorFlow | autodiff, optimizer, hardware execution |
| Keras | user-friendly modeling API |

### Heart Disease Notebook Pipeline

```text
Raw tabular data
   |
   v
Categorical -> one-hot
Numerical -> standardize
   |
   v
Train/test split
   |
   v
Model define
   |
   v
compile()
   |
   v
fit()
   |
   v
evaluate()
```

### Split Before Standardization

```text
Wrong:
full data mean/std -> split

Right:
split -> training mean/std -> apply to train and test
```

- reason: data leakage avoid karna

### Notebook Results

- baseline around `72.6%`
- neural model test accuracy around `83.61%`

### One-line Recall

`Epoch = full pass, batch = chunk, iteration = one update`

---

## Lecture 3B: Computer Vision Basics + Fashion MNIST

### Image Representation

```text
Grayscale image:
[height x width x 1]

RGB image:
[height x width x 3]
```

### Computer Vision Tasks

| Task | Output |
|---|---|
| image classification | one label for whole image |
| localization | object + rough location |
| object detection | many objects + boxes |
| semantic segmentation | class per pixel |
| instance segmentation | class per pixel + object identity |

### Fashion MNIST

- `70,000` grayscale images
- `10` classes
- `28 x 28` image size

### Dense Fashion MNIST Pipeline

```text
28x28 image
   |
   v
Flatten -> 784 vector
   |
   v
Dense(256, ReLU)
   |
   v
Dense(10, Softmax)
```

### Softmax

- raw scores ko probabilities me convert karta hai
- all class probabilities sum to `1`

### Sparse Categorical Cross-Entropy

- use when labels integer encoded hon
- example class label `3`, not one-hot `[0,0,0,1,...]`

### Notebook Result

- test accuracy around `88.45%`

### Key Limitation

- flatten spatial locality destroy karta hai
- better architecture for images = CNN

### One-line Recall

`Flatten image ko vector banata hai, CNN image ko naturally treat karta hai`

---

## Lecture 4: CNNs + Transfer Learning

### Dense Image Model ki Problems

```text
Image -> Flatten -> Dense

Problems:
1. too many parameters
2. spatial locality lost
3. pattern reuse weak
```

### Convolution

```text
Input image
   |
   v
Small filter slide hota hai
   |
   v
Feature map banta hai
```

- same filter poori image par reuse hota hai
- examples: vertical edge, horizontal edge, texture

### Pooling

```text
Feature map
   |
   v
MaxPool / AvgPool
   |
   v
Smaller feature map
```

- size reduce
- strongest local evidence preserve
- translation robustness improve

### CNN Hierarchy

```text
early layers   -> edges / textures
middle layers  -> motifs / parts
deep layers    -> object concepts
```

### CNN Architecture

```text
Image
  |
  v
Conv -> ReLU
Conv -> ReLU
Pool
Repeat
Flatten / Global Pool
Dense / Output
```

### Transfer Learning

```text
Pretrained ImageNet model
   |
   v
Old 1000-class head remove
   |
   v
New task-specific head add
   |
   v
Freeze or partially fine-tune
```

### Notebook Results

- Fashion MNIST CNN around `90.58%`
- Handbags/shoes scratch CNN around `86.84%`
- transfer-learning setup reached `100%` on tiny test set

### One-line Recall

`CNN = local + shared + reusable; transfer learning = borrow visual brain`

---

## Lecture 5: Text Vectorization + Bag-of-Words

### STIE Pipeline

```text
Text
  |
  v
Standardize
  |
  v
Tokenize
  |
  v
Index
  |
  v
Encode
```

### Terms

| Step | Meaning |
|---|---|
| standardize | lowercase, punctuation cleanup |
| tokenize | sentence ko pieces me todna |
| index | token -> integer ID |
| encode | integer -> vector representation |

### One-hot vs Multi-hot

| Type | Meaning |
|---|---|
| one-hot | one word ki identity |
| multi-hot | sentence me kaunse words present hain |
| count vector | word kitni baar aya |

### Bag-of-Words

```text
Sentence
  |
  v
Order ignore
  |
  v
Word presence / count vector
```

### Weakness

`dog bites man` vs `man bites dog`

- tokens same
- meaning different
- bag-of-words order lose karta hai

### Bigrams

- adjacent two-word context add karte hain
- example: `not good` ek distinct unit ban sakta hai

### Notebook Results

- simple BoW accuracy around `72.03%`
- bigrams ke saath around `75.09%`

### One-line Recall

`Bag-of-words ingredients yaad rakhta hai, recipe nahi`

---

## Lecture 6: Embeddings

### One-hot ki Problems

```text
1. huge sparse vectors
2. no semantic similarity
```

### Embedding Intuition

```text
Token ID
  |
  v
Dense vector
  |
  v
Nearby vectors = related words
```

### Distributional Hypothesis

`You shall know a word by the company it keeps`

- similar context -> similar meaning

### GloVe Intuition

- large corpus me co-occurrence statistics use karo
- aise vectors seekho jo context relations explain kar sakein

### Keras Pipeline

```text
Indexed token sequence
   |
   v
Embedding layer
   |
   v
Sequence of word vectors
   |
   v
GlobalAveragePooling1D
   |
   v
Sentence vector
   |
   v
Classifier
```

### Compared Strategies

| Method | Test accuracy |
|---|---|
| frozen GloVe | `0.6320` |
| fine-tuned GloVe | `0.6882` |
| learned from scratch | `0.7137` |

### One-line Recall

`One-hot says who, embedding says who + kis ke paas`

---

## Lecture 7: Transformers I

### Motivating Task: Slot Filling

```text
Input:
I want to fly from Boston to Denver tomorrow

Output:
O O O O B-fromcity O B-tocity B-date
```

### Architecture Requirements

```text
1. context chahiye
2. order chahiye
3. same-length output chahiye
```

### Self-Attention Intuition

```text
Current token
   |
   v
Decide karo kin dusre tokens ko dekhna hai
   |
   v
Context-aware token representation
```

### Transformer Encoder

```text
Token embeddings
   +
Positional embeddings
   |
   v
Self-attention
   |
   v
Feed-forward
   |
   v
Contextual embeddings
```

### Multi-head Preview

- different heads different relations seekhte hain

### Notebook Results

- overall accuracy around `98.64%`
- slot-only accuracy around `91.3%`

### One-line Recall

`Transformer = context + order + same-length output`

---

## Lecture 8: Transformers II + Hugging Face Pipelines

### Q, K, V

```text
Token embedding
   |
   +--> Query: mujhe kya chahiye?
   +--> Key: mere paas kya signal hai?
   +--> Value: meri actual content kya hai?
```

### Self-Attention Formula

```text
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

### Multi-head Attention

```text
Q,K,V
 |
 +--> Head 1
 +--> Head 2
 +--> Head 3
 +--> ...
 |
 v
Concatenate
 |
 v
Output projection
```

### Residual + Layer Norm

```text
x
 |
 +------+
 |      |
 |   Sublayer(x)
 |      |
 +---- add
        |
        v
   LayerNorm
```

### Why Important

- residual = gradient flow
- layer norm = stable scale
- stackable deep transformer blocks possible

### Hugging Face Tasks

- text classification
- NER
- question answering
- summarization
- text generation

### One-line Recall

`Q asks, K matches, V carries; residual saves, layer norm stabilizes`

---

## Lecture 9: Large Language Models I

### Next-Token Prediction

```text
the cat sat on the __
```

Model objective:

- next token predict karo

### Why Plain Self-Attention Fails

```text
If future token visible:
model can cheat by looking ahead
```

### Causal Mask

```text
Allowed attention:

token 1 -> 1
token 2 -> 1,2
token 3 -> 1,2,3
token 4 -> 1,2,3,4
```

- future positions blocked

### GPT-Style Model

```text
Token embeddings + positions
   |
   v
Causal self-attention blocks
   |
   v
Next-token probability distribution
```

### Decoding

| Method | Idea |
|---|---|
| greedy | best token every step |
| random sampling | sample from full distribution |
| top-k | only best `k` tokens |
| top-p | smallest set with cumulative mass `p` |
| temperature | randomness control |

### BPE Tokenization

```text
Start with characters
   |
   v
Frequent pairs merge karo
   |
   v
Subword vocabulary banao
```

### One-line Recall

`Causal mask future ko band karta hai; GPT token-by-token generate karta hai`

---

## Lecture 10: LLMs II + RAG

### Problem with Raw GPT-3

- fluent tha
- but instruction-following weak thi

### Instruction Tuning Flow

```text
Step 1: Supervised Fine-Tuning
instruction -> human-written good answer

Step 2: Reward Model
instruction + answer -> scalar score

Step 3: RLHF-style optimization
reward ke hisab se model behavior improve
```

### Pretraining vs Alignment

| Stage | Teaches |
|---|---|
| pretraining | language statistics, fluency |
| alignment | helpfulness, instruction following |

### RAG Flow

```text
Documents
   |
   v
Chunking
   |
   v
Chunk embeddings
   |
   v
User query embedding
   |
   v
Cosine similarity retrieval
   |
   v
Retrieved context + prompt
   |
   v
LLM answer
```

### When to Use What

| Need | Better choice |
|---|---|
| fresh factual knowledge | RAG |
| style/format behavior change | fine-tuning |

### One-line Recall

`Pretraining teaches language, alignment teaches behavior, RAG adds context`

---

## Lecture 10.5: Fine-Tuning + LoRA

### Full Fine-Tuning Problem

```text
Huge model
  |
  v
Need memory for:
1. parameters
2. gradients
3. optimizer states
```

### LoRA Idea

```text
Instead of full update:
Delta W

Use:
Delta W = B A

where rank is small
```

### LoRA Pipeline

```text
Base model weights frozen
   |
   v
Small trainable low-rank adapters
   |
   v
Cheap task adaptation
```

### Decision Rule

| Need | Choice |
|---|---|
| new external knowledge | RAG |
| lightweight behavior adaptation | LoRA |
| full deep adaptation with lots of compute | full fine-tuning |

### One-line Recall

`Freeze big, train small`

---

## Lecture 11: Diffusion Models

### Core Intuition

```text
Clean image
   |
   v
Noise add karna easy

So learn reverse:
Noise remove karna
```

### Training Setup

```text
Clean image
   |
   v
Add random noise
   |
   v
Noisy image + target cleaner image
   |
   v
Train denoiser
```

### Inference

```text
Pure noise
   |
   v
Denoise step 1
   |
   v
Denoise step 2
   |
   v
...
   |
   v
Generated image
```

### Better Target

- direct clean image predict karne ke bajay
- noise `epsilon` predict karna often better

### U-Net

```text
Left side  -> downsample / compress / features
Right side -> upsample / reconstruct
Skips      -> detail preserve
```

### CLIP

```text
Text encoder -> text embedding
Image encoder -> image embedding

Match pair close
Mismatch pair far
```

### Stable Diffusion

```text
Prompt
  |
  v
CLIP-style text embedding
  |
  v
Conditioned latent diffusion
  |
  v
U-Net denoising steps
  |
  v
Image
```

### One-line Recall

`Diffusion = start noisy, clean gradually; CLIP = prompt guidance`

---

## Most Important Comparisons

| Topic | A | B | Core difference |
|---|---|---|---|
| rules vs ML | hand-coded logic | learn from data | manual vs statistical learning |
| structured vs unstructured | tables | image/audio/text | predefined features vs raw signals |
| sigmoid vs softmax | binary | multi-class | one probability vs many probabilities |
| dense image model vs CNN | flatten everything | local filters | no locality vs locality-aware |
| bag-of-words vs embeddings | sparse counts | dense semantics | token presence vs meaning geometry |
| bidirectional attention vs causal attention | full context | only past context | understanding vs generation |
| fine-tuning vs RAG | behavior change | external knowledge retrieval | weights update vs context injection |
| full fine-tuning vs LoRA | all weights train | low-rank adapters train | expensive vs efficient |

---

## Formula Sheet

### Core Formulas

| Concept | Formula |
|---|---|
| sigmoid | `1 / (1 + e^-x)` |
| ReLU | `max(0, x)` |
| softmax | `exp(z_i) / sum_j exp(z_j)` |
| BCE | `-y log(p) - (1-y) log(1-p)` |
| MSE | `(1/n) * sum (y - y_hat)^2` |
| gradient update | `w <- w - alpha * grad` |
| dense params | `m*n + n` |
| self-attention | `softmax(QK^T / sqrt(d_k))V` |
| cosine similarity | `(a.b) / (||a|| ||b||)` |
| LoRA update | `W_new = W + BA` |

### Counts / Identities

- batches per epoch = `ceil(training_size / batch_size)`
- grayscale image shape = `(H, W, 1)`
- RGB image shape = `(H, W, 3)`
- color image batch shape = `(batch, H, W, 3)`

---

## Output-Layer Matching Sheet

| Target type | Output | Loss |
|---|---|---|
| single numeric value | linear | MSE |
| binary class | sigmoid | binary cross-entropy |
| multi-class class ID | softmax | sparse categorical cross-entropy |
| multi-class one-hot label | softmax | categorical cross-entropy |

---

## Keras/Training Checklist

```text
1. Problem type identify karo
2. Data preprocess karo
3. Split correctly karo
4. Architecture choose karo
5. Output layer match karo
6. Loss match karo
7. Optimizer choose karo
8. Validation monitor karo
9. Overfitting check karo
10. Test evaluate karo
```

---

## NLP/LLM Progress Ladder

```text
BoW
  |
  v
Embeddings
  |
  v
Transformer Encoder
  |
  v
Causal Transformer / GPT
  |
  v
Instruction-Tuned LLM
  |
  v
RAG / LoRA / Diffusion-era applications
```

---

## Vision Progress Ladder

```text
Pixels
  |
  v
Flatten + Dense
  |
  v
CNN
  |
  v
Transfer Learning
  |
  v
CLIP / Diffusion / Stable Diffusion
```

---

## Exam Traps

- `Backprop` aur `gradient descent` same nahi hote.
- `Epoch`, `batch`, `iteration` same nahi hote.
- `Softmax` binary classifier ka default nahi hai.
- `Sparse categorical cross-entropy` integer labels ke liye hoti hai.
- `Flatten` learning layer nahi, shape-conversion layer hai.
- `CNN` ka benefit sirf accuracy nahi, inductive bias bhi hai.
- `Bag-of-words` order lose karta hai.
- `Embeddings` semantic closeness encode kar sakti hain.
- `Transformer` sirf text generation architecture nahi, token-level tasks bhi kar sakta hai.
- `Causal mask` future peeking rokta hai.
- `Instruction tuning` aur `RAG` same problem solve nahi karte.
- `LoRA` aur quantization same cheez nahi hain.
- `Diffusion` one-shot image generation nahi, repeated denoising hai.

---

## Super-Short Memory Hooks

- `DL = learn representations`
- `Loss = how bad`
- `Gradient = which way`
- `CNN = local filters`
- `BoW = order gone`
- `Embedding = meaning geometry`
- `Transformer = attention decides context`
- `Causal mask = no future access`
- `RAG = retrieve then answer`
- `LoRA = freeze big, train small`
- `Diffusion = start noisy, clean gradually`

---

## Final 2-Minute Revision

```text
Lecture 1:
NN = weighted functions + activations

Lecture 2:
Training = loss -> gradient -> update

Lecture 3A:
Structured DL = preprocess + compile + fit + validate

Lecture 3B:
Images = tensors, multi-class => softmax

Lecture 4:
CNN beats flatten for images; transfer learning reuses features

Lecture 5:
Text needs STIE; BoW is simple but order-blind

Lecture 6:
Embeddings bring dense semantic meaning

Lecture 7:
Transformer encoder gives context-aware token vectors

Lecture 8:
QKV + multi-head + residual + layer norm = real transformer block

Lecture 9:
LLM = causal transformer trained for next-token prediction

Lecture 10:
Instruction tuning + reward model + RLHF + RAG

Lecture 10.5:
LoRA = low-rank efficient adaptation

Lecture 11:
Diffusion = denoise from noise; U-Net + CLIP = modern image generation
```

---

## Important Resources

### Primary Revision Files

- Detailed master notes: [MIT-15.773-Deep-Learning-Hinglish-Notes.md](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/hinglish-notes/MIT-15.773-Deep-Learning-Hinglish-Notes.md>)
- Fast revision sheet: [MIT-15.773-Deep-Learning-Cheatsheet.md](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/hinglish-notes/MIT-15.773-Deep-Learning-Cheatsheet.md>)

### Most Important PDFs

- Lecture 1: [mit15_773_s24_lec01.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec01.pdf>)
- Lecture 2: [mit15_773_s24_lec02.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec02.pdf>)
- Backprop example: [mit15_773_s24_lec02_backprop_example.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec02_backprop_example.pdf>)
- Lecture 3A: [mit15_773_s24_lec03a.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec03a.pdf>)
- Lecture 3B: [mit15_773_s24_lec03b.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec03b.pdf>)
- Lecture 4: [mit15_773_s24_lec04.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec04.pdf>)
- Lecture 5: [mit15_773_s24_lec05.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec05.pdf>)
- Lecture 6: [mit15_773_s24_lec06.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec06.pdf>)
- Lecture 7: [mit15_773_s24_lec07.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec07.pdf>)
- Lecture 8: [mit15_773_s24_lec08.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec08.pdf>)
- Lecture 9: [mit15_773_s24_lec09.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec09.pdf>)
- Lecture 10: [mit15_773_s24_lec10.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec10.pdf>)
- Lecture 10.5: [mit15_773_s24_lec10.5.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec10.5.pdf>)
- Lecture 11: [mit15_773_s24_lec11.pdf](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/mit15_773_s24_lec11.pdf>)

### Most Important Notebooks

- Structured data / heart disease: [HODL_SP24_Lec_03A_Heart_Disease_Prediction.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_03A_Heart_Disease_Prediction.ipynb>)
- Dense image baseline: [HODL_SP24_Lec_03B_Learning_an_Image_Classification_Model_from_Scratch.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_03B_Learning_an_Image_Classification_Model_from_Scratch.ipynb>)
- CNN image classification: [Copy_of_HODL_SP24_Lec_04A_A_CNN_for_Image_Classification.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/Copy_of_HODL_SP24_Lec_04A_A_CNN_for_Image_Classification.ipynb>)
- Transfer learning: [Copy_of_HODL_SP24_Lec_04B_Building_a_Handbags_Shoes_Classifier.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/Copy_of_HODL_SP24_Lec_04B_Building_a_Handbags_Shoes_Classifier.ipynb>)
- Bag-of-Words NLP: [HODL_SP24_Lec_05_Music_Genre_Classification.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_05_Music_Genre_Classification.ipynb>)
- Embeddings: [HODL_SP24_Lec_06_Word_Embeddings.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_06_Word_Embeddings.ipynb>)
- Transformers: [HODL_SP24_Lec_07_Transformers.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_07_Transformers.ipynb>)
- Hugging Face models: [HODL_SP24_Lec_08_Using_Pre_trained_Models_from_HuggingFace.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_08_Using_Pre_trained_Models_from_HuggingFace.ipynb>)
- RAG: [HODL_SP24_Lec_10_Retrieval_Augmented_Generation.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_10_Retrieval_Augmented_Generation.ipynb>)
- LoRA fine-tuning: [HODL_SP24_Lec_10_5_Finetuning_with_LORA.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_10_5_Finetuning_with_LORA.ipynb>)
- Stable Diffusion: [HODL_SP24_Lec_11_Stable_Diffusion.ipynb](</Users/krishna/Downloads/personal/AI learning/mit-15773-deep-learning/HODL_SP24_Lec_11_Stable_Diffusion.ipynb>)

### Best Revision Order

```text
1. Cheatsheet
2. Detailed Hinglish Notes
3. Lecture PDF
4. Matching notebook
5. Backprop PDF again before exam
```

### Last-Minute Priority

- If time is `30 mins`: cheatsheet + final revision section
- If time is `2 hours`: cheatsheet + detailed notes recall answers
- If time is `1 day`: full notes + selected PDFs + key notebooks

### External Links Mentioned in MIT Slides

#### Common MIT OCW Links

- MIT OCW home: `https://ocw.mit.edu`
- MIT OCW fair use FAQ: `https://ocw.mit.edu/help/faq-fair-use`
- MIT OCW terms: `https://ocw.mit.edu/terms`

#### Lecture 1 Links

- `https://arxiv.org/pdf/1512.03385.pdf`
- `https://dwfritz.com/smart-cosmetic-defect-detection-increases-productivity/`
- `https://en.wikipedia.org/wiki/Artificial_neural_network`
- `https://google-research.github.io/seanet/musiclm/examples/`
- `https://huggingface.co/spaces/nielsr/comparing-captioning-models`
- `https://magazine.sebastianraschka.com/p/ai-and-open-source-in-2023`
- `https://mpost.io/best-100-stable-diffusion-prompts-the-most-beautiful-ai-text-to-image-prompts/`
- `https://spectrum.ieee.org/dartmouth-ai-workshop`
- `https://twitter.com/petergyang/status/1707169696049668472`
- `https://www.swarovskioptik.com/us/en/hunting/products/binoculars/ax-visio`

#### Lecture 2 Links

- `https://arxiv.org/pdf/1712.09913.pdf`
- `https://en.wikipedia.org/wiki/Augustin-Louis_Cauchy`
- `https://kenndanielso.github.io/mlrefined/blog_posts/6_First_order_methods/6_4_Gradient_descent.html`

#### Lecture 3B Links

- `https://www.kaggle.com/datasets/zalando-research/fashionmnist`

#### Lecture 4 Links

- `https://arxiv.org/abs/1512.03385`
- `https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf`
- `https://cs231n.github.io/convolutional-networks/#conv`
- `https://huggingface.co/models`
- `https://pytorch.org/hub/`
- `https://setosa.io/ev/image-kernels/`
- `https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53`
- `https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1492032646`
- `https://www.kaggle.com/datasets/zalando-research/fashionmnist`
- `https://www.slideshare.net/xavigiro/image-classification-on-imagenet-d1l4-2017-upc-deep-learningfor-computer-vision/`
- `https://www.tensorflow.org/hub`

#### Lecture 5 Links

- `https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard`
- `https://www.anthropic.com/index/introducing-claude`
- `https://www.salesforce.com/news/press-releases/2023/03/07/einstein-generative-ai/`

#### Lecture 6 Links

- `https://nlp.stanford.edu/pubs/glove.pdf`
- `https://txt.cohere.com/sentence-word-embeddings/`

#### Lecture 7 Links

- `https://aclanthology.org/H90-1021/`
- `https://arxiv.org/abs/1706.03762`
- `https://blog.google/products/search/search-language-understanding-bert/`

#### Lecture 8 Links

- `http://arxiv.org/abs/2002.05709`
- `http://arxiv.org/abs/2012.06678`
- `https://arxiv.org/abs/1512.03385`
- `https://arxiv.org/abs/1706.03762`
- `https://arxiv.org/pdf/1706.03762.pdf`
- `https://arxiv.org/pdf/1810.04805.pdf`
- `https://arxiv.org/pdf/2010.11929.pdf`
- `https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf`
- `https://huggingface.co/models`
- `https://jalammar.github.io/illustrated-bert/`
- `https://keras.io/api/layers/normalization_layers/layer_normalization/`
- `https://www.sbert.net/index.html`

#### Lecture 9 Links

- `http://arxiv.org/abs/2005.14165`
- `https://arxiv.org/abs/1706.03762`
- `https://jaykmody.com/blog/gpt-from-scratch/`
- `https://observablehq.com/@simonw/gpt-tokenizer`
- `https://platform.openai.com/playground?mode=complete`
- `https://www.borealisai.com/research-blogs/tutorial6-neural-natural-language-generation-decoding-algorithms/`
- `https://www.youtube.com/watch?v=kCc8FmEb1nY`

#### Lecture 10 Links

- `http://arxiv.org/abs/2005.14165`
- `http://arxiv.org/abs/2009.01325`
- `http://arxiv.org/abs/2203.02155`
- `http://arxiv.org/abs/2205.11916`
- `https://arxiv.org/abs/2401.14423`
- `https://arxiv.org/pdf/2309.03409.pdf`
- `https://llama.meta.com/llama2`
- `https://magazine.sebastianraschka.com/p/finetuning-large-language-models`
- `https://openai.com/blog/ChatGPT/`
- `https://openai.com/blog/instruction-following/`
- `https://twitter.com/benjedwards/status/1644032568772161545?s=20`
- `https://twitter.com/karpathy/status/1655994367033884672?s=20`
- `https://twitter.com/quasimondo/status/1284509525500989445`
- `https://www.linkedin.com/feed/update/urn:li:activity:7150937271251136514/`
- `https://www.technologyreview.com/2023/02/08/1068068/ChatGPT-is-everywhere-heres-where-it-came-from/`
- `https://www.wayfair.com/furniture/pdp/latitude-run-alori-task-chair-w005270016.html`

#### Lecture 10.5 Links

- `https://llama.meta.com/llama2`
- `https://twitter.com/karpathy/status/1655994367033884672?s=20`

#### Lecture 11 Links

- `https://arxiv.org/abs/2006.11239`
- `https://arxiv.org/abs/2112.10752`
- `https://arxiv.org/pdf/1503.03585.pdf`
- `https://arxiv.org/pdf/2103.00020.pdf`
- `https://en.wikipedia.org/wiki/Rotunda_%28architecture%29`
- `https://huggingface.co/docs/diffusers/index`
- `https://lexica.art/`
- `https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net`
- `https://mspoweruser.com/best-midjourney-prompts/`
- `https://openai.com/research/video-generation-models-as-world-simulators`
- `https://openai.com/sora`
- `https://www.nytimes.com/2023/01/09/science/artificial-intelligence-proteins.html`
