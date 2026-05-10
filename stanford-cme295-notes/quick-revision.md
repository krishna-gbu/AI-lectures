# CME 295 Quick Revision

Fast-recall notes for quick revision. Focus is on memory hooks, comparisons, and exam-style recall.

## At a Glance

| Lecture | Core Shift | Fast Memory Line |
|---|---|---|
| 1 | Text representation se Transformer tak | `represent -> remember -> attend` |
| 2 | Transformer internals se BERT tak | `better positions -> better stability -> better encoder models` |
| 3 | Modern LLM behavior and serving | `generate -> prompt -> optimize` |
| 4 | Training stack and efficient finetuning | `pretrain -> tune -> compress` |
| 5 | Alignment by preferences | `compare -> score -> optimize` |
| 6 | Reasoning via RL | `think -> verify -> reinforce` |
| 7 | External knowledge and actions | `retrieve -> call -> act` |
| 8 | Evaluation and benchmark literacy | `measure -> judge -> debug` |
| 9 | Beyond text and future frontiers | `recap -> multimodal -> diffusion -> future` |

---

## Lecture 1

Memory hook:
`Text -> Tokens -> Embeddings -> RNN -> Attention -> Transformer`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| NLP basics | language sequential hoti hai | word order meaning change karta hai | order matters |
| Tokenization | text ko tokens me todna | model raw sentence nahi, token ids process karta hai | text -> pieces |
| Word representation | words ko vectors me map karna | NN ko numbers chahiye | one-hot bad, dense good |
| Word2vec | context se embeddings seekhna | semantic similarity milti hai | similar words paas aate hain |
| RNN | sequence ko step-by-step process karna | order capture hota hai | hidden state = running memory |
| LSTM | gated RNN | long-term info preserve karne ki koshish | forget, update, output |
| Attention | relevant parts ko directly dekhna | seq2seq bottleneck kam hota hai | compress-all-at-end problem solve |
| Self-attention | har token sabko dekh sakta hai | long dependencies easier | `Q,K,V` |
| Transformer | attention + FFN + positional encoding | parallel training aur strong sequence modeling | modern foundation |

### Most important comparisons

| Method | Strength | Weakness | Exam keyword |
|---|---|---|---|
| Word2vec | simple semantic embeddings | no order, no context | static embeddings |
| RNN | sequence order capture | vanishing gradients, slow | recurrence |
| LSTM | better long memory than RNN | still sequential and costly | gates |
| Transformer | long-range interaction + parallelism | attention cost high | self-attention |

### Fast contrasts

| Question | Short answer |
|---|---|
| Word2vec kya solve karta hai? | generic word meaning |
| RNN kya add karta hai? | order + running context |
| LSTM kyun aaya? | RNN ki long-memory weakness ke liye |
| Attention kyun aaya? | encoder ke final hidden state bottleneck ko avoid karne ke liye |
| Transformer kyun strong hai? | recurrence hata kar attention-based parallel computation |

### Key formulas and terms

- `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`
- `Q` = kya dhoondhna hai
- `K` = kis cheez ki matching hogi
- `V` = actual information
- Multi-head attention = multiple parallel attention views

### One-line recall

- Word2vec meaning deta hai, but context nahi.
- RNN context deta hai, but long-distance aur speed me weak hai.
- Transformer direct attention se sequence ke important parts ko connect karta hai.

---

## Lecture 2

Memory hook:
`Better Transformer internals -> Better positions -> Better normalization -> Better efficiency -> BERT`

### What changed across the lecture?

| Part | Kya seekha | Modern default / key point | Quick memory line |
|---|---|---|---|
| Position embeddings | order inject karna zaroori hai | absolute se relative better | attention ko distance chahiye |
| Sinusoidal PE | fixed mathematical encoding | extrapolate kar sakta hai | add pattern, no retrain |
| T5 bias / ALiBi | attention scores me relative bias | distance-aware attention | far tokens ko penalty |
| RoPE | query/key rotate by position | modern default | add nahi, rotate |
| LayerNorm | training stable banata hai | Pre-Norm preferred | normalize before block |
| RMSNorm | cheaper normalization | large models me common | no mean subtraction |
| Sparse / sliding attention | full `O(n^2)` cost se bachna | local window useful | efficiency for long context |
| MHA / GQA / MQA | K/V sharing | GQA practical balance | memory vs quality |
| BERT | encoder-only bidirectional model | representation-focused | understand, not generate |
| DistilBERT / RoBERTa | efficient vs better-trained BERT | same family, different goal | smaller vs stronger |

### Most important comparisons

| Topic | Option 1 | Option 2 | Best takeaway |
|---|---|---|---|
| Position | absolute | relative | relative zyada useful |
| Position encoding | sinusoidal | RoPE | sinusoidal adds, RoPE rotates |
| Norm placement | Post-Norm | Pre-Norm | Pre-Norm deep models me stable |
| Normalization | LayerNorm | RMSNorm | RMSNorm cheaper |
| Attention heads | MHA | GQA / MQA | GQA balance point |
| Model type | Encoder-only BERT | Decoder-only GPT | understanding vs generation |

