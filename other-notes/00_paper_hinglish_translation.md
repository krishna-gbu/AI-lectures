# Attention Is All You Need - Hinglish Translation

> Original Paper: Vaswani et al., NIPS 2017
> Ye paper ka direct Hinglish translation hai - koi extra explanation nahi hai.

---

## Authors

Ashish Vaswani (Google Brain), Noam Shazeer (Google Brain), Niki Parmar (Google Research), Jakob Uszkoreit (Google Research), Llion Jones (Google Research), Aidan N. Gomez (University of Toronto), Lukasz Kaiser (Google Brain), Illia Polosukhin

*Sabka equal contribution hai. Listing order random hai.*

---

## Abstract

Jo dominant sequence transduction models hain wo complex recurrent ya convolutional neural networks pe based hain jinme ek encoder aur ek decoder hota hai. Jo sabse accha perform karne wale models hain wo encoder aur decoder ko ek attention mechanism ke through connect karte hain. Hum ek nayi simple network architecture propose karte hain, the Transformer, jo purely attention mechanisms pe based hai, recurrence aur convolutions ko poori tarah se hata diya gaya hai. Do machine translation tasks pe experiments dikhate hain ki ye models quality mein superior hain jabki zyada parallelizable hain aur significantly kam time mein train hote hain. Hamara model WMT 2014 English-to-German translation task pe 28.4 BLEU achieve karta hai, jo existing best results (including ensembles) se 2 BLEU se zyada better hai. WMT 2014 English-to-French translation task pe, hamara model ek naya single-model state-of-the-art BLEU score 41.0 establish karta hai, sirf 3.5 din ki training ke baad aath GPUs pe, jo literature ke best models ki training costs ka ek chhota sa fraction hai.

---

## 1 Introduction

Recurrent neural networks, khaas taur pe long short-term memory [12] aur gated recurrent [7] neural networks, sequence modeling aur transduction problems jaise language modeling aur machine translation [29, 2, 5] mein state of the art approaches ke roop mein firmly establish ho chuke hain. Tab se bahut saare efforts ne recurrent language models aur encoder-decoder architectures [31, 21, 13] ki boundaries ko push karna jaari rakha hai.

Recurrent models typically input aur output sequences ki symbol positions ke saath computation ko factor karte hain. Positions ko computation time ke steps se align karke, ye hidden states h_t ki ek sequence generate karte hain, jo previous hidden state h_{t-1} aur position t ke input ka function hota hai. Ye inherently sequential nature training examples ke andar parallelization ko rok deti hai, jo longer sequence lengths pe critical ho jaata hai, kyunki memory constraints examples ke across batching ko limit kar dete hain. Recent work ne factorization tricks [18] aur conditional computation [26] ke through computational efficiency mein significant improvements achieve ki hain, jabki latter ke case mein model performance bhi improve hui hai. Lekin sequential computation ki fundamental constraint abhi bhi bani hui hai.

Attention mechanisms various tasks mein compelling sequence modeling aur transduction models ka ek integral part ban gaye hain, jo input ya output sequences mein unki distance ki chinta kiye bina dependencies ko model karne ki permission dete hain [2, 16]. Lekin kuch cases [22] ko chhod kar, aise attention mechanisms ek recurrent network ke saath conjunction mein use hote hain.

Is kaam mein hum Transformer propose karte hain, ek model architecture jo recurrence ko chhod deta hai aur input aur output ke beech global dependencies draw karne ke liye poori tarah se ek attention mechanism pe rely karta hai. Transformer significantly zyada parallelization allow karta hai aur sirf barah ghante ki training ke baad aath P100 GPUs pe translation quality mein ek naya state of the art reach kar sakta hai.

---

## 2 Background

Sequential computation ko reduce karne ka goal Extended Neural GPU [20], ByteNet [15] aur ConvS2S [8] ki foundation bhi hai, ye sab convolutional neural networks ko basic building block ke roop mein use karte hain, saari input aur output positions ke liye parallel mein hidden representations compute karte hain. In models mein, do arbitrary input ya output positions se signals ko relate karne ke liye required operations ki sankhya positions ke beech ki distance ke saath badhti hai, ConvS2S ke liye linearly aur ByteNet ke liye logarithmically. Isse distant positions ke beech dependencies seekhna mushkil ho jaata hai [11]. Transformer mein ye ek constant number of operations tak reduce ho jaata hai, halaanki attention-weighted positions ko average karne se reduced effective resolution ki cost pe, ek effect jisko hum Multi-Head Attention se counteract karte hain jaisa section 3.2 mein describe kiya gaya hai.

