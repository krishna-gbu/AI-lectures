# CME 295: Transformers & Large Language Models - Lecture 4 (Hinglish)
### Stanford | Afshine Amidi & Shervine Amidi

---

## Logistics (Slides 1-3)

**Slide 1:** Title slide hai. Course ka naam `CME 295: Transformers & Large Language Models`, ye `Lecture 4` hai by Afshine Amidi aur Shervine Amidi.

**Slide 2:** Midterm logistics di gayi:
- **Date:** Friday, October 24, 2025
- **Time:** 3:30 PM - 5:00 PM
- **Duration:** 1 hour 30 minutes
- **Location:** Thornton 110
- **Coverage:** Lectures 1, 2, 3, and 4

**Slide 3:** Final exam logistics di gayi:
- **Date:** Wednesday, December 10, 2025
- **Time:** 7:00 PM - 8:30 PM
- **Duration:** 1 hour 30 minutes
- **Location:** Hewlett Teaching Center 201
- **Coverage:** Lectures 5, 6, 7, 8, and 9

---

## Pichle Lecture Ka Recap (Slides 4-7)

**Slide 4:** "Recap of last episode..." se lecture ka recap start hota hai.

**Slide 5:** Pichle lecture ka MoE reminder dikhaya gaya:
- `G` = router / gate
- `FFNN1, FFNN2, ..., FFNNn` = experts
- Token ko selective experts ke paas bheja ja sakta hai

**Slide 6:** Same MoE recap ko transformer context ke andar reinforce kiya gaya. Point yeh hai ki large model ke saare weights ek hi token ke liye use karna zaroori nahi.

**Slide 7:** Previous lecture ki inference optimization techniques quickly list ki gayi:
- `KV cache`
- `PagedAttention`
- `Speculative decoding`
- `GQA`
- `Multi-head latent attention`
- `Multi-token prediction`

> **Takeaway:** Lecture 3 mostly inference-time efficiency aur modern LLM serving tricks par focused tha.

---

## Lecture Ka Overview (Slide 8)

**Slide 8:** Aaj ke lecture ke main topics list kiye gaye:
- Pretraining
- Training optimizations
- Supervised finetuning
- Parameter-efficient finetuning

---

## PART 1: Pretraining (Slides 9-27)

### 1.1 Paradigm Shift

**Slide 9:** Traditional machine learning paradigm dikhaya gaya:
> Har task ke liye alag model scratch se train karo.

Examples:
- Spam detection model
- Sentiment extraction model
- Translation model

**Slide 10:** Transfer learning ka idea introduce hua:
> Ek trained model ki knowledge ko dusre task ke liye reuse kiya ja sakta hai.

**Slide 11:** LLM training paradigm define hua:
> Pehle model ko language samajhna sikhao, phir usse specific task ke liye tune karo.

**Slide 12:** Step 1 highlight hua:
`Pretraining`

Result:
`"Pretrained" model`

**Slide 13:** Full 2-stage lifecycle dikhaya gaya:
1. **Pretraining**
2. **Tuning**

Uske baad same pretrained backbone ko multiple end tasks ke liye adapt kiya ja sakta hai.

> **Example:** Ek hi language-understanding model ko baad mein spam detection, sentiment analysis, ya translation ke liye alag se tune kiya ja sakta hai.

---

### 1.2 Pretraining Overview

**Slide 14:** Pretraining ka goal clear bola gaya:
> **Learn patterns of language and code**

Slide par mixed data dikhaya gaya:
- English prose
- Multi-lingual text
- Python / Go code

Point:
LLM sirf plain English nahi padhta; wo natural language + code + multiple languages ke patterns absorb karta hai.

> **Example:** Model ek taraf story-like paragraph padhta hai, aur doosri taraf class definition ya function syntax bhi.

**Slide 15:** Objective function explicitly diya gaya:
> **Predict next token**

Sequence example:
```text
[BOS] A teddy bear is -> ?
```

Yehi core autoregressive pretraining objective hota hai.

**Slide 16:** Data mixtures list ki gayi:
- Web-scraped text, e.g. Common Crawl, Wikipedia
- Code data, e.g. GitHub, StackOverflow

**Slide 17:** Scale emphasize ki gayi:
- Pretraining size approx. **trillions of tokens**
- Example:
  - `GPT-3`: `300 billion` tokens
  - `LLaMA 3`: `15 trillion` tokens

> **Example intuition:** Yeh normal ML dataset scale se orders of magnitude bada hota hai. Yahan "dataset" literally internet-scale hota hai.