### RoPE vs sinusoidal

| Method | Kaise kaam karta hai | Strength | Fast memory line |
|---|---|---|---|
| Sinusoidal | token embeddings me position pattern add hota hai | unseen length par extrapolate kar sakta hai | `add` |
| RoPE | `Q,K` rotate hote hain position ke according | relative distance naturally emerge hoti hai | `rotate` |

### Term: Extrapolate

| Term | Meaning | Example |
|---|---|---|
| Interpolate | training range ke andar generalize karna | train `1-100`, test `80` |
| Extrapolate | training range ke bahar generalize karna | train `1-100`, test `200` |

Transformer context:
- agar model ne training me sequence length `512` tak dekha hai, aur test time par `1024` par bhi kaam karta hai, to bolte hain wo longer context par extrapolate kar raha hai
- sinusoidal ya ALiBi jaisi methods isi wajah se useful boli jati hain

### MHA vs GQA vs MQA

| Method | Query Heads | K/V Heads | Benefit | Cost |
|---|---|---|---|---|
| MHA | many | many | max flexibility | max KV memory |
| GQA | many | grouped shared | quality-efficiency balance | some approximation |
| MQA | many | 1 shared pair | max efficiency | more quality tradeoff |

### BERT family recall

| Model | Core idea | Best use | Limitation |
|---|---|---|---|
| BERT | bidirectional encoder representations | classification, extraction, embeddings | text generation ke liye ideal nahi |
| DistilBERT | distilled smaller BERT | fast inference, lower compute | some capability drop |
| RoBERTa | BERT ko better training recipe se improve kiya | stronger encoder performance | still encoder-only |

### One-line recall

- Lecture 1 ne Transformer banaya, Lecture 2 ne usse modern banaya.
- Relative position absolute position se zyada useful nikli.
- BERT samajhne ke liye strong hai, GPT generate karne ke liye.

---

## Lecture 3

Memory hook:
`LLM basics -> MoE -> decoding -> prompting -> inference optimization`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| LLM overview | LLM = large language model | modern wave mostly decoder-only hai | next-token engine at scale |
| MoE | sab weights har input ke liye zaroori nahi | sparse compute possible hota hai | route only useful experts |
| Response generation | next token kaise choose hota hai | output quality decoding par depend karti hai | generation strategy matters |
| Prompting strategies | model ko kaise steer karein | prompt khud performance lever hai | good prompt = free gain |
| Inference optimizations | serving ko fast aur cheap banana | deployment me engineering critical hai | quality ke saath latency bhi matter karti hai |

### LLM fundamentals

| Question | Short answer |
|---|---|
| Language model kya karta hai? | token sequences ko probability assign karta hai |
| LLM ka "large" kya hai? | billions of parameters, huge data, huge compute |
| Modern default architecture kya hai? | decoder-only transformer |

### Dense vs sparse MoE

| Method | Kaise kaam karta hai | Strength | Risk |
|---|---|---|---|
| Dense MoE | sab experts weighted contribute karte hain | full mixture | compute heavy |
| Sparse MoE | sirf top-k experts active hote hain | large parameter count with controlled compute | routing collapse |

### MoE recall

| Concept | Fast memory line |
|---|---|
| Router / gate | decide karta hai kaunse experts active honge |
| Per-token routing | har token alag expert subset choose kar sakta hai |
| Routing collapse | same expert overused, baaki experts idle |
| Load balancing loss | experts me traffic distribute karne ke liye |

### Decoding strategies

| Method | Rule | Best use | Limitation |
|---|---|---|---|
| Greedy | highest-probability token choose karo | deterministic, simple | repetitive, locally optimal |
| Beam search | top-k paths maintain karo | structured tasks, search | costly, open-ended text me rigid |
| Sampling | distribution se sample karo | diversity | randomness badh sakti hai |
| Top-k | top k tokens ke beech sample | controlled randomness | fixed cutoff |
| Top-p | smallest set with cumulative prob >= p | adaptive randomness | tuning needed |
| Temperature | logits sharpen / flatten karo | creativity control | low = repetitive, high = error-prone |
| Guided decoding | only valid outputs allow karo | JSON / schema / constrained output | flexibility kam |

### Prompting strategies

| Technique | Core idea | Best use | Limitation |
|---|---|---|---|
| Prompt structure | clear instruction + context + format | everyday prompting | poor prompts confuse model |
| In-context learning | examples prompt ke andar do | no-weight-update adaptation | context window limited |
| Chain-of-thought | model ko reasoning steps likhne do | math, logic, multi-step tasks | verbose aur not always reliable |
| Self-consistency | multiple reasoning paths sample karo | reasoning improvement | extra inference cost |

### ICL vs finetuning

| Method | Kahan hota hai | Cost | Memory line |
|---|---|---|---|
| ICL | prompt ke andar | inference-time | teach by examples now |
| Finetuning | model weights me | training-time | teach by changing weights |

### Inference optimization map

