# CME 295: Transformers & Large Language Models - Lecture 3 (Hinglish)
### Stanford | Afshine Amidi & Shervine Amidi

---

## Pichle Lecture Ka Recap (Slides 1-6)

**Slide 1:** Title slide hai. Course ka naam `CME 295: Transformers & Large Language Models`, ye `Lecture 3` hai by Afshine Amidi aur Shervine Amidi.

**Slide 2:** "Recap of last episode..." se lecture start hota hai. Pichle lecture ke transformer-based model families ko yaad kiya ja raha hai.

**Slide 3:** Pehli category: **Encoder-Decoder** models.
- Use case: **text-to-text**
- Examples: `T5`, `mT5`, `ByT5`

> **Example:** Translation, summarization, question generation.

**Slide 4:** Doosri category: **Encoder-Only** models.
- Output usually class prediction ya representation extraction hota hai
- Example task: sentiment classification
- Examples: `BERT`, `DistilBERT`, `RoBERTa`

> **Example:** "Yeh movie boring thi" -> `Negative`

**Slide 5:** Teesri category: **Decoder-Only** models.
- Ye bhi text-to-text karte hain, but **autoregressive generation** ke through
- Example: `GPT series`

> **Example:** Prompt do: "Once upon a time..." -> model aage story likhega.

**Slide 6:** Recap ka key takeaway: aaj ke modern LLM wave ka center mostly **decoder-only transformers** hain.

---

## Lecture Ka Overview (Slide 7)

**Slide 7:** Aaj ke lecture ke main topics list kiye gaye:
- LLM overview
- MoE-based LLMs
- Response generation
- Prompting strategies
- Inference optimizations

---

## PART 1: LLM Overview (Slides 8-15)

### 1.1 Terminology

**Slides 8-9:** Basic term define kiya gaya:
`LLM = Large Language Model`

**Slide 10:** "Language model" ki core definition di gayi:
> A language model token sequences ko probabilities assign karta hai.

Matlab model yeh estimate karta hai ki kaunsa token sequence natural ya likely hai.

> **Example:** "The teddy bear is" ke baad:
> - `reading` ka probability high ho sakta hai
> - `banana` ka probability lower ho sakta hai

**Slide 11:** Focus fir se isi baat par hai ki "LLM" sirf marketing term nahi hai, base still ek **language model** hi hai.

**Slide 12:** "Large" ka matlab roughly yeh hota hai:
- **Model size:** billions of parameters ya usse zyada
- **Training data:** 100s of billions of tokens ya usse zyada
- **Compute:** bahut saare GPUs / large-scale training infrastructure

> **Example:** Chhota model kuch million ya few hundred million parameters ka ho sakta hai, jabki LLM billions tak chala jaata hai.

---

### 1.2 LLM Characteristics

**Slides 13-14:** Modern LLMs ko yahan **decoder-only transformer-based models** ke roop mein present kiya gaya. Yani architecture ka main skeleton transformer decoder stack hota hai.

**Slide 15:** Common decoder-only LLM examples diye gaye:
- `GPT series`
- `LLaMA`
- `Gemma`
- `DeepSeek`
- `Mistral`
- `Qwen`

> **Example intuition:** In sab models ka core behavior similar family ka hota hai:
> prompt lo -> next token predict karo -> token by token output build karo.

---

## PART 2: MoE-Based LLMs (Slides 16-31)

**Slide 16:** Section divider. Ab lecture **MoE-based LLMs** par shift hota hai.

---

### 2.1 Motivation for MoE

**Slide 17:** Motivation ek simple picture se diya gaya: model bahut bada ho sakta hai, lekin har input ke liye poora model use karna shayad zaroori nahi.

**Slide 18:** Core idea:
> **Not all weights are useful in every forward pass.**

Yani har token ke liye full huge model activate karna inefficient ho sakta hai.

> **Example:** Agar prompt coding ke baare mein hai, toh shayad kuch neurons ya submodules zyada useful hon; poem ke liye kuch aur.