---

### 1.3 FLOPs, FLOPS, Scaling, and Chinchilla

**Slide 18:** Notation introduce hui:
- `FLOPs` = **Floating-point Operations**
- Yeh computation quantity ko represent karta hai

**Slide 19:** `FLOPS` ya `FLOP/s` ka distinction diya gaya:
- `FLOPs` = kitna computation hua
- `FLOPS` = प्रति second kitna computation ho raha hai

> **Example:** Agar 1 trillion operations required hain, wo `FLOPs` hua. Agar GPU 100 teraFLOPS speed par kaam kar raha hai, wo performance rate hua.

**Slide 20:** Pehla big takeaway:
`Scaling`

Meaning:
Model size, data size, aur compute scale karne se performance generally predictable way mein improve hoti hai.

**Slide 21:** Doosra takeaway:
`Sample efficiency`

Meaning:
Better-scaled models same amount of data se zyada effective learning kar sakte hain.

**Slide 22:** Teesra takeaway:
`Chinchilla law`

Practical interpretation:
> Fixed compute budget ke under sirf model ko bada karna enough nahi; data quantity aur model size ka balance important hai.

**Slide 23:** Same Chinchilla-style point reinforce hua:
- Compute-optimal training mein parameters aur training tokens ka healthy balance chahiye
- Undertrained giant model suboptimal ho sakta hai

> **Example analogy:** Sirf bada student lena enough nahi; usse padhne ke liye enough books aur enough study time bhi dena padega.

**References:**
- Kaplan et al., 2020 - "Scaling Laws for Neural Language Models"
- Hoffmann et al., 2022 - "Training Compute-Optimal Large Language Models"

---

### 1.4 Challenges of Pretraining

**Slide 24:** Cost-related challenges list kiye gaye:
- At least millions of dollars
- Bahut time lagta hai
- Environment / electricity cost high hoti hai

**Slide 25:** Learned-knowledge side ke challenges add kiye gaye:
- `Knowledge cutoff`
- Hard to edit knowledge
- `Plagiarism` concerns

**Slide 26:** Combined picture dikhaya gaya:
- Financially expensive
- Environmentally expensive
- Knowledge frozen ho sakti hai
- Mistakes ya outdated information ko directly patch karna hard hota hai

**Slide 27:** Knowledge-cutoff concern ko concrete product view se connect kiya gaya.

> **Example:** Agar model 2025 tak ke data par trained hai, toh uske baad ki events usse naturally nahi pata hongi jab tak re-training ya external retrieval use na kiya jaye.

---

## PART 2: Training Optimizations (Slides 28-81)

**Slide 28:** Section divider. Ab focus training optimizations par shift hota hai.

---

### 2.1 Setup of LLM Training

**Slide 29:** LLM training ko transformer architecture ke context mein place kiya gaya.

**Slide 30:** Same setup ko aur reinforce kiya gaya: training ke liye actual large transformer stack use hota hai.

**Slide 31:** Explicit message:
> Large-scale training needs **many GPUs**

Yeh laptop-level problem nahi hai; cluster-scale problem hai.

---

### 2.2 Memory Breakdown During Training

**Slide 32:** Training recap ka pehla step:
`Initialization`

Memory component:
- **Model parameters**
- Scale: billions se 100s of billions tak

**Slide 33:** `Forward pass`

Memory component:
- **Activations**
- Inka size depend karta hai:
  - model size
  - batch size
  - context length

**Slide 34:** `Backward pass`

Memory component:
- **Gradients**

**Slide 35:** `Weights update`

Memory component:
- **Optimizer state**
- Example: Adam optimizer additional running statistics maintain karta hai

> **Big picture:** Training memory sirf weights ki wajah se nahi jaati. Parameters + activations + gradients + optimizer state milkar total memory banate hain.

---

### 2.3 Bottleneck: Memory

**Slide 36:** GPU hardware ke context mein memory bottleneck introduce hua.

**Slide 37:** Explicit point:
> GPU memory limited hoti hai, often order of **10s of GB**

Problem:
Model aur training state us limit ko easily hit kar sakte hain.

> **Example:** Agar model weights hi dozens of GB le rahe hain, toh activations aur optimizer state ke liye jagah bahut quickly khatam ho sakti hai.

---

### 2.4 Data Parallelism

**Slide 38:** Data parallelism ka idea:
- Batch ko multiple devices mein divide karo
- Same model har device par replicate karo