| Technique | Idea | Benefit | Tradeoff |
|---|---|---|---|
| KV cache | previous keys/values reuse karo | redundant compute bachti hai | memory cost badhta hai |
| GQA / MQA | K/V heads share karo | KV cache smaller hota hai | some quality tradeoff |
| PagedAttention | KV cache ko paged storage me manage karo | fragmentation aur waste kam | serving-system complexity |
| Latent KV compression | compressed K/V store karo | long-context memory reduction | approximation |
| Speculative decoding | small draft model propose, big model verify | faster decoding | extra system design |
| MTP | one step me multiple future tokens predict karo | speed direction | training/design complexity |

### Exact vs approximation

| Bucket | Meaning | Examples |
|---|---|---|
| Exact efficiency | same answer faster / cheaper | KV cache, PagedAttention, speculative decoding |
| Approximation | thoda structure change karke speed / memory gain | GQA, latent attention, MTP |

### One-line recall

- Lecture 3 ne dikhaya ki modern LLM sirf architecture nahi, decoding and serving problem bhi hai.
- MoE ka idea hai: parameter count bada rakho, per-token compute controlled rakho.
- Final output utna hi achha hota hai jitni achhi decoding strategy aur prompt design hoti hai.

---

## Grand Summary: Lecture 1-3

| Lecture | Core theme | Most important exam idea |
|---|---|---|
| 1 | sequence modeling evolution | RNN se attention aur phir Transformer tak jump |
| 2 | modern Transformer internals | RoPE, Pre-Norm, GQA, BERT family |
| 3 | modern LLM operation | decoder-only, MoE, decoding, prompting, serving |

### 3-line mega memory

- Lecture 1: model ko text samjhana seekho.
- Lecture 2: Transformer ko stable, efficient, aur task-specific banao.
- Lecture 3: LLM ko practical generation system ki tarah samjho.

---

## Lecture 4

Memory hook:
`Pretraining -> Scaling -> Training systems -> Instruction tuning -> LoRA / QLoRA`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| Pretraining | internet-scale data par LM train hota hai | base knowledge yahin se aati hai | knowledge comes from scale |
| Scaling laws | model, data, compute ka balance matter karta hai | bigger alone enough nahi | Chinchilla = balance |
| Training memory | params + activations + gradients + optimizer state | bottleneck often memory hota hai | training != just weights |
| Parallelism / ZeRO | multi-GPU training organize karna | trillion-scale training possible hota hai | shard redundancy |
| FlashAttention / precision | same training ko faster/cheaper banana | IO aur precision engineering critical hai | systems matter |
| SFT / instruction tuning | helpful assistant behavior sikhana | pretraining se raw knowledge, SFT se usability | knowledge != helpfulness |
| LoRA / QLoRA | low-cost adaptation | small GPUs par finetuning practical hoti hai | adapt without full retrain |

### Training lifecycle

| Stage | Input signal | Goal | Output |
|---|---|---|---|
| Pretraining | huge raw text/code corpus | language/world patterns learn karna | base model |
| SFT / instruction tuning | curated input-output pairs | helpful assistant behavior | instruction-following model |
| Preference tuning | winner-loser preference signal | tone, safety, alignment polish | aligned assistant |

### Memory breakdown during training

| Memory component | Kab use hota hai | Why it matters |
|---|---|---|
| Parameters | initialization onward | model size ka base footprint |
| Activations | forward pass | batch size / context length se blow up ho sakte hain |
| Gradients | backward pass | learning ke liye needed |
| Optimizer state | weight update | Adam jaisi methods extra memory leti hain |

### Data parallelism vs model parallelism vs ZeRO

| Method | Core idea | Strength | Limitation |
|---|---|---|---|
| Data parallelism | same model har GPU par, batch split | simple and common | state duplication zyada |
| Model parallelism | model khud GPUs me split | giant model fit karna | coordination complexity |
| ZeRO | redundant state shard karo | memory efficiency huge | system complexity |

### ZeRO stages

| Stage | Kya shard hota hai |
|---|---|
| ZeRO-1 | optimizer state |
| ZeRO-2 | optimizer state + gradients |
| ZeRO-3 | optimizer state + gradients + parameters |

### Full finetuning vs LoRA vs QLoRA

| Method | Kya train hota hai | Strength | Limitation |
|---|---|---|---|
| Full finetuning | saare weights | max flexibility | expensive |
| LoRA | low-rank adapters | low trainable params, task swapping easy | placement and LR matter |
| QLoRA | quantized frozen base + LoRA adapters | even lower VRAM | quantization complexity |

### Pretraining vs instruction tuning

| Question | Pretraining | Instruction tuning |
|---|---|---|
| Data scale | trillions of tokens | thousands to millions of examples |
| Goal | general knowledge | helpful behavior |
| Objective | next-token prediction | next-token prediction conditioned on instruction |
| Output style | factual but not necessarily helpful | assistant-like responses |

### One-line recall

- Lecture 4 ka main point: strong LLM banana model design se kam, training pipeline se zyada linked hai.
- Pretraining knowledge deta hai, SFT helpfulness deta hai.
- LoRA aur QLoRA ne adaptation ko practical banaya.

