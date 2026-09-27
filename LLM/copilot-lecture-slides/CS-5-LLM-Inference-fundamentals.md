# CS-5: LLM Inference Fundamentals

## Comprehensive Guide to Running Large Language Models

---

## Part 1: Understanding Inference (Pages 1-5)

### What is Inference?

**Definition:**

Inference is the process of running a trained model to generate predictions or outputs.

**Comparison:**

- **Training:** Teaching the model (expensive, one-time)
- **Inference:** Using the model to make predictions (cheap, repeated)

**Analogy:**

Think of a university:
- **Training:** Study for 4 years (expensive in time and money)
- **Inference:** Use your knowledge to solve problems (cheap, can do repeatedly)

### Inference vs. Training: Key Differences

| Aspect | Training | Inference |
|--------|----------|-----------|
| **Cost** | Millions | Cents |
| **Frequency** | Once | Millions of times |
| **Hardware** | Many GPUs | Few GPUs or CPUs |
| **Optimization** | Accuracy | Speed + Cost |
| **Memory** | Massive | Moderate |
| **Power** | Huge | Lower |

### Why Inference Optimization Matters

**Real-World Example:**

ChatGPT serving millions of users:

- Cost without optimization: $100 million/month
- Cost with optimization: $10 million/month (90% savings!)

**The Inference Equation:**

```
Cost = (Time per Request) × (Number of Requests) × (Hardware Cost per Unit Time)
```

Optimize any factor:
- Faster inference → Lower cost
- Better efficiency → Lower hardware cost
- Better batching → Higher throughput

### Section 1: Slide 5 - Inference Process

**Slide 5 Content: Two-Phase Inference Process**

**Phase 1: Prefill (Processing Prompt)**

```
Input: "Translate to French: Hello, how are you?"
       ↓
Tokenize: [Translate, to, French, :, Hello, ...]
       ↓
Batch Process: All tokens at once
       ↓
Output: 48 heads of attention, embeddings computed
```

Key characteristics:
- Process all input tokens simultaneously
- Compute attention across all tokens at once
- High computation per token
- Latency: Depends on prompt length

**Phase 2: Generation (Producing Output)**

```
Input (from prefill): Hidden states from prompt processing
       ↓
Generate: Predict one token at a time
       ↓
Reprocess: Token 1 produced
           Reprocess with token 1 to produce token 2
           Reprocess with tokens 1+2 to produce token 3
       ↓
Continue: Until model says "end"
```

Key characteristics:
- Generate one token per step
- Each step requires reprocessing all previous tokens
- Higher latency per token
- Low computation per token (one forward pass)

**Why Two Phases?**

Different computational characteristics:
- Prefill: Compute-bound (lots of math needed)
- Generation: Memory-bound (need to read model weights many times)

Different optimizations apply to each!

---

## Part 2: The Generation Process (Pages 6-15)

### Autoregressive Generation

**What is Autoregressive?**

"Auto" (self) + "regressive" (predicting from past).

Model predicts next word using:
- Prompt (if first token)
- Previous generated words

**Process Example:**

```
Step 1:
  Input: "Write a poem about"
  Output: "Write a poem about [love]"
  
Step 2:
  Input: "Write a poem about love"
  Output: "Write a poem about love [by]"

Step 3:
  Input: "Write a poem about love by"
  Output: "Write a poem about love by [Shakespeare]"

Step 4:
  Input: "Write a poem about love by Shakespeare"
  Output: "Write a poem about love by Shakespeare [a]"
  
... continues until [END]
```

### Greedy Decoding vs. Sampling

**Greedy Decoding:**

Always pick the most likely next token:

```
Model predicts:
  "love": 45%
  "poetry": 20%
  "beauty": 15%
  "others": 20%

Pick: "love" (highest probability)
```

