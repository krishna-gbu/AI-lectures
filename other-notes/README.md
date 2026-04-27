# Other Notes Roadmap

Ye folder `MIT 15.773` lecture notes ka replacement nahi hai. Ye ek focused `Transformer deep-dive + implementation prep` folder hai.

Primary rule:

- `mit-15773-deep-learning/hinglish-notes/` = broad Deep Learning course map
- `other-notes/` = Transformer specialization track

## Best Order

Recommended order:

1. [01_paper_explanation.md](./01_paper_explanation.md)
2. [02_mathematics.md](./02_mathematics.md)
3. [04_math_worksheet.md](./04_math_worksheet.md)
4. [05_implementation_guide.md](./05_implementation_guide.md)
5. [06_implementation_todo.md](./06_implementation_todo.md)

Reference-only files:

- [00_paper_hinglish_translation.md](./00_paper_hinglish_translation.md)
- [03_mathematics_complete.md](./03_mathematics_complete.md)
- [07_pca.md](./07_pca.md)

## File Roles

| File | Use | When to read |
|---|---|---|
| `00_paper_hinglish_translation.md` | direct translation of the paper | only when you want original-paper wording |
| `01_paper_explanation.md` | best conceptual explanation of the paper | start here |
| `02_mathematics.md` | embeddings, similarity, tokenization, padding, masking math | after paper intuition |
| `03_mathematics_complete.md` | giant reference encyclopedia | only when stuck on a topic |
| `04_math_worksheet.md` | pen-and-paper transformer practice | after basic math understanding |
| `05_implementation_guide.md` | component-by-component implementation roadmap | before coding |
| `06_implementation_todo.md` | execution checklist and milestone tracker | during coding |
| `07_pca.md` | deep PCA supplement | only if embedding visualization needs detail |

## What To Do Now

Ab best next step theory aur add karna nahi hai. Best next step:

1. `01` ko read karo for architecture intuition.
2. `02` me embedding, cosine similarity, padding, masking clear karo.
3. `04` ke `Section 1` se `Section 9` tak hand-solve karo.
4. `05` me scaled dot-product attention aur multi-head attention flow read karo.
5. `06` ke Milestone 1 se actual coding start karo.

Execution bridge:

- coding scaffold created at [../transformer-from-scratch/README.md](../transformer-from-scratch/README.md)

## Suggested Study Loop

Day 1:

- `01_paper_explanation.md`
- `02_mathematics.md` until cosine similarity

Day 2:

- rest of `02_mathematics.md`
- `04_math_worksheet.md` Part A and Part B

Day 3:

- `05_implementation_guide.md`
- `transformer-from-scratch` Milestone 1 code

## What Not To Do

- `03_mathematics_complete.md` ko line-by-line primary book mat banao.
- `00_paper_hinglish_translation.md` se start mat karo.
- implementation start karne se pehle aur naye notes collect mat karo.

## Known Gaps

- Kuch older notes companion scripts ka mention karte hain, but wo files workspace me present nahi hain.
- Isliye real coding path ke liye `transformer-from-scratch` folder ko active source of truth rakho.
