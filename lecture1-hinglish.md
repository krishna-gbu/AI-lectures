# CME 295: Transformers & Large Language Models — Lecture 1 (Hinglish)
### Stanford | Afshine Amidi & Shervine Amidi

---

## Lecture Ka Overview (Slides 1-2)

**Slide 1:** Title slide. Course ka naam `CME 295: Transformers & Large Language Models`, ye `Lecture 1` hai by Afshine Amidi aur Shervine Amidi. Stanford ICME department.

**Slide 2:** Lecture ke topics list kiye gaye:
- NLP overview
- Tokenization
- Word representation
- **RNNs**
- Self-attention mechanism
- Transformer architecture
- End-to-end example

---

## PART 1: NLP Overview (Slides 3-8)

**Slide 3:** Section divider. Topic: **NLP overview**.

---

### 1.1 NLP Kya Hai?

**Slide 4:** **NLP = Natural Language Processing** introduce kiya gaya. NLP ka goal hai ki computers human language ko samjhein, process karein aur generate karein.

> **Example:** Jab tum Google pe "weather today" type karte ho, ya Alexa se "gaana bajao" bolte ho — wo sab NLP hai!

**Slide 5:** NLP ke common tasks list kiye gaye:
- **Text classification** — spam detection, sentiment analysis
- **Named Entity Recognition (NER)** — entities identify karna (names, places)
- **Machine Translation** — ek language se doosri mein
- **Question Answering** — sawaal ka jawab dhundhna
- **Text Generation** — naya text likhna

> **Example:** "Ye movie bekar thi" → Sentiment = Negative. "Narendra Modi ne Delhi mein speech di" → NER: Person = Narendra Modi, Location = Delhi.

**Slide 6:** NLP ka evolution dikhaya gaya — rule-based systems se statistical methods, phir deep learning tak ka safar.

**Slide 7:** Modern NLP ka core building block: **Transformer architecture** (2017). Iske baad sab badal gaya — BERT, GPT, aur saare modern LLMs isi par based hain.

**Slide 8:** Key insight: Language **sequential** hai — words ka order matter karta hai. "Dog bites man" aur "Man bites dog" mein same words hain lekin matlab alag hai!

> **Example:** "Maine usse maara" vs "Usne mujhe maara" — order badla, matlab badla!

---

## PART 2: Tokenization (Slides 9-16)

**Slide 9:** Section divider. Topic: **Tokenization**.

---

### 2.1 Tokenization Kya Hai?

**Slide 10:** Text ko chhote pieces (tokens) mein todna = **Tokenization**. Ye NLP pipeline ka pehla step hai.

> **Example:** "A cute teddy bear is reading" → ["A", "cute", "teddy bear", "is", "reading"]

**Slide 11:** Different tokenization strategies:
- **Word-level:** Har word ek token
- **Character-level:** Har character ek token
- **Subword-level:** Words ko meaningful subparts mein todo

> **Example Subword:** "unbelievable" → ["un", "##believ", "##able"]

**Slide 12:** **Subword tokenization** aajkal sabse popular hai. Kyunki:
- Vocabulary size manageable rehta hai
- Unknown words handle ho jaate hain (OOV problem solve)
- Rare words bhi subword pieces se represent ho sakte hain

> **Example:** Agar vocabulary mein "playing" nahi hai, toh "play" + "##ing" se kaam chal jaayega!

**Slide 13:** Common tokenization algorithms:
- **BPE (Byte Pair Encoding)** — GPT series mein use hota hai
- **WordPiece** — BERT mein use hota hai
- **SentencePiece** — T5, multilingual models mein

**Slide 14:** BPE algorithm ka basic idea: sabse frequent character pairs ko repeatedly merge karo jab tak desired vocabulary size na mil jaaye.

> **Example:** Corpus: "low lower lowest"
> - Start: individual characters ["l", "o", "w", "e", "r", "s", "t"]
> - Merge 1: "l" + "o" → "lo" (sabse frequent pair)
> - Merge 2: "lo" + "w" → "low"
> - Continue...

