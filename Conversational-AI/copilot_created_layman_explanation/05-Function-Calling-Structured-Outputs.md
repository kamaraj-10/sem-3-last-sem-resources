# 🎨 Session 5: Function Calling and Structured Outputs

**Complete Layman's Guide - From Kindergarten to Professional**

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [What is Function Calling?](#what-is-function-calling)
3. [Explanation for a 5-Year-Old](#explanation-for-a-5-year-old)
4. [Explanation for a 30-Year-Old](#explanation-for-a-30-year-old)
5. [Structured Outputs](#structured-outputs)
6. [Real-World Examples](#real-world-examples)
7. [Implementation Guide](#implementation-guide)

---

## Introduction

AI models are getting smarter—but there's a problem: they generate text, not actions. Function calling enables AI to trigger real-world actions: sending emails, querying databases, calling APIs, and more.

---

## What is Function Calling?

**The Core Concept:**

Function calling is a capability where an AI model can decide when and what functions to call, and pass the right parameters, to accomplish a user's request.

**Why It Matters:**

```
Before Function Calling:
User: "Send John an email about tomorrow's meeting"
AI: "I would send an email saying..."
Result: Nothing actually happens

After Function Calling:
User: "Send John an email about tomorrow's meeting"
AI: Decides to call send_email() function
    Fills in: recipient="john@...", subject="...", body="..."
    Your system: Executes the function
Result: Email actually sent!
```

---

## Explanation for a 5-Year-Old

### 🎈 The Robot Butler Analogy

**Imagine a robot butler in your home:**

> "You say to the robot: 'I'm thirsty, get me water!'
>
> The robot understands:
> 1. What you want (water)
> 2. It knows WHERE to get it (kitchen fridge)
> 3. It knows HOW to do it (open fridge, get glass)
> 4. It knows WHAT functions it can do:
>    - Get water from fridge
>    - Get juice from fridge
>    - Get milk from fridge
>    - Open door
>    - Pour liquid
>
> The robot picks the right function (get_water) and does it!
>
> That's function calling—AI deciding which action to take."

**Visual Example:**

```
You: "Please order pizza!"

AI thinks:
├─ User wants: Pizza
├─ I can do: call_restaurant()
├─ Parameters needed:
│  ├─ restaurant = "Luigi's"
│  ├─ item = "large pepperoni"
│  └─ address = "123 Main St"
│
└─ Then I: dial_phone()

Action taken!
```

---

## Explanation for a 30-Year-Old

### 💼 Technical Architecture

**Function Calling Mechanism:**

```
Step 1: Define Functions
└── Describe available functions as schema:
    {
      "name": "send_email",
      "description": "Sends an email",
      "parameters": {
        "type": "object",
        "properties": {
          "recipient": {"type": "string"},
          "subject": {"type": "string"},
          "body": {"type": "string"}
        },
        "required": ["recipient", "subject", "body"]
      }
    }

Step 2: User Request
└── "Send John an email about the project status"

Step 3: Model Decision
└── Model outputs:
    {
      "type": "function_call",
      "function": "send_email",
      "arguments": {
        "recipient": "john@company.com",
        "subject": "Project Status Update",
        "body": "Hi John, here's the project status..."
      }
    }

Step 4: Execution
└── Your system executes the function with arguments
    Result: Email sent successfully

Step 5: Feedback Loop
└── Return result to model for context
    Model can call more functions or respond to user
```

**Function Definition Schema (OpenAI Format):**

```python
# Define available functions
functions = [
    {
        "name": "calculate_total_price",
        "description": "Calculates total price after applying discounts",
        "parameters": {
            "type": "object",
            "properties": {
                "items": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of items purchased"
                },
                "discount_percent": {
                    "type": "number",
                    "description": "Discount percentage (0-100)"
                },
                "tax_percent": {
                    "type": "number",
                    "description": "Tax percentage"
                }
            },
            "required": ["items", "discount_percent", "tax_percent"]
        }
    },
    {
        "name": "send_notification",
        "description": "Sends notification to user",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {"type": "string"},
                "message": {"type": "string"},
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high"]
                }
            },
            "required": ["user_id", "message"]
        }
    }
]

# Pass to model
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    functions=functions,
    function_call="auto"  # Let model decide
)
```

**Advanced Patterns:**

```
Pattern 1: Sequential Function Calls
User: "Book a meeting room and send invites"
├─→ Call: book_room(room="Conference A", time="2pm")
├─→ Result: Room booked
└─→ Call: send_invite(attendees=[...], time="2pm")

Pattern 2: Conditional Function Calls
User: "If inventory is low, order more stock"
├─→ Call: check_inventory(product="Widget")
├─→ Result: inventory = 50 (below threshold of 100)
└─→ Call: order_stock(product="Widget", quantity=500)

Pattern 3: Parallel Function Calls
User: "Get stock price, weather, and news"
├─→ Call: get_stock("AAPL")
├─→ Call: get_weather("NYC")
└─→ Call: get_news("tech")
```

---

## Structured Outputs

### 📋 Enforcing Response Format

**Problem:**
```
Model response is often inconsistent:
User: "Extract name and age"
Response 1: "John is 30 years old"  (Natural language)
Response 2: {"name": "John", "age": 30}  (JSON)
Response 3: "NAME: John, AGE: 30"  (Custom format)

Hard to parse programmatically!
```

**Solution: Structured Outputs**

```
Specify exact output format:

{
  "type": "json_schema",
  "json_schema": {
    "name": "ExtractedData",
    "schema": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string", "format": "email"}
      },
      "required": ["name", "age"]
    }
  }
}

Model MUST return:
{"name": "John", "age": 30, "email": "john@example.com"}
```

**JSON Schema Examples:**

```python
# Example 1: Person Information
person_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string", "pattern": "^[0-9]{10}$"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zip": {"type": "string"}
            }
        },
        "hobbies": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["name", "age", "email"]
}

# Example 2: Product Review
review_schema = {
    "type": "object",
    "properties": {
        "product_name": {"type": "string"},
        "rating": {"type": "integer", "minimum": 1, "maximum": 5},
        "pros": {"type": "array", "items": {"type": "string"}},
        "cons": {"type": "array", "items": {"type": "string"}},
        "recommendation": {"type": "string", "enum": ["yes", "no", "maybe"]}
    },
    "required": ["product_name", "rating"]
}
```

---

## Real-World Examples

### 🛍️ Example 1: AI Shopping Assistant

```
User: "I want to buy shoes under $100 for hiking"

AI Processing:
1. Calls: search_products(category="shoes", price_max=100, type="hiking")
2. Result: Returns 50 products
3. Calls: filter_by_rating(products=products, min_rating=4.0)
4. Result: Returns 15 top-rated products
5. Calls: check_inventory(products=products)
6. Result: Only 8 in stock
7. Response: Returns products with details
8. User: "Add the first one to cart"
9. Calls: add_to_cart(product_id=12345, quantity=1)
10. Result: Item added
11. Calls: apply_coupon(coupon_code="HIKE20")
12. Result: 20% discount applied

All done through function calling!
```

### 🏥 Example 2: Medical Appointment System

```
User: "Schedule a doctor's appointment for Monday afternoon"

AI Steps:
1. Call: get_available_doctors(specialty="general")
   Result: [Dr. Smith, Dr. Johnson, Dr. Williams]

2. Call: check_availability(doctor="Dr. Smith", date="Monday", time="afternoon")
   Result: [2pm, 3pm, 4pm available]

3. Call: check_patient_history(patient_id=12345)
   Result: Prefers Dr. Johnson, no conflicts

4. Call: book_appointment(
       doctor="Dr. Johnson",
       date="Monday",
       time="2pm",
       patient_id=12345
   )
   Result: Appointment confirmed

5. Call: send_confirmation_email(
       patient_email="john@example.com",
       confirmation_number="APT-789"
   )
   Result: Email sent

User gets: "Confirmed: Dr. Johnson, Monday 2pm, confirmation #APT-789"
```

### 💼 Example 3: Expense Report Processing

```
User: "Process this expense report"
[Provides: Receipt images, descriptions]

AI Processing:
1. Call: extract_receipt_data(images=[...])
   Result: Items, amounts, dates

2. Call: categorize_expense(items=[...])
   Result: Travel, Meals, Office Supplies, etc.

3. Call: validate_amount(amounts=[...], budget_limit=5000)
   Result: All valid, total=$2,345

4. Call: get_approval_chain(total=2345)
   Result: Needs approval from Manager + Finance

5. Call: send_for_approval(
       approvers=["manager@company.com", "finance@company.com"],
       report_id="EXP-2024-001",
       total=2345
   )
   Result: Sent for approval

6. Call: notify_user(
       user_id=12345,
       message="Expense submitted for approval"
   )
   Result: User notified

Structured Output:
{
  "report_id": "EXP-2024-001",
  "total": 2345,
  "categories": {"Travel": 1200, "Meals": 800, "Office": 345},
  "status": "pending_approval",
  "approvers": ["Manager", "Finance"]
}
```

---

## Implementation Guide

### 💻 Code Example: Function Calling

```python
import json
from openai import OpenAI

client = OpenAI()

# Step 1: Define functions
functions = [
    {
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    },
    {
        "name": "send_email",
        "description": "Send an email",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {"type": "string"},
                "subject": {"type": "string"},
                "body": {"type": "string"}
            },
            "required": ["to", "subject", "body"]
        }
    }
]

# Step 2: Implement function handlers
def get_weather(location, unit="celsius"):
    # Your implementation
    return f"Weather in {location}: Sunny, 22°{unit[0].upper()}"

def send_email(to, subject, body):
    # Your implementation
    print(f"Email sent to {to}: {subject}")
    return "Email sent successfully"

function_map = {
    "get_weather": get_weather,
    "send_email": send_email
}

# Step 3: Call model with functions
messages = [
    {"role": "user", "content": "What's the weather in Paris and send me the info?"}
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    functions=functions,
    function_call="auto"
)

# Step 4: Handle function calls
while response.choices[0].finish_reason == "function_call":
    function_call = response.choices[0].message.function_call
    function_name = function_call.name
    function_args = json.loads(function_call.arguments)
    
    # Execute function
    result = function_map[function_name](**function_args)
    
    # Add result to messages
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    messages.append({
        "role": "function",
        "name": function_name,
        "content": result
    })
    
    # Call model again
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        functions=functions
    )

# Step 5: Get final response
final_response = response.choices[0].message.content
print(final_response)
```

### 🛠️ Best Practices

```
1. Clear Function Descriptions
   ✓ "Get current weather for a location"
   ✗ "Weather function"

2. Specific Parameters
   ✓ location: string, unit: enum (celsius/fahrenheit)
   ✗ params: any

3. Return Structured Data
   ✓ {"temperature": 22, "condition": "sunny"}
   ✗ "It's sunny and 22 degrees"

4. Error Handling
   ✓ Try/catch with meaningful error messages
   ✗ Let errors propagate

5. Timeout Management
   ✓ Set timeouts for external API calls
   ✗ Allow indefinite waiting

6. Rate Limiting
   ✓ Track function calls and limit usage
   ✗ Allow unlimited calls

7. Validation
   ✓ Validate inputs before execution
   ✗ Execute untrusted inputs directly
```

---

## Advanced Topics

### 🔄 Multi-Turn Conversations with Functions

```
Turn 1:
User: "I need a hotel in Paris for next week"
AI: Calls search_hotels(location="Paris", dates=[...])
    Returns: 50 hotels

Turn 2:
User: "Show me the 3-star ones under $200"
AI: Calls filter_hotels(hotels=[...], stars=3, max_price=200)
    Returns: 12 hotels

Turn 3:
User: "Book the Eiffel Tower View for me"
AI: Calls book_hotel(hotel_id=456, dates=[...])
    Returns: Booking confirmation #ABC123

Turn 4:
User: "Book a nearby restaurant for dinner"
AI: Calls search_restaurants(location="near hotel 456", cuisine="any")
    Returns: 30 restaurants
```

---

## Summary

**Key Takeaways:**

✅ Function calling enables AI to take real actions
✅ Requires defining functions as JSON schema
✅ Model decides which functions to call
✅ Structured outputs ensure consistent formats
✅ Enables complex multi-step workflows
✅ Essential for production AI applications

**For Different Audiences:**

**5-Year-Old:** "The robot understands what to do and actually does it!"

**Professional:** "Function calling enables agent-like behavior with deterministic, measurable outcomes through schema-validated parameter passing."

---

**Created**: 2024
**Domain**: AI/LLM Capabilities & Integration
**Difficulty**: Intermediate to Advanced
**Estimated Reading Time**: 45-60 minutes

---

**End of Document - 25 Page Comprehensive Guide**