**Slide 39:** Downside visible hua:
- Parameters replicate hote hain
- Gradients replicate hote hain
- Optimizer state bhi replicate hota hai

Matlab simple data parallelism easy hai, but redundant memory bahut consume karta hai.

> **Example:** 8 GPUs hain toh same model ki 8 copies memory mein baithi ho sakti hain.

---

### 2.5 ZeRO: Reducing Redundancy

**Slide 40:** `ZeRO = Zero Redundancy Optimization`

Core idea:
> Jo state sab devices par duplicate hai, use intelligently shard/share karo.

**Slide 41:** `ZeRO-1`
- Optimizer state share/shard karo

**Slide 42:** `ZeRO-2`
- Optimizer state + gradients share/shard karo

**Slide 43:** `ZeRO-3`
- Optimizer state + gradients + parameters sab shard/share karo

> **Example intuition:** Har GPU ko poora warehouse dene ke bajay, alag-alag shelves divide kar do.

**Reference:** Rajbhandari et al., 2019 - "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"

---

### 2.6 Model Parallelism

**Slide 44:** Jab model ek single device mein fit nahi hota, tab:
`Model parallelism`

Variants listed:
- **Tensor Parallelism (TP)**
- **Pipeline Parallelism (PP)**
- **Sequence Parallelism (SP)**
- **Context Parallelism (CP)**
- **Expert Parallelism (EP)**

Point:
Data parallelism batch ko split karta hai; model parallelism model computation ko split karta hai.

> **Example:** Ek bahut bada FFN ya attention block ko multiple GPUs ke beech divide karna.

---

### 2.7 FlashAttention

**Slide 45:** FlashAttention introduce hua:
> GPU ke hardware hierarchy ko use karke exact attention ko faster banana

**Slides 46-47:** GPU internals ka key memory hierarchy intuition diya gaya:
- `SRAM` = chhota but fast
- `HBM` = bada but relatively slow
- `CU` = compute unit

Core issue:
Attention ke standard implementation mein slow memory traffic bahut hota hai.

**Slide 48:** Standard self-attention computation ka context introduce hua.

**Slide 49:** Same baseline reinforce ki gayi.

**Slide 50:** Standard attention step 1:
`LOAD Q, K from HBM by blocks`

**Slide 51:** Step 2:
`Compute S`

Usually:
```text
S = QK^T
```

**Slide 52:** Step 3:
`WRITE S to HBM`

**Slide 53:** Step 4:
`READ S from HBM`

**Slide 54:** Step 5:
`Compute P`

Usually:
```text
P = softmax(S)
```

**Slide 55:** Step 6:
`WRITE P to HBM`

**Slide 56:** Step 7:
`LOAD P, V from HBM by blocks`

**Slide 57:** Step 8:
`Compute O`

Usually:
```text
O = PV
```

**Slide 58:** Step 9:
`WRITE O to HBM`

Problem:
- Full score matrix `S` materialize hota hai
- Full probability matrix `P` materialize hota hai
- HBM read/write bahut zyada hoti hai

**Slides 59-61:** FlashAttention ka pehla main idea:
> HBM read/writes minimize karo using **tiling** via SRAM

**Slide 62:** Trick:
> Full attention matrix ko softmax se pehle explicitly materialize karna zaroori nahi

**Slides 63-68:** Operational view:
- Q, K, V ke blocks SRAM mein load karo
- Output `O` ka block compute karo
- Result ko HBM mein write karo

Point:
Intermediate giant matrices avoid karke IO cost bahut kam hoti hai.

**Slides 69-70:** Backward pass ka second idea:
> Kabhi-kabhi store karne se better hota hai **recompute** karna

This is counterintuitive but important:
- more FLOPs
- less runtime

Reason:
IO bottleneck kabhi pure arithmetic se zyada expensive hota hai.

**Slide 71:** Final result:
> FlashAttention significant speedup deta hai **with exact computation**

Yeh approximate trick nahi, efficient exact implementation hai.

> **Example analogy:** Agar kitchen shelf bahut slow ho aur counter bahut fast, toh saari cheezein baar-baar shelf se lane ke bajay counter par small batches mein kaam karo.

**Reference:** Dao et al., 2022 - "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"

---

### 2.8 Numerical Precision

**Slides 72-73:** Floating-point precision motivate ki gayi. Real numbers ko computer limited precision ke saath represent karta hai.

**Slide 74:** Float representation introduce hui.

**Slide 75:** Different formats ka bit split diya gaya:

| Format | Sign | Exponent | Mantissa |
|-------|------|----------|----------|
| `FP16` | 1 | 5 | 10 |
| `FP32` | 1 | 8 | 23 |
| `FP64` | 1 | 11 | 52 |
| `BFLOAT16` | 1 | 8 | 7 |

Point:
- More bits -> more precision/range
- Fewer bits -> less memory and potentially faster compute

**Slide 76:** GPU example dikhaya gaya.

**Slide 77:** Main hardware intuition:
> **Lower precision -> faster processing**

Trade-off:
- speed up
- lower memory use
- but numerical stability risk

---

### 2.9 Mixed Precision Training

**Slide 78:** Objective:
> Training ko faster aur memory-efficient banana

**Slide 79:** Forward pass strategy:
- activations low precision mein

**Slide 80:** Backward pass strategy:
- gradient updates low precision mein

**Slide 81:** Weight update strategy:
- model weights high precision mein rakho

So mixed precision ka practical recipe:
- forward/backward mein cheap precision use karo
- master weights safer high precision mein maintain karo

> **Example:** Kaam fast pencil se karo, lekin final ledger clean ink mein maintain karo.

**Reference:** Micikevicius et al., 2017 - "Mixed Precision Training"

---

## PART 3: Supervised Finetuning and Instruction Tuning (Slides 82-104)

**Slide 82:** Section divider. Ab lecture finetuning side par move karta hai.

---

### 3.1 First-Part Recap

**Slide 83:** Pehle part ka summary dikhaya gaya:
- Initialized model
- Pretraining
- Result: model with basic knowledge about language, code, etc.

Point:
Pretraining base intelligence deta hai, but assistant behavior automatically guarantee nahi karta.

---

### 3.2 Pretrained Model Behavior

**Slide 84:** Example prompt diya gaya:
`Can I put my teddy bear in the washer?`

Pretrained model se expected helpful answer immediately nahi milta.

**Slide 85:** Pretrained model ka answer factual-sounding but not directly helpful tha:
- materials explain kar raha hai
- safety-oriented actionable answer directly nahi de raha

Point:
Pretraining knowledge deta hai, but helpfulness / instruction following separately train karni padti hai.

**Slide 86:** Remedy slide:
`Initialized model -> Pretraining -> Finetuning`

Result:
- Pretraining -> general knowledge
- Finetuning -> task-specific helpful behavior

---

### 3.3 Supervised Finetuning (SFT)

**Slide 87:** Term define hua:
`SFT = Supervised FineTuning`

Idea:
> Model ke weights ko desired behavior ke according tune karo.

Strategy:
- Desired input/output pairs collect karo
- Input ke given output ko next-token objective se train karo

**Slide 88:** Special case highlight hua:
> Instruction-following data par SFT = **Instruction tuning**

> **Example:**  
> Input: "List 3 teddy bear activities."  
> Desired output: proper bulleted helpful response

---

### 3.4 Instruction Tuning Overview

**Slide 89:** Goal:
> Model ko "graduate" karke helpful assistant banana

**Slide 90:** Multiple example tasks dikhaye gaye:
- Story writing
- List generation
- Poem creation
- Explanation

Matlab instruction tuning model ko broader assistant-style response behavior sikhati hai.

**Slide 91:** Objective function still wahi high-level next-token prediction hi rehta hai, but now:
> **predict next token given the input instruction**

Example form:
```text
Input: Do X.
Output: Sure ...
```

**Slide 92:** Data mixtures for instruction tuning:
- Assistant dialogs
- Synthetic instructions
- Math / reasoning / code
- Safety alignment
- etc.

Data human-written bhi ho sakta hai aur synthetic bhi.

**Slide 93:** Scale:
- Thousands to millions of examples
- Example:
  - `GPT-3`: `13 thousand`
  - `LLaMA 3`: `10 million`

> **Observation:** Pretraining tokens trillions mein the, but instruction tuning examples usse kaafi kam hote hain.

---

### 3.5 Behavior After Instruction Tuning

**Slide 94:** Same washer question ab `Pretrained + instruction tuned LLM` ko diya gaya.

**Slide 95:** Tuned model ka answer zyada directly helpful tha:
> "No, it might get damaged. Try hand washing instead."

Point:
- assistant-style helpfulness improve hoti hai
- concise actionable answer milta hai
- raw knowledge se behavior-level refinement hoti hai

---

### 3.6 Challenges in SFT / Instruction Tuning