Self-attention, jise kabhi kabhi intra-attention bhi kehte hain, ek attention mechanism hai jo ek single sequence ki different positions ko relate karta hai taaki sequence ki ek representation compute ho sake. Self-attention ko kai tasks mein successfully use kiya gaya hai jinme reading comprehension, abstractive summarization, textual entailment aur task-independent sentence representations seekhna shaamil hai [4, 22, 23, 19].

End-to-end memory networks ek recurrent attention mechanism pe based hain sequence-aligned recurrence ki jagah aur simple-language question answering aur language modeling tasks pe accha perform karte dikhaye gaye hain [28].

Hamari jaankaari ke mutaabiq, Transformer pehla transduction model hai jo poori tarah se self-attention pe rely karta hai apne input aur output ki representations compute karne ke liye bina sequence-aligned RNNs ya convolution use kiye. Aage ke sections mein, hum Transformer describe karenge, self-attention ko motivate karenge aur [14, 15] aur [8] jaise models ke upar iske advantages discuss karenge.

---

## 3 Model Architecture

Zyaadatar competitive neural sequence transduction models mein ek encoder-decoder structure hota hai [5, 2, 29]. Yahaan, encoder ek input sequence of symbol representations (x1, ..., xn) ko continuous representations ki ek sequence z = (z1, ..., zn) mein map karta hai. z diye jaane pe, decoder phir ek output sequence (y1, ..., ym) of symbols generate karta hai ek element ek time pe. Har step pe model auto-regressive [9] hai, pehle se generate kiye gaye symbols ko next generate karte waqt additional input ke roop mein consume karta hai.

Transformer is overall architecture ko follow karta hai stacked self-attention aur point-wise, fully connected layers use karke encoder aur decoder dono ke liye, jo Figure 1 ke left aur right halves mein dikhaya gaya hai, respectively.

### 3.1 Encoder aur Decoder Stacks

**Encoder:** Encoder N = 6 identical layers ke ek stack se bana hai. Har layer ke do sub-layers hain. Pehla ek multi-head self-attention mechanism hai, aur doosra ek simple, position-wise fully connected feed-forward network hai. Hum har do sub-layers ke around ek residual connection [10] employ karte hain, jiske baad layer normalization [1] aata hai. Matlab, har sub-layer ka output LayerNorm(x + Sublayer(x)) hai, jahaan Sublayer(x) wo function hai jo sub-layer khud implement karta hai. In residual connections ko facilitate karne ke liye, model ke saare sub-layers, saath hi embedding layers, d_model = 512 dimension ke outputs produce karte hain.

**Decoder:** Decoder bhi N = 6 identical layers ke ek stack se bana hai. Har encoder layer ke do sub-layers ke alawa, decoder ek teesra sub-layer insert karta hai, jo encoder stack ke output pe multi-head attention perform karta hai. Encoder ki tarah, hum har sub-layers ke around residual connections employ karte hain, jiske baad layer normalization aata hai. Hum decoder stack mein self-attention sub-layer ko bhi modify karte hain taaki positions ko subsequent positions pe attend karne se roka ja sake. Ye masking, is fact ke saath combine hoke ki output embeddings ek position se offset hain, ensure karta hai ki position i ke liye predictions sirf i se kam positions pe known outputs pe depend kar sakte hain.

### 3.2 Attention

Ek attention function ko ek query aur key-value pairs ke ek set ko ek output mein map karne ke roop mein describe kiya ja sakta hai, jahaan query, keys, values, aur output sab vectors hain. Output values ka ek weighted sum ke roop mein compute hota hai, jahaan har value ko assign kiya gaya weight query ke saath corresponding key ki ek compatibility function se compute hota hai.

#### 3.2.1 Scaled Dot-Product Attention

Hum apne particular attention ko "Scaled Dot-Product Attention" kehte hain (Figure 2). Input mein d_k dimension ke queries aur keys hain, aur d_v dimension ki values hain. Hum query ke saath saari keys ke dot products compute karte hain, har ek ko sqrt(d_k) se divide karte hain, aur values pe weights obtain karne ke liye ek softmax function apply karte hain.

