# CS-6: LLM Optimization I

## Advanced Techniques for Efficient Large Language Model Inference

---

## Part 1: Optimization Philosophy (Pages 1-5)

### Why Optimization Matters

**The Cost Problem:**

Running LLMs at scale is expensive:

```
1 million users asking 10 questions/day = 10 million requests/day
Without optimization: $1 million/day
With optimization: $100,000/day (10x savings!)
```

Savings compound - billions annually!

### Classification of Optimizations

**Computational (Speed):**
- Reduce operations
- Parallelize better
- Use specialized hardware

**Memory (Space):**
- Reduce model size
- Reduce intermediate activations
- Compress data structures

**Quality Trade-off:**
- Lose some accuracy for speed/memory
- Need to measure impact carefully

### Understanding Trade-offs

```
Quality
  |
  |●─── Full Model (reference)
  |  ╲
  | ●  ╲ Optimized Model (2x faster)
  |  ╲
  | ●  ╲ Very Optimized (4x faster, 2% loss)
  |╯ ●╲
  └────●─────→ Inference Speed
       Highly Optimized (10x faster, 5% loss)
```

Decision: Pick optimal point for your use case.

### Section 1: Slide 5 - Two-Phase Inference

**Slide 5 Content: Prefill vs. Decoding Phase**

**Deep Understanding:**

Phase 1 - **Prefill (Prompt Processing):**

```
Input: User prompt of varying length
Task: Process all tokens simultaneously
Operation: Heavy matrix multiplications
Memory pattern: Sequential reads
Key metric: Total time (minimize)
```

Characteristics:
- Compute-bound (lots of math)
- Can be parallelized effectively
- Throughput-friendly (can batch many prompts)

Optimizations:
- Kernel fusion
- Better memory layout
- Quantization

**Phase 2 - Decoding (Token Generation):**

```
Input: Single token at a time
Task: Generate one token per step
Operation: Repeated matrix-vector multiplies
Memory pattern: Need to load weights N times
Key metric: Time per token (minimize)
```

Characteristics:
- Memory-bound (reading weights is bottleneck)
- Hard to parallelize (inherently sequential)
- Latency-sensitive (each step adds ~100ms)

Optimizations:
- KV cache (already done by default)
- Batch generation (continuous batching)
- Mixed precision for weights

**Why Different Phases Need Different Optimizations?**

Different computational characteristics:
- Prefill: Can do 100 tokens in ~same time as 10 (throughput increases)
- Decoding: 100 tokens takes 10x time as 10 tokens (sequential)

Result: Optimize prefill for throughput, decoding for latency.

---

## Part 2: Advanced Computational Optimizations (Pages 6-15)

### Matrix Multiplication Optimization

**Problem:**

Matrix multiplications are 90%+ of inference time.

For LLM:
```
Output = Input × Weight^T
(batch, seq, hidden) × (hidden, hidden)
```

This is a huge operation!

**Optimization 1: Tensor Cores**

Modern GPUs (V100, A100) have specialized hardware:

```
FP32 (float32): Regular computation
Tensor Cores: Dedicated hardware for matrix mult
```

Tensor cores:
- 10-100x faster for matrix multiplications
- Work best with specific data layouts
- Enable efficient inference

**Optimization 2: Blocked Computation**

Instead of multiplying all at once, break into blocks:

```
Full: (4096, 4096) × (4096, 4096) = 68 billion operations

Blocked (2 blocks):
  (2048, 4096) × (4096, 2048) + (2048, 4096) × (4096, 2048)
  Better cache locality!
```

**Benefit:** Better use of CPU cache, fewer memory stalls.

### Attention Optimization

**Standard Attention:**

```
1. Compute Q × K^T (expensive!)
2. Apply softmax
3. Multiply by V
```

**Optimization 1: Flash Attention (revisited)**

Reduce memory usage for intermediate results:

```
Instead of materializing full Q × K^T (N×N matrix)
Process in tiles and stream results
Same result, less peak memory!
```

