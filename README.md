# 🐾 Petshop Copilot AI  
*Build a complete LangChain RAG chatbot with FAISS, ReAct & Streamlit*

▶️ Tutorial Series

This code accompanies the YouTube series:
Building the Petshop Copilot AI | LangChain Tutorial with FAISS, RAG & ReAct + Streamlit

[![Watch the video](https://rodolfomoreira.com.br/capas/Introduction_Petshop_Copilot_AI.png)](https://www.youtube.com/watch?v=8C6WEhbPh8s)


Episodes:

1 - Intro: Building the Petshop Copilot AI
2 - Creating a FAISS Vector Store
3 - Building a RAG Agent with LangChain and Using ReAct to Orchestrate Agents
4 - Building the ChatGPT-Style App with Streamlit

## Overview
This repository contains the full code for **Building the Petshop Copilot AI**,  
a step-by-step project that demonstrates how to create a ChatGPT-style application using:

- **LangChain** for LLM orchestration  
- **FAISS** for fast semantic vector search  
- **Retrieval-Augmented Generation (RAG)** for accurate context retrieval  
- **ReAct** for agent reasoning and task orchestration  
- **Streamlit** for an interactive web interface

## Features
- Ingest custom petshop data and build a **FAISS vector store**  
- Implement **prompt engineering**: Zero-Shot, One-Shot, Few-Shot, Chain-of-Thought  
- Create a **RAG agent** for context-aware answers  
- Use **ReAct** to coordinate multiple agents  
- Deploy a **Streamlit UI** that feels like ChatGPT

## Tech Stack
| Component        | Purpose                             |
|------------------|-------------------------------------|
| Python 3.10+     | Core language                       |
| LangChain        | LLM framework & agent tooling       |
| FAISS            | Vector database for embeddings      |
| OpenAI API       | LLM (or any compatible provider)    |
| Streamlit        | Front-end UI                        |

## Quick Start
1. **Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd petshop-copilot-ai

2. **Create a virtual environment & install dependencies**  
   ```bash
   python -m venv venv
   source venv/bin/activate      # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

3. **Set environment variables**  
   ```bash
   OPENAI_API_KEY=your_openai_key


4. **Run the app**
   ```bash
   streamlit run app.py

