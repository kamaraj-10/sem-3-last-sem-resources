# CS-7: LLM Optimization II

## Advanced Techniques and Cutting-Edge Optimizations

---

## Part 1: Beyond Standard Optimizations (Pages 1-5)

### The Remaining Challenges

**After applying standard optimizations (CS-6):**

We've achieved:
- 10-20x throughput improvement
- 2-5x latency reduction
- 4x memory savings with quantization

**Remaining bottlenecks:**

1. Long sequences still slow
2. Some models can't fit even with int8
3. Quality loss from aggressive quantization
4. Still expensive to serve at huge scale

### Emerging Solutions

**New Paradigms:**

1. **Mixture of Experts:** Use different parts for different inputs
2. **Distillation:** Train smaller models from large ones
3. **Speculative Decoding:** Generate multiple tokens speculatively
4. **Retrieval Augmentation:** Don't process full context
5. **Adaptive Methods:** Dynamic precision and batch sizing

### Why Innovation Continues

**The Incentive Structure:**

```
If you can reduce inference cost by 2x:
- Save billions for large companies
- Win in market competition
- Everyone wants to do it

Result: Constant innovation and optimization race
```

### Section 1: Slide 5 - Advanced Attention

**Slide 5 Content: Sparse Attention Patterns**

**Problem with Dense Attention:**

Standard attention attends to all tokens:

```
Token position 10 attends to: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Complexity: O(N²) attention

For 32K tokens: 1 billion attention operations!
```

**Idea: Sparse Attention Patterns**

Only attend to subset of tokens:

```
Local Attention:
  Token 10 attends to: 8, 9, 10, 11, 12 (window of ±2)
  Complexity: O(N × window_size)

Strided Attention:
  Token 10 attends to: 0, 5, 10, 15, 20 (every 5th token)
  Complexity: O(N × stride)

Combination:
  Some layers local, some strided
  Complexity: Lower than dense, better coverage
```

**Trade-off Analysis:**

```
Attention Type    | Speed | Memory | Quality
Dense             | 1x    | 1x     | Baseline
Local (W=512)     | 10x   | 0.1x   | ~95%
Strided           | 20x   | 0.05x  | ~85%
Local + Strided   | 15x   | 0.08x  | ~92%
```

**When to Use:**

- Long documents (>4K tokens): Use sparse
- Code generation: Local attention usually enough
- Very long context (>50K): Essential

**Real Implementation:**

LongFormer and Reformer use these patterns.

---

## Part 2: Mixture of Experts (MoE) (Pages 6-15)

### The Core Idea

**Observation:**

Not all parameters needed for all inputs.

Example:
- Code input: Use code expert
- Math input: Use math expert
- NLP input: Use language expert

**Mixture of Experts:**

Replace large dense layer with multiple expert layers:

```
Dense Layer (Standard):
  Input → [Giant Matrix] → Output (all params used)

Mixture of Experts:
  Input → Router → Expert 1 (for this input)
       ├→ Expert 2 (not used)
       ├→ Expert 3 (for this input)
       └→ Expert 4 (not used)
       
  Output combines selected experts
```

### The Router Mechanism

**How Router Works:**

```
Router output: Probability for each expert

Example output:
  Expert 1: 0.1% (almost no contribution)
  Expert 2: 45% (primary expert)
  Expert 3: 54% (primary expert)
  Expert 4: 0.9% (almost no contribution)

Input processes through 2 and 3 primarily
```

**Learned Routing:**

Router can be learned end-to-end:
- During training, model learns which inputs→which experts
- Different tasks route to different experts
- Specialization emerges

### Benefits and Challenges

**Benefits:**

1. **Efficiency:** Not all params needed per token
2. **Scale:** Can have 100s of experts without per-token cost increase
3. **Specialization:** Different experts learn different skills
4. **Capacity:** Total model capacity grows without latency increase

**Challenges:**

1. **Load Balancing:** Ensure experts used equally
   - Without balance: Some experts overused, others unused
   - Solution: Add auxiliary loss to encourage balance

2. **Training Complexity:** Routing decisions need to be learned
   - Non-differentiable routing: Can't use backprop directly
   - Solution: Gumbel-softmax or similar tricks

3. **Inference Overhead:** Need to select experts for each token
   - Routing computation: ~1-2% overhead
   - Acceptable trade-off for savings

### Load Balancing Deep Dive

