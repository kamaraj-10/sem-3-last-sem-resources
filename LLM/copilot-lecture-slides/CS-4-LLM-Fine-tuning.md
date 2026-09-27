# CS-4: Large Language Model Fine-Tuning

## Comprehensive Guide to Adapting LLMs to Specific Tasks

---

## Part 1: Understanding Fine-Tuning Fundamentals (Pages 1-5)

### What is Fine-Tuning?

**Definition:**

Taking a pretrained LLM and training it further on task-specific data to specialize its behavior.

**Analogy:**

Think of a graduate student:
- **University Education:** Learn fundamentals (pretraining)
- **Research Specialization:** Focus on specific field (fine-tuning)

Same fundamental skills, but specialized for a particular task.

### Why Fine-Tune?

**Problems with Base Models:**

1. Base model is general-purpose (not optimized for specific tasks)
2. Base model might not follow specific formats
3. Base model might have undesired behaviors
4. Base model lacks task-specific knowledge

**Benefits of Fine-Tuning:**

1. **Better Performance:** 5-30% improvement on specific tasks
2. **Cost Efficiency:** Only train on relevant data
3. **Safety:** Remove undesired behaviors
4. **Format Control:** Ensure specific output formats
5. **Knowledge Addition:** Add new domain knowledge

**Example:**

Base ChatGPT: Can do many things but not optimized for customer service

Fine-tuned ChatGPT: Specifically trained to respond like a customer service representative

Result: Fewer hallucinations, better service-specific responses

### Section 1: Slide 5 - Fine-Tuning Methods

**Slide 5 Content: Different Fine-Tuning Approaches**

**Method 1: Full Fine-Tuning (SFT - Supervised Fine-Tuning)**

Train on labeled input-output examples:

```
Input: "How do I return this product?"
Output: "Here's our return process: ..."

Input: "What's your shipping policy?"
Output: "We ship within..."
```

Process:
1. Show the model correct input-output pairs
2. Let it learn to predict correct outputs
3. Update all parameters

**Benefits:**
- Simple to understand and implement
- Maximum performance improvement possible
- Direct behavior control

**Drawbacks:**
- Need labeled data (expensive)
- Need large supervised dataset for best results
- Training all parameters is compute-intensive

**When to Use:**
- Task-specific performance is critical
- Have plenty of labeled data
- Budget allows for training

**Method 2: Instruction Fine-Tuning**

Fine-tune on diverse instruction-following examples:

```
[System] You are a helpful assistant.
[User] Summarize this text: [long text]
[Assistant] [summary]
```

Train on diverse instructions:
- Summarization
- Translation
- Question answering
- Code explanation

**Benefits:**
- Model learns to follow diverse instructions
- Generalizes to unseen tasks
- Creates more versatile model

**Method 3: Reinforcement Learning from Human Feedback (RLHF)**

This is how ChatGPT was created:

```
Step 1: SFT on high-quality examples
Step 2: Collect human feedback on model outputs
Step 3: Train reward model (learns what humans prefer)
Step 4: Use reward model to train policy (LLM)
```

**Process:**
1. Model generates multiple responses
2. Human rates which is best
3. Reward model learns to predict human preferences
4. LLM trained to maximize reward

**Benefits:**
- Aligns with human preferences
- Can optimize for specific values
- Creates safer, more helpful models

**Drawbacks:**
- Complex to implement
- Requires human feedback at scale
- Expensive and slow

**When to Use:**
- Need alignment with specific values
- Safety is critical
- Have resources for human feedback

---

## Part 2: Fine-Tuning Techniques (Pages 6-15)

### Parameter-Efficient Fine-Tuning (PEFT)

**Problem with Full Fine-Tuning:**

Large models have billions of parameters:
- GPT-3: 175 billion parameters
- Fine-tuning all: Requires massive compute
- Cost: Millions of dollars

**Solution: Only Train Subset of Parameters**

### Technique 1: LoRA (Low-Rank Adaptation)

**Key Idea:**

Instead of training all parameters, add small "adaptors":

```
Output = Original_Layer(Input) + Adapter(Input)
```

Adapter is much smaller than original layer.

**Mathematical Detail:**

```
Large Update = ΔW (billions of params)
Split into:
  ΔW = A × B  (where A and B are much smaller)

Instead of training ΔW (billions of params):
  Train A and B (thousands of params)
```

