# AgentWeaver – Vertical AI Agent Framework

**AgentWeaver** is a modular multi-agent framework tailored for domain-specific AI automation. It supports orchestrating autonomous LLM-driven agents across industry verticals such as Healthcare, Legal, and Finance.

## 🚀 Features
- 🤖 Multi-agent system with roles: Planner, Retriever, Executor, Evaluator
- 🧠 Integration with LLMs (OpenAI, Claude, HuggingFace)
- 🔌 Plug-and-play support for domain tools and APIs
- 📊 Streamlit-based observability dashboard
- 🗃️ Vector database integration (Chroma, Weaviate)

## 🏗️ Project Structure
```
agentweaver-vertical-ai/
├── agents/                  # Core autonomous agent modules
├── verticals/               # Domain-specific logic (healthcare, legal, finance)
├── tools/                   # Generic tools for agents (search, APIs)
├── vector_store/            # Embedding + vector DB integration
├── orchestration/           # Messaging and agent communication layer
├── dashboard/               # Streamlit interface for real-time agent monitoring
├── tests/                   # Unit/integration tests
├── requirements.txt         # Python dependencies
└── .env.example             # Environment variables template
```

## 📦 Installation
```bash
git clone https://github.com/yourusername/agentweaver-vertical-ai.git
cd agentweaver-vertical-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## ⚙️ Configuration
Create a `.env` file based on the `.env.example`:
```
OPENAI_API_KEY=your_key
VECTOR_DB_PATH=./vector_store/index
```

## 🧪 Running the Dashboard
```bash
streamlit run dashboard/streamlit_app.py
```

## 📚 Example Use Case: Healthcare EHR Assistant
- Planner Agent receives a goal: "Summarize and flag unusual patient risks"
- Retriever queries vector DB for relevant context
- Executor processes EHR file with LLM
- Evaluator ensures findings meet quality thresholds

## 📌 Roadmap
- [ ] Agent memory and state persistence
- [ ] Fine-tuned vertical models
- [ ] Agent routing and skill tagging
- [ ] Docker & deployment templates

## 🤝 Contributing
PRs are welcome! Please include tests and follow PEP8.

## 📄 License
MIT License © 2025 AgentWeaver Contributors