**Optimization 2: Multi-Head Attention Parallelization**

```
Sequential approach:
  Head 1: 100ms
  Head 2: 100ms
  Head 3: 100ms
  Total: 300ms

Parallel approach (8 heads on 8 cores):
  Total: 40ms (slight overhead)
```

GPUs can parallelize all heads - essentially free!

**Optimization 3: Grouped Query Attention (GQA)**

Reduce number of keys and values:

```
Full: 96 query heads, 96 key heads, 96 value heads
GQA:  96 query heads, 8 key heads, 8 value heads (shared)

Memory reduction: ~90%
Speed improvement: ~2x
```

---

## Part 3: Memory and I/O Optimization (Pages 16-25)

### The Memory Wall Problem

**Modern Computing Reality:**

```
Compute speed: 100 TFLOPS (trillion operations/second)
Memory bandwidth: 1 TB/second

Time to fetch 1 element: 0.01 seconds / FLOP
Time to compute with 1 element: 0.00000001 seconds / FLOP

Ratio: 1,000,000x slower to fetch than compute!
```

**Implication:**

Memory access is the bottleneck, not computation!

This is especially true for inference.

### Memory Hierarchy Optimization

```
Registers       (tiny, fast)
↓
L1 Cache        (small, fast)
↓
L2 Cache        (medium, medium speed)
↓
L3 Cache        (large, slower)
↓
VRAM/HBM        (huge, slowest)
```

**Optimization:** Keep data in cache as long as possible!

**Technique: Tiling**

Process small tiles that fit in cache:

```
(4096, 4096) matrix → 16x16 = 256 tiles of (256, 256)

Process each tile:
  Load tile → L3 cache
  Do computation
  Write result
  Load next tile

Result: Much less memory bandwidth used!
```

### Weight Quantization Revisited

**Extreme quantization strategies:**

Normal:
```
Weights: float32 (4 bytes each)
For 70B model: 280GB
```

Quantization:
```
int8:  70B × 1 byte = 70GB (4x smaller)
int4:  70B × 0.5 byte = 35GB (8x smaller)
fp8:   70B × 1 byte = 70GB (but optimized)
```

**Important Question:**

Does quantized model lose quality?

Research findings:
- int8: < 1% accuracy loss
- int4: 1-3% accuracy loss
- With proper calibration: Can be minimal!

### KV Cache Optimization

**Problem:**

KV cache grows with sequence length:

```
GPT-3 + 2000 tokens: ~5GB cache per request
GPT-3 + 32000 tokens: ~80GB cache per request!
```

**Optimization 1: KV Cache Quantization**

Store cache in int8 instead of float32:

```
Savings: 4x
Impact: Minimal (cache has low precision needs)
```

**Optimization 2: KV Cache Pruning**

Remove less important tokens from cache:

```
Input: "I bought a car yesterday. The car is blue. [Question about color]"

Important tokens for question: "car", "blue"
Less important: "I", "bought", "a", "yesterday"

Keep: Top 70% by importance
Discard: Bottom 30%

Result: 30% cache reduction, 2-5% quality impact
```

**Optimization 3: Sparse Attention + KV Cache**

Use sparse attention pattern:

```
Local attention: Keep cache for nearby tokens only
Result: Logarithmic growth instead of linear!
```

---

## Part 4: Batching and Scheduling (Pages 26-35)

### Advanced Batching Strategies

**Challenge:**

Different requests finish at different times:

```
Request A: "Hello" → 1 token output → 100ms
Request B: "Write a poem" → 50 token output → 5000ms
Request C: "Hi" → 1 token output → 100ms
```

**Static batching:** Wait for A, B, C to finish together
- Total time: 5100ms
- GPU idle: Yes (A and C done early)

**Dynamic batching:** Remove requests when done
- Total time: ~1500ms (3x faster!)
- GPU utilized better

### Continuous Batching Deep Dive

**The Algorithm:**