**Load Balancing Strategies:**

**Strategy 1: Importance-Weighted Load Balancing**

```
Each expert has "importance" score

If Expert 1 has high importance:
  - But gets low fraction of tokens
  - Add penalty to encourage routing to it

If Expert 2 has low importance:
  - But gets high fraction of tokens
  - Add penalty to reduce routing to it

Result: Balanced usage aligned with capacity
```

**Strategy 2: Token Choice Routing**

Rather than token choosing expert:

```
Traditional: Token→Router→Expert
Problem: Popular experts overloaded, rare experts unused

Token Choice: Expert→Chooses tokens
Each expert picks top-K most important tokens

Result: Experts have equal load!
```

**Example:**

```
1000 tokens, 8 experts, each can handle 125 tokens

Traditional routing:
  Expert 1: 300 tokens (overloaded!)
  Expert 2: 200 tokens
  Expert 3: 100 tokens
  Expert 4-8: rest

Token choice:
  Each expert picks 125 best tokens
  Experts 1-8: 125 tokens each (perfectly balanced!)
```

---

## Part 3: Knowledge Distillation (Pages 16-25)

### What is Distillation?

**The Problem:**

Large models are powerful but slow:
- GPT-3 (175B): Excellent quality, 10 seconds per request
- Needed: Faster, cheaper

**The Idea:**

Train a small model to mimic large model:

```
Large Model (Teacher):     Small Model (Student):
175B parameters     →      7B parameters
Slow inference             Fast inference
Expert knowledge    →      Learn from teacher
```

**The Process:**

1. Train large model (expensive, done once)
2. Collect outputs from large model
3. Train small model to match outputs
4. Use small model in production

### How Distillation Works

**Temperature Control:**

When large model produces outputs:

```
Large model softmax (T=1, normal):
  Yes: 90%
  No: 10%

Soft targets with T=4 (softer):
  Yes: 70%
  No: 30%

Soft targets are easier to learn from!
```

**Loss Function:**

```
Loss = α × CausalLoss (matching teacher outputs)
     + β × DirectLoss (matching actual labels)

Typically α=0.9, β=0.1
Focus mostly on matching teacher
```

### Quality vs. Size Trade-off

**Distillation Results:**

```
Model Size | Base Quality | After Distillation | Speed vs Base
175B       | 100%         | 100%               | 1x
70B        | 85%          | 90% (distilled)    | 2.5x
7B         | 45%          | 70% (distilled)    | 25x
```

**Key Insight:**

Small distilled model can significantly improve on base small model by learning from large model.

### When to Use Distillation

**Good for:**
- Need very fast inference
- Quality can be 90% of full model
- Budget allows training time
- Have large teacher model

**Not good for:**
- Need maximum quality
- No large teacher available
- Very long training time available

---

## Part 4: Speculative Decoding (Pages 26-35)

### Section 4: Slide 30 - Advanced Decoding Strategies

**Slide 30 Content: Speculative Generation**

### The Core Idea

**Problem with Standard Generation:**

Generate one token at a time:

```
Generate token 1: Use full model
Generate token 2: Use full model again
Generate token 3: Use full model again
...
```

Each step requires processing all previous tokens.

**Speculative Idea:**

Use small model to guess multiple tokens,
Then verify with large model:

```
Step 1: Small model generates tokens 1-5 quickly (~10ms)
Step 2: Large model verifies tokens 1-5 (~50ms)
        If all match: Accept all 5 tokens!
        If diverges at token 3: Accept 1-2, regenerate from 3

Total: 60ms for 3-5 tokens (vs 150-250ms normally)
```

### How Verification Works

**Verification Process:**

```
Tokens generated: [A, B, C, D, E]
Small model confidence: 60%, 50%, 45%, 40%, 35%

Verify: Process [A, B, C, D, E] through large model
Large model output probabilities:
  [A: 90%, B: 85%, C: 40%, D: 10%, E: 5%]

Matching check:
  A matches 90% > 60% ✓ Accept
  B matches 85% > 50% ✓ Accept
  C matches 40% < 45% ✗ Reject

Result: Accept A, B. Regenerate from C.
```

### Efficiency Gains

**When It Works Well:**

- Small model is decent at predicting
- Large and small models agree on first few tokens
- Batch sizes allow verification

**Speedup:**

