# Jailbreak Arena

**Jailbreak Arena** is a GenAI challenge game built with **Streamlit** and **LangChain**. It simulates prompt injection scenarios where players attempt to bypass AI constraints and extract hidden information. The goal is to explore how well language models can follow rules, and how easily they can be tricked.

This project is designed as a learning tool for experimenting with prompt design, retrieval-based context, agent behavior, and custom AI tools.

---

- **LangChain agents** to manage AI behavior and tool usage
- **Prompt engineering** to define strict behavioral constraints for the AI
- **RAG (Retrieval-Augmented Generation)** to embed clues and context in documents
- **Custom tools** for tasks like search and decoding
- **Arena Agent** the main agent that runs the game loop and interacts with the user throughout each challenge.
- **Evaluator Agent** that checks whether a jailbreak attempt was successful

---

## How to Run Locally

1. Clone the repository:
git clone https://github.com/ReemaIsrani/jailbreak-arena.git
cd jailbreak-arena

2. Set up a virtual environment:
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. Setup environment variables:
Create a .env file with GROQ_API_KEY, HF_TOKEN, LANGSMITH env variables

4. Install dependencies:
pip install -r requirements.txt

6. Start the app:
streamlit run app.py