Practice mein, hum attention function ko ek saath queries ke ek set pe compute karte hain, jo ek matrix Q mein packed hote hain. Keys aur values bhi matrices K aur V mein packed hote hain. Hum outputs ka matrix aise compute karte hain:

```
Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V     ... (1)
```

Do sabse zyada commonly used attention functions hain additive attention [2], aur dot-product (multiplicative) attention. Dot-product attention hamari algorithm ke identical hai, sirf 1/sqrt(d_k) ke scaling factor ko chhod kar. Additive attention compatibility function ko ek single hidden layer wale feed-forward network se compute karta hai. Jabki dono theoretical complexity mein similar hain, dot-product attention practice mein bahut faster aur zyada space-efficient hai, kyunki ise highly optimized matrix multiplication code se implement kiya ja sakta hai.

Jabki d_k ki chhoti values ke liye dono mechanisms similarly perform karte hain, additive attention d_k ki badi values ke liye bina scaling ke dot product attention se outperform karta hai [3]. Humara andaaza hai ki d_k ki badi values ke liye, dot products magnitude mein bade ho jaate hain, softmax function ko un regions mein push karte hain jahaan uske paas extremely small gradients hote hain. Is effect ko counteract karne ke liye, hum dot products ko 1/sqrt(d_k) se scale karte hain.

> Footnote: Ye illustrate karne ke liye ki dot products kyun bade hote hain, maano ki q aur k ke components independent random variables hain jinke mean 0 aur variance 1 hai. Tab unka dot product, q . k = sum(q_i * k_i) for i=1 to d_k, ka mean 0 aur variance d_k hai.

#### 3.2.2 Multi-Head Attention