```
Iteration 1:
  Batch: [A (0/1), B (0/50), C (0/1)]
  Process prefill phase: ~100ms
  Generate 1 token from each
  A and C have 1 token, so they're complete

Iteration 2:
  Batch: [B (1/50), D_new (0/10), E_new (0/5)]
  Generate 1 token from each
  E will complete in ~5 iterations

Iteration 3:
  Batch: [B (2/50), D (1/10), F_new (0/100)]
  Continue...
```

**Result:** Always utilizing GPU, minimum idle time!

### Section 4: Slide 30 - Two-Phase Inference Optimization

**Slide 30 Content: Image credits and advanced batching**

**Advanced Scheduling Policies:**

**Policy 1: Throughput-Optimized**

```
Goal: Maximize total requests handled
Strategy: Large batches, sacrifice individual latency
Example: Batch size = 64
Result: 100 requests/min, 2 second latency each
```

**Policy 2: Latency-Optimized**

```
Goal: Minimize individual request latency
Strategy: Small batches, fast responses
Example: Batch size = 8
Result: 30 requests/min, 200ms latency each
```

**Policy 3: Balanced (SLA-Aware)**

```
Goal: Maximize throughput while meeting latency SLA
Strategy: Dynamic batch size based on queue depth
Example: If queue empty, low latency. If queue deep, high throughput
Result: 70 requests/min, <500ms latency 99% of time
```

### Prefill-Decoding Separation

**Optimization Idea:**

Use different batch sizes for prefill and decoding:

```
Prefill Phase:
  Can handle large batches (throughput-bound)
  Batch size: 64
  Process 64 prompts in ~100ms

Decoding Phase:
  Each prompt needs individual attention
  Batch size: Can be different for each prompt length
  Process all decodings in parallel
```

**Advanced Technique:**

```
Prefill batches of size 64: Process in 100ms
Decode phase uses KV cache from prefill
Interleave: While decoding, start next prefill batch

Result: 2-3x throughput improvement!
```

---

## Part 5: Serving Systems and Optimization (Pages 36-45)

### vLLM: Continuous Batching System

**What is vLLM?**

Open-source system optimized for LLM serving.

**Key Innovations:**

1. **Continuous batching:** Remove requests when done
2. **Dynamic memory management:** Flexible memory allocation
3. **Optimized kernels:** Specialized CUDA kernels
4. **Multi-GPU support:** Distribute across GPUs

**Performance Gains:**

vLLM vs. standard serving:
```
Throughput: 10-20x improvement
Latency: 2-5x improvement
```

Why? Better batching, kernel optimization, memory efficiency.

### Hardware Selection for Inference

**GPU Choices:**

| GPU | Memory | Perf | Cost | Best For |
|-----|--------|------|------|----------|
| A100 | 40-80GB | Highest | Highest | Large models |
| A10 | 24GB | Medium | Medium | Medium models |
| T4 | 16GB | Low | Low | Small models |
| L4 | 24GB | High | Medium | Inference |

**Recommendation:**

For inference: L40S or A100 offer best price-performance.

### Scaling Strategies

**Strategy 1: Single GPU**

Batch small, serve as fast as possible.

Bottleneck: GPU memory

**Strategy 2: Multi-GPU on Single Machine**

Distribute batch across GPUs.

```
GPU 0: Part of batch
GPU 1: Part of batch
GPU 2: Part of batch
GPU 3: Part of batch

Result: 4x throughput!
```

**Strategy 3: Distributed Across Machines**

Different requests on different machines.

```
Server 1: Requests 1-100/sec
Server 2: Requests 101-200/sec
Load Balancer: Route to least busy

Result: Near-linear scaling with machines
```

---

## Part 6: End-to-End Optimization Examples (Pages 46-50)

### Example 1: Chat Server Optimization

**Setup:**

- Model: GPT-3.5-turbo-like (20B parameters)
- Hardware: Single A100 (40GB)
- Goal: 1000 concurrent users, <1 second latency

**Bottleneck Analysis:**