**Slide 15:** Special tokens introduce kiye gaye:
- `[BOS]` / `<s>` — Beginning of Sequence
- `[EOS]` / `</s>` — End of Sequence
- `[PAD]` — Padding token (fixed length ke liye)
- `[UNK]` — Unknown token

> **Example:** "Hello world" → `[BOS] Hello world [EOS] [PAD] [PAD]`

**Slide 16:** Vocabulary size ka trade-off:
- **Chhoti vocabulary** → zyada tokens per sentence, slow processing
- **Badi vocabulary** → kam tokens but zyada memory, rare words better covered

---

## PART 3: Word Representation (Slides 17-34)

**Slide 17:** Section divider. Topic: **Word representation**.

---

### 3.1 Token Representations — Motivation

**Slide 18:** Core problem: computers numbers samajhte hain, words nahi. Toh words ko numbers mein convert karna padega.

**Slide 19:** **Naive approach: One-hot encoding.** Har word ko ek vector dena jismein sirf ek position par 1 ho, baaki sab 0.

> **Example:** Vocabulary = {teddy bear, soft, book}
> - teddy bear = [1, 0, 0]
> - soft = [0, 1, 0]
> - book = [0, 0, 1]

**Problem:**
- `<teddy bear, book>` = 0 (dot product)
- `<teddy bear, soft>` = 0
- Saare words equally distant hain! "Soft" aur "teddy bear" ka koi relation nahi dikhta.

**Slide 20:** **Better approach: Learned embeddings.** Words ko dense vectors mein represent karo jahan similar words similar vectors mein hon.

> **Example:** Learned embeddings ke baad:
> - soft = [0.95, 0.32, 0.01]
> - `<teddy bear, book>` ~ 0 (still unrelated)
> - `<teddy bear, soft>` ~ 1 (related words close!)

---

### 3.2 Word2vec

**Slide 21:** **Word2vec** introduce hota hai:
- Neural network with a **proxy task** over billions of words
- Learns an **embedding layer**
- Proxy tasks: **CBOW** aur **Skip-gram**

**Slide 22:** **Proxy Tasks:**
- **CBOW (Continuous Bag of Words):** Surrounding words se center word predict karo
  - Context: "...A **cute** teddy bear **is** **reading**..." → Predict: "teddy bear"
- **Skip-gram:** Center word se surrounding words predict karo
  - Input: "teddy bear" → Predict: "A", "cute", "is", "reading"

> **Example CBOW:** "Maine ___ khaya" — "Maine" aur "khaya" se beech ka word guess karo → "khaana"
> **Example Skip-gram:** "khaana" diya → predict karo ki aas-paas "Maine", "khaya" hain

**Slide 23:** Word2vec **Architecture:**
- Input layer: size V (vocabulary size, one-hot)
- Hidden layer: size d (embedding dimension — typically 100-300)
- Output layer: size V

> **Example:** V = 10,000 words, d = 300
> - Input: one-hot vector [0,0,...,1,...,0] (size 10,000)
> - Hidden: dense embedding [0.2, 0.9, ...] (size 300)
> - Output: probability distribution over 10,000 words

---

### 3.3 Word2vec Example — Predicting Next Word (Step-by-Step)

**Slides 24-30:** Word "A" se "cute" predict karna:

**Slide 24:** Input word = "A", Target = predict "cute"

**Slide 25:** "A" ka one-hot vector input mein jaata hai: `[1,0,0,0,0,0]`

**Slide 26:** Hidden layer mein dense representation ban jaati hai: `[0.2, 0.9]`

**Slide 27:** Output layer probability distribution deti hai: `[0.2, 0.4, 0.1, 0.1, 0.1, 0.1]`
- Position 2 (cute) par probability sabse zyada = 0.4 (red highlight)

> **Example:** Network ne seekh liya ki "A" ke baad "cute" aane ki probability sabse zyada hai!

**Slides 28-30:** Ab "cute" input hai, "teddy bear" predict karna hai:

**Slide 28:** Input word = "cute", one-hot = `[0,1,0,0,0,0]`

**Slide 29:** Hidden layer: `[0.8, 0.4]`

**Slide 30:** Output: `[0.2, 0.2, 0.2, 0.1, 0.2, 0.1]` — "teddy bear" (position 4) par 0.2 highlighted

**Slides 31-32:** Similarly "is" aur "reading" ke liye bhi same process — har word apne context se predict hota hai.

---

### 3.4 Word2vec Ka Result — Embedding Space

**Slide 33:** Training ke baad kya milta hai? Ek **embedding space** jahan:
- Similar words **close** hote hain
- Unrelated words **door** hote hain

> **Example:** "teddy bear" aur "soft" ka embedding close hoga.
> "Persian poetry" aur "art" close honge.
> Lekin "teddy bear" aur "Persian poetry" door honge.

**Slide 34:** Famous Word2vec relationships:
- king - man + woman ≈ queen
- Paris - France + Italy ≈ Rome

> **Example Hindi:** raja - aadmi + aurat ≈ rani!

**Reference:** Mikolov et al., 2013 — "Efficient Estimation of Word Representations in Vector Space"

---

## PART 4: Recurrent Neural Networks — RNNs (Slides 35-56)

**Slide 35:** Section divider. Topic: **RNNs** (bold, current topic).

---

### 4.1 RNN Overview

**Slide 36:** **RNN = Recurrent Neural Network**
- Pehli baar 1980s mein introduce hui
- Neural networks ka ek class jahan connections **temporal sequence** banate hain
- General form: input `x<t>` aata hai, hidden state `a<t>` update hota hai, output `y<t>` nikalta hai

> **Example:** Socho ek conveyor belt par ek-ek karke words aa rahe hain. Har word par machine apni "memory" (hidden state) update karti hai aur prediction deti hai.

---

### 4.2 RNN Step-by-Step Example

**Slides 37-48:** "A cute teddy bear is reading" sentence par RNN ka step-by-step walkthrough:

**Slide 37:** Starting position — sirf "A" token hai

**Slide 38:** "A" RNN cell mein jaata hai, cell process karta hai

**Slide 39:** Cell output deta hai: predicts "cute". Hidden state aage pass hota hai.

**Slide 40:** Ab "cute" input aata hai, pichla hidden state bhi milta hai

**Slide 41:** RNN cell "cute" aur previous memory dono use karke process karta hai

**Slide 42:** Output: predicts "teddy bear". Hidden state phir aage pass.

**Slide 43-44:** "teddy bear" aata hai → predict "is"

**Slide 45-46:** "is" aata hai → predict "reading"

**Slide 47:** Poora sequence unfold hota hai — har step par input + previous hidden state = new output + new hidden state

**Slide 48:** Final unfolded RNN:
```
A → [RNN] → cute
cute → [RNN] → teddy bear
teddy bear → [RNN] → is
is → [RNN] → reading
```
Har cell same weights share karta hai, lekin hidden state carry forward hota hai!

> **Example:** Jaise tum ek story sun rahe ho — har sentence ke baad tumhare brain mein ek "summary" ban jaata hai. Naya sentence aata hai toh purana summary + naya input = updated summary. Yehi RNN ka hidden state hai!

---

### 4.3 RNN Ke Use Cases

**Slide 49:** Teen main categories:

| Type | Input → Output | Example |
|------|---------------|---------|
| **Classification** | Many → One | Sentiment analysis: "I love it" → Positive (3/5) |
| **Multi-classification** | Many → Many (same length) | POS tagging: har word ka tag |
| **Generation** | Many → Many (different length) | Translation: English → French |

> **Example Hindi:**
> - Classification: "Ye bahut accha tha" → Positive
> - Tagging: "Maine/Pronoun khaana/Noun khaya/Verb"
> - Translation: "I love you" → "Main tumse pyaar karta hoon"

**Reference:** VIP Cheatsheets for CS 230, Amidi.