**Slides 19-22:** Model ko experts mein todne ka visual intuition diya gaya:
- `E1, E2, ..., En` = experts
- `G` = gating / router module
- Router decide karta hai ki kis input ke liye kaunse experts useful honge

> **Analogy:** Socho ek hospital hai:
> - ek doctor heart specialist hai
> - ek skin specialist
> - ek neuro specialist
> Har patient ko sab doctors ke paas nahi bhejte; relevant doctor choose karte hain.

---

### 2.2 Overview of MoEs

**Slide 23:** Term define hua:
`MoE = Mixture of Experts`

Isme multiple expert networks hote hain aur ek router / gate unka combination control karta hai.

**Slide 24:** **Dense MoE** introduce hua:
- Output = **all expert outputs ka weighted average**
- Har expert contribute karta hai, bas weight alag hota hai

Conceptually:
```text
y = sum_i g_i E_i(x)
```
jahan `g_i` gate weight hai.

> **Example:** Agar 3 experts ke weights `0.1, 0.8, 0.05` hain, toh second expert ka influence sabse zyada hoga.

**Slide 25:** **Sparse MoE** introduce hua:
- Output = **sirf selected experts ka weighted average**
- Selection often **top-k routing** se hoti hai

Conceptually:
```text
y = sum_{i in Top-k(x)} g_i E_i(x)
```

> **Example:** Agar 64 experts hain aur top-2 routing use ho rahi hai, toh har token ke liye sirf 2 experts active honge.

**Benefit:** Parameter count huge ho sakta hai, but per-token compute relatively controlled rehta hai.

**Reference:** Shazeer et al., 2017 - "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"

---

### 2.3 MoE in Transformer-Based Models

**Slides 26-27:** Transformer architecture ke context mein MoE dikhaya gaya. Uska intuition yeh hai ki transformer ke kuch dense FFN blocks ko expert-based FFN blocks se replace kiya ja sakta hai.

**Slide 28:** Important point explicitly bola gaya:
> **Routing done for each token!**

Yani har token alag experts ke paas ja sakta hai.

> **Example:** Same sentence mein:
> - technical word kisi "reasoning" expert ke paas ja sakta hai
> - common narrative word kisi "general language" expert ke paas

Practical view:
- Self-attention sab tokens ko mix karta hai
- FFN/MoE block token-wise operate karta hai
- Isliye routing naturally **per-token** ki ja sakti hai

---

### 2.4 Training Challenge: Routing Collapse

**Slide 29:** MoE training ka ek major problem introduce hua:
`routing collapse`

**Symptom:** Same expert baar-baar select hota rehta hai, baaki experts underused rehte hain.

> **Example:** Agar 8 experts hain aur 90% tokens sirf expert 3 ke paas ja rahe hain, toh effective capacity waste ho rahi hai.

**Slide 30:** Is problem ka remedy diya gaya:
- Auxiliary loss add karo
- Objective yeh hai ki baaki experts bhi "part of the game" bane rahein
- Load balancing encourage ki jaati hai

Slide par do quantities mention hui:
- `f_i` = fraction of tokens routed to expert `i`
- `P_i` = average routing probability for expert `i`

Switch-style load-balancing auxiliary loss commonly is tarah likha jaata hai:
```text
L_aux = alpha * N * sum_i f_i P_i
```

Matlab router ko is direction mein train kiya jaata hai ki load zyada evenly distribute ho.

> **Example analogy:** Agar class teacher har sawal ka jawab sirf ek hi student se le, toh baaki students kabhi improve nahi karenge.

**Reference:** Fedus et al., 2021 - "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"

---

### 2.5 Interpreting Experts

**Slide 31:** Experts ko interpret karne ki idea dikhayi gayi. Visualization mein har color ek expert ko represent karta hai.

Point:
- Experts often random nahi hote
- Kuch experts specific token types, topics, ya patterns par specialize kar sakte hain