```
Scenario 1: Small model accuracy 80%
  Expected tokens accepted per verification: ~3-4
  Speedup: ~2x

Scenario 2: Small model accuracy 90%
  Expected tokens accepted per verification: ~4-5
  Speedup: ~2.5x

Scenario 3: Small model accuracy 50%
  Expected tokens accepted per verification: ~1-2
  Speedup: ~1.2x (not worth it)
```

### Small Model Selection

**Choice 1: Use Smaller Version**

Use 7B as small model for 70B large model.

Pros:
- Understands similar concepts
- Reasonable accuracy

Cons:
- Significant overhead for small model inference
- Still needs GPU

**Choice 2: Quantized Version**

Use quantized version of same model.

```
70B model full precision (20x)
70B model int8 quantized (2-4x speedup)
```

Pros:
- Same model, just compressed
- Minimal accuracy loss

Cons:
- Need to support both precision levels

**Choice 3: Distilled Model**

Use distilled small model trained from large.

Pros:
- Optimized to predict large model
- Good accuracy for speculation

Cons:
- Training overhead

---

## Part 5: Adaptive Precision (Pages 36-45)

### Dynamic Precision Selection

**Core Idea:**

Don't use same precision for all:

```
Difficult layers: float32 (precision matters)
Standard layers: float16 (good balance)
Attention softmax: float32 (stability needed)
Embeddings: int8 (can be compressed)
```

**Benefits:**

- Quality of fp32 where needed
- Speed of int8 where possible
- Customized per layer

### Layer-Wise Precision

**Observation:**

Different layers have different precision requirements:

```
Layer | Critical? | Precision | Speed-up vs fp32
Emb   | No        | int8      | 4x
Attn  | Yes       | fp32      | 1x
FFN1  | Maybe     | fp16      | 2x
FFN2  | Maybe     | fp16      | 2x
Out   | Yes       | fp32      | 1x
```

### Adaptive Batch Sizing

**Dynamic Batch Size:**

Adjust batch size based on queue depth:

```
Queue empty: Batch size = 8 (latency priority)
Queue moderate: Batch size = 32 (balanced)
Queue full: Batch size = 64 (throughput priority)

Result: Low latency when needed, high throughput when possible!
```

### Adaptive Context Window

**Idea:**

Use different context lengths:

```
Short queries: Process full history
Long queries: Keep only recent context (sliding window)
```

Trade-off:
- Shorter context: Faster
- Longer context: Better quality

---

## Part 6: Emerging Optimizations (Pages 46-50)

### Retrieval-Augmented Generation (RAG)

**Problem:**

Processing very long documents is expensive.

**Solution:**

Only process relevant documents:

```
Query: "What is the capital of France?"

Full doc (100K tokens):
  [Lots of irrelevant content]

Retrieved (1K tokens):
  [Only relevant section about Paris]

Process only relevant part!
```

**Benefits:**

- 100x reduction in processing
- Better quality (less noise)
- Can handle unlimited document length

### Token-Level Pruning

**Idea:**

Not all tokens equally important.

```
Input: "The quick brown fox jumped over the lazy dog"

Importance scores:
  The: 0.1 (low)
  quick: 0.3 (medium)
  fox: 0.9 (high)
  jumped: 0.8 (high)
  over: 0.2 (low)
  the: 0.1 (low)
  lazy: 0.5 (medium)
  dog: 0.9 (high)

Prune: Remove low-importance tokens
Result: Process fewer tokens without quality loss!
```

### Tensor Parallelism and Optimization

**Vertical Parallelism:**

Split model columns across GPUs:

```
Layer (4096, 4096) → GPU1 handles (4096, 2048)
                  → GPU2 handles (4096, 2048)

Benefit: Fit larger models
```

**Pipeline Parallelism:**

Split model layers across GPUs:

```
GPU1: Layers 1-25
GPU2: Layers 26-50
GPU3: Layers 51-96

Benefit: Larger batches, pipeline stages
```

---

## Part 7: Future and Conclusions (Pages 51-55)

### The Optimization Landscape (2024+)

**Current State:**

Standard techniques provide 10-50x speedup:
- Continuous batching
- Flash attention
- Quantization
- Kernel fusion

**Emerging Techniques:**

- Speculative decoding (2-3x)
- Mixture of experts (2-5x for scale)
- Better routing/scheduling (1.5-2x)
- Custom hardware (2-10x)

### Hardware Evolution

**Custom Inference Hardware:**