---

## Lecture 5

Memory hook:
`Preference data -> Reward model -> PPO / RLHF -> DPO`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| Preference tuning motivation | SFT ke baad bhi model misaligned ho sakta hai | helpfulness, tone, safety polish hoti hai | helpful != aligned enough |
| Preference data | answers compare karna easy hota hai | scalable signal milta hai | compare > write perfect answer |
| Reward modeling | `(prompt, response)` ko score karna | RLHF ka judge stage | train a scorer first |
| RLHF | reward maximize with policy updates | classic alignment pipeline | powerful but heavy |
| PPO | controlled RL updates | reward hacking se bachna | conservative RL |
| BoN | RL ko bypass karne ka workaround | simple lagta hai | inference expensive |
| DPO | supervised-style preference optimization | RLHF simplify hota hai | winner should beat loser |

### Preference data formats

| Format | Kya hota hai | Best use |
|---|---|---|
| Pointwise | har response ko score | ek single numeric quality score |
| Pairwise | do responses compare | RLHF / DPO ka core |
| Listwise | multiple responses rank | full ranking tasks |

### RLHF pipeline

| Step | Input | Output | Key idea |
|---|---|---|---|
| Reward modeling | prompt + candidate responses + preferences | reward score | better/worse learn karo |
| RL stage | prompt | improved policy | reward maximize karo, but base se bahut na hato |

### RLHF flow recall

| View | Flow | Memory line |
|---|---|---|
| Normal user | `prompt -> improved policy -> response` | user ko sirf final model dikhta hai |
| Model trainer | `prompt -> policy response -> reward model + KL check + value estimate -> PPO -> improved policy` | ye background training loop hota hai |

### PPO intuition

| Term | Meaning | Memory line |
|---|---|---|
| Reward | final quality signal | good response ko promote karo |
| Value function | expected reward estimate | baseline banata hai |
| Advantage | reward minus baseline | expected se kitna better nikla |
| KL control | base/reference se door jaane par penalty | reward hacking se bachao |

Memory shortcut:
`Reward = score, Value = expected score, Advantage = actual minus expected, KL = drift control`

### PPO-Clip vs PPO-KL

| Variant | Kaise control karta hai updates | Fast memory line |
|---|---|---|
| PPO-Clip | policy ratio clip karta hai | jump limit karo |
| PPO-KL | KL divergence penalty lagata hai | distribution drift punish karo |

Memory shortcut:
`Clip = update jump limit, KL = deviation penalty`

### RLHF vs DPO

| Topic | RLHF | DPO |
|---|---|---|
| Setup | multi-stage | supervised-style |
| Extra models | reward + value + reference | mainly reference model |
| Complexity | high | lower |
| Intuition | reward optimize through RL | winner ko loser se zyada probable banao |

Memory shortcut:
`RLHF = reward model + RL, DPO = preference pairs ko directly optimize`

### BoN vs RLHF

| Method | Benefit | Cost |
|---|---|---|
| BoN | training simpler | inference expensive |
| RLHF | policy itself improve hoti hai | training complex |

Memory shortcut:
`BoN = best sampled answer choose karo, RLHF = model ko hi better train karo`

### One-line recall

- Lecture 5 ne dikhaya ki alignment ka natural signal "best answer kaunsa hai?" hota hai.
- RLHF powerful hai but engineering-heavy hai.
- DPO ka pitch hai: preference learning ko supervised form me simplify karo.

---

## Lecture 6

Memory hook:
`Reasoning -> Verifiable rewards -> GRPO -> R1`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| Reasoning framing | answer-only se reasoning+answer output | harder tasks me intermediate steps useful | think before answer |
| Reasoning benchmarks | math/coding style verifiable tasks | reasoning ko objective way me score kar sakte hain | verification matters |
| Pass@k / Cons@k | multi-attempt evaluation | one-shot accuracy enough nahi | retries matter |
| Verifiable rewards | formatting + correctness | RL signal automate hota hai | measurable reasoning |
| GRPO | group-relative RL update | reasoning RL ko tailor karta hai | group baseline |
| Length pathology | RL output ko unnecessarily lamba bana sakta hai | optimization bug samajhna zaroori | longer != better |
| DeepSeek R1 | reasoning RL pipeline case study | RL-only vs hybrid recipe contrast | R1-Zero vs R1 |
| Distillation | reasoning traces students ko transfer | cheaper models me capability la sakte ho | copy the reasoning style |

### Old vs new output paradigm

| Paradigm | Flow |
|---|---|
| Earlier | `Question -> LLM -> Answer` |
| Reasoning model | `Question -> LLM -> Reasoning chain -> Answer` |

### Reasoning metrics

| Metric | Meaning | Best use |
|---|---|---|
| Pass@1 | single try success | one-shot setting |
| Pass@k | k attempts me at least 1 success | code / verifiable tasks |
| Cons@k | majority/consensus correctness | multi-sample reasoning |

### PPO vs GRPO