> **Example:** Ek expert numbers/dates par strong ho sakta hai, doosra code-like syntax par, teesra multilingual fragments par.

**Reference:** Jiang et al., 2024 - "Mixtral of Experts"

---

## PART 3: Response Generation (Slides 32-74)

**Slide 32:** Section divider. Ab focus **response generation** par shift hota hai.

---

### 3.1 Next Token Prediction

**Slides 33-41:** Autoregressive generation ko progressive animation se samjhaya gaya.

Sequence kuch is tarah build hoti hai:
```text
[BOS] -> A -> teddy -> bear -> is -> ?
```

Model har step par:
- pichle saare tokens leta hai
- next token ki probability distribution nikalta hai
- ek token choose karta hai
- usse sequence mein append kar deta hai

Formal idea:
```text
P(x_1, x_2, ..., x_T) = product_t P(x_t | x_<t)
```

> **Example:** "A teddy bear is" ke baad model `reading`, `sleeping`, `cute`, `soft` jaise next-token candidates score karega.

---

### 3.2 Predicting Next Token

**Slides 42-44:** Yahan emphasis hai ki decoder-only LLM ka core job next token ke liye poori vocabulary par probability distribution banana hota hai.

High-level pipeline:
- hidden state niklo
- vocabulary logits compute karo
- probabilities obtain karo

> **Example:** Agar vocabulary mein 50,000 tokens hain, toh har step par model 50,000 possible next-token scores produce karta hai.

---

### 3.3 Greedy Decoding

**Slide 45:** Pehla decoding idea:
**Greedy decoding**

Rule:
> Har step par highest predicted probability wala token choose karo.

```text
next_token = argmax p(token | context)
```

> **Example:** Agar probabilities hain:
> - `cute`: 0.40
> - `sleepy`: 0.25
> - `old`: 0.10
> Toh greedy decoding `cute` choose karega.

**Slide 46:** Limitation batayi gayi:
- output hamesha optimal nahi hota
- naturalness kam ho sakti hai
- diversity kam hoti hai

> **Example:** Greedy decoding repeatedly same safe phrase choose kar sakta hai, jaise "The teddy bear is very very cute..."

---

### 3.4 Beam Search

**Slides 47-54:** Doosra idea:
**Beam search**

Rule:
- Ek token par commit karne ke bajay
- top `k` most likely paths maintain karo
- har step par in paths ko expand karo
- cumulative score ke basis par best beams rakho

> **Example:** `k = 2` ho toh model ek path `a cute ...` aur doosra `the sleepy ...` dono track kar sakta hai.

Beam search intuition:
1. Start from `[BOS]`
2. Top-k next tokens lo
3. Har surviving path ko aage expand karo
4. Best-scoring complete sequence choose karo

> **Example:**  
> Beam 1: `a -> cute -> teddy -> bear`  
> Beam 2: `the -> sleepy -> dog -> ...`

**Slide 55:** Limitations:
- computation zyada lagti hai
- diversity/creativity phir bhi limited ho sakti hai

Greedy se better search milta hai, par open-ended generation mein beam search kabhi-kabhi too rigid lag sakta hai.

---

### 3.5 Sampling

**Slide 56:** Teesra idea:
**Sampling**

Rule:
> Next token ko probability distribution se sample karo.

Yeh generation ko more flexible aur diverse banata hai.

> **Example:** Agar `cute` = 0.4 aur `sleepy` = 0.3 hai, toh sampling mein dono aa sakte hain; greedy mein sirf `cute` aata.

**Slide 57:** **Top-k sampling**
- Sirf top `k` most probable tokens consider karo
- Unhi ke beech random sampling karo

> **Example:** `k = 4` ho toh sirf top 4 tokens ke beech sample hoga; baaki impossible maan liye jayenge.

**Slide 58:** **Top-p sampling** (nucleus sampling)
- Sabse chhota token set choose karo jiska cumulative probability `>= p` ho
- Fir us set ke beech sample karo

