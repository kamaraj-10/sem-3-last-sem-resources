# CS-2: Large Language Model Training

## Comprehensive Guide to Understanding LLM Training

---

## Part 1: The Foundation - What Training Means (Pages 1-5)

### What Does "Training" Mean?

When we say an LLM is "trained," we mean the model learned from examples:

**Simple Analogy:**
- A child learns language by hearing it (input examples)
- A model learns language by reading text (input examples)

**The Process:**
1. Show the model tons of text
2. Tell it to predict the next word
3. When it's wrong, adjust its internal "brain" (parameters) slightly
4. Repeat millions of times with different text
5. Eventually, it becomes very good at prediction

### Self-Supervised Learning: The Key Innovation

**Traditional Supervised Learning (Old Way):**
```
Input: "The dog is __"
Output: "happy" (human labels this)
```

Problem: Need humans to label everything. Very expensive and slow.

**Self-Supervised Learning (LLM Way):**
```
Input: "The dog is happy and __"
Output: "playful" (comes naturally from the text itself!)
```

Insight: The text itself provides the labels! We don't need human annotation.

### Why This Matters

Self-supervised learning allowed us to:
1. Use ALL text on the internet (not just labeled data)
2. Train models 1000x larger than before
3. Create models that work well for many tasks without special tuning

**Example from Slide 5:**

The training process described:
- Model reads vast amounts of text
- Tries to predict the next word
- Gets corrected automatically (the actual next word is the label)
- Learns language structure without explicit rules

**Two Types of Self-Supervised Tasks:**

1. **Causal Language Modeling (GPT style):**
   - Predict the next word given previous words
   - Example: "The quick brown fox jumps __" → predict "over"
   - Used for: Chatbots, text generation

2. **Masked Language Modeling (BERT style):**
   - Predict a hidden word given context before AND after
   - Example: "The quick brown __ jumps over" → predict "fox"
   - Used for: Understanding, classification tasks

---

## Part 2: Understanding Training Mechanisms (Pages 6-15)

### The Loss Function: Teaching the Model

**What is Loss?**

"Loss" is a number that measures how wrong the model is:
- Loss = 0: Perfect prediction
- Loss = 100: Terrible prediction

**Simple Example:**

Model predicts: "The dog is jumping with 90% confidence"
Actual word: "sleeping"

Loss = -log(0.10) ≈ 2.3 (high loss because very wrong)

vs.

Model predicts: "The dog is sleeping with 85% confidence"
Actual word: "sleeping"

Loss = -log(0.85) ≈ 0.16 (low loss because mostly right)

### Backpropagation: The Learning Algorithm

**How the Model Learns:**

Think of it like learning to throw darts:

1. **Make prediction** (throw dart)
2. **Check error** (how far from target)
3. **Adjust position** (move slightly)
4. **Repeat** (throw again from new position)

**In LLMs:**

1. **Forward Pass:** Process input, make prediction
2. **Calculate Loss:** Compare prediction to actual
3. **Backward Pass:** Calculate gradients (how much to adjust each parameter)
4. **Update Parameters:** Adjust weights using gradients
5. **Repeat** with next batch of data

**The Magic:**

With backpropagation, billions of parameters can be adjusted automatically to minimize loss. No human programming needed!

### The Training Dataset: Quality Matters

**What Gets Used for Training:**

Common sources:
- Wikipedia (knowledge)
- Books (reasoning, narrative)
- Code repositories (logic)
- Web text (diverse information)
- Academic papers (deep knowledge)

**Important Insight:**

The training data quality and content directly affects the model:
- Trained on mostly tech = better at programming
- Trained on diverse data = better at many tasks
- Trained on biased data = biased model
- Trained on low-quality data = low-quality output

**Example:**
GPT-3 was trained on 570GB of text. That's like having read thousands of books millions of times over. The model absorbed patterns about:
- Grammar and syntax
- Facts and knowledge
- Writing styles
- Problem-solving approaches

---

## Part 3: Deep Dive into Training Concepts (Pages 16-25)

### Training Phases and Curriculum

**Phase 1: Pretraining (The Long Learning)**

Duration: Weeks to months on thousands of GPUs
Data: Hundreds of billions of words
Goal: Learn general language patterns

Process:
```
Epoch 1: Read all 300 billion words, lose: 4.5
Epoch 2: Read again, loss: 4.2
Epoch 3: Read again, loss: 3.9
...
Epoch 100: Read again, loss: 2.1
```

Each time through, the model gets better at prediction.

**Why So Long?**
- The model needs to see patterns multiple times
- Complex patterns need multiple exposures
- Larger models need more training