**Slide 96:** Challenges list kiye gaye:
- Very high-quality data needed
- Sensitive to prompt distribution
- Generalization issues
- Difficult to evaluate
- Computationally expensive

> **Example:** Agar tuning data sirf ek specific prompt style mein hai, toh model dusri phrasing par utna robust nahi ho sakta.

---

### 3.7 Benchmarks and Evaluation

**Slide 97:** Evaluation dimensions:
- General knowledge: `MMLU`
- Basic reasoning: `ARC-Challenge`
- Math reasoning: `GSM8K`
- Code generation: `HumanEval`

**Slide 98:** Benchmark validity concern raise ki gayi.

Practical caution:
- Agar benchmark task se contamination ho
- ya evaluation benchmark hi training mein leak ho jaye
- toh comparison confounded ho sakta hai

> **Takeaway:** Benchmark score useful hai, but blindly trust nahi karna chahiye.

**Reference:** Dominguez-Olmedo et al., 2024 - "Training on the Test Task Confounds Evaluation and Emergence"

---

### 3.8 "Real-Life" Feeling

**Slide 99:** Chatbot Arena type platforms ka idea introduce hua:
- Websites user prompts par A/B tests run karti hain
- Real human preference data capture hota hai

**Slide 100:** Benefit:
> Yeh systems "vibes" ko number dene ki koshish karte hain

**Slide 101:** Challenges:
- Unequal exposure / cold start problem
- Easy to rig
- Users factuality jaise important aspects ko accurately assess nahi karte
- Personal preference bias
- Safety penalization

**Slide 102:** Same challenges fir reinforce kiye gaye, aur final point diya gaya:
> Evaluation khud ek hard problem hai

**Reference:** Huang et al., 2025 - "Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards"

---

### 3.9 Lifecycle View and Lecture 5 Preview

**Slide 103:** Next lecture ke liye teaser:
- Initialized model
- Pretraining
- Finetuning
- `Preference tuning`

Future goal:
model ko aur aligned banana, taaki wo kam misbehave kare.

**Slide 104:** LLM lifecycle summary:
1. Pretraining -> basic knowledge
2. Finetuning -> specific tasks
3. Preference tuning -> better alignment / less misbehavior

---

## PART 4: Parameter-Efficient Finetuning (Slides 105-128)

**Slide 105:** Section divider. Ab parameter-efficient finetuning start hota hai.

---

### 4.1 LoRA: Low-Rank Adaptation

**Slide 106:** Context:
Full SFT resource intensive hota hai, aur har kisi ke paas large GPUs nahi hote.

Idea:
`LoRA = Low-Rank Adaptation`

Core concept:
> Full weight matrix ko fully retrain mat karo; update ko low-rank form mein represent karo.

Slide intuition:
```text
W ~= W0 + BA
```

jahan:
- `W0` = frozen original weight
- `A, B` = chhote trainable low-rank matrices

**Slide 107:** Discussion:
- Full parameters train karne ki zaroorat nahi
- Similar performance mil sakti hai
- Related methods: prefix tuning, adapters

> **Example:** Poori building ko rebuild karne ke bajay sirf ek modular extension add karo.

**Reference:** Hu et al., 2021 - "LoRA: Low-Rank Adaptation of Large Language Models"

---

### 4.2 Full Finetuning vs LoRA

**Slide 108:** Regular finetuning:
> Full matrix `W` optimize hoti hai

**Slide 109:** LoRA finetuning:
> Base matrix `W0` mostly frozen rehti hai, aur low-rank update optimize hota hai

Practical consequence:
- trainable parameters dramatically kam
- memory and optimizer cost kam

---

### 4.3 Swap Matrices = Swap Tasks

**Slides 110-112:** LoRA ka major deployment benefit dikhaya gaya:
- Same base model `W0`
- Alag tasks ke liye alag `A, B` matrices

Examples:
- spam detection LoRA
- sentiment extraction LoRA
- translation LoRA

> **Example:** Same phone par alag SIM cards jaisi socho. Base device same, behavior module change ho jaata hai.

Point:
base model reuse hota hai; task-specific adapters swap kiye ja sakte hain.

---

### 4.4 Kahan Apply Karein LoRA?

**Slide 113:** Original LoRA paper ke experimented locations dikhaye gaye.

**Slide 114:** Modern guidance ka updated view dikhaya gaya:
- Aajkal more targeted placement use hoti hai
- Slide ek "most important location" highlight karti hai

Practical message:
> LoRA ko har jagah lagana zaroori nahi; sahi target modules choose karna important hai.

