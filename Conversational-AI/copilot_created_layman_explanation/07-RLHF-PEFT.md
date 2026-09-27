# 🎁 Session 7: RLHF and PEFT (Reinforcement Learning & Parameter Efficient Fine-tuning)

**Complete Layman's Guide - From Kindergarten to Professional**

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [What is RLHF?](#what-is-rlhf)
3. [Explanation for a 5-Year-Old](#explanation-for-a-5-year-old)
4. [Explanation for a 30-Year-Old](#explanation-for-a-30-year-old)
5. [PEFT Methods](#peft-methods)
6. [Real-World Applications](#real-world-applications)
7. [Implementation Guide](#implementation-guide)

---

## Introduction

How did ChatGPT become so good at following instructions? It wasn't just trained on text—it was trained using human feedback. This revolutionized AI.

RLHF (Reinforcement Learning from Human Feedback) and PEFT (Parameter Efficient Fine-Tuning) are the techniques that transformed language models from average to exceptional.

---

## What is RLHF?

**The Core Concept:**

RLHF is training AI using human feedback as the reward signal. Instead of just predicting the next word, the AI learns what humans consider "good" responses.

**Why It Matters:**

```
Before RLHF:
- AI predicts next word based on training data
- Results: Sometimes weird, sometimes wrong
- Example: "How to make a bomb" → Surprisingly detailed response!

After RLHF:
- AI learns what humans find helpful and harmless
- Results: More aligned with human values
- Example: "How to make a bomb" → "I can't help with that"

Alignment = Better, safer AI
```

---

## Explanation for a 5-Year-Old

### 🎈 Teaching Your Pet a New Trick

**Imagine teaching your dog to sit:**

> "Method 1 (No Feedback):
> You throw a ball and hope the dog sits.
> Sometimes it does, sometimes it doesn't.
> The dog doesn't really learn the pattern.
>
> Method 2 (With Feedback - RLHF):
> - Dog does something
> - If it sits → TREAT! (reward!)
> - If it stands → No treat
> - Dog learns: Sitting = good, standing = bad
> - After repeating 100 times: Dog sits every time!
>
> Humans did the same with AI:
> - AI generates a response
> - Human says: 'That's good!' or 'That's bad'
> - AI learns to generate good responses
> - Result: Helpful, aligned AI
>
> That's RLHF!"

**Visual Comparison:**

```
❌ Regular Training (Pattern Matching):
AI: Sees "How to hack a computer" in training data
    Learns to continue with hacking instructions
Result: Unsafe

✅ RLHF (Learning from Human Feedback):
AI: Generates response
Human: "That response is harmful, rate it 1/10"
AI: Learns to avoid harmful responses
Result: Safe & helpful
```

---

## Explanation for a 30-Year-Old

### 💼 Technical Deep Dive

**RLHF Pipeline:**

```
Stage 1: Collect Human Feedback
├── Generate multiple responses to prompts
├── Have humans rank responses (A > B > C)
├── Convert rankings to preference pairs
│   ("Response A is better than Response B")
└── Collect 10,000+ preference labels

Stage 2: Train Reward Model
├── Input: prompt + response
├── Output: score (how good is the response?)
├── Architecture: Binary classification (better/worse)
├── Loss: Cross-entropy on preference pairs
├── Result: R_model(prompt, response) → 0-1 score

Stage 3: RL Training
├── Use reward model as training signal
├── Policy: Language model generating responses
├── For each prompt:
│   ├── Generate multiple responses (beam search)
│   ├── Score with reward model
│   ├── Use RL algorithm (PPO) to maximize score
│   └── Avoid mode collapse with KL divergence penalty
└── Result: Model that maximizes human preferences

Stage 4: Iterative Refinement
├── Sample model responses
├── Get more human feedback
├── Update reward model
├── Continue RL training
└── Repeat until convergence
```

**Key Algorithms:**

```
PPO (Proximal Policy Optimization):

Loss = E[min(r_t * Ā_t, clip(r_t, 1-ε, 1+ε) * Ā_t)]

Where:
- r_t = probability ratio (new policy / old policy)
- Ā_t = advantage (how good is this action?)
- clip(r_t, 1-ε, 1+ε) = prevent extreme updates

Benefit: Stable training, avoids catastrophic updates
```

**Reward Model Architecture:**

```
Typical design:

Input:
- Prompt: "Explain quantum computing"
- Response 1: [detailed, accurate explanation]
- Response 2: [vague, incorrect explanation]

Model:
├── Embed prompt and responses
├── Compute relevance/quality score
├── Preference score: How much better is Response 1?
└── Range: -2 (very bad) to +2 (very good)

Training Data:
- Humans rank pairs of responses
- Convert to: (prompt, better_response, worse_response)
- Train to maximize: score(better) > score(worse)

Accuracy: 80-90% on held-out preferences
```

---

## PEFT Methods

### ⚡ Parameter Efficient Fine-Tuning

**Problem:**
```
Full Fine-tuning Challenges:
- GPT-3: 175B parameters
- Memory needed: 700GB+ (4 × 175B in float32)
- Not practical for most organizations

Solution: PEFT
- Only train small subset of parameters
- 99% reduction in memory
- Similar performance
```

**Main PEFT Methods:**

**1. LoRA (Low-Rank Adaptation)**

```
Idea: Instead of updating W directly, update a small 
      low-rank decomposition

Original: W (large matrix)
Update: W_new = W + ΔW

LoRA: W_new = W + A × B
where A and B are small matrices (rank r << original)

Example:
Original layer: 768 × 768 = 589,824 parameters
LoRA update: 768 × 16 + 16 × 768 = 24,576 parameters

Savings: 96% fewer parameters to train!

Code:
from peft import LoraConfig, get_peft_model
config = LoraConfig(
    r=16,  # rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05
)
model = get_peft_model(model, config)
```

**2. QLoRA (Quantized LoRA)**

```
Combines:
- 4-bit quantization (compress model)
- LoRA (efficient fine-tuning)

Benefits:
- 75% memory reduction vs LoRA
- 99.9% reduction vs full fine-tuning
- Run large models on consumer GPU!

Example:
- 70B parameter model
- Full fine-tune: 280GB memory
- LoRA: 10GB memory
- QLoRA: 2.4GB memory (fits on RTX 3090!)
```

**3. Prefix Tuning**

```
Idea: Add learnable tokens at input, freeze model

Prefix: [learn_1, learn_2, ..., learn_k] + actual prompt

Advantages:
- Very small parameter count
- Easy to deploy (just save prefix)
- Multiple tasks with single model

Trade-off:
- Slightly lower performance than LoRA
- Less flexible
```

**4. Adapter Tuning**

```
Idea: Insert small adapter modules between layers

Architecture:
Dense → Adapter (smaller hidden size) → Dense

Parameters:
- Original: 768 → 768
- Adapter: 768 → 64 → 768 (tiny!)

Benefit:
- Multiple adapters can be loaded
- Switch between tasks
- Compact storage
```

### 📊 PEFT Comparison

```
Method            Memory  Speed  Quality  Code
──────────────────────────────────────────────
Full Fine-tune    700GB   1x     100%     Simple
LoRA              10GB    1.2x   98%      Easy
QLoRA             2.4GB   1.4x   97%      Easy
Adapter           5GB     1.1x   97%      Medium
Prefix            3GB     1.05x  95%      Medium

Recommendation: Use QLoRA for best balance
```

---

## Real-World Applications

### 🎯 Example 1: Creating ChatGPT-like Model

**Process OpenAI likely used:**

```
Step 1: Base Model
├── Start with GPT-3 (175B params)
├── Trained on diverse web data
└── Result: Can predict next word, but not aligned

Step 2: Supervised Fine-tuning (SFT)
├── Hire contractors: $50-100/hour
├── Collect 10,000 high-quality prompt-response pairs
├── Fine-tune on this data
├── Result: Model knows correct format, basic alignment
├── Cost: ~$100-500K

Step 3: Reward Model Training
├── Have humans rank 50,000 prompt pairs
├── Train separate model to predict preferences
├── Cost: ~$50-200K

Step 4: RLHF Fine-tuning
├── Use PPO algorithm with reward model
├── Train on 1M+ prompts
├── Iteratively improve
├── Cost: ~$1-5M (significant compute)

Step 5: Deployment
├── Serve to users
├── Collect more feedback
├── Continue improving

Total Investment: $2-10M per model
But: Enables $1B+ product!
```

### 🏥 Example 2: Domain-Specific Medical Model

**Fine-tuning Llama 2 for medical use:**

```
Scenario: Need medical diagnosis assistant

Option A: Use GPT-4
- Cost: $50 per complex query
- Privacy: Data goes to OpenAI
- Licensing: Terms of service issues
- Compliance: HIPAA challenges

Option B: Fine-tune Llama 2 with PEFT
├── Collect 10,000 medical cases (labeled)
├── Use QLoRA for efficiency
├── Training cost: $200
├── Running cost: ~$0.01 per query
├── Privacy: On-premise operation
├── Compliance: Full control

Results:
- Sensitivity: 94% (correctly identifies cases)
- Specificity: 96% (correctly rejects non-cases)
- Cost: 100x cheaper than GPT-4
- Privacy: HIPAA compliant
- Speed: Sub-100ms latency

ROI: Pay for itself in first week
```

### 💼 Example 3: Customer Service Personalization with PEFT

**Personalized support for different customer segments:**

```
Base Model: Llama 2 7B

Segment 1: Technical Users
├── Fine-tune with LoRA
├── Data: Technical support tickets
├── Tone: Detailed, code-heavy
├── Adapter parameters: 3M (vs 7B base)

Segment 2: Non-technical Users
├── Fine-tune with LoRA
├── Data: Simple support tickets
├── Tone: Friendly, step-by-step
├── Adapter parameters: 3M

Segment 3: Business Users
├── Fine-tune with LoRA
├── Data: Enterprise support
├── Tone: Professional, ROI-focused
├── Adapter parameters: 3M

At Runtime:
- Identify customer segment
- Load appropriate adapter (3MB each)
- Inference uses same base model + adapter
- Result: Personalized experience, 3% of full model size

Cost:
- Training: $1,000 total
- Storage: 30MB (3 adapters × 3MB each)
- vs. training 3 separate models: 21GB storage

Savings: 99% reduction in storage
```

---

## Implementation Guide

### 💻 Code Example: QLoRA Fine-tuning

```python
# Fine-tune Llama 2 with QLoRA

from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from bitsandbytes import quantization_config

# Step 1: Load model in 4-bit
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b",
    quantization_config=quantization_config,
)

# Step 2: Configure LoRA
lora_config = LoraConfig(
    r=16,  # LoRA rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# Step 3: Get PEFT model
model = get_peft_model(model, lora_config)

# Step 4: Prepare dataset
def prepare_data(example):
    return {
        "input_ids": tokenizer(
            example["text"],
            max_length=512,
            truncation=True,
            return_tensors="pt"
        )["input_ids"]
    }

dataset = dataset.map(prepare_data)

# Step 5: Train
trainer = Trainer(
    model=model,
    train_dataset=dataset,
    args=TrainingArguments(
        output_dir="./output",
        num_train_epochs=3,
        per_device_train_batch_size=4,  # Small due to limited memory
        learning_rate=1e-4,
    )
)

trainer.train()

# Step 6: Save and load
model.save_pretrained("./my-adapter")  # Only saves adapter, not full model

# Load later
model = get_peft_model(base_model, lora_config)
model.load_adapter("./my-adapter")
```

### 🛠️ Best Practices

```
RLHF Best Practices:
□ Collect diverse feedback (multiple annotators)
□ Use clear labeling guidelines
□ Monitor reward model accuracy
□ Avoid reward hacking (model gaming the metric)
□ Use KL penalty to stay close to base model
□ Regular validation on held-out preferences

PEFT Best Practices:
□ Start with LoRA (good balance)
□ Increase rank if performance insufficient
□ Use QLoRA for memory constraints
□ Test different target modules
□ Monitor training vs validation quality
□ Save adapters separately from base model
```

---

## Advanced Concepts

### 🚀 Beyond Basic RLHF

**DPO (Direct Preference Optimization):**

```
Simplification of RLHF:
- Skip reward model training
- Directly optimize on preferences
- Fewer steps, faster training
- Same performance!

Equation:
L = -log σ(β log p_θ(y_w|x) - β log p_θ(y_l|x))

Where:
- σ = sigmoid
- y_w = preferred response
- y_l = non-preferred response
- β = temperature parameter
```

**IPO (Identity Preference Optimization):**

Even simpler variant of DPO with better properties.

---

## Summary

**Key Takeaways:**

✅ RLHF aligns AI with human values and preferences
✅ Makes AI more helpful, harmless, and honest
✅ PEFT enables efficient fine-tuning on consumer hardware
✅ QLoRA combines quantization + LoRA for best efficiency
✅ Methods like LoRA achieve 98% of full fine-tune performance
✅ Multiple adapters can run on single base model

**For Different Audiences:**

**5-Year-Old:** "We teach AI what's good and bad by showing it examples, just like training a dog with treats!"

**Professional:** "RLHF with PPO and preference-based reward modeling coupled with QLoRA-based parameter-efficient adaptation enables cost-effective alignment and customization of large language models at scale."

---

**Created**: 2024
**Domain**: LLM Alignment & Efficient Fine-tuning
**Difficulty**: Advanced
**Estimated Reading Time**: 45-60 minutes

---

**End of Document - 25 Page Comprehensive Guide**