d_model-dimensional keys, values aur queries ke saath ek single attention function perform karne ki jagah, humne ye beneficial paaya ki queries, keys aur values ko h baar different, learned linear projections ke saath d_k, d_k aur d_v dimensions mein linearly project kiya jaaye. In projected versions ke har ek pe hum attention function parallel mein perform karte hain, d_v-dimensional output values yield karte hain. Inhe concatenate kiya jaata hai aur ek baar phir project kiya jaata hai, resulting in final values, jaisa Figure 2 mein dikhaya gaya hai.

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
jahaan head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
```

Jahaan projections parameter matrices hain W_i^Q jo R^{d_model x d_k} mein hai, W_i^K jo R^{d_model x d_k} mein hai, W_i^V jo R^{d_model x d_v} mein hai aur W^O jo R^{h*d_v x d_model} mein hai.

Is kaam mein hum h = 8 parallel attention layers, ya heads employ karte hain. Inme se har ek ke liye hum d_k = d_v = d_model/h = 64 use karte hain. Har head ki reduced dimension ki wajah se, total computational cost full dimensionality ke saath single-head attention ke similar hai.

#### 3.2.3 Hamare Model mein Attention ke Applications

Transformer multi-head attention ko teen different tareekon se use karta hai:

- "Encoder-decoder attention" layers mein, queries previous decoder layer se aate hain, aur memory keys aur values encoder ke output se aate hain. Ye decoder mein har position ko input sequence ki saari positions pe attend karne ki permission deta hai. Ye sequence-to-sequence models [31, 2, 8] mein typical encoder-decoder attention mechanisms ki nakal karta hai.

- Encoder mein self-attention layers hain. Ek self-attention layer mein saari keys, values aur queries ek hi jagah se aate hain, is case mein, encoder ki previous layer ka output. Encoder mein har position encoder ki previous layer ki saari positions pe attend kar sakta hai.

- Isi tarah, decoder mein self-attention layers decoder mein har position ko decoder ki saari positions pe us position tak aur usse including attend karne ki permission dete hain. Humein decoder mein leftward information flow ko rokna hoga taaki auto-regressive property preserve ho sake. Hum ise scaled dot-product attention ke andar implement karte hain softmax ke input mein un saari values ko mask out karke (minus infinity set karke) jo illegal connections se correspond karti hain. Figure 2 dekho.

### 3.3 Position-wise Feed-Forward Networks

Attention sub-layers ke alawa, hamare encoder aur decoder ki har layer mein ek fully connected feed-forward network hai, jo har position pe separately aur identically apply hota hai. Ye do linear transformations se bana hai jinke beech ek ReLU activation hai.

```
FFN(x) = max(0, x W_1 + b_1) W_2 + b_2     ... (2)
```

Jabki linear transformations different positions pe same hain, ye layer se layer different parameters use karte hain. Ise describe karne ka doosra tareeqa hai kernel size 1 ke do convolutions ke roop mein. Input aur output ki dimensionality d_model = 512 hai, aur inner-layer ki dimensionality d_ff = 2048 hai.

### 3.4 Embeddings aur Softmax

Doosre sequence transduction models ki tarah, hum input tokens aur output tokens ko d_model dimension ke vectors mein convert karne ke liye learned embeddings use karte hain. Hum decoder output ko predicted next-token probabilities mein convert karne ke liye usual learned linear transformation aur softmax function bhi use karte hain. Hamare model mein, hum do embedding layers aur pre-softmax linear transformation ke beech same weight matrix share karte hain, [24] ke similar. Embedding layers mein, hum un weights ko sqrt(d_model) se multiply karte hain.

### 3.5 Positional Encoding

Kyunki hamare model mein na recurrence hai aur na convolution, model ko sequence ke order ka use karne ke liye, humein tokens ki relative ya absolute position ke baare mein kuch information inject karni padegi. Is liye, hum encoder aur decoder stacks ke neeche input embeddings mein "positional encodings" add karte hain. Positional encodings ki dimension embeddings ke same d_model hai, taaki dono ko sum kiya ja sake. Positional encodings ke bahut se choices hain, learned aur fixed [8].

Is kaam mein, hum different frequencies ki sine aur cosine functions use karte hain:

```
PE(pos, 2i)     = sin(pos / 10000^(2i/d_model))
PE(pos, 2i + 1) = cos(pos / 10000^(2i/d_model))
```

Jahaan pos position hai aur i dimension hai. Matlab, positional encoding ki har dimension ek sinusoid se correspond karti hai. Wavelengths 2*pi se 10000*2*pi tak ek geometric progression form karti hain. Humne ye function isliye choose kiya kyunki humara hypothesis tha ki ye model ko relative positions se attend karna aasaani se seekhne dega, kyunki kisi bhi fixed offset k ke liye, PE_{pos+k} ko PE_{pos} ke ek linear function ke roop mein represent kiya ja sakta hai.

Humne learned positional embeddings [8] use karne ka bhi experiment kiya, aur paaya ki dono versions ne lagbhag identical results produce kiye (Table 3 row (E) dekho). Humne sinusoidal version isliye choose kiya kyunki ye model ko training ke dauran encounter ki gayi sequence lengths se lambi sequence lengths tak extrapolate karne ki permission de sakta hai.

---

## 4 Self-Attention Kyun

Is section mein hum self-attention layers ke various aspects ki comparison recurrent aur convolutional layers se karte hain jo commonly use hote hain ek variable-length sequence of symbol representations (x1, ..., xn) ko ek equal length ki doosri sequence (z1, ..., zn) mein map karne ke liye, jahaan x_i, z_i R^d mein hain, jaise ek typical sequence transduction encoder ya decoder mein ek hidden layer. Self-attention ke use ko motivate karte hue hum teen desiderata consider karte hain.

Pehla hai per layer total computational complexity. Doosra hai computation ki wo amount jo parallelized ho sakti hai, jo minimum number of sequential operations required se measure hoti hai.

Teesra hai network mein long-range dependencies ke beech path length. Long-range dependencies seekhna bahut se sequence transduction tasks mein ek key challenge hai. In dependencies ko seekhne ki ability ko affect karne wala ek key factor network mein forward aur backward signals ko traverse karne wale paths ki length hai. Input aur output sequences mein positions ke kisi bhi combination ke beech ye paths jitne chhote honge, long-range dependencies seekhna utna aasan hoga [11]. Isliye hum different layer types se bane networks mein kisi bhi do input aur output positions ke beech maximum path length ki bhi comparison karte hain.

Table 1 mein note kiya gaya hai:

| Layer Type | Complexity per Layer | Sequential Operations | Maximum Path Length |
|---|---|---|---|
| Self-Attention | O(n^2 . d) | O(1) | O(1) |
| Recurrent | O(n . d^2) | O(n) | O(n) |
| Convolutional | O(k . n . d^2) | O(1) | O(log_k(n)) |
| Self-Attention (restricted) | O(r . n . d) | O(1) | O(n/r) |

Jaisa Table 1 mein note kiya gaya, ek self-attention layer saari positions ko constant number of sequentially executed operations ke saath connect karta hai, jabki ek recurrent layer ko O(n) sequential operations chahiye. Computational complexity ke terms mein, self-attention layers recurrent layers se faster hain jab sequence length n representation dimensionality d se chhoti hai, jo machine translations mein state-of-the-art models ke saath use hone wali sentence representations ke saath aksar hota hai, jaise word-piece [31] aur byte-pair [25] representations. Bahut lambi sequences wale tasks ke liye computational performance improve karne ke liye, self-attention ko respective output position ke around centered input sequence mein sirf size r ki ek neighborhood consider karne tak restrict kiya ja sakta hai. Ye maximum path length ko O(n/r) tak badha dega. Hum is approach ko future work mein aur investigate karne ka plan karte hain.

Kernel width k < n wali ek single convolutional layer input aur output positions ke saare pairs ko connect nahi karti. Aisa karne ke liye contiguous kernels ke case mein O(n/k) convolutional layers ka ek stack chahiye, ya dilated convolutions [15] ke case mein O(log_k(n)), jo network mein kisi bhi do positions ke beech longest paths ki length badhata hai. Convolutional layers generally recurrent layers se zyada expensive hain, k ke factor se. Separable convolutions [6], however, complexity ko considerably decrease karte hain, O(k . n . d + n . d^2) tak. Lekin k = n ke saath bhi, separable convolution ki complexity ek self-attention layer aur ek point-wise feed-forward layer ke combination ke equal hai, jo approach hum apne model mein lete hain.

Ek side benefit ke roop mein, self-attention zyada interpretable models yield kar sakta hai. Hum apne models se attention distributions inspect karte hain aur appendix mein examples present aur discuss karte hain. Na sirf individual attention heads clearly different tasks perform karna seekhte hain, bahut se sentences ki syntactic aur semantic structure se related behavior exhibit karte dikhte hain.

---

## 5 Training

Ye section hamare models ke liye training regime describe karta hai.

### 5.1 Training Data aur Batching

Humne standard WMT 2014 English-German dataset pe train kiya jisme lagbhag 4.5 million sentence pairs hain. Sentences ko byte-pair encoding [3] se encode kiya gaya, jiska ek shared source-target vocabulary lagbhag 37000 tokens ka hai. English-French ke liye, humne significantly bada WMT 2014 English-French dataset use kiya jisme 36M sentences hain aur tokens ko 32000 word-piece vocabulary [31] mein split kiya. Sentence pairs ko approximate sequence length ke hisaab se ek saath batch kiya gaya. Har training batch mein sentence pairs ka ek set tha jisme lagbhag 25000 source tokens aur 25000 target tokens the.

### 5.2 Hardware aur Schedule

Humne apne models ko 8 NVIDIA P100 GPUs wali ek machine pe train kiya. Hamare base models ke liye poore paper mein describe kiye gaye hyperparameters use karke, har training step mein lagbhag 0.4 seconds lage. Humne base models ko total 100,000 steps ya 12 ghante tak train kiya. Hamare big models ke liye (Table 3 ki bottom line mein describe kiya gaya), step time 1.0 second tha. Big models ko 300,000 steps (3.5 din) ke liye train kiya gaya.

### 5.3 Optimizer

Humne Adam optimizer [17] use kiya beta_1 = 0.9, beta_2 = 0.98 aur epsilon = 10^-9 ke saath. Humne training ke course pe learning rate ko vary kiya, is formula ke mutaabiq:

```
lrate = d_model^(-0.5) . min(step_num^(-0.5), step_num . warmup_steps^(-1.5))     ... (3)
```

Ye pehle warmup_steps training steps ke liye learning rate ko linearly increase karne se correspond karta hai, aur uske baad step number ke inverse square root ke proportionally decrease karne se. Humne warmup_steps = 4000 use kiya.

### 5.4 Regularization

Hum training ke dauran teen types ki regularization employ karte hain:

**Residual Dropout:** Hum har sub-layer ke output pe dropout [27] apply karte hain, isse pehle ki ye sub-layer input mein add ho aur normalized ho. Iske alawa, hum encoder aur decoder dono stacks mein embeddings aur positional encodings ke sums pe dropout apply karte hain. Base model ke liye, hum P_drop = 0.1 ki rate use karte hain.

**Label Smoothing:** Training ke dauran, humne epsilon_ls = 0.1 ki value ka label smoothing [30] employ kiya. Ye perplexity ko hurt karta hai, kyunki model zyada unsure hona seekhta hai, lekin accuracy aur BLEU score improve hote hain.

---

## 6 Results

### 6.1 Machine Translation

WMT 2014 English-to-German translation task pe, big transformer model (Table 2 mein Transformer (big)) best previously reported models (including ensembles) ko 2.0 BLEU se zyada se outperform karta hai, 28.4 ka ek naya state-of-the-art BLEU score establish karta hai. Is model ka configuration Table 3 ki bottom line mein listed hai. Training mein 8 P100 GPUs pe 3.5 din lage. Hamara base model bhi saare previously published models aur ensembles ko surpass karta hai, kisi bhi competitive model ki training cost ke ek fraction pe.

WMT 2014 English-to-French translation task pe, hamara big model 41.0 ka BLEU score achieve karta hai, saare previously published single models ko outperform karta hai, previous state-of-the-art model ki training cost ke 1/4 se bhi kam pe. English-to-French ke liye train kiye gaye Transformer (big) model ne 0.3 ki jagah P_drop = 0.1 dropout rate use kiya.

Base models ke liye, humne last 5 checkpoints ko average karke ek single model use kiya, jo 10-minute intervals pe likhe gaye the. Big models ke liye, humne last 20 checkpoints average kiye. Humne beam search use kiya beam size 4 aur length penalty alpha = 0.6 [31] ke saath. Ye hyperparameters development set pe experimentation ke baad choose kiye gaye. Humne inference ke dauran maximum output length ko input length + 50 set kiya, lekin jab possible ho tab jaldi terminate kiya [31].

Table 2 hamare results summarize karta hai aur hamari translation quality aur training costs ki comparison literature ke doosre model architectures se karta hai. Hum ek model ko train karne mein use hone wale floating point operations ki sankhya estimate karte hain training time, use kiye gaye GPUs ki sankhya, aur har GPU ki sustained single-precision floating-point capacity ke estimate ko multiply karke.

**Table 2: Transformer previous state-of-the-art models se better BLEU scores achieve karta hai**

| Model | BLEU EN-DE | BLEU EN-FR | Training Cost EN-DE | Training Cost EN-FR |
|---|---|---|---|---|
| ByteNet [15] | 23.75 | | | |
| GNMT + RL [31] | 24.6 | 39.92 | 2.3 . 10^19 | 1.4 . 10^20 |
| ConvS2S [8] | 25.16 | 40.46 | 9.6 . 10^18 | 1.5 . 10^20 |
| MoE [26] | 26.03 | 40.56 | 2.0 . 10^19 | 1.2 . 10^20 |
| GNMT + RL Ensemble [31] | 26.30 | 41.16 | 1.8 . 10^20 | 1.1 . 10^21 |
| ConvS2S Ensemble [8] | 26.36 | 41.29 | 7.7 . 10^19 | 1.2 . 10^21 |
| **Transformer (base)** | **27.3** | **38.1** | **3.3 . 10^18** | |
| **Transformer (big)** | **28.4** | **41.0** | **2.3 . 10^19** | |

### 6.2 Model Variations

Transformer ke different components ki importance evaluate karne ke liye, humne apne base model ko different tareekon se vary kiya, English-to-German translation pe development set, newstest2013 pe performance mein change measure kiya. Humne previous section mein describe kiya gaya beam search use kiya, lekin checkpoint averaging nahi kiya. Hum ye results Table 3 mein present karte hain.

Table 3 rows (A) mein, hum attention heads ki sankhya aur attention key aur value dimensions vary karte hain, computation ki amount constant rakhte hue, jaisa Section 3.2.2 mein describe kiya gaya. Jabki single-head attention best setting se 0.9 BLEU worse hai, quality bahut zyada heads ke saath bhi drop hoti hai.

**Table 3: Transformer architecture pe Variations**

| | N | d_model | d_ff | h | d_k | d_v | P_drop | epsilon_ls | train steps | PPL (dev) | BLEU (dev) | params x10^6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 6 | 512 | 2048 | 8 | 64 | 64 | 0.1 | 0.1 | 100K | 4.92 | 25.8 | 65 |
| big | 6 | 1024 | 4096 | 16 | | | 0.3 | | 300K | 4.33 | 26.4 | 213 |

Table 3 rows (B) mein, hum observe karte hain ki attention key size d_k ko reduce karna model quality ko hurt karta hai. Ye suggest karta hai ki compatibility determine karna aasan nahi hai aur dot product se zyada sophisticated compatibility function beneficial ho sakta hai. Hum rows (C) aur (D) mein aur observe karte hain ki, expected ke mutaabiq, bade models better hain, aur dropout over-fitting avoid karne mein bahut helpful hai. Row (E) mein hum apni sinusoidal positional encoding ko learned positional embeddings [8] se replace karte hain, aur base model se lagbhag identical results observe karte hain.

---

## 7 Conclusion

Is kaam mein, humne Transformer present kiya, pehla sequence transduction model jo poori tarah se attention pe based hai, encoder-decoder architectures mein sabse zyada commonly use hone wali recurrent layers ko multi-headed self-attention se replace karta hai.

Translation tasks ke liye, Transformer recurrent ya convolutional layers pe based architectures se significantly faster train ho sakta hai. WMT 2014 English-to-German aur WMT 2014 English-to-French dono translation tasks pe, hum ek naya state of the art achieve karte hain. Former task mein hamara best model saare previously reported ensembles ko bhi outperform karta hai.

Hum attention-based models ke future ke baare mein excited hain aur unhe doosre tasks pe apply karne ka plan karte hain. Hum Transformer ko text ke alawa input aur output modalities wali problems tak extend karne ka plan karte hain aur large inputs aur outputs jaise images, audio aur video ko efficiently handle karne ke liye local, restricted attention mechanisms investigate karne ka plan karte hain. Generation ko kam sequential banana hamara ek aur research goal hai.

Hamare models ko train aur evaluate karne ke liye use kiya gaya code https://github.com/tensorflow/tensor2tensor pe available hai.

**Acknowledgements:** Hum Nal Kalchbrenner aur Stephan Gouws ke fruitful comments, corrections aur inspiration ke liye grateful hain.

---

## References

[1] Ba et al. Layer normalization. 2016.
[2] Bahdanau et al. Neural machine translation by jointly learning to align and translate. 2014.
[3] Britz et al. Massive exploration of neural machine translation architectures. 2017.
[4] Cheng et al. Long short-term memory-networks for machine reading. 2016.
[5] Cho et al. Learning phrase representations using RNN encoder-decoder for statistical machine translation. 2014.
[6] Chollet. Xception: Deep learning with depthwise separable convolutions. 2016.
[7] Chung et al. Empirical evaluation of gated recurrent neural networks on sequence modeling. 2014.
[8] Gehring et al. Convolutional sequence to sequence learning. 2017.
[9] Graves. Generating sequences with recurrent neural networks. 2013.
[10] He et al. Deep residual learning for image recognition. 2016.
[11] Hochreiter et al. Gradient flow in recurrent nets: the difficulty of learning long-term dependencies. 2001.
[12] Hochreiter & Schmidhuber. Long short-term memory. 1997.
[13] Jozefowicz et al. Exploring the limits of language modeling. 2016.
[14] Kaiser & Sutskever. Neural GPUs learn algorithms. 2016.
[15] Kalchbrenner et al. Neural machine translation in linear time. 2017.
[16] Kim et al. Structured attention networks. 2017.
[17] Kingma & Ba. Adam: A method for stochastic optimization. 2015.
[18] Kuchaiev & Ginsburg. Factorization tricks for LSTM networks. 2017.
[19] Lin et al. A structured self-attentive sentence embedding. 2017.
[20] Kaiser. Can active memory replace attention? 2016.
[21] Luong et al. Effective approaches to attention-based neural machine translation. 2015.
[22] Parikh et al. A decomposable attention model. 2016.
[23] Paulus et al. A deep reinforced model for abstractive summarization. 2017.
[24] Press & Wolf. Using the output embedding to improve language models. 2016.
[25] Sennrich et al. Neural machine translation of rare words with subword units. 2015.
[26] Shazeer et al. Outrageously large neural networks: The sparsely-gated mixture-of-experts layer. 2017.
[27] Srivastava et al. Dropout: a simple way to prevent neural networks from overfitting. 2014.
[28] Sukhbaatar et al. End-to-end memory networks. 2015.
[29] Sutskever et al. Sequence to sequence learning with neural networks. 2014.
[30] Szegedy et al. Rethinking the inception architecture for computer vision. 2015.
[31] Wu et al. Google's neural machine translation system. 2016.
[32] Zhou et al. Deep recurrent models with fast-forward connections for neural machine translation. 2016.