**Phase 2: Fine-tuning (The Specialized Learning)**

Duration: Hours to days
Data: High-quality examples for specific task
Goal: Specialize for chatbot, coding, etc.

Process:
```
Start with pretrained model (already knows language)
Show examples of good chatbot responses
Model learns: How should a helpful assistant respond?
```

**Analogy:**
- Pretraining: Get a general education (read widely)
- Fine-tuning: Specialize in medicine/law (take additional courses)

### Hyperparameters: The Choices

Various choices affect training:

**Learning Rate:** How fast to adjust parameters
- Too high: Overshoots the solution (like running too fast on a slippery floor)
- Too low: Takes forever to train (like crawling)
- Just right: Converges smoothly

**Batch Size:** How many examples before updating
- Larger batch: Smoother training but needs more memory
- Smaller batch: Noisier but uses less memory

**Number of Epochs:** How many times to see all data
- More epochs: Better learning but diminishing returns
- Too many: Overfitting (memorizes instead of learns patterns)

**Optimizer:** The algorithm for updating parameters
- Adam: Popular, adapts learning rate
- SGD: Simple, sometimes better
- Others: Specialized for different scenarios

### The Challenge of Scale: Why Training is Hard

**Computational Cost:**
- GPT-3 training: ~300 years of single GPU computation
- Cost: ~$4.6 million in cloud compute
- Time: Actually completed in ~34 days using 1,000s of GPUs

**Memory Requirements:**
- Storing model: 175B parameters × 2 bytes (float16) = 350GB per copy
- Multiple copies needed for different stages
- Total memory: Multiple terabytes

**Solution: Distributed Training**

```
Single GPU: 1 training step per 10 seconds
10 GPUs perfectly synced: 10 training steps per 10 seconds
1000 GPUs: 1000 steps per 10 seconds (but coordination is hard!)
```

Challenges in distributed training:
- Network communication (bottleneck)
- Synchronization (waiting for slowest GPU)
- Fault tolerance (if one GPU fails, restart)

### Section 3: Slide 30 - Scaling Laws (Deep Analysis)

**Slide 30 Content: Scaling Laws**

Scaling laws are empirical findings showing how model performance relates to:
1. Model size (number of parameters)
2. Training data size (number of tokens)
3. Computation (total operations)

**Key Finding: The Power Law**

Performance ∝ (Scale)^(-α)

Where α is typically 0.07 to 0.1

**What This Means:**

Performance improves logarithmically with scale:
- 10B parameters model: Baseline
- 100B parameters model: ~10% better (logarithmic improvement!)
- 1T parameters model: ~20% better

**Important Implications:**

1. **Size matters, but with diminishing returns**
   - 2x bigger ≠ 2x better
   - 2x bigger ≈ 10-15% better

2. **No capability ceiling found yet**
   - Even at 1T parameters, still improving
   - Suggests models can keep getting better

3. **Compute efficiency**
   - Sometimes training longer is better than making bigger
   - Sometimes data quality beats raw data quantity

**Practical Implications for Training:**

```
Option A: Train small model (10B) on all data
Option B: Train large model (100B) on subset of data
Option C: Train medium model (50B) on carefully selected data

Research shows: B or C often beats A
```

### Beyond Pure Scaling: Compound Factors

**Emergent Abilities:**

Some abilities only appear above a certain scale:

```
Model Size | Ability
10B       | Can answer simple questions
50B       | Can chain reasoning (if A then B, if B then C)
100B+     | Can understand nuanced instructions
200B+     | Can do "in-context learning" (learn from examples in conversation)
```

**Why This Happens:**

With more capacity:
- The model can store more knowledge
- Can develop more sophisticated internal representations
- Can perform operations internally without being explicitly programmed

**Real Example:**

Small models: "Q: What's 2+2? A: __ " → Often wrong
Large models: "Q: What's 2+2? A: 4"
Larger models: "Let me think through this step by step: 2+2 = (2+1)+1 = 3+1 = 4"

---

## Part 4: The Optimization Problem (Pages 26-35)

### What We're Actually Optimizing

**The Mathematical Goal:**

Minimize: Loss = Average(negative log probability of correct next token)

In simple terms:
- For each word in training data
- Predict its probability
- High probability → low loss → good
- Low probability → high loss → bad
- Minimize the average loss across all training data

### Different Loss Objectives

**Causal (Next Token Prediction):**
```
"The dog is" → Predict "happy"
Loss = -log(P(happy | "The dog is"))
```