---

### 4.4 LSTM — Long Short-Term Memory

**Slide 50:** **LSTM** introduce hota hai:
- 1997 mein introduce hua (Hochreiter & Schmidhuber)
- RNN ka advanced version — **structured hidden state** ke saath
- **4 gates** hain:
  - `Gamma_f` — **Forget gate** (kya bhoolna hai)
  - `Gamma_u` — **Update gate** (kya naya add karna hai)
  - `Gamma_r` — **Reset/Relevance gate**
  - `Gamma_o` — **Output gate** (kya output mein dena hai)

- **Cell state `c<t>`** alag se flow karti hai — ye long-term memory hai
- **Hidden state `a<t>`** short-term memory hai

> **Example:** Socho tumhare paas ek notebook (cell state) hai aur ek whiteboard (hidden state).
> - Forget gate: purane notes mein se kuch mita do
> - Update gate: naye notes add karo
> - Output gate: whiteboard par sirf relevant cheezein likho
> LSTM isliye achha hai kyunki wo long-term information preserve kar sakta hai!

**Reference:** Hochreiter & Schmidhuber, 1997 — "Long Short-Term Memory"

---

### 4.5 Methods Ka Summary — Word2vec vs RNN

**Slide 51:** Comparison table:

| Method | Pros | Cons |
|--------|------|------|
| **Word2vec** (CBOW, Skip-gram) | Very simple yet powerful; Intuitive embeddings | Word order nahi matter karta; Embeddings context-aware nahi hain |
| **RNNs** (traditional RNN, LSTM) | Word order matters; State-of-the-art results | **Vanishing gradient problem**; Slow computations |

> **Example Vanishing Gradient:** Agar sentence bahut lamba hai — "The cat, which sat on the mat and looked at the bird that was flying over the tall building near the river, **was** sleeping" — yahan "cat" aur "was" bahut door hain. RNN ko itni door ki dependency yaad rakhna mushkil hai kyunki gradients training mein shrink ho jaate hain.

> **Example Context Problem:** Word2vec mein "bank" ka embedding same hai chahe "river bank" ho ya "money bank". RNN context use kar sakta hai!

---

## PART 5: History of Attention (Slides 52-57)

**Slide 52:** **Attention** ka history:
- 2014 mein introduce hua
- Translation tasks mein **long-term dependencies** ka real issue tha
- Seq2seq models lambi sequences "remember" nahi kar paate the

> **Example:** "A cute teddy bear is reading" ko French mein translate karna hai: "Un ours en peluche mignon lit"

**Slide 53:** Seq2seq model dikhaya gaya — encoder (green) English words process karta hai, decoder (blue) French words generate karta hai. Problem: encoder ka last hidden state mein poori sentence ki information compress karni padti hai!

**Slide 54:** **Attention mechanism** ka solution: decoder ko **directly encoder ke saare hidden states** dekhne do, sirf last wala nahi!
- Green arrows dikhate hain ki "?" predict karte waqt decoder "reading", "teddy bear" wagairah ko directly attend kar sakta hai

> **Example:** French word "lit" (reads) predict karte waqt model directly "reading" ko attend karega — 5 words peeche ki information bhi accessible hai!

**Slide 55:** Final translation complete: "Un ours en peluche mignon **lit**"

> **Example Hindi:** "Ek pyaara teddy bear padh raha hai" translate karte waqt "padh" word ke liye model seedha "reading" ko dekhega — beech ke saare words skip karke!

**Reference:** Bahdanau et al., 2014 — "Neural Machine Translation by Jointly Learning to Align and Translate"

---

## PART 6: Self-Attention Mechanism (Slides 58-68)

**Slide 58:** Section divider. Topic: **Self-attention mechanism** (bold, current topic).

---

### 6.1 Overview of the Transformer

**Slide 59:** **Transformer** introduce hota hai:
- 2017 paper **"Attention is All You Need"** mein introduce hua
- **Self-attention** mechanism par rely karta hai
- Machine translation tasks par state-of-the-art results