**Reference:** Schulman et al., 2025 - "LoRA Without Regret"

---

### 4.5 Training Dynamics of LoRA

**Slide 115:** Two empirical observations:
- LoRA ko full finetuning se **higher learning rate** chahiye hoti hai
- Large batch sizes par LoRA comparatively worse perform kar sakta hai

**Slide 116:** Same points ko "empirical" emphasis ke saath reinforce kiya gaya.

> **Takeaway:** LoRA sirf parameter trick nahi hai; uski training dynamics bhi alag hoti hain.

---

### 4.6 QLoRA

**Slide 117:** `QLoRA` introduce hua:
> Frozen weights ko quantize karke memory bottleneck aur reduce karo

**Slide 118:** Structural idea:
- Base frozen weights `W0` quantized store hote hain
- LoRA matrices `A, B` full precision mein trainable rehte hain

**Slide 119:** More explicit:
- `W0` stored quantized
- `A, B` stored in full precision

**Slide 120:** Computations full precision mein ki ja sakti hain while frozen base stays quantized in memory.

Point:
memory बचती hai without giving up trainable adapter flexibility.

**Reference:** Dettmers et al., 2023 - "QLoRA: Efficient Finetuning of Quantized LLMs"

---

### 4.7 Efficient Quantization Tricks

**Slide 121:** Trick:
`NF4 = 4-bit NormalFloat`

Idea:
- Normal-like weight distributions ko better capture karne ke liye quantization bins intelligently place karo
- Uniform splitting ki jagah normal quantiles based splitting use karo

**Slides 122-124:** Quantization comparison dikhaya gaya:
- No quantization
- Single quantization
- Double quantization

Concept:
- Single quantization mein weights quantize hote hain
- Double quantization mein quantization constants ko bhi quantize kar diya jata hai

**Slide 125:** Explicit punchline:
> Double quantization = quantization ... **done two times**

> **Example analogy:** Pehle kapde compress karo, phir compression settings file ko bhi compress kar do.

---

### 4.8 QLoRA Benefits

**Slide 126:** Benefits:
- VRAM savings se smaller GPUs par finetuning possible hoti hai
- Memory/quality trade-off better hota hai

**Slide 127:** Orders of magnitude from reported `LLaMA 65B` results:
- Around **16x VRAM savings** during finetuning
- Double quantization extra around **6%** save kar sakti hai

> **Example:** Jahan full finetuning impossible lagti thi, wahan QLoRA practical bana sakta hai.

---

## Closing (Slide 128)

**Slide 128:** "Thank you for your attention!" se lecture close hota hai.

---

## Lecture 4 Ka Big Picture

Is lecture ka core message yeh tha:
- LLMs ka main training lifecycle `pretraining -> finetuning -> preference tuning` hai
- Pretraining internet-scale data aur huge compute demand karta hai
- Training bottleneck aksar raw math se kam, aur memory / IO se zyada hota hai
- Isliye ZeRO, FlashAttention, aur mixed precision jaisi engineering tricks critical hain
- Helpful assistant behavior ke liye SFT / instruction tuning zaroori hai
- Full finetuning costly hai, isliye LoRA aur QLoRA practical alternatives ban gaye hain

> **One-line summary:** Lecture 4 ne dikhaya ki strong LLM banana sirf architecture ka kaam nahi; training pipeline, memory engineering, finetuning strategy, aur quantization sab equally important hain.

---

## Key Papers Referenced

1. **"Scaling Laws for Neural Language Models"** - Kaplan et al., 2020
2. **"Training Compute-Optimal Large Language Models"** - Hoffmann et al., 2022
3. **"ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"** - Rajbhandari et al., 2019
4. **"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"** - Dao et al., 2022
5. **"Mixed Precision Training"** - Micikevicius et al., 2017
6. **"Finetuned Language Models are Zero-Shot Learners"** - Wei et al., 2022
7. **"Training on the Test Task Confounds Evaluation and Emergence"** - Dominguez-Olmedo et al., 2024
8. **"Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards"** - Huang et al., 2025
9. **"LoRA: Low-Rank Adaptation of Large Language Models"** - Hu et al., 2021
10. **"LoRA Without Regret"** - Schulman et al., 2025
11. **"QLoRA: Efficient Finetuning of Quantized LLMs"** - Dettmers et al., 2023

---

*Stanford CME 295 Lecture 4 - all 128 slides covered in Hinglish with slide numbers, explanations, and practical intuition.*