> **Example:** `p = 0.90` ho toh model top 3 tokens le sakta hai ek context mein, aur top 20 tokens doosre context mein. Set size dynamic hota hai.

**Reference:** "Super Study Guide: Transformers and Large Language Models", Amidi et al., 2024.

---

### 3.6 Probabilities Kaise Banti Hain?

**Slide 59:** Question explicitly poocha gaya:
> But how are probabilities obtained?

**Slides 60-61:** High-level answer:
- Model har vocabulary token ke liye **logits** banata hai
- Fir **softmax** un logits ko probability distribution mein convert karta hai

```text
p_i = exp(z_i) / sum_j exp(z_j)
```

jahan `z_i` token `i` ka logit hai.

> **Example:** Agar logits `[2.0, 1.0, 0.0]` hain, toh softmax ke baad pehle token ki probability sabse zyada hogi.

---

### 3.7 Temperature

**Slide 62:** Temperature introduce kiya gaya. Temperature output probabilities ko tweak karne deta hai.

Standard form:
```text
p_i(T) = exp(z_i / T) / sum_j exp(z_j / T)
```

**Slide 63:** Slide intuition:
- **Small `T`** -> distribution sharper hoti hai
- **High `T`** -> distribution flatter hoti hai

**Slide 64:** Impact summarized:
- Low temperature -> more deterministic, safer, repetitive bhi ho sakta hai
- High temperature -> more random, creative, but error-prone bhi ho sakta hai

> **Example:**  
> `T = 0.2` -> model almost greedy jaisa behave karega  
> `T = 1.2` -> rare tokens ko bhi chance milega

**Suggested Reading:** He et al., 2025 - "Defeating Nondeterminism in LLM Inference"

---

### 3.8 Guided Decoding

**Slide 65:** Motivation:
kabhi hume output specific format mein chahiye hota hai, jaise JSON.

Prompt example slide par roughly:
```text
Generate a description of my 33-year old teddy bear who likes reading.
Do this in JSON format.
```

Desired output shape:
```json
{
  "first_name": "teddy",
  "last_name": "bear",
  "age": 33,
  "hobby": "reading"
}
```

**Slides 66-74:** Guided decoding ka core idea:
> Har step par sirf **valid next tokens** ko allow karo.

Matlab:
- agar `{` ke baad key expected hai, toh random word `road` valid nahi hona chahiye
- agar `:` expected hai, toh closing brace `}` allow nahi honi chahiye
- agar integer expected hai, toh quoted string galat ho sakti hai

> **Example:** JSON generate karte waqt:
> - opening brace ke baad `"first_name"` valid ho sakta hai
> - `sun` ya `road` invalid ho sakte hain

Benefit:
- Structured output reliability improve hoti hai
- Parsable output milne ke chances bahut badh jaate hain

> **Analogy:** Jaise exam mein multiple-choice answer sheet ho, aur system tumhe sirf valid bubbles fill karne de.

---

## PART 4: Prompting Strategies (Slides 75-84)

**Slide 75:** Section divider. Ab topic **prompting strategies** hai.

---

### 4.1 Context Length / Context Size / Window Size

**Slide 76:** Terminology introduce hui:
- `Context length`
- `Context size`
- `Window size`

Yeh roughly us maximum input-output history ko refer karte hain jo model ek baar mein dekh sakta hai.

> **Example:** Agar model ka context window 8K tokens hai, toh wo ek baar mein maximum around 8,000 tokens ka working context handle karega.

**Slide 77:** Discussion point:
orders of magnitude input type aur model dono par depend karte hain.

Matlab:
- text vs code vs multimodal inputs alag behave kar sakte hain
- har model ka supported context alag hota hai

**Slide 78:** Important warning:
> Beware of **context rot**

Yani context badhane se hamesha performance better nahi hoti. Bahut lamba input dene par model relevant cheezein dilute ya ignore bhi kar sakta hai.

> **Example:** 100-page prompt mein important instruction beech mein daba sakti hai.