**Slide 60:** Sentence "a cute teddy bear is reading ." dikhaya gaya. Token `teddy bear` highlight hai.

**Slide 61:** Self-attention ka core idea: **har token apne sentence ke saare tokens ko dekhta hai** apni representation banane ke liye.
- `teddy bear` neeche hai, upar se saare tokens (`a`, `cute`, `teddy bear`, `is`, `reading`, `.`) ki information aati hai

> **Example:** "Teddy bear" apna matlab samajhne ke liye "cute", "reading" wagairah sabse context leta hai.

---

### 6.2 Attention Mechanism — Query, Key, Value

**Slide 62:** **Q, K, V** concept introduce hota hai:
- **Query (Q):** "Main kya dhundh raha hoon?" — current token ka sawaal
- **Key (K):** "Mere paas kya hai?" — har token ka label/tag
- **Value (V):** "Mere paas actual information kya hai?" — har token ka content

**Slide 63:** `teddy bear` token ka query `q_teddy bear` banta hai.

**Slide 64:** Query sabhi tokens ke keys `k_a^T, k_cute^T, k_teddy bear^T, k_is^T, k_reading^T, k_.^T` ke saath match hota hai (dot product).

**Slide 65:** Values `v_a, v_cute, v_teddy bear, v_is, v_reading, v_.` bhi dikhaye gaye. Final output = weighted sum of values, jahan weights query-key similarity se aate hain.

> **Example:** Library mein jaake socho:
> - **Query** = tumhara sawaal ("mujhe ML ki book chahiye")
> - **Key** = har book ka title/tag
> - **Value** = book ka actual content
> - Matching: query aur keys ka dot product → sabse relevant book ko sabse zyada weight milega!

---

### 6.3 Attention Formula

**Slide 66:** Efficient matrix computation ka formula:
```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) × V
```

**Slide 67:** Formula ke saath **Scaled Dot-Product Attention** aur **Multi-Head Attention** dono diagrams dikhaye gaye (original paper se):
- Left: MatMul → Scale → Mask (optional) → SoftMax → MatMul
- Right: Multiple heads parallel, phir Concat → Linear

> **Example:** d_k = 64 ho toh sqrt(64) = 8 se divide karte hain. Bina scaling ke dot products bahut bade ho sakte hain aur softmax saturate ho jaayega — matlab ek token ko 99.9% weight mil jaayega aur baaki sabko 0.

**Reference:** Vaswani et al., 2017 — "Attention Is All You Need"

---

## PART 7: Transformer Architecture (Slides 69-81)

**Slide 69:** Section divider. Topic: **Transformer architecture** (bold, current topic).

---

### 7.1 Architecture Overview

**Slide 70:** Full transformer architecture diagram dikhaya gaya. Components:

**Attention layer (MHA):**
- Self-attention (Encoder-Encoder, Decoder-Decoder)
- Encoder-Decoder attention layer

**Feed Forward Neural Network (FFNN)**

**Positional Encoding (PE)**

> **Example:** Transformer = ek factory. Raw materials (tokens) aate hain → Encoding section (encoder) mein process hote hain → Manufacturing section (decoder) mein final product banta hai.

---

### 7.2 Input

**Slide 71:** **Input layer:**
- Text is "tokenized"
- **Learned embeddings** for tokens
- Parameters: V (vocabulary size), d_model (embedding dimensions)

> **Example:** "A cute teddy bear is reading." → tokenize → har token ko d_model = 512 dimension ka vector milta hai

---

### 7.3 Positional Encoding

**Slide 72:** **Positional encoding** — ek trick!
- **Position information** inputs mein add karo
- Learned ya hardcoded (sinusoidal) ho sakta hai
- Goal: model ko relative input position samjhana

Two heatmaps dikhaye gaye:
- Left: Embedding values (sin/cos patterns)
- Right: Position similarity (dot product matrix)

