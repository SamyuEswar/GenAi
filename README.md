#  GENAI Essentials Exercises

This repository contains a series of beginner-friendly exercises to understand how Generative AI applications are built using:

* Groq API
* OpenAI-compatible APIs
* LangChain
* LangGraph
* Langfuse (Tracing & Monitoring)

##  Exercises Overview

### 🔹 Exercise 1: Basic LLM Call

* Uses Groq API with OpenAI-compatible client
* Sends a simple prompt to the model
* Displays response

### 🔹 Exercise 2: LangChain Agent with Tool

* Creates a simple AI agent
* Uses a custom tool (`get_word_length`)
* Agent decides when to use tool

### 🔹 Exercise 3: LangGraph Basic Chatbot

* Builds chatbot using LangGraph
* Uses state-based message flow

### 🔹 Exercise 4: LangGraph with Tools

* Integrates tools inside LangGraph
* Agent can:

  * Call tools (weather, sum)
  * Return responses dynamically

### 🔹 Exercise 5: Langfuse Integration

* Adds tracing & monitoring
* Tracks model calls and responses

## ⚙️ Setup Instructions

### 1️⃣ Install Python Packages
```bash
python -m pip install openai langchain langchain-groq langgraph python-dotenv langfuse
```
### 2️⃣ Create `.env` File
```bash
GROQ_API_KEY=your_api_key_here
GROQ_MODEL_NAME=llama-3.3-70b-versatile

#### Necessary for Exercise 5 alone
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```
### 3️⃣ Run Exercises
```bash
python main.py
```

## Conclusion
These exercises provide a step-by-step approach to understanding:
 📌Basic AI calls → Agents → Graph workflows → Tools → Monitoring

## 🎯 Conclusion

These exercises provide a step-by-step approach to understanding:

* Basic AI calls → Agents → Graph workflows → Tools → Monitoring