**Reference:** Hong et al., 2025 - "Context Rot: How Increasing Input Tokens Impacts LLM Performance"

---

### 4.2 Prompt Ki Main Structure

**Slide 79:** Prompt ka recommended structure dikhaya gaya. Example bedtime-story prompt ke through 4 components highlight kiye gaye:
- **Context**
- **Instructions**
- **Input**
- **Constraints**

Illustration:
- Context: teddy bear ko bedtime story chahiye
- Instructions: story specific location mein honi chahiye
- Input: `Location: Country of teddy bears`
- Constraints: story tired teddy bears ke liye suitable ho

> **Example template:**
```text
Context: You are writing a bedtime story.
Instruction: Keep it calm and soft.
Input: Location = Country of teddy bears
Constraints: Suitable for tired teddy bears
```

Point: achha prompt sirf raw question nahi hota; usme role, task, data aur limits clearly alag ki ja sakti hain.

---

### 4.3 In-Context Learning (ICL)

**Slide 80:** Term define hua:
`ICL = In-Context Learning`

Idea:
model ko examples prompt ke andar dekar behavior steer karna.

**Slide 81:** Do modes compare kiye gaye:

**Zero-shot learning**
- Koi example nahi diya jaata
- Performance base model ki capability par heavily depend karti hai

**Few-shot learning**
- Prompt mein input/output examples diye jaate hain
- Performance often better hoti hai

> **Example:**
> Zero-shot:
> "Convert this review to sentiment."
>
> Few-shot:
> "Review: Great movie -> Positive  
> Review: Waste of time -> Negative  
> Review: Acting was decent -> ?"

**Slide 82:** Few-shot ka trade-off:
- examples banana effort leta hai
- prompt length badh jaati hai
- cost aur latency dono increase hote hain

> **Rule of thumb:** Few-shot often better hota hai, but free nahi hota.

**Reference:** Brown et al., 2020 - "Language Models are Few-Shot Learners"

---

### 4.4 Chain of Thought

**Slide 83:** Idea:
> Reasoning explain karne se performance improve ho sakti hai.

Slide example:
- Bear 2020 mein born hua
- Is saal age 4 hai
- Next year age 5 hogi

Point:
- step-by-step reasoning intermediate logic expose karti hai
- model arithmetic / reasoning tasks mein better perform kar sakta hai

Benefits and trade-offs:
- Interpretability improve hoti hai
- More tokens lagte hain
- Cost aur latency badhte hain

> **Example:**  
> Direct answer: `5`  
> CoT answer: "Is saal 4 hai, next year ek saal aur add hoga, isliye 5."

**Reference:** Wei et al., 2022 - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"

---

### 4.5 Self-Consistency

**Slide 84:** Idea:
> Multiple reasoning paths generate karo aur unhe aggregate karo.

Yani ek hi reasoning chain par depend mat karo. Kai candidate solutions lo aur final answer majority / best aggregation se choose karo.

Slide ke example mein:
- do reasoning paths answer `5` par pahunchte hain
- ek path galat answer `4` deta hai
- aggregation ke baad final answer `5` choose hota hai

> **Example:** Agar 5 generated solutions mein 4 ne same answer diya, toh us answer par trust zyada ho sakta hai.

Trade-off:
- performance improve ho sakti hai
- lekin compute aur cost badhte hain

**Reference:** Wang et al., 2022 - "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

---

## PART 5: Inference Optimizations (Slides 85-124)

**Slide 85:** Section divider. Ab focus **inference optimizations** par shift hota hai.

---

### 5.1 Challenges

**Slide 86:** Motivation:
LLM inference expensive hai. Sawal yeh hai ki complexity kaise reduce ki jaaye.

**Slide 87:** "Exact" efficiency ke 3 categories di gayi:
- Avoid redundancies
- Memory management
- Reformulate the math

**Slide 88:** Do broad buckets compare kiye gaye:

**Exact efficiency**
- Avoid redundancies
- Memory management
- Reformulate the math