> **Example:** Bina positional encoding ke "I love you" aur "you love I" same lagenge! Position info add karne se model ko pata chalega ki "I" pehle hai aur "you" baad mein.

**Reference:** Vaswani et al., 2017 & Kazemnejad, 2019

---

### 7.4 Encoder

**Slide 73:** **Encoder** ka structure:
- Encoder-Encoder attention / **self-attention**
- Feed Forward Neural Network
- Normalization layer (Add & Norm)
- Parameters: N (layers stacked), h (attention heads), d_FF, d_key, d_value, d_model

> **Example:** N = 6 layers, h = 8 heads, d_model = 512. Matlab 6 encoder layers stack honge, har layer mein 8 parallel attention heads honge.

---

### 7.5 Output "Shifted Right"

**Slide 74:** **Decoder input** — "shifted right":
- Learned embeddings for output tokens
- Practice mein `[BOS]` token se start hota hai during translation
- Parameters: V, d_model

> **Example:** Translation: "A cute teddy bear" → "[BOS] Un ours en peluche mignon"
> Decoder ko pehle [BOS] milta hai, phir wo step-by-step generate karta hai.

---

### 7.6 Decoder

**Slide 75:** **Decoder** ka structure:
- **Decoder-Decoder attention** / self-attention (masked — future tokens nahi dekh sakta!)
- **Encoder-Decoder attention** (encoder ki output attend karta hai)
- Feed Forward Neural Network
- Normalization layer
- Parameters: N, h, d_FF, d_key, d_value, d_model

> **Example:** French word "mignon" generate karte waqt decoder sirf "Un", "ours", "en", "peluche" ko dekh sakta hai (mask lagta hai future pe). Par encoder side se poora English sentence attend kar sakta hai!

---

### 7.7 Output

**Slide 76:** Final output layer:
- **Linear projection** (decoder output ko vocabulary size tak project karo)
- **Softmax** — probability distribution over vocabulary
- Classification problem: har position par "next word kya hoga?" predict karo

> **Example:** Decoder ke baad vector aata hai → Linear layer → Softmax → [0.001, 0.0003, ..., **0.4**, ..., 0.002] → Word with highest probability = "Un"

---

### 7.8 Computational Tricks

**Slide 77:** **Multi-head attention:**
- Multiple self-attention layers **parallel** mein chalo
- Har head alag pattern seekhta hai
- CNN ke multiple filters jaisa concept

> **Example:** Head 1 grammar relationships dekhta hai, Head 2 semantic similarity, Head 3 position patterns. Sab milkar rich representation banate hain.

**Slide 78:** **Label smoothing:**
- Overconfidence bad hai (2015 vision paper)
- True labels mein **noise** introduce karo:
```
q(k|x) = delta_{k,y}  →  q'(k|x) = (1 - epsilon) × delta_{k,y} + epsilon × u(k)
```
- Benefits: overfitting prevent, accuracy aur BLEU score improve

> **Example:** Hard label: [1, 0, 0, 0] (100% sure "cat")
> Smoothed: [0.9, 0.033, 0.033, 0.033] (90% sure, thoda uncertainty)
> Ye model ko zyada robust banata hai!

---

## PART 8: End-to-End Example — Translation (Slides 82-135)

**Slide 82:** Section divider. Topic: **End-to-end example** (bold).

---

### 8.1 Input Processing

**Slide 83:** Raw sentence: `A cute teddy bear is reading.`

**Slide 84:** Tokenization:
```
["A", "cute", "teddy bear", "is", "reading", "."]
```

**Slide 85:** Special tokens add:
```
["[BOS]", "A", "cute", "teddy bear", "is", "reading", ".", "[EOS]"]
```

**Slide 86:** `[BOS]` highlight — sequence ka starting token.

---

### 8.2 Embedding Generation

**Slide 87:** Har token ka **embedding** vector generate hota hai (lookup table se).

**Slide 88:** **Position embedding** add hota hai — har position ka unique vector.

**Slide 89-90:** Token embedding + Position embedding = **position-aware embedding**.

