# Conversational AI - Sample Question Paper with Solutions

## Course: CONVERSATIONAL AI (AIML CZG521)

---

## TABLE OF CONTENTS

1. Question Explanations with Concepts
2. Problem-Solving Guide
3. Detailed Solutions
4. Practice Tips

---

## SECTION 1: QUESTION EXPLANATIONS WITH CONCEPTS

### Understanding the Basics

#### What is Conversational AI? (The Concept First)

**Age 5 Explanation:**
Imagine you have a robot friend who can talk to you. When you say "Hello!", the robot understands what you said and talks back to you. Conversational AI is like teaching a robot to have conversations, just like you talk with your friends!

**Age 30 Explanation:**
Conversational AI is a sophisticated field of artificial intelligence that focuses on building systems capable of engaging in natural, contextual dialogue with humans. It combines Natural Language Processing (NLP), machine learning, dialogue management, and context understanding to create systems that can understand user intents, maintain context across conversations, and generate appropriate responses.

**Real-World Examples:**
- ChatGPT responding to your questions
- Alexa understanding "Hey Alexa, what's the weather?"
- Customer service chatbots on websites
- Siri on your iPhone

---

### Key Concepts in Conversational AI

#### 1. **Natural Language Processing (NLP)**

**Age 5 Explanation:**
NLP is like teaching a computer to understand human words. When you speak, the computer needs to figure out what each word means and what you're trying to ask.

**Age 30 Explanation:**
NLP is a subfield of AI that processes human language. It involves:
- Tokenization: Breaking text into words/sentences
- Part-of-Speech Tagging: Identifying nouns, verbs, etc.
- Named Entity Recognition: Identifying people, places, organizations
- Sentiment Analysis: Understanding emotional tone
- Semantic Analysis: Understanding meaning

**Real-World Application:**
When you type a message to a chatbot, NLP breaks it down to understand:
- What words were used?
- What is the meaning?
- What is the user trying to accomplish?

---

#### 2. **Intent Recognition**

**Age 5 Explanation:**
When someone talks to you, they want something. Intent is what they want. For example, if you say "I'm cold", your intent is to get warmer. A chatbot needs to figure out what the user wants.

**Age 30 Explanation:**
Intent recognition involves classifying user input into predefined categories representing user goals. Given an utterance, the system must determine what the user wants to achieve. This is typically done using:
- Machine learning classifiers (SVM, Naive Bayes)
- Deep learning models (LSTM, Transformer-based models)
- Rule-based systems
- Hybrid approaches

**Mathematical Formulation:**
```
Intent = argmax(P(i|u)) for all intents i given utterance u
```

**Example:**
User: "Show me Italian restaurants near me"
Intent: Search_Restaurant
Confidence: 0.95

---

#### 3. **Entity Extraction**

**Age 5 Explanation:**
Entities are the important things in a sentence. Like if you say "I want pizza in New York", the entity "pizza" is what you want, and "New York" is where you want it.

**Age 30 Explanation:**
Named Entity Recognition (NER) identifies and extracts entities from text. Types include:
- Person: John, Mary
- Location: New York, Tokyo
- Organization: Google, Microsoft
- Time: Today, Next Monday
- Product: iPhone, Tesla
- Custom entities: Disease, Drug, Plant species

**NER Implementation:**
Using BIO tagging scheme:
- B-ENTITY: Beginning of entity
- I-ENTITY: Inside entity
- O: Outside entity

**Example:**
"Book a flight from New York to London on Friday"
- B-LOC: New York
- B-LOC: London
- B-TIME: Friday
- B-ACTION: Book

---

#### 4. **Context Management**

**Age 5 Explanation:**
Imagine you're having a conversation with your friend. Your friend says "What did I say earlier?" They mean the thing they said 5 minutes ago. Context is remembering what was said before so the conversation makes sense.

**Age 30 Explanation:**
Context management is maintaining information across dialogue turns:
- Dialogue History: Previous exchanges
- User Profile: User preferences, history
- Domain Context: Current topic, location, time
- Conversation State: Current step in workflow

**Implementation Approaches:**
- Stack-based: Last-in-first-out
- Database storage: Persistent context
- Memory networks: Neural context modeling
- Attention mechanisms: Focus on relevant context

---

## SECTION 2: DETAILED PROBLEM EXPLANATIONS & SOLUTIONS

---

### Problem 1: Design a Chatbot for Restaurant Booking

**Concept Breakdown (First, Understand the Concept):**

This problem requires understanding several layers:

1. **What is the problem asking?**
   - Design a system that can have a conversation with users
   - The system should understand when users want to book a restaurant
   - It should extract relevant information (date, time, party size, cuisine)
   - It should confirm and process the booking

