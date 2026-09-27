# CS-3: Advancements in Large Language Model Architecture

## Comprehensive Guide to Modern LLM Innovations

---

## Part 1: Understanding Architecture Evolution (Pages 1-5)

### What is Architecture?

**Architecture** = The blueprint or design of how an LLM is structured.

**Analogy:**
- A house can be built in many ways:
  - Traditional design: Standard walls, doors, windows
  - Modern design: Open floor plan, smart features
  - Both are houses, but designed differently
- Similarly, LLMs can be built with different designs:
  - Original Transformer (2017)
  - Modern variants with improvements

### Why Improve Architecture?

**Problems with Original Transformer:**

1. **Slow:** Processing is sequential on long texts
2. **Memory Hungry:** Attention mechanism memory grows with sequence length squared
3. **Inefficient:** Lots of unnecessary computation
4. **Limited Context:** Can't handle extremely long documents

**Solutions (Modern Advancements):**

1. **Faster attention mechanisms:** Process more efficiently
2. **Sparse attention:** Only attend to relevant tokens, not all
3. **Grouped operations:** Process tokens together
4. **Efficient normalizations:** Reduce computational overhead

### Section 1: Slide 5 Deep Dive

**Slide 5 Content: RMSNorm**

**What is Layer Normalization?**

Original Transformer used LayerNorm to stabilize training:

```
For each position, normalize:
Output = (Value - Mean) / (StdDev + epsilon) × Weight + Bias
```

Problem:
- Computes mean AND standard deviation
- Computing both takes computation
- Mean isn't always necessary

**What is RMSNorm (Root Mean Square Norm)?**

Simplified version:
```
Output = Value / RMS(Value) × Weight
```

Where RMS = √(mean of squares)

**Benefits:**

1. **Faster:** RMS is simpler to compute than mean + stddev
2. **Same effectiveness:** Works as well as LayerNorm
3. **Fewer parameters:** No bias term needed
4. **Better for large models:** Optimization improvements compound

**Real-World Impact:**

- LLaMA models use RMSNorm
- Saves ~30% computation on normalization
- With billions of normalizations, this adds up!

**Intuition:**

Think of RMSNorm as a simplified version of LayerNorm:
- LayerNorm: Careful quality control (measure everything)
- RMSNorm: Good enough quality control (measure just scale)

Both work well, but RMSNorm is faster.

---

## Part 2: Major Architectural Innovations (Pages 6-15)

### Innovation 1: Grouped Query Attention (GQA)

**Problem with Multi-Head Attention:**

Original Transformer uses many attention heads:
```
Q: 64 heads, each attending separately
K (keys): 64 heads
V (values): 64 heads
```

This requires storing many separate attention representations.

**Grouped Query Attention Solution:**

```
Q: 64 heads (independent)
K: 8 heads (shared groups)
V: 8 heads (shared groups)
```

"Group" the K and V heads:
- Multiple query heads share one key and value head
- Reduces computation and memory
- Maintains quality (queries still independent)

**Analogy:**

Imagine a teacher with 64 student groups:
- Original: Each group gets independent notes
- GQA: 8 master notes, with 8 groups sharing each

**Impact:**
- LLaMA uses this
- Reduces KV cache size ~8x
- Faster inference (especially with long sequences)

### Innovation 2: Rotary Position Encoding (RoPE)

**Problem with Original Position Encoding:**

Original Transformers added position information:
```
Position 1: Add [1, 0, 0, 0, ...]
Position 2: Add [0, 1, 0, 0, ...]
Position 3: Add [0, 0, 1, 0, ...]
```

Problem: Doesn't generalize to longer sequences than training saw

**Rotary Position Encoding:**

Instead of adding position, rotate the embedding:
```
Embedding at position N = Embedding × Rotation_Matrix(N)
```

**Benefits:**
1. **Extrapolates:** Works well on sequences longer than training
2. **Relative positions:** Focus on distance between tokens, not absolute
3. **Better performance:** Improves model capabilities

**Intuition:**

Imagine GPS coordinates:
- Absolute position: "I'm at latitude 40, longitude -74"
  - Doesn't help if I move to a different city
- Relative position: "I'm 5 miles north and 3 miles east of the center"
  - Works anywhere you are

RoPE is more like relative positions.

### Innovation 3: Swiglu Activation

**What are Activations?**

After linear transformation, use a non-linear function:
```
Output = Activation(Linear(Input))
```

Common activations:
- ReLU: max(0, x)
- GELU: Smooth version of ReLU

**Original Transformer:**
```
Linear → GELU → Linear
```

**Swiglu:**
```
Linear → Swiglu gate
```

Swiglu combines:
- Gating mechanism (decide what to pass)
- Swish activation (smooth gating)
- Learned weights for flexibility

**Why Better?**