**Slide 91:** Saare tokens ke position-aware embeddings ready.

**Slide 92:** Sab embeddings milkar **position-aware embeddings matrix** ban jaata hai.

**Slide 93:** Matrix compact form mein — ye encoder ka input hai.

---

### 8.3 Encoder Processing

**Slide 94:** Encoder block dikhaya gaya — position-aware embeddings matrix encoder mein jaata hai.

**Slide 95:** Encoder ke andar **Wq, Wk, Wv** weight matrices dikhaye gaye — ye Q, K, V banane ke liye hain.

**Slide 96:** Q (Query), K (Key), V (Value) matrices generate hote hain:
```
Q = Embeddings × Wq
K = Embeddings × Wk
V = Embeddings × Wv
```

**Slide 97:** Attention formula apply hota hai:
```
softmax(QK^T / sqrt(d_k)) × V
```
Result ek output matrix hai.

**Slide 98:** **PAUSE** — yahan ruk ke samjho ki kya ho raha hai!

---

### 8.4 Attention Ka Matrix Walkthrough

**Slide 99:** **Q matrix** dikhaya gaya — har row ek token ka query vector hai:
```
[BOS], A, cute, teddy bear, is, reading, ., [EOS]
```

**Slide 100-101:** **K^T matrix** dikhaya gaya — K ka transpose. Q × K^T karne par har query har key ke saath interact karega.

**Slide 102:** **QK^T** matrix — attention scores:
```
<q_[BOS], k_[BOS]>   <q_[BOS], k_A>   <q_[BOS], k_cute>  ...
<q_A, k_[BOS]>       <q_A, k_A>       ...
<q_cute, k_[BOS]>    ...              ...
...                   ...              ...
```
Har cell = query-key dot product = similarity score.

**Slide 103:** **V matrix** bhi dikhaya gaya — har row ek token ka value vector.

**Slide 104:** **QK^T × V** ka result:
```
Row 1: <q_[BOS], k_[BOS]> × v_[BOS] + <q_[BOS], k_A> × v_A + <q_[BOS], k_cute> × v_cute + ...
Row 2: <q_A, k_[BOS]> × v_[BOS] + <q_A, k_A> × v_A + ...
```
Har row = ek token ka **weighted average of all values**, jahan weights similarity scores hain!

**Slide 105:** Final insight:
```
softmax(QK^T / sqrt(d_k)) × V = weighted average of values
```
Weights **query-key similarity** `<q, k>` ka function hain.

> **Example:** Token "reading" ka query sabse zyada "teddy bear" ki key ke saath match kare, toh "teddy bear" ka value zyada contribute karega "reading" ki final representation mein!

---

### 8.5 Multi-Head Attention in Encoder