**Masked (Fill the Blank):**
```
"The __ is happy" → Predict "dog"
Loss = -log(P(dog | "The __ is happy"))
```

**Contrastive (Which is most similar):**
```
Query: "positive review"
Good example: "I loved this product! ⭐⭐⭐⭐⭐"
Bad example: "I hated this product! ⭐"
Loss = penalize if good scores lower than bad
```

### Avoiding Common Training Problems

**Problem 1: Overfitting**

Model memorizes training data instead of learning patterns:
```
Train Loss: 0.1 (very low)
Test Loss: 3.5 (very high)
```

Cause: Too many parameters, not enough data, or too many epochs

Solution:
- More diverse training data
- Regularization techniques
- Early stopping

**Problem 2: Underfitting**

Model doesn't learn enough from data:
```
Train Loss: 2.5 (still high)
Test Loss: 2.6 (similar, both high)
```

Cause: Model too small, not enough training, or poor learning rate

Solution:
- Larger model
- More training
- Better hyperparameters

**Problem 3: Mode Collapse**

Model only generates a few types of outputs:
```
Q: "Write a poem about love"
A: "Love is great, love is wonderful, love is amazing..."
(Repeats with slight variations)
```

Cause: Training objective doesn't encourage diversity

Solution:
- Better data curation
- Diverse training examples
- Different loss formulations

### Techniques to Improve Training

**1. Data Augmentation:**

Transform existing data to create new examples:
- Paraphrase sentences
- Back-translation (translate to other language and back)
- Token replacement

**2. Regularization:**

Techniques to prevent overfitting:
- Dropout: Randomly ignore some neurons during training
- Layer normalization: Normalize hidden states
- Weight decay: Penalize large parameters

**3. Curriculum Learning:**

Train on easy examples first, hard ones later:
- Start with simple sentences
- Progress to complex
- Model learns fundamentals first

---

## Part 5: From Training to Deployment (Pages 36-45)

### Checkpoints: Saving Progress

During training, models are saved periodically:

```
Step 0:     Loss = 5.0, Save checkpoint_0
Step 1000:  Loss = 4.2, Save checkpoint_1000
Step 10000: Loss = 3.1, Save checkpoint_10000
Step 100000: Loss = 2.1, Save checkpoint_100000
```

Why save checkpoints?
- Can resume if training interrupted
- Can compare different stages
- Can choose best version
- Can analyze learning progression

### Evaluation During Training

**Metrics to Monitor:**

1. **Training Loss:** How well on seen data
2. **Validation Loss:** How well on unseen data
3. **Test Loss:** Final evaluation on held-out test set
4. **Specific Tasks:** Accuracy on specific benchmarks

**The Learning Curves:**

```
Loss
  |    Training Loss (decreasing smoothly)
  |   /
  |  /  Validation Loss (decreases but plateaus)
  | /
  |/___________________________
         Training Steps →
```

**When to Stop?**

Typically when:
- Validation loss plateaus (not improving)
- Overfitting becomes clear (train loss << validation loss)
- Budget runs out (money, time, or compute)

### Transfer Learning: Why Pretraining Matters

**Without Pretraining:**
```
Train model from scratch for task
- Millions of parameters to learn
- Need huge labeled dataset
- Takes weeks/months
- Often fails with small data
```

**With Pretraining:**
```
Start with pretrained LLM
- Already learned language structure
- Fine-tune on task-specific data
- Takes hours/days
- Works well even with small data
```

**Example:**
- Task: Classify emails as spam or not spam
- Without pretraining: Need 100,000 labeled emails
- With pretraining: Works well with 1,000 labeled emails

This is why pretrained models are so valuable!

---

## Part 6: Real-World Training Examples (Pages 46-50)

### GPT-3 Training Process (Historical Example)

**Specifications:**
- Parameters: 175 billion
- Training data: 570 GB of text (processed into 499 billion tokens)
- Training time: ~34 days on 1,024 V100 GPUs
- Estimated cost: $4.6 million

**Learning Timeline:**
```
Day 1-5:    Model learns basic patterns, loss dropping rapidly
Day 5-15:   Model learns semantic relationships, knowledge facts
Day 15-25:  Fine-tuning behaviors, special tokens, edge cases
Day 25-34:  Convergence, diminishing improvements
```

**Key Findings:**
- Scaling from 1.3B to 175B parameters improved performance ~3x
- Larger models were more sample-efficient (learned faster with less data)
- Emergent abilities appeared (e.g., doing arithmetic, translation, Q&A)

### Modern Training Considerations

**Efficiency Improvements:**