- GELU: Fixed function
- Swiglu: Learned gating function

The model learns what activation to apply!

**Analogy:**

- GELU: A fixed valve that lets water through at certain pressure
- Swiglu: A smart valve that adjusts based on what water is coming

---

## Part 3: Advanced Normalization Techniques (Pages 16-25)

### Beyond RMSNorm: Layerwise Adaptive Rate Scaling (LARS)

**Problem:**

Different layers learn at different rates:
- Early layers: Learn quickly
- Middle layers: Medium speed
- Late layers: Learn slowly

Using same learning rate for all isn't optimal.

**LARS Solution:**

Adaptive learning rate per layer:
```
For each layer:
  Learning_rate = global_lr × (layer_norm / gradient_norm)
```

**Effect:**
- Fast layers get slower learning rate
- Slow layers get faster learning rate
- Better balance

### The Role of Temperature in Training

**Temperature Parameter:**

Used in softmax when creating attention weights:

```
Attention_weights = Softmax(Scores / Temperature)
```

- High temperature: Softer attention (spread out)
- Low temperature: Sharper attention (focused)

**During Training:**

- Warm-up phase: Higher temperature (explore broadly)
- Main training: Lower temperature (focus on good solutions)
- Can improve convergence

### Normalization in Different Contexts

**In Embeddings:**
- Normalize all embeddings to same scale
- Helps stability at start of model

**In Hidden States:**
- Normalize between layers
- Prevents explosion or vanishing values
- Most important effect

**In Output:**
- Optional, but helps stability
- Especially important for numerical stability

**Intuition:**

Normalizations are like shock absorbers:
- Without them: Vibrations grow, system becomes unstable
- With them: Vibrations absorbed, smooth operation

---

## Part 4: Efficiency Innovations (Pages 26-35)

### Flash Attention: The Game-Changer

**Section 4: Slide 30 - Flash Attention Deep Dive**

**Problem with Standard Attention:**

Standard implementation:
```
1. Compute all Q×K^T (attention scores for all pairs)
2. Store in memory (N×N matrix, huge!)
3. Apply softmax
4. Multiply by values
```

For 12K token sequence:
- Attention matrix: 12K × 12K = 144 million entries
- Memory: ~580 MB just for attention matrix
- On A100 GPU: Out of Memory error!

**Root Cause:**

The intermediate N×N matrix must fit in fast memory (HBM).

With long sequences, this matrix is enormous.

**Flash Attention Solution:**

Process attention in blocks, streaming to fast memory:

```
Instead of:
  Compute: All(Q×K^T) → Store → Softmax → Multiply by V

Do:
  For each block of tokens:
    Compute: Block(Q×K^T) → Softmax → Multiply by V
    Stream to/from memory
    Accumulate results
```

**Benefits:**
- Same result (mathematically identical)
- Much less peak memory usage
- Faster (reduction in memory bottlenecks)
- Enables longer sequences

**Real Impact:**

Example from slide:
- **Without Flash Attention:** 12K token prompt causes OOM
- **With Flash Attention:** Same model runs fine
- **No weight changes:** Model behavior identical
- **Key insight:** Architecture, not algorithm, was the problem

**Why This Matters:**

Flash Attention is now standard in modern models:
- LLaMA uses it
- Latest models assume it
- Enables practical long-context models

**Intuition:**

Original attention: Try to see the whole library at once
Flash attention: Look at sections of library sequentially, combine results

Same view of library, different approach.

### Sparse Attention

**Motivation:**

In long sequences, model doesn't need all tokens:

```
"The quick brown fox jumps over the lazy dog..."
"...In fact, the fox was actually quite smart..."

When reading second sentence, word "dog" from first sentence isn't crucial.
```

**Sparse Attention Idea:**

Don't compute attention between all pairs. Only compute for "nearby" or "important" tokens.

**Common Patterns:**

1. **Local attention:** Token attends to nearby tokens only
   - Token position 10 attends to positions 8-12
   - Reduces computation to O(n × window_size)

2. **Strided attention:** Token attends to every Kth token
   - Token position 10 attends to positions 0, 5, 10, 15, 20...
   - Reduces computation

3. **Combination:** Mix local and strided attention

**Trade-off:**

- Faster: Sparse attention is faster
- Quality: Might miss important long-range relationships
- Best: Use for specific layers, not all

### Efficient Position Embeddings

**Challenge with Long Sequences:**

Position encodings trained on 2K token contexts might break at 32K tokens.

**Solutions:**

1. **Interpolation:** Scale position indices
2. **ALiBi (Attention with Linear Biases):** Simpler approach, adds bias instead of encoding
3. **NTK (Non-Trainable Kernel):** Mathematical approach to extrapolate positions

**Effect:**

Enable models to handle longer contexts than training without full retraining.