Initial: 10 requests/sec throughput, 100ms latency

Problems:
- Batch size too small
- Not using continuous batching
- Weights in float32

**Optimizations Applied:**

1. Continuous batching: +3x throughput
2. int8 quantization: +2x throughput, -0.5% accuracy
3. Kernel fusion: +1.2x throughput
4. Memory optimization: Allows batch size 32 vs 16

**Results:**

- Throughput: 60 requests/sec
- Latency: 500ms (90th percentile)
- Cost: $0.01 per request
- Users handled: 60 × 60 = 3,600 concurrent

### Example 2: Code Generation Optimization

**Setup:**

- Model: CodeLLaMA-70B (very large)
- Hardware: 4x A100 GPUs
- Goal: Fast code generation for IDE

**Challenges:**

- Large model doesn't fit on single GPU
- Variable length prompts (1-10K tokens)
- Need <5 second response time

**Optimizations:**

1. Quantization to int8: Fits in 1x A100
2. Speculative decoding: Predict multiple tokens
3. Dynamic batching: Handle variable lengths
4. Context pruning: Keep recent relevant code

**Results:**

- Response time: 3-4 seconds
- Throughput: 20 requests/min
- Model quality: Maintained

### Example 3: Multi-Language Translation

**Setup:**

- Model: Large multilingual model (100B params)
- Hardware: 8x GPUs
- Goal: Translate millions of documents

**Strategy:**

1. **Profiling first:** Identify bottlenecks
   - Prefill: 30% of time
   - Decoding: 70% of time

2. **Optimize accordingly:**
   - Prefill: Larger batches, throughput-focused
   - Decoding: Continuous batching, latency matter less

3. **Hardware allocation:**
   - GPUs 1-4: Prefill processing (large batches)
   - GPUs 5-8: Decoding (output generation)
   - Load balancer: Route requests

**Results:**

- 1000 documents/minute
- Cost: $0.001 per document
- Near-linear scaling with GPUs

---

## Part 7: Summary and Future (Pages 51-55)

### Optimization Principles

1. **Measure first:** Profile to find real bottlenecks
2. **Understand hardware:** Use GPUs appropriately
3. **Trade-off strategically:** Quality vs speed/cost
4. **Keep it simple:** Complex optimizations often not worth it
5. **Monitor in production:** Track performance over time

### Optimization Hierarchy (Priority Order)

```
1. ✅ Continuous batching (biggest impact)
2. ✅ Kernel fusion (10-30% improvement)
3. ✅ Mixed precision (4x memory, minimal quality loss)
4. ✅ Flash attention (2-3x for long sequences)
5. ✅ Speculative decoding (2-3x for decoding)
6. ✅ Hardware selection (already optimized in practice)
7. ⚠️  Extreme quantization (risky for quality)
```

### Future Optimization Directions

- **Custom silicon:** Inference-specific chips
- **Sparse models:** Only activate needed parameters
- **Retrieval-augmented:** Don't process full context
- **Distillation:** Smaller models matching large ones
- **Adaptive methods:** Change precision/batch dynamically

### Quiz: Test Understanding

**Q1:** Why is memory I/O the bottleneck in inference?
- A: GPUs are too slow
- B: Memory bandwidth much slower than compute speed
- C: Quantization causes issues
- **Answer: B** - 1,000,000x slower to fetch than compute!

**Q2:** Continuous batching improves throughput by removing what?
- A: Model parameters
- B: Low-quality requests
- C: Completed requests, allowing new requests into batch
- **Answer: C** - Better GPU utilization

**Q3:** In two-phase inference, why use different optimizations?
- A: It's always optimal
- B: Prefill is compute-bound, decoding is memory-bound
- C: Different hardware for each phase
- **Answer: B** - Fundamentally different characteristics

---

**End of CS-6: LLM Optimization I**

*These optimization techniques can reduce inference costs by 10-100x. The next course (CS-7) covers advanced optimization techniques including mixture of experts and other cutting-edge methods.*
