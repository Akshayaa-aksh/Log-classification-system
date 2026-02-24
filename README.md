# AI Log Classification & Incident Analysis System

## Overview

This project implements an AI-driven log monitoring pipeline that processes raw logs, classifies them, detects repetition patterns, and generates structured incident reports using a local Large Language Model (LLM) via Ollama.

The system converts unstructured logs into actionable intelligence by performing classification, aggregation, spike detection, and AI-based incident summarization.

---

##  System Architecture

Raw Logs  
→ Log Classifier  
→ Log Aggregator  
→ Incident Agent (LLM via Ollama)  
→ Structured Incident Report (JSON)

---

## Features

- Automatic log level detection (info / warn / error / critical)
- Log categorization (database, network, authentication, performance, unknown)
- Severity scoring (1–5)
- Short log summary generation
- Frequency-based grouping of repeated logs
- Spike detection for repeated errors
- AI-generated incident summary using Ollama (llama3)
- Structured JSON output for integration with monitoring systems

## Technologies Used

Python
Ollama (Local LLM)
llama3 model
requests library
Regular Expressions

🖥️ Setup Instructions

1️⃣ Install Ollama
2️⃣ Pull Model :
ollama pull llama3
3️⃣ Start Ollama Server
ollama serve
4️⃣ Install Python Dependencies
pip install requests
5️⃣ Run the Project
python main.py