**Slides 106-109:** Encoder mein pehle single-head attention dikhaya, phir:
- **h times** repeat — h parallel attention heads
- Har head ke alag Wq, Wk, Wv
- Outputs concat karke **Wo** se multiply

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) × Wo
```

> **Example:** 8 heads hain toh 8 alag-alag perspectives se sentence ko dekhte hain. Ek head syntax dekhta hai, ek semantics, ek proximity — phir sab combine!

---

### 8.6 Feed Forward Network + Final Encoder Output

**Slides 110-111:** Self-attention ke baad **Feed Forward Network** aata hai. Encoder ka final structure:
```
Input → Self-Attention Layer → Add & Norm → FFN → Add & Norm → Output
```

**Slide 112:** Output = **context-aware encoded embeddings** — har token ki representation ab poore sentence ka context carry karti hai!

**Slide 113-114:** Encoder block complete dikhaya gaya. Multiple layers (N times) stack honge.

> **Example:** Input "teddy bear" ka embedding pehle sirf "teddy bear" ki dictionary meaning tha. Encoder ke baad ye embedding "cute teddy bear jo reading kar raha hai" ka poora context carry karti hai!

---

### 8.7 Decoder Processing

**Slide 115:** Encoder complete, ab **decoder** start hota hai. Encoded embeddings encoder se aati hain. Decoder ko `[BOS]` token milta hai.

**Slide 116-117:** Decoder ke andar:
1. **Self-attention layer** (masked — sirf past tokens dekh sakta hai)
2. **Encoder-Decoder attention layer** (encoder ki output attend karta hai)

**Slide 118-119:** Add & Norm layers har sublayer ke baad.

**Slide 120:** **Feed forward network** decoder mein bhi hai.

**Slide 121:** **Softmax layer** — final probability distribution over vocabulary.

**Slide 122:** Output probabilities: `[0.001, 0.0003, ..., 0.4, ..., 0.002]` — highest probability wala word = **"Un"** (French mein "A").

**Slide 123:** "Un" generate ho gaya! Ab decoder block complete dikhaya.

---

### 8.8 Autoregressive Generation

**Slide 124:** "Un" output ko decoder ke input mein add karo: `[BOS] Un`

**Slide 125:** Decoder phir se run hota hai → predicts "ours en peluche"

**Slide 126-127:** Process continue hota hai:
```
[BOS] → Un
[BOS] Un → ours en peluche
[BOS] Un ours en peluche → mignon
[BOS] Un ours en peluche mignon → lit
[BOS] Un ours en peluche mignon lit → [EOS]
```

**Slide 128:** Final result:
- Input (English): "A cute teddy bear is reading."
- Output (French): "Un ours en peluche mignon lit."

> **Example Hindi:** Agar Hindi translation hoti:
> "A cute teddy bear is reading." → "Ek pyaara teddy bear padh raha hai."
> Har step mein decoder ek word generate karta, previous words + encoder output use karke!

---

### 8.9 Complete Architecture Summary

**Slides 129-135:** Full pipeline recap with detailed encoder internals:

**Slide 129:** Encoder mein Wq, Wk, Wv → Q, K, V matrices

**Slide 130:** Q, K, V generated

**Slide 131:** Attention formula applied: `softmax(QK^T/sqrt(d_k)) × V`

**Slide 132-133:** Multi-head: h times parallel attention → concat → Wo

**Slide 134:** Self-attention layer → Add & Norm → FFN → Add & Norm → encoded embeddings

**Slide 135:** Final slide — **"Thank you for your attention!"**

---

## Summary Table

| Topic | Key Idea | Takeaway |
|-------|----------|----------|
| NLP Overview | Computers ko language samjhana | Sequential nature important |
| Tokenization | Text → tokens | Subword (BPE/WordPiece) preferred |
| Word Representation | Words → numbers | One-hot bad, learned embeddings good |
| Word2vec | Proxy task se embeddings seekho | CBOW & Skip-gram |
| RNNs | Sequential processing with memory | Vanishing gradient problem |
| LSTM | RNN + gates for long-term memory | Forget, Update, Output gates |
| Attention | Directly relevant parts attend karo | Seq2seq bottleneck solve |
| Self-Attention | Har token sabko dekhe | Q, K, V framework |
| Transformer | Self-attention + FFN + PE | Encoder-Decoder architecture |
| Multi-Head | Parallel attention perspectives | Richer representations |

---

## Key Papers Referenced:

1. **"Attention Is All You Need"** — Vaswani et al., 2017 (Transformer)
2. **"Efficient Estimation of Word Representations in Vector Space"** — Mikolov et al., 2013 (Word2vec)
3. **"Neural Machine Translation by Jointly Learning to Align and Translate"** — Bahdanau et al., 2014 (Attention)
4. **"Long Short-Term Memory"** — Hochreiter & Schmidhuber, 1997 (LSTM)
5. **"Transformer Architecture: The Positional Encoding"** — Kazemnejad, 2019
6. **"VIP Cheatsheets for Stanford's CS 230"** — Amidi (RNN figures)
7. **"Super Study Guide: Transformers & Large Language Models"** — Amidi, 2024

---

*Stanford CME 295 Lecture 1 — All 135 slides covered in Hinglish with slide numbers, examples, aur formulas.*