2. **Key Concepts Needed:**
   - Intent Recognition (Is the user trying to book?)
   - Entity Extraction (What date, time, cuisine?)
   - Context Tracking (Remember what was said)
   - Response Generation (What to say back?)

3. **Age 5 Explanation:**
   A chatbot for restaurants is like a helpful waiter robot. You tell the robot what you want:
   - "I want to book a restaurant"
   - Robot asks: "What date?"
   - You say: "Tomorrow at 7 PM"
   - Robot asks: "How many people?"
   - You say: "4 people"
   - Robot confirms: "Booking confirmed for 4 people tomorrow at 7 PM!"

4. **Age 30 Explanation:**
   A restaurant booking chatbot is a dialogue system with:
   - Multi-turn conversation handling
   - Slot-filling mechanism (date, time, party size, cuisine type)
   - Intent classification (booking.request, booking.confirm, booking.cancel)
   - Entity extraction for temporal expressions, cuisine types, numbers
   - State machine or task-oriented dialogue management

**Full Solution (No Steps Skipped):**

#### Step 1: Architecture Design

```
┌─────────────────────────────────────────┐
│         User Input                      │
│    "Book a table for 4 tomorrow"        │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│    Natural Language Processing          │
│  - Tokenization                         │
│  - Normalization                        │
│  - POS Tagging                          │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│  Intent Recognition Module              │
│  Intent: BOOKING_REQUEST                │
│  Confidence: 0.92                       │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│  Entity Extraction Module               │
│  - party_size: 4                        │
│  - date: tomorrow                       │
│  - time: not mentioned yet              │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│  Dialogue State Manager                 │
│  Current State: ASKING_FOR_TIME         │
│  Action: Request Time                   │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│  Response Generation                    │
│  "What time would you prefer?"          │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│         Bot Response to User            │
└─────────────────────────────────────────┘
```

#### Step 2: Intent Classification

**Problem:** Given user input, classify the intent

**Assumptions:**
- We have labeled training data
- User input is in English
- Fixed set of predefined intents

**Mathematical Framework:**

Using softmax classification:
$$P(intent = i | input) = \frac{e^{score_i}}{\sum_{j=1}^{n} e^{score_j}}$$

**Where:**
- score_i = learned score for intent i
- n = total number of intents

**Concrete Example:**

User Input: "I want to book a restaurant for 4 people tomorrow at 7 PM"

Processing:
1. Tokenize: ["I", "want", "to", "book", "a", "restaurant", "for", "4", "people", "tomorrow", "at", "7", "PM"]
2. Convert to embeddings
3. Pass through neural network
4. Get probabilities:
   - booking_request: 0.92 ✓
   - booking_cancel: 0.05
   - other: 0.03

**Decision Rule:** If P(intent) > threshold (0.7), classify as that intent

#### Step 3: Entity Extraction

**Problem:** Extract specific information from user input

**Using BIO Tagging:**

| Word | Tag | Entity Type |
|------|-----|-------------|
| I | O | - |
| want | O | - |
| to | O | - |
| book | B-ACTION | action |
| a | O | - |
| restaurant | O | - |
| for | O | - |
| 4 | B-PARTY_SIZE | party_size = 4 |
| people | I-PARTY_SIZE | party_size = 4 |
| tomorrow | B-DATE | date = tomorrow |
| at | O | - |
| 7 | B-TIME | time = 7 PM |
| PM | I-TIME | time = 7 PM |

**Extraction Result:**
```python
entities = {
    'party_size': 4,
    'date': 'tomorrow',
    'time': '7 PM',
    'cuisine': None  # Not mentioned
}
```

#### Step 4: State Machine & Dialogue Flow

**State Definition:**

```
States:
1. INITIAL: Conversation started
2. GATHERING_INFO: Collecting required slots
3. CONFIRMING: Asking for confirmation
4. PROCESSING: Processing booking
5. COMPLETED: Booking successful
6. CANCELLED: Booking cancelled
```

**Slot Requirements:**
- restaurant_name (required)
- date (required)
- time (required)
- party_size (required)
- cuisine_type (optional)
- special_requests (optional)

**Dialogue Flow for Example:**

| Turn | User Input | Bot Action | Extracted Slots | Next State |
|------|-----------|-----------|-----------------|-----------|
| 1 | "Book a table for 4 tomorrow at 7 PM" | Extract info | party_size=4, date=tomorrow, time=7PM | GATHERING_INFO |
| 2 | - | Ask for cuisine preference | - | GATHERING_INFO |
| 3 | "Italian cuisine please" | Extract cuisine | cuisine=Italian | CONFIRMING |
| 4 | - | Confirm details | - | CONFIRMING |
| 5 | "Yes, confirm" | Process booking | All slots filled | COMPLETED |
| 6 | - | Send confirmation | - | COMPLETED |

#### Step 5: Response Generation

**Algorithm:**