**Approximations**
- Architectural changes
- Embedding representations
- Token prediction

Point:
Kabhi hum exact same answer ko faster paana chahte hain, aur kabhi thoda approximation tolerate karke zyada speed lena chahte hain.

---

### 5.2 KV Caching

**Slide 89:** Attention-based tricks section start hoti hai.

**Slides 90-95:** Motivation progressively dikhayi gayi:
har naya token generate karte waqt usse saare previous tokens ke saath interact karna padta hai.

Without caching:
- step 1 par kuch compute hota hai
- step 2 par previous work ka large part dubara hota hai
- step 3 par aur dubara

Yeh redundant hai.

**Slides 96-100:** Solution:
**KV caching = Key-Value caching**

Idea:
- previous tokens ke **keys** aur **values** cache mein store karo
- naya token aane par purane K/V dubara recompute mat karo
- sirf new token ka query banao aur cached K/V use karo

> **Example:** Agar sequence hai `a cute teddy bear is ...`, toh `a`, `cute`, `teddy`, `bear` ke K/V ek baar cache ho jaayenge. Next step par unhe fir se compute nahi karna padega.

Benefit:
- autoregressive decoding faster hota hai
- redundant attention computation kam hoti hai

Trade-off:
- memory cost badh jaati hai, kyunki KV cache store karna padta hai

---

### 5.3 Sharing Attention Heads

**Slides 101-102:** Vanilla multi-head attention mein:
```text
#query heads = #key heads = #value heads = h
```

Yani har query head ke corresponding K/V heads bhi alag-alag hote hain.

**Slide 103:** Key idea:
> Query groups ke beech key/value heads share karo.

Isse KV cache memory reduce hoti hai.

**Slide 104:** Teen variants compare kiye gaye:

**MHA = Multi-Head Attention**
- Full separate Q/K/V heads
- Sabse zyada flexibility
- Sabse zyada KV memory cost

**MQA = Multi-Query Attention**
- Many query heads
- Single shared key head + single shared value head
- Max efficiency

**GQA = Grouped-Query Attention**
- Query heads groups mein divide hote hain
- Har group shared K/V use karta hai
- Balance between quality and efficiency

**Slide 105:** GQA ko formula-style relation se dikhaya gaya:
```text
#query heads = h
#key heads = #value heads = G < h
```

> **Example:** `h = 32`, `G = 8` ho toh 32 query heads ke liye sirf 8 K heads aur 8 V heads rakhe jaayenge.

> **Analogy:** 32 employees hain, par 32 alag secretaries ke bajay 8 shared secretaries use kar rahe ho.

---

### 5.4 PagedAttention

**Slide 106:** Observation:
KV cache store karte waqt kaafi memory waste ho sakti hai.

**Slide 107:** Solution:
**PagedAttention**

Idea:
- K aur V ko contiguous block mein force karne ke bajay
- unhe paged / non-contiguous memory style mein store karo
- wasted memory reduce karo

> **Analogy:** Jaise OS virtual memory pages use karta hai, waise hi KV storage ko smarter chunks mein manage karo.

Benefit:
- serving efficiency better hoti hai
- fragmentation aur waste kam hota hai

**Reference:** Kwon et al., 2023 - "Efficient Memory Management for Large Language Model Serving with PagedAttention"

---

### 5.5 Latent Attention for KV Cache Compression

**Slide 108:** Goal:
memory mein stored `K` aur `V` ki dimension reduce karni hai.

**Slide 109:** Core idea:
full-size K/V directly store karne ke bajay **compressed representations** store karo.

> **Example:** Bade vector ko chhote latent space mein compress karke rakho, aur zarurat par reconstruct/use karo.

**Slides 110-114:** Before/after style visualization dikhata hai:
- **Before:** full big representations memory mein padhi hain
- **After:** shared / compressed latent representation store ki ja rahi hai

Point:
- KV cache footprint reduce ho sakta hai
- especially long-context inference mein yeh bahut useful ho sakta hai