**Benefits:**
1. **Efficiency:** 1000x fewer parameters to train
2. **Speed:** Trains in hours instead of weeks
3. **Cost:** ~$100 instead of $1 million
4. **Multiple Adapters:** Can create many task-specific adapters

**Example:**

Original layer: 1000 × 1000 parameters = 1 million params

LoRA approach:
- A: 1000 × 8 = 8K params
- B: 8 × 1000 = 8K params
- Total: 16K params (99% reduction!)

**How It Works:**

During training:
1. Original weights (frozen): GPT-3 params unchanged
2. Adapter A: Small matrix, trained
3. Adapter B: Small matrix, trained
4. During inference: Include both

Result: Same quality improvement with 1000x fewer trainable params

### Technique 2: Prefix Tuning

**Idea:**

Add learnable "prefix" to each layer's input:

```
Input tokens + Learned Prefix → Layer → Output
```

Only the prefix is trained, not layer weights.

**Benefits:**
- Simple to implement
- Good for specific tasks
- Can quickly switch between tasks

**Drawback:**
- Less flexible than LoRA
- Requires prefix for each layer

### Technique 3: Adapter Modules

**Idea:**

Insert small neural networks between layers:

```
Layer Output → Adapter → Next Layer
              (trainable)
```

Adapters are small networks (e.g., 64 hidden units).

**Structure:**
- Down projection: Compress to small dimension
- Activation: Non-linearity
- Up projection: Expand back to original

**Benefit:**
- More flexible than prefix tuning
- Moderate parameter efficiency

### Comparison of PEFT Methods

| Method | Params | Speed | Quality | Flexibility |
|--------|--------|-------|---------|------------|
| Full FT | 100% | Slow | Best | Maximum |
| LoRA | 1-5% | Fast | Very Good | Good |
| Prefix | 0.1-1% | Very Fast | Good | Limited |
| Adapter | 5-10% | Fast | Good | Good |

---

## Part 3: Data Preparation and Training (Pages 16-25)

### Preparing Fine-Tuning Data

**Data Format:**

For instruction-following fine-tuning:

```
{
  "instruction": "Translate the following text to French:",
  "input": "Hello, how are you?",
  "output": "Bonjour, comment allez-vous?"
}
```

Or simpler:

```
{
  "prompt": "Translate to French: Hello, how are you?",
  "completion": "Bonjour, comment allez-vous?"
}
```

**Data Quality is Critical**

Better data > More data

Examples:
- 1,000 perfect examples > 100,000 medium examples
- Diverse examples > Repetitive examples
- Clear examples > Ambiguous examples

### Dataset Size Recommendations

```
Few examples (1-10):     Can't fine-tune effectively
Small dataset (10-100):  LoRA/Adapter methods work
Medium (100-1000):       Good for specific tasks
Large (1000+):           Full fine-tuning viable
```

**Diminishing Returns:**

```
Performance
    |     ___
    |    /
    |   /
    |  /  (rapid improvement)
    | /
    |/_________________
    100  1K  10K  100K
         Dataset Size
```

After ~10K examples, improvements slow down.

### Training Hyperparameters

**Learning Rate:**
- Full FT: 1e-5 to 5e-5
- LoRA: 1e-4 to 5e-4 (can be higher)
- Prefix: 1e-4 to 5e-4

Higher learning rates work for PEFT because updating fewer params.

**Batch Size:**
- Small (8-16): If limited memory
- Medium (32-64): Typical
- Large (128+): If fine-tuning many examples

**Epochs:**
- Full FT: 2-5 epochs (avoid overfitting)
- LoRA: 5-20 epochs (can see more without overfitting)
- Adapter: 10-30 epochs (similar to LoRA)

### Avoiding Common Mistakes

**Mistake 1: Overfitting**

Training loss drops to 0, but test performance doesn't improve.

Solution:
- Use early stopping (stop when validation loss plateaus)
- Regularization techniques
- More diverse training data

**Mistake 2: Catastrophic Forgetting**

Model forgets original knowledge while learning new task.

```
Before FT:  Good at general tasks, bad at specific task
After FT:   Good at specific task, worse at general tasks
```

Solution:
- Use lower learning rates
- Use PEFT (preserves base model)
- Mix task-specific and general data

**Mistake 3: Training on Test Data**

Model overfits to test set.

Solution:
- Use separate validation and test sets
- Don't tune hyperparameters on test set

---