---

## Part 5: Architectural Innovations for Scale (Pages 36-45)

### Mixture of Experts (MoE)

**Basic Idea:**

Instead of using all parameters for every input, use different experts for different inputs:

```
Input → Router → Expert 1 (selected for this input)
     ↙ → Expert 2 (not used for this input)
      ↘ → Expert 3 (selected for this input)
```

**Benefits:**

1. **Parameter efficiency:** Not all parameters used every time
2. **Specialization:** Each expert learns different skills
3. **Scalability:** Can add experts without increasing per-token cost

**Example:**

Imagine writing an essay:
- All paragraphs: English grammar expert (all tokens)
- Tech paragraphs: Also use CS expert
- Biology paragraphs: Also use biology expert

Different experts for different content.

**Challenges:**

- Load balancing: Need all experts used approximately equally
- Training complexity: Routing decisions need to be learned
- Inference: Need to know which experts to use

### Section 4: Slide 30 - Advanced Routing

**Slide Content: Token Choice and Load Balancing**

Modern routing strategies:

1. **Top-1 Routing:** Each token goes to best expert
   - Deterministic
   - Simple
   - Can lead to imbalance

2. **Top-K Routing:** Each token goes to K best experts
   - More robust
   - Combines multiple experts
   - More computation

**Load Balancing:**

Techniques to ensure all experts are used:

1. **Auxiliary loss:** Penalize if experts are imbalanced
2. **Token Choice:** Each expert chooses which tokens to accept
   - Each expert picks top tokens instead of token picking expert
   - More control over load

**Practical Example:**

Consider 8 experts:

**Top-1 Routing (bad distribution):**
```
Expert 1: 50% of tokens (overloaded)
Expert 2: 40% of tokens
Expert 3: 5% of tokens
Expert 4-8: 1% each (underutilized)
```

**With Load Balancing (good distribution):**
```
Expert 1: 12.5% of tokens
Expert 2: 12.5% of tokens
...
Expert 8: 12.5% of tokens (balanced)
```

**Trade-off:**

Perfect balance might not be optimal (some experts are better for some tokens), but balance prevents collapse.

---

## Part 6: Modern Model Examples (Pages 46-50)

### LLaMA: Production Architecture

LLaMA's architectural choices:

1. **RMSNorm:** For efficiency
2. **Rotary Embeddings:** For better generalization
3. **Grouped Query Attention:** For faster inference
4. **Swiglu:** For better expressiveness
5. **Flash Attention:** For handling sequences

**Result:**
- 65B LLaMA > 175B GPT-3 in many tasks
- Much less compute needed
- Production-ready models possible

### Recent Trends (2023-2024)

1. **Smaller, Better Models:** Better training data > larger models
2. **Open Source:** LLaMA, OLMo enable innovation
3. **Inference Optimization:** Flash Attention, KV cache reduction
4. **Context Length:** Increasing from 2K to 100K+ tokens
5. **Multimodal:** Adding vision to language models

---

## Part 7: Summary and Future Directions (Pages 51-55)

### Key Architectural Principles

| Principle | Implementation | Benefit |
|-----------|-----------------|---------|
| **Efficiency** | RMSNorm, GQA | Lower compute cost |
| **Generalization** | RoPE, better embeddings | Works on longer sequences |
| **Expressiveness** | Swiglu, better activations | More powerful models |
| **Speed** | Flash Attention | Faster inference |
| **Specialization** | Mixture of Experts | Scaling without cost increase |

### Understanding the Trend

Modern architectures focus on:
1. **Efficiency:** Do more with less compute
2. **Scalability:** Grow without quadratic costs
3. **Robustness:** Work in diverse scenarios
4. **Practicality:** Actually deployable

The key insight: The fundamentals (Transformers) are solid, but engineering matters enormously.

### Quiz: Test Your Understanding

**Q1:** Why does RMSNorm work better than LayerNorm for large models?
- A: RMSNorm is mathematically better
- B: RMSNorm is faster to compute with similar results
- C: RMSNorm requires fewer parameters
- **Answer: B** - Efficiency without sacrificing quality

**Q2:** What problem does Flash Attention solve?
- A: Slow matrix multiplication
- B: Large intermediate attention matrix requiring excessive memory
- C: Incorrect attention computation
- **Answer: B** - The N×N matrix was the bottleneck

**Q3:** Grouped Query Attention improves by reducing which of the following?
- A: Query heads
- B: Key and value head count (through sharing)
- C: All attention heads equally
- **Answer: B** - Shares K and V heads across query groups

---

**End of CS-3: Advancements in Large Language Model Architecture**

*Understanding these architectural innovations is crucial for understanding why modern models are more efficient and capable. The next courses cover training optimization (CS-4) and inference (CS 5-6).*
