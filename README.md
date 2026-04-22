#  AutoStream AI Agent - Social-to-Lead Workflow

## Overview

This project is a Conversational AI Agent built for a fictional SaaS product **AutoStream**, an AI-powered video editing platform for content creators.

The agent is designed to:

* Understand user intent
* Answer product-related queries using RAG
* Identify high-intent users
* Capture leads through a structured workflow


## Features

* Intent Detection (Greeting, Pricing/Policies, High Intent)
* RAG-based Knowledge Retrieval using local JSON
* Multi-turn Conversation Handling (State Management)
* Lead Capture Workflow (Name, Email, Platform)
* Tool Execution (mock API)
* Gemini LLM Integration for natural responses
* Lead Storage (captured leads saved locally in CSV)


## Tech Stack

* Python 3.9+
* Gemini API (`google-genai`)
* dotenv
* JSON (local knowledge base)


## Project Structure

```
project/
│── main.py
│── utils.py
│── knowledge_base.json
│── requirements.txt
│── .env
│── leads.csv (generated after successful lead capture)
```


## How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/maitriishahh/Social-to-Lead-Agentic-Workflow
cd AutoStream-AI-Agent
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file:

```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the agent

```
python main.py
```

## Demo Video
[Watch Demo Video](https://github.com/user-attachments/assets/18b4ad31-21da-4c2b-99b0-74acef13fe67)

The demo showcases:

* Pricing query handled via RAG
* High-intent detection
* Step-by-step lead collection
* Successful lead capture using mock tool

## Example Interaction

User → Pricing query  
Bot → Returns plan details (RAG)

User → Shows intent to buy  
Bot → Starts lead collection (name → email → platform)

Bot → Captures lead successfully


## Architecture Explanation

The design used in this project is modular in nature and involves modules like intent detection, a RAG pipeline and state-driven conversations.

Instead of implementing LangGraph or AutoGen, a state management module is developed using the python dictionary class. The state maintains memory between multiple conversations and stores variables like user intent, user lead details including name, email address, platform and the conversation stage. It gives precise control over the conversation flow and ensures that the state is remembered through multiple conversations.

A local JSON file containing AutoStream prices and policies serves as the knowledge base in the RAG pipeline. Upon receiving any user query, the relevant information is extracted and provided to the Gemini Language Model (LLM).

A rule-based intent detection system is designed in the agent. Priority is given to users who exhibit high intent during the conversations. Upon detecting high intent, the system enters the lead gathering phase and calls for a mock tool upon collecting all the required data from the users.

## WhatsApp Integration using Webhooks

To integrate this agent with WhatsApp, a webhook-based architecture can be used.

When a user sends a message on WhatsApp, the WhatsApp Business API (such as Meta Cloud API or Twilio) forwards the message to a backend server via a webhook (HTTP POST request).

The backend server processes the incoming message and passes it to the AI agent. The agent performs intent detection, retrieves relevant information using RAG or collects user details if the intent is high.

Once the response is generated, the backend sends it back to the WhatsApp API, which delivers the message to the user.

This enables real-time, scalable communication and allows the agent to function as a conversational lead-generation system on WhatsApp.


## Conclusion

This project demonstrates a real-world conversational AI workflow combining intent detection, RAG, state management and tool execution to convert user interactions into actionable business leads.