## Part 4: Advanced Fine-Tuning Strategies (Pages 26-35)

### Multi-Task Fine-Tuning

**Idea:**

Train on multiple tasks simultaneously:

```
Task 1 (30%): Customer service responses
Task 2 (40%): Technical question answering
Task 3 (30%): Product recommendations
```

**Benefits:**
- More general model
- Prevents overfitting to single task
- Better transfer to new tasks

**Implementation:**

During training:
1. Sample from each task dataset
2. Mix in specific proportions
3. Update model on all tasks

### Curriculum Learning for Fine-Tuning

**Idea:**

Train on easier examples first, hard examples later:

```
Phase 1: Train on simple, clear examples
Phase 2: Train on medium-difficulty examples
Phase 3: Train on hard/ambiguous examples
```

**Benefits:**
- Faster convergence
- Better final performance
- Fewer training steps needed

**Example:**

For customer service:
- Phase 1: Simple greeting recognition
- Phase 2: Basic question answering
- Phase 3: Complex complaints and returns

### Catastrophic Forgetting Deep Dive

**Problem:**

When fine-tuning on new task, model "forgets" old knowledge:

```
Original model: Knows facts, can reason, good at general tasks
After FT on task X: Excellent at task X, worse at everything else
```

**Why It Happens:**

All billions of parameters adjusted to new task, away from original distribution.

**Solutions:**

**1. Regularization:**

Add penalty for changing parameters too much:

```
Loss = Task_Loss + λ × ||Original_Weights - New_Weights||²
```

Forces small changes to parameters.

**2. Adapter/LoRA:**

Don't change original weights, only add adapter:
- Original weights: Fixed
- Adapters: Trainable

Best solution for catastrophic forgetting.

**3. Mixed Training Data:**

Keep some general data in training:
- 70% task-specific data
- 30% general data

Reminds model of original knowledge.

**4. Lower Learning Rate:**

Slower updates mean smaller parameter changes.

### Zero-Shot and Few-Shot Adaptability

**Zero-Shot:**

No fine-tuning on task, but prompt well:

```
"Classify the following review as positive or negative.
Review: 'This product is amazing!'"
```

Works with good base models.

**Few-Shot:**

Show a few examples in prompt:

```
"Classify sentiment. Examples:
  'Great product!' → Positive
  'Terrible quality' → Negative
  'Product: This is amazing!' → "
```

Often better than zero-shot without fine-tuning.

**Fine-Tuning Combines Best:**

Examples:
- Zero-shot: 70% accuracy
- Few-shot: 75% accuracy
- Fine-tuned: 85% accuracy

Trade-off: Zero-shot costs nothing, fine-tuning costs compute but gives best results.

---

## Part 5: Production Considerations (Pages 36-45)

### Evaluating Fine-Tuned Models

**Metrics to Track:**

1. **Task Accuracy:** How often model is correct
2. **F1 Score:** Balance between precision and recall
3. **Human Evaluation:** Quality rated by humans
4. **Generalization:** Performance on held-out test set
5. **Safety Metrics:** Unwanted behaviors

**Benchmark Datasets:**

Standard datasets for evaluation:
- GLUE: General language understanding
- SQuAD: Question answering
- MMLU: Broad knowledge
- HumanEval: Code generation

### Deployment Strategies

**Strategy 1: Managed API**

Use provider's API with fine-tuned model:
- OpenAI fine-tuned GPT-3
- HuggingFace Hub
- AWS SageMaker

Pros: Automatic scaling, updates
Cons: Limited control, ongoing costs

**Strategy 2: Self-Hosted**

Deploy your model:

```
Fine-tuned model → Package → Docker → Server → API
```

Pros: Full control, one-time compute
Cons: Maintenance burden, scaling complexity

**Strategy 3: Hybrid**

Use PEFT adapters as plugins:

```
Base model (shared) + Task adapter 1 + Task adapter 2
                   + Task adapter 3
```

Pros: Memory efficient, multiple tasks
Cons: Coordination complexity

### Monitoring Fine-Tuned Models

**Drift Detection:**

Monitor for performance degradation:

```
Performance over time:
Week 1: 85% accuracy ✓
Week 2: 84% accuracy ✓
Week 3: 82% accuracy ✓
Week 4: 75% accuracy ✗ (degradation detected)
```

Possible causes:
- Input distribution changed
- Seasonal effects
- User behavior shifted

**Solution:**