| Topic | PPO | GRPO |
|---|---|---|
| Baseline idea | value function / estimated advantage | group-average reward |
| Complexity | more classical RL setup | reasoning tasks me simpler framing |
| Intuition | expected reward se compare | same-prompt sample group se compare |

### Verifiable rewards

| Reward type | Example |
|---|---|
| Formatting reward | `<think> ... </think>` block present hai |
| Correctness reward | math answer sahi, tests pass |

### R1-Zero vs R1

| Model | Recipe | Strength | Weakness / note |
|---|---|---|---|
| R1-Zero | RL-only reasoning | proof that reasoning can emerge | formatting/readability issues |
| R1 | SFT + GRPO hybrid | more polished and general | more pipeline complexity |

Memory shortcut:
`R1-Zero = reasoning emerge ho sakti hai, R1 = reasoning ko clean aur general banana`

### R1-Zero -> R1 flow

```text
V3-Base
  -> GRPO with reasoning data
  -> R1-Zero
  -> long reasoning traces generate
  -> human clean-up / small SFT
  -> GRPO with reasoning data
  -> large SFT with reasoning + general data
  -> final GRPO with reasoning + non-reasoning rewards
  -> R1
```

Key clarification:
- `R1-Zero` ko dubara pretrain karna main idea nahi hai
- better view: `R1-Zero` proof-of-concept + reasoning-data source bana, aur usse polished hybrid pipeline se `R1` bana

### Distillation contrast

| Style | Simple meaning | Example |
|---|---|---|
| Classic distillation | student teacher ke token probabilities copy kare | teacher next word ke liye `cat` ko high probability deta hai, student bhi waise hi learn kare |
| Reasoning distillation | student teacher ka full solve-karne ka tareeka learn kare | teacher math solution me steps likhta hai, student un steps + final answer ka pattern SFT se learn kare |

### One-line recall

- Lecture 6 ka core idea: sirf prompt se kaam nahi chalta, strong reasoning ke liye RL + verifiable checks chahiye.
- GRPO PPO jaisa RL hai, but reasoning tasks me group-average baseline ki wajah se simpler lagta hai.
- R1-Zero ne dikhaya reasoning emerge ho sakti hai; R1 ne dikhaya use clean, stable, aur general kaise banana hai.

---

## Lecture 7

Memory hook:
`RAG -> Tool calling -> Agents`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| RAG motivation | pretrained model ka cutoff aur hallucination issue | external knowledge connect hota hai | memory enough nahi |
| Knowledge base creation | docs collect, chunk, embed | retrieval quality ki foundation | bad chunks, bad retrieval |
| Retrieval stages | candidate retrieval + reranking | recall aur precision alag optimize hote hain | broad fetch, then sort |
| Tool calling | model ko external functions use karna sikhana | compute, search, action possible | beyond text-only |
| Tool selection | tool overload ko route karna | latency aur quality improve hoti hai | show only relevant APIs |
| MCP | standard interface for model-tool connection | ecosystem integration easier | standardization matters |
| Agents / ReAct | observe-plan-act loop | single answer se autonomous workflow tak shift | looped behavior |
| A2A | multiple agents coordination | specialization scalable hoti hai | standard agent communication |

### RAG pipeline

| Step | Kya hota hai |
|---|---|
| Retrieve | relevant chunks dhoondo |
| Augment | prompt me retrieved context add karo |
| Generate | LLM augmented prompt par answer de |

### Candidate retrieval vs reranking

| Stage | Goal | Common methods | Key metric |
|---|---|---|---|
| Candidate retrieval | recall maximize | semantic search, BM25, hybrid | `Recall@k` |
| Reranking | precision / ordering improve | cross-encoder reranker | `Precision@k`, `NDCG@k`, `RR@k` |

### Retrieval methods

| Method | Strength | Weakness |
|---|---|---|
| Semantic search | concept match karta hai | exact lexical matches miss kar sakta hai |
| BM25 / keyword | exact term retrieval me strong | semantic mismatch me weak |
| Hybrid | dono worlds ka blend | more system complexity |

### RAG vs tool calling vs agents

| System | Kya karta hai | Best for |
|---|---|---|
| RAG | external text retrieve karta hai | knowledge grounding |
| Tool calling | function/API invoke karta hai | computation, search, actions |
| Agent | repeated observe-plan-act loop me kaam karta hai | multi-step autonomous tasks |

### ReAct loop

| Step | Meaning |
|---|---|
| Observe | kya pata hai, kya missing hai |
| Plan | next action decide karo |
| Act | tool ya action run karo |
| Repeat | new observation ke saath fir plan banao |

### Tool selection problem

| Problem | Solution |
|---|---|
| too many APIs prompt ko clutter karte hain | router pehle relevant subset choose kare |
| latency badhti hai | selected tool list chhota rakho |
| wrong tool affordance confusion | better routing + better API design |

### One-line recall

- RAG model ko extra knowledge deta hai.
- Tool calling model ko duniya ke saath interact karne deta hai.
- Agent un dono ko loop me daal kar goal pursue karta hai.

---

## Lecture 8