**Reference:** DeepSeek, 2023 - "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model"

---

### 5.6 Speculative Decoding

**Slide 115:** Token-generation tricks section start hoti hai.

**Slide 116:** Idea:
> Ek **draft (small)** model tokens propose karega, aur ek **target (big)** model unhe validate karega.

Yeh technique:
- small model ki speed ka benefit leti hai
- big model ki quality maintain karne ki koshish karti hai

**Slide 117:** Draft model multiple tokens propose karta hai:
```text
P1, P2, ..., Pk
```

Example:
```text
[BOS] my teddy bear -> is -> cute -> and -> smart
```

**Slide 118:** Target model corresponding probabilities nikalta hai:
```text
Q1, Q2, ..., Qk, Qk+1
```

Point:
target model verify karta hai ki draft ke proposed tokens acceptable hain ya nahi.

**Slide 119:** Acceptance/rejection logic diya gaya.
Let:
- `P_i(token)` = draft model probability
- `Q_i(token)` = target model probability

High-level rule:
- Agar target draft token ko enough support karta hai, token accept
- Otherwise token probabilistically accept/reject ho sakta hai
- Rejection par correction sampling ki jaati hai from `[Q_i - P_i]_+`

Slide wording ke according:
- If `Q_i(token) >= P_i(token)`, token accept
- Otherwise token ko probability `Q_i(token) / P_i(token)` se accept karo
- Rejection par next token ko corrected distribution se re-sample karo aur exit

> **Example intuition:** Chhota model rough draft likhta hai, bada model proofreader ki tarah check karta hai.

Benefit:
- decoding speed up ho sakti hai
- quality target model se anchored rehti hai

**Reference:** Chen et al., 2023 - "Accelerating Large Language Model Decoding with Speculative Sampling"

---

### 5.7 Multi-Token Prediction (MTP)

**Slide 120:** Term define hua:
`MTP = Multi-Token Prediction`

Idea:
model ek baar mein sirf next token nahi, balki multiple future tokens predict karne ki koshish karta hai.

> **Example:** `[BOS] my teddy bear` se model `is`, `cute`, `and`, `smart` jaise several future positions par parallel predictions train kar sakta hai.

**Slide 121:** Core training idea:
> `k` prediction heads train karo jo `t+1, t+2, ..., t+k` positions predict karein.

Yeh decoding ko accelerate karne ki direction mein ek aur idea hai.

**Reference:** Gloeckle et al., 2024 - "Better & Faster Large Language Models via Multi-token Prediction"

---

### 5.8 Final Summary of Optimization Space

**Slide 122:** Lecture ek baar fir summarize karti hai ki optimization ke bahut dimensions hote hain:

**Exact efficiency**
- Avoid redundancies
- Memory management
- Reformulate the math

**Approximations**
- Architectural changes
- Embedding representations
- Token prediction

**Slide 123:** Concrete remedies ko categories ke saath map kiya gaya:

**Exact-side examples**
- `KV cache`
- `PagedAttention`
- `Speculative decoding`

**Approximation-side examples**
- `Grouped query attention`
- `Latent attention`
- `Multi-token prediction`

Yeh ek practical engineer's view deta hai:
LLM inference optimize karna sirf ek trick ka kaam nahi hai; multiple layers par sochna padta hai.

---

## Closing (Slide 124)

**Slide 124:** "Thank you for your attention!" se lecture close hota hai.

---

## Lecture 3 Ka Big Picture

Is lecture ka main message yeh tha:
- Modern LLMs mostly decoder-only hote hain
- Scale badhane ke liye MoE jaise sparse architectures use kiye ja sakte hain
- Output quality heavily decoding strategy par depend karti hai
- Prompt design bhi model performance ka major lever hai
- Real-world deployment mein inference optimization equally important hai

> **One-line summary:** LLM banana sirf model architecture ka problem nahi hai; routing, decoding, prompting, aur serving efficiency sab equally important pieces hain.