- Retrain periodically
- Monitor key metrics
- Alert on drift
- Plan retraining cycle

---

## Part 6: Real-World Examples (Pages 46-50)

### Example 1: Customer Service Chatbot

**Setup:**

Base model: GPT-3.5-turbo
Task: Customer service responses

**Fine-Tuning Data:**

1,000 examples of:
- Customer questions
- Ideal responses

**Method:**

- LoRA for efficiency
- ~10K trainable parameters
- Training time: 2 hours on single GPU
- Cost: ~$50

**Results:**

- Accuracy: Improved from 70% to 85%
- Response quality: Noticeably better
- Safety: Fewer problematic responses

### Example 2: Medical Question Answering

**Setup:**

Base model: Llama-2-70B
Task: Medical question answering

**Fine-Tuning Data:**

10,000 medical Q&A pairs

**Method:**

- Instruction fine-tuning
- Full parameters (more critical for domain)
- Training time: 1 week on 8 A100 GPUs
- Cost: ~$5,000

**Results:**

- Accuracy: Improved from 60% to 82%
- Specialized knowledge: Strong medical reasoning
- Safety: Fewer dangerous errors

### Example 3: Code Generation

**Setup:**

Base model: Codex
Task: Python code generation

**Fine-Tuning Data:**

5,000 Python code examples with explanations

**Method:**

- LoRA for efficiency
- Training time: 4 hours
- Cost: ~$100

**Results:**

- Code correctness: Improved from 45% to 72%
- Style match: Code matches team style
- Performance: Fewer runtime errors

---

## Part 7: Advanced Topics and Future (Pages 51-55)

### Continual Learning

**Challenge:**

Continually adapt to new data without forgetting old knowledge.

**Approaches:**

1. **Experience Replay:** Mix old and new data
2. **Dynamic Adapter Allocation:** Create new adapters for new tasks
3. **Continual Fine-Tuning:** Periodic retraining on new data

### Domain Adaptation

**Challenge:**

Model trained on one domain (news) but deployed on another (medical).

**Solutions:**

1. **Fine-tuning:** Train on target domain
2. **Unsupervised Adaptation:** Learn from unlabeled target data
3. **Multi-Domain Training:** Train on multiple domains

### Federated Fine-Tuning

**Challenge:**

Fine-tune on sensitive user data without centralizing data.

**Solution:**

```
User 1 Device: Fine-tune locally
User 2 Device: Fine-tune locally
    ↓
Aggregate updates
    ↓
Improve shared model
```

Benefits: Privacy preserved, distributed learning

---

## Summary and Key Takeaways (Pages 56+)

### Fine-Tuning Principles

1. **Choose your method:**
   - Full FT: Best quality, most compute
   - LoRA: Good balance
   - Prefix: Fast, less flexible

2. **Prepare data carefully:**
   - Quality > Quantity
   - Clear examples > Ambiguous
   - Diverse > Repetitive

3. **Prevent catastrophic forgetting:**
   - Use PEFT methods
   - Lower learning rates
   - Mix task and general data

4. **Evaluate thoroughly:**
   - Task-specific metrics
   - Generalization tests
   - Human evaluation

5. **Monitor in production:**
   - Track performance
   - Detect drift
   - Plan retraining

### Decision Framework

**When to use which method:**

```
Need best quality? → Full fine-tuning
Limited budget? → LoRA
Need quick adaptation? → Prefix tuning
Multiple tasks? → Adapters
Training many tasks? → Multi-task FT
```

### Quiz: Test Understanding

**Q1:** Why does LoRA work better than naively training all parameters?
- A: It's mathematically proven
- B: It trains fewer but more important parameters
- C: It's just faster, not better
- **Answer: B** - Low-rank adaptation targets critical parameters

**Q2:** What causes catastrophic forgetting?
- A: Memory limitations
- B: Model architecture issues
- C: Parameters adjusted away from original distribution
- **Answer: C** - Especially with large learning rates

**Q3:** For a small dataset (100 examples), what's best?
- A: Full fine-tuning
- B: LoRA or adapter methods
- C: No fine-tuning possible
- **Answer: B** - PEFT prevents overfitting with small data

---

**End of CS-4: Large Language Model Fine-Tuning**

*Fine-tuning is how most practical LLM applications are built. Understanding these techniques is essential for deployment. The next courses focus on inference optimization (CS 5-6) for making fine-tuned models fast and efficient.*