Memory hook:
`Human eval -> Rule metrics -> LLM-as-a-Judge -> Agent debugging -> Benchmarks`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| Human evaluation | gold-standard signal | high quality but expensive | best, but slow |
| Rule-based metrics | automatic scoring | cheap and scalable | narrow and brittle |
| LLM-as-a-Judge | flexible automated evaluation | rubric-based scalable judging | useful but biased |
| Structured judging | schema-based output | parse and aggregate easy | judge ko constrained rakho |
| Pointwise / pairwise | single-score vs A/B compare | evaluation mode select karna padta hai | compare or rate |
| Judge biases | position, verbosity, self-enhancement | naive judge unreliable ho sakta hai | judge the judge |
| Tool / agent evaluation | pipeline stage-wise debug | final answer enough nahi | trace failures |
| Benchmarks | capability slices | score ko context me samjho | maps, not territory |

### Human vs rule metrics vs LaaJ

| Method | Strength | Weakness | Best use |
|---|---|---|---|
| Human evaluation | richest signal | slow, costly, subjective | calibrated gold subset |
| Rule-based metrics | cheap, automatic | wording-sensitive, narrow | quick baseline checks |
| LLM-as-a-Judge | flexible, scalable, rationale de sakta hai | bias-prone | large-scale screening |

### Pointwise vs pairwise

| Mode | Kya karta hai | Best use | Trap |
|---|---|---|---|
| Pointwise | ek response ko absolute rate karta hai | rubric scoring, pass/fail | scale calibration hard |
| Pairwise | do responses compare karta hai | A/B, model comparisons | order bias aa sakta hai |

### Judge biases

| Bias | Problem | Remedy |
|---|---|---|
| Position bias | first option ko unfair edge | A/B and B/A dono score karo |
| Verbosity bias | lamba answer ko better maan lena | explicit rubric, length awareness |
| Self-enhancement bias | apni hi style/model ko prefer karna | same model ko judge + contestant mat banao |

### Good judging practice

| Practice | Why useful |
|---|---|
| structured output | parse reliable hota hai |
| low temperature | reproducibility better |
| rationale before score | more interpretable judgments |
| human calibration | judge drift check hota hai |

### Tool / agent failure map

| Layer | Failure examples | Fix direction |
|---|---|---|
| Tool prediction | tool call hi nahi kiya, wrong tool, wrong args | better router / prompting / SFT |
| Tool execution | backend wrong response, exception, empty output | tool implementation fix |
| Final synthesis | tool result sahi but answer galat summarize hua | better grounding / better output format |

### Benchmark map

| Benchmark family | Example | Kya measure karta hai |
|---|---|---|
| Knowledge | MMLU | breadth of knowledge |
| Reasoning | AIME, PIQA | multi-step or commonsense reasoning |
| Coding | SWE-bench | real repo software engineering |
| Safety | HarmBench | harmful compliance risk |
| Agents | tau-bench | tool-using multi-step reliability |

### Benchmark warnings

| Risk | Meaning |
|---|---|
| Data contamination | test data training me leak ho gaya |
| Goodhart's Law | metric ko target banaoge to metric misleading ho jayega |
| Pareto tradeoff | best model depends on cost, quality, latency, safety balance |

### One-line recall

- Evaluation khud ek engineering problem hai.
- LLM judge useful hai, but calibrated aur bias-aware hona chahiye.
- Agent systems ko final answer se nahi, full pipeline trace se evaluate karo.

---

## Lecture 9

Memory hook:
`Course recap -> Multimodal transformers -> Diffusion LLMs -> Future frontiers`

### What changed across the lecture?

| Part | Kya seekha | Kyun important hai | Quick memory line |
|---|---|---|---|
| Course rewind | lectures 1-8 ko connect kiya | full arc clear hota hai | foundations to deployment |
| ViT | images ko patch tokens bana kar transformer me feed kiya | transformer text ke bahar gaya | image as token sequence |
| VLM | image + text combine karke answer generation | multimodal AI standard direction hai | see + speak |
| ARM limitation | token-by-token decoding sequential hai | inference bottleneck reveal hota hai | one token at a time |
| Diffusion LLM | masked refinement alternative | faster decoding direction | refine many positions together |
| Future frontiers | hardware, multimodality, safety, personalization | field still open hai | lots unsolved |

### ViT vs VLM

| Model | Input | Output | Core idea |
|---|---|---|---|
| ViT | image patches | class / visual representation | image ko token sequence treat karo |
| VLM | image + text | text response | vision and language ko combine karo |

### ARM vs diffusion-style text modeling

| Topic | ARM | Diffusion / MDM |
|---|---|---|
| Generation style | left-to-right next token | masked tokens ko repeatedly refine karo |
| Parallelism | inference sequential | more joint refinement possible |
| Current maturity | mainstream default | active research frontier |
| Pitch | strong ecosystem and quality | speed and alternate decoding dynamics |

### Diffusion LLM intuition

| Stage | Image world | Text world |
|---|---|---|
| Forward process | noise add karna | masking / corruption |
| Reverse process | denoise karna | masked text recover karna |