- TPUs (Google): Optimized matrix multiply
- Groq: Speed-of-light processing
- Cerebras: Huge on-chip memory
- NVIDIA H200: High bandwidth memory

**Impact:**

Specialized hardware can provide 5-50x speedup for inference.

### Software Stack Evolution

**Better Serving Systems:**

- Ray Serve: Distributed
- BentoML: Easy deployment
- KServe: Kubernetes-native
- Ollama: Local-first

**Better Compilers:**

- TVM: Auto-optimize kernels
- OpenAI Triton: Easy to write optimized code
- Modular Mojo: Language for optimization

### The Fundamental Limit

**Theoretical Minimum:**

To generate response, must:
1. Read model weights (memory bandwidth bound)
2. Compute FLOPs (computation)
3. Read prompt (memory I/O)

```
Time = max(Weights_Read_Time, Computation_Time, IO_Time)

Optimization can reduce each, but not below physical limits.
```

**Current State vs. Limits:**

```
Current inference: ~70% of theoretical efficiency
Room for improvement: 1.3-2x with perfect optimization
```

### Practical Recommendations

**For Production Systems:**

1. **Start simple:** Continuous batching + quantization
2. **Measure:** Profile to find real bottlenecks
3. **Optimize:** Apply techniques to bottlenecks only
4. **Monitor:** Track performance in production
5. **Iterate:** Regular optimization cycles

**Cost Reality:**

```
Without optimization: $100 per 1M tokens
With standard optimization: $5-10 per 1M tokens
With aggressive optimization: $1-2 per 1M tokens
Theoretical limit: ~$0.1-0.5 per 1M tokens
```

### Quiz: Test Understanding

**Q1:** When is speculative decoding effective?
- A: Always speeds up 2x
- B: Only when small model predicts well (>80% accuracy)
- C: Only for very long sequences
- **Answer: B** - Effectiveness depends on small model quality

**Q2:** Mixture of Experts improves efficiency by:
- A: Making all parameters smaller
- B: Using only relevant experts per input
- C: Eliminating attention
- **Answer: B** - Reduces computation by processing selected experts

**Q3:** Why does Retrieval-Augmented Generation speed up inference?
- A: Uses better model
- B: Processes only relevant documents
- C: Doesn't actually speed up
- **Answer: B** - 100x reduction by skipping irrelevant content

---

## Key Takeaways Across All Optimization Courses

### Optimization Hierarchy (Final)

```
Level 1 (Essential - 10x improvement):
  ✓ Continuous batching
  ✓ Flash attention
  
Level 2 (Very Good - 3-5x improvement):
  ✓ Quantization (int8)
  ✓ Kernel fusion
  
Level 3 (Good - 2-3x improvement):
  ✓ Speculative decoding
  ✓ Better scheduling
  
Level 4 (Advanced - 1.5-2x improvement):
  ✓ Mixture of Experts
  ✓ Distillation
  
Level 5 (Frontier):
  ✓ Custom hardware
  ✓ Model architecture improvements
  ✓ Novel algorithms
```

### Total Potential Improvement

```
Base model:                1x
+ Continuous batching:     10x
+ Quantization:            2x
+ Speculative decoding:    2x
+ Better scheduling:       1.3x
+ Advanced techniques:     1.5x

Total: ~50-80x improvement!
```

---

**End of CS-7: LLM Optimization II**

*These techniques represent the cutting edge of LLM optimization. Continued innovation in hardware, software, and algorithms will drive further improvements in efficiency and capability. The optimization race will continue indefinitely as inference cost directly translates to revenue impact.*

---

## Final Comprehensive Learning Path

### Understanding LLMs (CS-1)
- Foundation concepts
- Attention mechanism
- Transformer architecture

### Training (CS-2)
- Self-supervised learning
- Scaling laws
- Training efficiency

### Architecture (CS-3)
- Modern innovations
- RMSNorm, RoPE, GQA
- Flash Attention

### Adaptation (CS-4)
- Fine-tuning methods
- LoRA, adapters
- Training on specific tasks

### Inference Basics (CS-5)
- Autoregressive generation
- KV cache
- Batching strategies

### Optimization I (CS-6)
- Continuous batching
- Quantization
- Memory optimization

### Optimization II (CS-7)
- Sparse attention
- Mixture of Experts
- Distillation & Speculation

**Progression:** Fundamentals → Building → Running → Optimizing

Each course builds on previous knowledge!