**Characteristics:**
- Deterministic (same input → same output)
- Sometimes boring (doesn't explore alternatives)
- Fast (no randomness)
- Good for factual tasks

**Sampling (Temperature Control):**

Sample from probability distribution (not always pick max):

```
Low temperature (0.1):
  "love": 95%  ← Almost always picked
  "poetry": 3%
  "beauty": 2%

High temperature (2.0):
  "love": 20%
  "poetry": 20%
  "beauty": 20%
  "others": 40%  ← More diverse options
```

**Characteristics:**
- Stochastic (random element)
- More creative (explores alternatives)
- Slower (sampling overhead)
- Good for creative tasks

**Temperature Intuition:**

Temperature controls "randomness":
- 0: Most certain predictions
- 1: Natural probabilities
- 2+: Very random, might not make sense

### Top-K and Top-P Sampling

**Problem with Basic Sampling:**

At high temperature, can generate nonsensical tokens:

```
Model outputs:
  "love": 20%
  "[UNK]": 5%
  "asfasdf": 3%
  "🎪": 2%

With temperature 2.0, we might pick "[UNK]"!
```

**Top-K Sampling:**

Only consider top K most likely tokens:

```
K=10 means: Consider only top 10 tokens
Ignore the rest

Result: Only reasonable tokens considered
```

**Top-P (Nucleus) Sampling:**

Consider tokens with cumulative probability ≥ P:

```
"love": 30% ← included
"poetry": 25% ← included
"beauty": 20% ← included
"words": 15% ← included
"emotion": 5% ← included (total = 95%, ≥ 90%)
"joy": 2% ← excluded (would be 97%)
"others": remaining
```

**Why These Work:**

Prevents catastrophic failures while maintaining diversity.

---

## Part 3: Sequence Length and Context (Pages 16-25)

### The KV Cache Problem

**What is KV Cache?**

During generation, need to reprocess all previous tokens:

```
Step 1: Process "hello" → Extract Key, Value
Step 2: Process "hello how" → Re-extract Key, Value for "hello" (waste!)
                             → Extract Key, Value for "how"
Step 3: Process "hello how are" → Re-extract for "hello", "how" (waste!)
                                → Extract for "are"
```

Redundant computation!

**Solution: Cache Keys and Values**

```
Step 1: Process "hello" → Store Key, Value in cache
Step 2: Use cached KV for "hello", process "how" → Add to cache
Step 3: Use cached KV for "hello" + "how", process "are" → Add to cache
```

Result: Massive speedup!

**KV Cache Size:**

```
For one token: (# layers) × (# heads) × (hidden dim per head) × 2 (K and V)

GPT-3 (96 layers, 96 heads, 128 dims):
  Per token: 96 × 96 × 128 × 2 = 2.4 MB per token
  
For 2000 token sequence:
  2.4 MB × 2000 = 4.8 GB just for KV cache!
```

**Implication:**

KV cache can dominate memory usage, limiting sequence length!

### Attention Complexity with Long Sequences

**Computing Attention is Expensive:**

```
Attention = Softmax(Q × K^T) × V
```

For sequence of length N:
- Q × K^T: N × N matrix (N² operations!)
- With 12,000 tokens: 144 million operations just for this!

**Memory Requirements:**

N × N matrix in memory:
```
2000 tokens: 4M entries → 16 MB (fine)
12000 tokens: 144M entries → 576 MB (manageable)
100000 tokens: 10B entries → 40 GB (out of memory!)
```

The intermediate attention matrix becomes the bottleneck!

### Context Length in Modern Models

**Training Context:**
- Original Transformers: 2K tokens
- GPT-3: 2K tokens
- Recent models: 4K-32K tokens
- Latest models: 100K+ tokens

**How to Extend Context:**

1. **Simple interpolation:** Scale position indices
2. **Rotary Position Embeddings:** Naturally extrapolate
3. **Retrieval Augmented Generation:** Don't store all context, retrieve relevant parts

**Trade-off:**

Longer context = More memory, more compute per token

Shorter context = Limited information, might miss context

---

## Part 4: Batch Processing (Pages 26-35)

### Batch Processing for Efficiency

**Problem with Single Requests:**

```
Request 1: Takes 2 seconds
Request 2: Takes 2 seconds (overlaps with Request 1)
Request 3: Takes 2 seconds (overlaps)
...

If handled sequentially: 2s per request
If handled in parallel: 2s for all (batching)
```

**Batching Efficiency:**

```
Single request latency: 2s
Batch of 32 requests: 2s total (0.0625s per request on average!)
```

### Continuous Batching

**Problem with Traditional Batching:**

```
Request A: Done after 1s
Request B: Done after 2s
Request C: Done after 3s

Wait for all to finish: Total time = 3s

But we could have started processing new requests
as soon as A was done!
```

**Continuous Batching Solution:**

```
Time 0: A, B, C start
Time 1: A finishes
        Add request D to batch
        Batch now: B, C, D
Time 2: B finishes
        Add requests E, F to batch
        Batch now: C, D, E, F
...
```

Result: Better GPU utilization, faster overall throughput!

### Batching Strategy Considerations

**Batch Size Effects:**

```
Batch Size | Latency | Throughput | Memory
1          | Lowest  | Lowest     | Lowest
8          | Medium  | Better     | Higher
32         | Higher  | Best       | Highest
64         | Highest | Stays same | Too much?
```

**Sweet Spot:**

Usually batch size of 8-32 is optimal.

Balance between:
- Latency (don't want too long)
- Throughput (want high)
- Memory (can't exceed GPU memory)

### Static vs. Dynamic Batching

**Static Batching:**

All requests processed for fixed length:

```
Requests: A (10 tokens), B (50 tokens), C (30 tokens)
Process all for max(50) = 50 steps
Waste: 40 + 0 + 20 = 60 token steps wasted
```

**Dynamic Batching (Continuous Batching):**

Remove requests when done:

```
Time 0-10: Process A, B, C for 10 steps
           A done, add D
Time 10-30: Process B, C, D for 20 steps
           C done, add E
Time 30-50: Process B, D, E for 20 steps
           B done
...
```

Less waste, higher efficiency!

---

## Part 5: Quantization and Optimization (Pages 36-45)

### Model Quantization

**Problem:**

Modern models use float32 or float16 (32 or 16 bits per number):

```
GPT-3 (175B params) in float32: 175B × 4 bytes = 700 GB!
```

This is massive!

**Quantization Idea:**

Use fewer bits:

```
float32 (32 bits): Range -3.4e38 to 3.4e38 (huge range, high precision)
float16 (16 bits): Range -65504 to 65504 (still large, less precision)
int8 (8 bits):    Range -128 to 127 (small, low precision)

Trade precision for memory!
```

### Quantization Methods

**Post-Training Quantization (PTQ):**

```
Train model in float32
  ↓
Convert to int8 (or int4)
  ↓
Use for inference
```

Simple, but loses accuracy.

**Quantization-Aware Training (QAT):**

```
Train model while aware of quantization
Simulate int8 operations during training
  ↓
Model learns to work well at low precision
  ↓
Convert to int8 at end
```

Better accuracy, more training required.

### Bit Widths and Trade-offs

| Bits | Size Reduction | Accuracy Loss | Speed Up |
|------|---|---|---|
| 32 | 1x | None | 1x |
| 16 | 2x | Minimal | 2x |
| 8 | 4x | Small (1-2%) | 2-3x |
| 4 | 8x | Moderate (2-5%) | 3-4x |
| 2 | 16x | Significant (5-10%) | 4-5x |
| 1 | 32x | Too much | 6-8x |

**Practical Common:**

- float16: Standard for most inference (good balance)
- int8: Good for optimization (4x memory reduction)
- int4: Very aggressive (8x reduction, some accuracy loss)

### Section 4: Slide 30 - Advanced Techniques

**Slide 30 Content: Optimization Techniques**

**Technique 1: Kernel Fusion**

**Problem:**

Each operation is a separate kernel call:

```
Matrix multiply → Wait for result
Activation → Wait for result
Add bias → Wait for result
```

Overhead!

**Solution:**

Fuse operations into single kernel:

```
Matrix multiply + Activation + Bias → Single fused kernel
```

**Benefits:**
- Reduced kernel launch overhead
- Better cache utilization
- 10-30% speedup

**Technique 2: Mixed Precision**

**Idea:**

Use different precision for different operations:

```
Large matrix multiplications: float16 (fast)
Attention softmax: float32 (stable)
Biases: int8 (memory efficient)
```

**Benefits:**
- Speed of low precision
- Stability of high precision
- Memory efficient

**Technique 3: Speculative Decoding**

**Idea:**

Generate multiple tokens speculatively, verify later:

```
Step 1: Generate tokens 1-5 quickly with small model
Step 2: Verify with large model (in one pass)
Step 3: If matches, use all 5 tokens
        If diverges at token 3, use tokens 1-2, regenerate token 3
```

**Benefits:**
- Up to 2-3x speedup for generation
- Same quality (verified by large model)

---

## Part 6: Practical Deployment (Pages 46-50)

### Deployment Infrastructure

**Option 1: Cloud APIs (OpenAI, Anthropic)**

```
Request → Cloud API → Inference → Response
```

Pros:
- No infrastructure needed
- Instant availability
- Updates automatic

Cons:
- Per-request costs
- Latency overhead
- Data privacy concerns

**Option 2: Self-Hosted (on-premise)**

```
Model → Your GPU → Your server → Your API
```

Pros:
- Full control
- Privacy
- No per-request costs (after initial investment)

Cons:
- Need hardware
- Need to manage updates
- Need MLOps expertise

**Option 3: Hybrid**

```
Popular requests → Fast local cache
Rare requests → Call cloud API
```

Best of both worlds!

### Inference Serving Frameworks

Popular options:

1. **TensorRT-LLM:** NVIDIA (very optimized)
2. **vLLM:** Open source (easy to use)
3. **Ollama:** Simple, local-first
4. **Ray Serve:** Distributed, scalable
5. **HuggingFace TGI:** Text generation inference

### SLA Requirements

**SLA = Service Level Agreement**

Key metrics:

1. **Latency:** Time to first token, time per token
2. **Throughput:** Requests per second
3. **Availability:** % of time service works
4. **Cost:** Per-request cost

Typical trade-offs:

```
Low latency (100ms) → Expensive, high-end hardware
Medium latency (500ms) → Standard hardware, batching
High latency (2-5s) → Cheap, highly batched
```

---

## Part 7: Summary and Future (Pages 51-55)

### Inference Optimization Hierarchy

```
1. Model Architecture (biggest impact)
   - Better architecture = faster inherently
   
2. Batching (high impact)
   - Continuous batching can 5-10x throughput
   
3. Quantization (medium impact)
   - int8 saves memory, 4x reduction
   
4. Kernel Fusion (medium impact)
   - 10-30% speedup
   
5. Speculative Decoding (emerging)
   - 2-3x speedup for generation
```

### Memory Optimization Strategy

```
Model weights: Use quantization
KV cache: Use continuous batching, shorter contexts
Activations: Careful batching, kernel fusion
```

### Real-World Constraints

**Challenge 1: Latency Budget**

User expects response in < 1 second:
- Batch size: Limited
- Can't wait for large batches
- Trade throughput for latency

**Challenge 2: Context Length**

Longer context = Better quality but slower:
- Dynamic window: Keep only recent context
- Retrieval: Get only relevant parts of long document

**Challenge 3: Cost Pressure**

Each request must be profitable:
- If margin is 1 cent per request, can't wait 10 seconds
- Need highly efficient inference
- Continuous optimization required

### Quiz: Test Understanding

**Q1:** Why is KV cache important for inference?
- A: Stores model weights
- B: Prevents recalculating attention for previous tokens
- C: Stores training history
- **Answer: B** - Avoids redundant computation

**Q2:** What's the main bottleneck in long-sequence generation?
- A: Model training
- B: Attention matrix size grows quadratically
- C: Tokenization
- **Answer: B** - O(N²) memory for N tokens

**Q3:** Dynamic batching is better than static because:
- A: It's always faster
- B: Removes latency variance
- C: Removes requests when done instead of waiting
- **Answer: C** - Continuous GPU utilization

---

**End of CS-5: LLM Inference Fundamentals**

*Understanding inference is crucial for deploying practical LLM systems. The optimization techniques discussed here reduce costs by 10-100x. The next course (CS-6) covers advanced inference optimization strategies.*