### Future frontier checklist

| Frontier | Why important |
|---|---|
| cross-modal idea sharing | ek modality ki trick dusri me transfer ho sakti hai |
| hardware co-design | performance sirf model se nahi, systems se bhi aata hai |
| safety and hallucination | deployment ka main bottleneck |
| personalization / continuous learning | current systems ki weak spot |

### One-line recall

- Lecture 9 ka message: Transformers ab sirf text model nahi rahe.
- Diffusion LLMs sequential decoding ka serious alternative explore kar rahe hain.
- Field mature lagti hai, but foundational research abhi khatam nahi hui.

---

## Course Summary: Lecture 1-9

| Bucket | Lectures | Core idea |
|---|---|---|
| Foundations | 1-3 | text representation, Transformer, LLM generation and serving |
| Training and alignment | 4-6 | pretraining, SFT, preference tuning, reasoning RL |
| Systems and future | 7-9 | RAG, tools, agents, evaluation, multimodality, diffusion |

### Final 9-lecture memory chain

- Lecture 1: text ko vectors aur sequence model me badlo.
- Lecture 2: Transformer ko stable, positional, aur encoder-friendly banao.
- Lecture 3: decoder-only LLM ko generate aur serve karna samjho.
- Lecture 4: pretraining aur efficient finetuning stack samjho.
- Lecture 5: human preferences se alignment sikhao.
- Lecture 6: reasoning ko verifiable rewards aur RL se scale karo.
- Lecture 7: model ko external knowledge aur tools se jodo.
- Lecture 8: quality ko measure, judge, aur debug karna seekho.
- Lecture 9: text se bahar jao aur next research frontiers dekho.

---

## Formula Sheet

Ye section quick revision ke liye hai. Har formula ke saath:
- `Where used` = kis lecture/topic me aata hai
- `Why used` = formula ka job kya hai
- `Mini example` = yaad rakhne ke liye chhota use case

### 1. Scaled Dot-Product Attention

`Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`

| Field | Note |
|---|---|
| Where used | Lecture 1-2, Transformer self-attention |
| Why used | query ko sab keys se compare karke relevant values ka weighted mix banata hai |
| Why divide by `sqrt(d_k)` | raw dot products bahut bade ho jate hain; softmax saturate na ho isliye scaling hoti hai |
| Mini example | agar token `bear` ko `cute` aur `reading` dono se relation chahiye, attention un dono ko higher weight de sakta hai |

### 2. Softmax

`p_i = exp(z_i) / sum_j exp(z_j)`

| Field | Note |
|---|---|
| Where used | Lecture 1-3, attention scores aur next-token probabilities |
| Why used | raw logits ko probability distribution me convert karta hai |
| Mini example | logits `[2, 1, 0]` me first token ki probability sabse zyada hogi |

### 3. Relative Attention Bias

`Attention = softmax(<q_m, k_n> / sqrt(d_k) + bias(m, n))`

| Field | Note |
|---|---|
| Where used | Lecture 2, relative position methods |
| Why used | attention score me distance information inject karne ke liye |
| Mini example | near tokens ko extra positive bias ya far tokens ko penalty mil sakti hai |

### 4. ALiBi

`bias(m, n) = mu * (n - m)`

| Field | Note |
|---|---|
| Where used | Lecture 2, linear relative bias |
| Why used | distance badhne par attention naturally reduce karna |
| Mini example | agar current token se koi token 10 positions dur hai, uska bias 2 positions dur token se zyada negative hoga |

### 5. RoPE Rotation

`R(theta, m) = [cos(m*theta)  -sin(m*theta); sin(m*theta)  cos(m*theta)]`

and key idea:

`q_m^T k_n` relative distance `(n - m)` par depend kar sakta hai

| Field | Note |
|---|---|
| Where used | Lecture 2, RoPE positional encoding |
| Why used | absolute position add karne ke bajay query/key ko rotate karke relative position capture karna |
| Mini example | position 5 aur 3 ka relation same tarah model ho sakta hai jaise 105 aur 103 ka, kyunki relative gap same hai |

### 6. Pre-Norm and Post-Norm

Post-Norm:

`Output = LayerNorm(x + SubLayer(x))`

Pre-Norm:

`Output = x + SubLayer(LayerNorm(x))`

| Field | Note |
|---|---|
| Where used | Lecture 2, Transformer block design |
| Why used | normalization se training stable hoti hai |
| Why Pre-Norm matters | deep transformers me gradients zyada stable rehte hain |
| Mini example | modern LLM blocks often Pre-Norm use karte hain taaki training blow up na kare |

### 7. RMSNorm

`RMSNorm(x) = gamma * x / sqrt(mean(x^2) + epsilon)`

| Field | Note |
|---|---|
| Where used | Lecture 2, modern normalization |
| Why used | vector magnitude normalize karke training stable rakhna, but LayerNorm se cheaper hona |
| Mini example | agar vector values bahut large hain, RMSNorm unhe controlled scale par le aata hai |

### 8. Distillation KL Loss

