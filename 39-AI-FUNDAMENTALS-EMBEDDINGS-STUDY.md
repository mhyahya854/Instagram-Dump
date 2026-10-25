# 39 — One-Day AI Fundamentals: Embeddings and Meaning as Vectors

Captured 2026-10-25. The spoken reel says “go to this website and click Start,” then describes text embeddings and the famous king − man + woman ≈ queen analogy. **Exact original website unidentified.** Listed learning sites below are comparable independent examples, not claimed to be the creator's page.

## Plain-English explanation

Computers operate on numeric representations. A **token** is a word, subword or other text unit; a **token embedding** is a learned vector of numbers representing that token in a model's internal feature space. A sentence/document embedding encodes text as a vector that can be compared to others. Contextual models can produce different representations for a token depending on surrounding words.

A **vector** is an ordered numerical list, e.g. [0.2, −0.8, 0.5, ...]. Each dimension is learned, not typically a human-readable “happiness coordinate.” In suitable trained spaces, semantically related items often cluster by cosine similarity or related measures, though “closer” depends on model/task/normalization.

## What the famous analogy illustrates (and does not)

In some static word embedding systems, vector(king) − vector(man) + vector(woman) lies near vector(queen). This is a *demonstration of learned relation directions*, **not a universal law**: results depend on training data, model, tokenization, vocabulary and inherent gender stereotypes. Modern contextual token representations do not always support the same simple linear arithmetic interpretation.

## Small worked toy example (illustrative numbers, not trained model weights)

Suppose we deliberately assign two interpretable dimensions: first = royalty (0 ordinary, 1 royal), second = traditionally feminine label (0 male-coded, 1 female-coded).

- man = [0, 0]
- woman = [0, 1]
- king = [1, 0]
- queen = [1, 1]

Then king − man + woman = [1, 0] − [0, 0] + [0, 1] = [1, 1] = queen.

In real embeddings, vectors often have hundreds or thousands of learned dimensions; labels, stereotypes and relations are much less clean.

## Beginner learning path that fits in a study day (not a mastery promise)

1. **Tokens and prediction:** how strings become tokens; language models predict token distributions.
2. **Embeddings:** numbers capture learned patterns; distinguish static vs contextual and tokens vs sentences.
3. **Similarity and search:** compare document vectors with cosine similarity; understand retrieval errors.
4. **Attention and transformers:** contextual information changes token interpretation; don't assume attention equals explanation.
5. **Generation and evaluation:** sampling temperature, hallucinations, model version, reference/citation and task-specific tests.
6. **Agent tools and trust:** an AI model is not the browser/database; external tools have access boundaries and require permissions.
7. **Practical task:** encode a small document set, rank queries, inspect false positives and describe what your model failed to retrieve.

## Related, real interactive resources (not verified as reel's original)

- https://www.doc.ic.ac.uk/~nuric/demos/word2vec_demo.html — academic Word2Vec learning demo; train on supplied corpus and visualize vector neighbors.
- https://wordcanvas3d.vercel.app/ — interactive tokenizer/embedding/vector playground with source https://github.com/Akage1234/WordCanvas3D.
- https://prod.bigspark.ai/learn/demos/ — embedding explanation demo; multiple learning modules.
- https://bitbootcamp.com/play/embeddings — intuition, vector examples and guided exercises.

## Privacy and correctness caveats

Embedding models can encode bias, private details and domain confusions. Similarity does not prove factual accuracy; RAG must link back to authoritative document content. Don't load personal/confidential documents into a random online demo. Local execution still needs model weights and suitable runtime.

## Future offline archive

Preserve this explanation, toy arithmetic and mini exercises in text. External interactive demos and their model weights won't be available offline from a Markdown hyperlink alone.