Recent models improve on GPT-3 while using less compute:

1. **Better Architecture:** Efficiency improvements in Transformer design
2. **Better Data:** Curated datasets beat raw internet data
3. **Better Training:** Techniques like flash attention speed things up
4. **Better Algorithms:** Improved optimization methods

Result: LLaMA-65B > GPT-3-175B with 50x less compute during training

### Training vs. Inference: The Asymmetry

**Training:**
- Expensive (millions of dollars)
- Slow (weeks to months)
- One-time cost
- Requires GPUs optimized for training

**Inference:**
- Cheap (cents per 1M tokens with optimization)
- Fast (milliseconds per response)
- Per-user cost
- Can use specialized inference hardware

**Implication:**
Once trained, models are cheap to run. The expensive part is the initial training.

---

## Part 7: Challenges and Future Directions (Pages 51+)

### The Energy Problem

**Current Reality:**
- Training large models uses huge amounts of electricity
- Estimated: GPT-3 training ≈ 1,300 MWh (enough to power 100 homes for a year)
- Carbon emissions: ~600 tons CO2 (equivalent to driving a car 1,200,000 miles)

**Future Directions:**
- More efficient architectures
- Renewable energy for training
- Smaller models with better training methods
- Distillation (small models learn from large ones)

### The Data Problem

**Issue:**
We're running out of high-quality text data on the internet. Current estimates:
- ~2 trillion tokens of high-quality text exist
- Already training models on most of it
- May need synthetic data or non-text data soon

**Solutions Being Explored:**
- Training on code (more structured than text)
- Synthetic data (generate examples)
- Multimodal training (images + text + audio)
- Reinforcement learning (learn from feedback, not just text)

### The Capability Problem

**Question:**
Can we keep improving LLMs by just scaling?

**Evidence:**
- Scaling laws hold (improvements continue)
- But gains are slower
- Some capabilities seem limited by architecture

**Solutions Being Explored:**
- New architectures (beyond Transformers)
- Hybrid approaches (combining different model types)
- Knowledge integration (explicitly add facts)
- Reasoning capabilities (train for step-by-step logic)

---

## Summary: Key Takeaways

### The Training Process Overview

1. **Collect Data:** Billions of words from diverse sources
2. **Pretrain:** Self-supervised learning (predict next word)
3. **Fine-tune:** Supervised learning (learn specific task)
4. **Evaluate:** Test on benchmarks
5. **Deploy:** Use in production

### Important Insights

**Insight 1: Scale is powerful**
- Larger models learn better with same compute
- But efficiency diminishes logarithmically
- 10x bigger ≠ 10x better, but still significantly better

**Insight 2: Data quality > Data quantity**
- 100M high-quality words > 1B low-quality words
- Curated data beats raw internet
- Diverse data beats narrow data

**Insight 3: Self-supervised learning is revolutionary**
- No need for human labels
- Can use all text data
- Enables trillion-parameter models

**Insight 4: Pretraining transfers powerfully**
- Pretrained models work well with little task-specific data
- Save computation time and resources
- Enable quick adaptation to new tasks

### Learning Framework

**To truly understand training:**

1. **Know the objective:** Minimize loss on language prediction
2. **Understand backprop:** How gradients flow backward
3. **Grok the scaling:** Performance improves with scale but not linearly
4. **Learn the tricks:** Regularization, curriculum, careful hyperparameters
5. **Appreciate the cost:** Massive compute and energy requirements

---

## Quiz: Test Your Understanding

**Q1:** Why is self-supervised learning better than supervised learning for LLMs?
- A: It requires human labels, so more accurate
- B: It automatically provides labels from text structure, enabling use of all data
- C: It's faster to implement
- **Answer: B** - Self-supervised learning uses the text itself as labels

**Q2:** What does "loss" measure in training?
- A: How happy the model is
- B: How wrong the model's predictions are
- C: How much money we spent
- **Answer: B** - Loss quantifies prediction error

**Q3:** If a model has high training loss but also high validation loss, what's likely happening?
- A: Overfitting
- B: Underfitting
- C: Perfect training
- **Answer: B** - Both losses are high, so model isn't learning well (underfitting)

**Q4:** Scaling laws suggest that making a model 10x larger will improve performance by approximately:
- A: 10x
- B: 3-5x
- C: 1.5-2x
- **Answer: C** - Performance scales logarithmically, not linearly

---

**End of CS-2: Large Language Model Training**

*Understanding training is crucial for comprehending why models behave as they do and how to improve them. The next course (CS-3) explores architectural innovations that make training more efficient and effective.*