`Loss = KL(y_T || y_S) = sum_i y_T^(i) * log(y_T^(i) / y_S^(i))`

| Field | Note |
|---|---|
| Where used | Lecture 2, DistilBERT style distillation |
| Why used | student model ko teacher distribution imitate karane ke liye |
| Mini example | teacher bol raha hai token probs `[0.7, 0.2, 0.1]`; student ko bhi similar distribution seekhni hai |

### 9. Bradley-Terry Preference Probability

`p(y_i > y_j) = exp(r_i) / (exp(r_i) + exp(r_j)) = sigma(r_i - r_j)`

| Field | Note |
|---|---|
| Where used | Lecture 5, reward modeling |
| Why used | do responses me kaunsa better hai, usko reward scores se probability form me express karna |
| Mini example | agar `r_i = 3` aur `r_j = 1` hai, toh response `i` ke preferred hone ki probability zyada hogi |

### 10. Advantage Estimate

`Advantage ~= Reward - Baseline`

| Field | Note |
|---|---|
| Where used | Lecture 5 PPO, Lecture 6 reasoning RL intuition |
| Why used | actual result expected result se kitna better ya worse tha, ye measure karna |
| Mini example | reward `0.9` aur baseline `0.5` ho to advantage positive hai, so action ko encourage karo |

### 11. PPO-Clip Objective

`L_clip(theta) = E[min(r_t(theta) A_t, clip(r_t(theta), 1-eps, 1+eps) A_t)]`

where

`r_t(theta) = pi_theta(a_t | s_t) / pi_old(a_t | s_t)`

| Field | Note |
|---|---|
| Where used | Lecture 5, RLHF |
| Why used | policy update ko bahut aggressive hone se rokna |
| Mini example | naya policy ratio bahut high ho gaya to `clip` us jump ko limit kar deta hai |

### 12. PPO with KL Penalty

`L_klpen(theta) = E[r_t(theta) A_t - beta * KL(pi_old(. | s_t), pi_theta(. | s_t))]`

| Field | Note |
|---|---|
| Where used | Lecture 5, RLHF stability |
| Why used | base ya old policy se bahut zyada drift ko punish karna |
| Mini example | agar model reward chase karte hue weird outputs dene lage, KL term use anchor karta hai |

### 13. DPO Loss

`L_DPO = -E[log sigma(beta * ((log(pi_theta(y_w|x)/pi_ref(y_w|x))) - (log(pi_theta(y_l|x)/pi_ref(y_l|x)))))]`

| Field | Note |
|---|---|
| Where used | Lecture 5, Direct Preference Optimization |
| Why used | winner response ko loser se zyada likely banana, without full RL loop |
| Mini example | same prompt par better answer ko model higher probability de, worse answer ko lower probability de |

### 14. GRPO Advantage

`Advantage ~= Reward - Avg(reward of group)`

| Field | Note |
|---|---|
| Where used | Lecture 6, GRPO |
| Why used | same prompt ke multiple sampled outputs me relative winner identify karna |
| Mini example | 4 responses ke rewards `[0.9, 0.7, 0.4, 0.2]` hain, avg `0.55` hai; first response ka advantage positive hai |

### 15. Precision@k

`Precision@k = (# relevant items in top-k) / k`

| Field | Note |
|---|---|
| Where used | Lecture 7 retrieval, Lecture 8 evaluation mindset |
| Why used | top-k retrieved results kitne clean/relevant hain ye measure karna |
| Mini example | top-5 me 4 relevant chunks mile to `Precision@5 = 4/5 = 0.8` |

### 16. Recall@k

`Recall@k = (# relevant items in top-k) / (total relevant items)`

| Field | Note |
|---|---|
| Where used | Lecture 7 candidate retrieval |
| Why used | system ne kitne relevant chunks cover kiye, ye dekhna |
| Mini example | total 10 relevant chunks the, top-5 me 4 mil gaye, to `Recall@5 = 4/10 = 0.4` |

### 17. Reciprocal Rank

`RR = 1 / rank_of_first_relevant_item`

| Field | Note |
|---|---|
| Where used | Lecture 7 retrieval evaluation |
| Why used | pehla useful result kitni jaldi aaya, ye measure karna |
| Mini example | first relevant chunk rank 2 par hai, to `RR = 1/2 = 0.5` |

### 18. Pass@k Intuition

`Pass@k = probability that at least 1 of k attempts succeeds`

| Field | Note |
|---|---|
| Where used | Lecture 6 reasoning/coding evaluation |
| Why used | multi-try systems ko fair way me evaluate karna |
| Mini example | agar model 5 code attempts deta hai aur unme se ek sahi test pass karta hai, task Pass@5 me successful mana jayega |

### Formula Memory Shortcuts

| Formula family | Memory shortcut |
|---|---|
| Attention | compare -> normalize -> mix |
| Positional methods | distance inject karo |
| Normalization | scale control karo |
| Distillation | student ko teacher jaisa banao |
| Preference learning | winner ko loser se upar rakho |
| RL | reward lo, but too far mat jao |
| Retrieval metrics | top-k me kitna sahi mila |