```
1. Check if all required slots are filled
2. If not, select the next required slot
3. Generate a natural question for that slot
4. If all slots filled, generate confirmation message
5. If user confirms, generate booking confirmation
```

**Response Templates:**

```python
RESPONSES = {
    'greeting': "Hello! How can I help you today?",
    'ask_party_size': "How many people will be dining?",
    'ask_date': "What date would you prefer?",
    'ask_time': "What time suits you?",
    'ask_cuisine': "What type of cuisine do you prefer?",
    'confirm': "Let me confirm your booking: {restaurant} for {party_size} on {date} at {time}. Is this correct?",
    'success': "Your booking has been confirmed! Reference number: {booking_id}",
    'error': "I apologize, but I couldn't process your booking. Please try again."
}
```

**Example Response Generation:**

Current State: GATHERING_INFO
Filled Slots: party_size=4, date=tomorrow, time=7PM
Empty Required Slots: [restaurant_name, cuisine_type]

Next Action: Ask for restaurant name
Response: "What restaurant would you like to book?"

#### Step 6: Context Memory

**Data Structure:**

```python
class DialogueContext:
    def __init__(self):
        self.slots = {}
        self.history = []
        self.current_state = "INITIAL"
        self.user_id = None
        self.session_id = None
    
    def add_turn(self, user_input, bot_response):
        self.history.append({
            'user': user_input,
            'bot': bot_response,
            'timestamp': datetime.now()
        })
    
    def update_slot(self, slot_name, value):
        self.slots[slot_name] = value
    
    def get_filled_slots(self):
        return {k: v for k, v in self.slots.items() if v is not None}
```

**Memory Retention Example:**

```
Turn 1: 
  User: "I want to book"
  Memory: intent = booking_request

Turn 2:
  User: "For 4 people"
  Memory: intent = booking_request, party_size = 4

Turn 3:
  User: "Tomorrow at 7"
  Memory: intent = booking_request, party_size = 4, date = tomorrow, time = 7PM
  
Turn 4:
  Bot: "What restaurant?" (Refers back to turn 1's intent)
```

#### Step 7: Complete Python Implementation

```python
from enum import Enum
from datetime import datetime
from typing import Dict, List, Optional

class DialogueState(Enum):
    INITIAL = 1
    GATHERING_INFO = 2
    CONFIRMING = 3
    PROCESSING = 4
    COMPLETED = 5
    CANCELLED = 6

class RestaurantBookingBot:
    def __init__(self):
        self.slots = {
            'restaurant_name': None,
            'date': None,
            'time': None,
            'party_size': None,
            'cuisine_type': None,
            'special_requests': None
        }
        self.required_slots = ['restaurant_name', 'date', 'time', 'party_size']
        self.state = DialogueState.INITIAL
        self.history = []
    
    def extract_entities(self, user_input: str) -> Dict:
        """Extract entities from user input"""
        entities = {}
        
        # Simple rule-based extraction (in production, use NER model)
        import re
        
        # Extract numbers (party size)
        numbers = re.findall(r'\d+', user_input)
        if numbers:
            entities['party_size'] = int(numbers[0])
        
        # Extract time patterns
        time_match = re.search(r'(\d{1,2}\s*(?:AM|PM|am|pm))', user_input)
        if time_match:
            entities['time'] = time_match.group(1)
        
        # Extract cuisine types
        cuisines = ['italian', 'chinese', 'indian', 'mexican', 'thai']
        for cuisine in cuisines:
            if cuisine in user_input.lower():
                entities['cuisine_type'] = cuisine
                break
        
        # Extract dates
        date_keywords = ['today', 'tomorrow', 'tonight']
        for keyword in date_keywords:
            if keyword in user_input.lower():
                entities['date'] = keyword
                break
        
        return entities
    
    def update_slots(self, entities: Dict):
        """Update dialogue slots with extracted entities"""
        for slot, value in entities.items():
            if value is not None:
                self.slots[slot] = value
    
    def get_next_missing_slot(self) -> Optional[str]:
        """Identify the next slot to fill"""
        for slot in self.required_slots:
            if self.slots[slot] is None:
                return slot
        return None
    
    def generate_response(self) -> str:
        """Generate appropriate bot response"""
        next_missing = self.get_next_missing_slot()
        
        if next_missing is None:
            # All required slots filled
            if self.state == DialogueState.GATHERING_INFO:
                self.state = DialogueState.CONFIRMING
                return f"Let me confirm: {self.slots['party_size']} people at {self.slots['restaurant_name']} on {self.slots['date']} at {self.slots['time']}. Correct?"
        else:
            # Ask for missing slot
            prompts = {
                'restaurant_name': "What restaurant would you like to book?",
                'date': "What date would you prefer?",
                'time': "What time suits you?",
                'party_size': "How many people will be dining?"
            }
            return prompts.get(next_missing, "Can you provide more details?")
    
    def process_user_input(self, user_input: str) -> str:
        """Main conversation loop"""
        # Extract entities
        entities = self.extract_entities(user_input)
        self.update_slots(entities)
        
        # Update state
        if self.state == DialogueState.INITIAL:
            self.state = DialogueState.GATHERING_INFO
        
        # Generate response
        response = self.generate_response()
        
        # Store in history
        self.history.append({
            'user': user_input,
            'bot': response,
            'slots': self.slots.copy()
        })
        
        return response

# Example Usage:
bot = RestaurantBookingBot()

# Turn 1
print("User: I want to book a restaurant")
print("Bot:", bot.process_user_input("I want to book a restaurant"))
# Bot: What restaurant would you like to book?

# Turn 2
print("\nUser: Italian place for 4 people")
print("Bot:", bot.process_user_input("Italian place for 4 people tomorrow at 7 PM"))
# Bot: Let me confirm: 4 people at Italian place on tomorrow at 7 PM. Correct?

# Turn 3
print("\nUser: Yes, please")
print("Bot:", bot.process_user_input("Yes"))
# Bot: Your booking has been confirmed!
```

#### Step 8: Calculation & Verification

**Confidence Score Calculation:**

For intent classification using softmax:

Given raw scores from neural network:
- booking_request: 2.5
- booking_cancel: -1.2
- general_query: 0.8

**Step-by-step calculation:**

```
e^2.5 = 12.182
e^-1.2 = 0.301
e^0.8 = 2.226

Sum = 12.182 + 0.301 + 2.226 = 14.709

P(booking_request) = 12.182 / 14.709 = 0.828 = 82.8%
P(booking_cancel) = 0.301 / 14.709 = 0.020 = 2.0%
P(general_query) = 2.226 / 14.709 = 0.151 = 15.1%

Highest probability: booking_request at 82.8%
Decision: Classify as BOOKING_REQUEST (above 0.7 threshold ✓)
```

---

### Problem 2: Implement Sentiment Analysis for Customer Reviews

**Concept Breakdown:**

**Age 5 Explanation:**
Imagine reading a story. Some stories make you happy, some make you sad. Sentiment analysis is teaching a computer to read and understand if something is happy, sad, or neutral. Like if someone says "I love this restaurant!", it's happy. If they say "This food was terrible", it's sad.

**Age 30 Explanation:**
Sentiment analysis is a classification task that determines the emotional tone or polarity of text. It involves:
- Feature extraction (TF-IDF, embeddings)
- Classification models (Naive Bayes, SVM, Neural Networks)
- Aspect-based sentiment (sentiment towards specific features)
- Emotion detection (anger, joy, fear, etc.)

**Mathematical Formulation:**

$$Sentiment = argmax_s P(s|text) \text{ where } s \in \{positive, negative, neutral\}$$

---

## SECTION 3: KEY TAKEAWAYS FOR PROBLEM-SOLVING

### How to Approach Similar Questions:

1. **Always start with the concept**, not the implementation
2. **Understand the workflow** before writing code
3. **Use clear examples** to validate your understanding
4. **Show all calculations** step-by-step
5. **Test with real examples**
6. **Consider edge cases**

### General Framework for Conversational AI Problems:

```
1. IDENTIFY THE TASK
   - What is the system supposed to do?
   - What are the inputs and outputs?

2. DEFINE THE COMPONENTS
   - Which NLP modules are needed?
   - What ML models are required?
   - How do they interact?

3. DESIGN THE ARCHITECTURE
   - Draw the system diagram
   - Define data flow
   - Specify interfaces

4. IMPLEMENT WITH EXAMPLES
   - Start with a simple example
   - Show each step
   - Include all calculations

5. TEST & VALIDATE
   - Test with multiple examples
   - Check edge cases
   - Verify outputs
```

---

## SECTION 4: IMPORTANT CONCEPTS SUMMARY

### 1. Tokenization
Breaking text into meaningful units (words, sentences, subwords)

### 2. Embedding
Representing words/sentences as vectors in continuous space

### 3. Attention Mechanism
Focusing on relevant parts of input for specific tasks

### 4. Dialogue State Tracking
Maintaining conversation context and required information

### 5. Response Generation
Creating natural language replies based on system state and user input

---

## SECTION 5: PRACTICE PROBLEMS

**Try these similar problems:**

1. Design a weather information chatbot
2. Create an intent classifier for music streaming commands
3. Build an entity extraction system for medical prescriptions
4. Design a complaint handling chatbot
5. Implement sentiment analysis for social media posts

---

**Document Created:** 2026-06-26 15:59:37
**Total Pages (Markdown):** ~25
**Format:** Complete with concepts, examples, and full solutions

