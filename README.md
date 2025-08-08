# Analyser-GPT

Analyser-GPT is an AI-powered data analysis tool built with [Streamlit](https://streamlit.io/) and [AutoGen AgentChat](https://microsoft.github.io/autogen/) that allows you to upload CSV datasets, describe the analysis you want, and receive results with both explanations and visualizations.

The system uses a **multi-agent architecture**:
- **Data Analyser Agent** — Understands the dataset and generates Python code to perform analysis.
- **Code Executor Agent** — Executes the generated code inside a Docker container for security and reproducibility.

---

## 🚀 Features
- **CSV Upload & Analysis**: Upload your dataset and describe your desired analysis in natural language.
- **Multi-Agent Collaboration**: Autonomous coordination between a code-writing agent and a code-execution agent.
- **Docker-Sandboxed Execution**: Ensures code is executed securely in an isolated container.
- **Interactive Streamlit UI**: Chat-style interface for task input and response viewing.
- **Visualization Support**: Automatically displays generated plots.

---

## 📂 Folder Structure

```
ANALYSER-GPT/
│
├── agents/                # Agents and their prompts
│   ├── prompts/
│   │   ├── data_analyser_message.py
│   │   └── __init__.py
│   ├── code_executor_agent.py
│   ├── data_analyser_agent.py
│   └── __init__.py
│
├── config/                # Configuration utilities
│   ├── constants.py
│   ├── docker_util.py
│   └── __init__.py
│
├── models/                # Model client configurations
│   ├── openai_model_client.py
│   └── __init__.py
│
├── teams/                 # Multi-agent orchestration
│   ├── analyser_gpt.py
│   └── __init__.py
│
├── temp/                  # Temporary storage for uploaded files & outputs
├── main.py                # CLI entry point for running analysis
├── streamlit_app.py       # Streamlit web app entry point
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed to git)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Adonpm/analyser-gpt.git
   cd analyser-gpt
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Install and run Docker**
   - Make sure [Docker](https://www.docker.com/) is installed and running.
   - The code executor will run inside a Docker container.

---

## 🖥️ Running the Application

### **Option 1: Run with Streamlit UI**
```bash
streamlit run streamlit_app.py
```
- Upload a CSV file.
- Type your analysis request in the chat input.
- View generated outputs and plots interactively.

### **Option 2: Run via CLI**
```bash
python main.py
```
- Modify `task` inside `main.py` to change the analysis query.
- Outputs will be printed to the console.

---

## 📌 Example Usage
**Task**:  
> "Can you give me a graph of types of flowers in my data Iris.csv?"

**Steps**:
1. Upload `Iris.csv` via the Streamlit app.
2. Enter the above task in the chat input.
3. The **Data Analyser Agent** writes code to plot flower types.
4. The **Code Executor Agent** executes the code inside Docker.
5. The resulting graph appears in the UI.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit** — UI framework
- **AutoGen AgentChat** — Multi-agent orchestration
- **Docker** — Secure code execution
- **OpenAI API** — LLM model backend
- **Pandas / Matplotlib** — Data processing & visualization

---

## 🤝 Contributing
Contributions are welcome!  
You can:
- Improve prompts
- Add new visualization types
- Enhance Docker sandboxing
- Improve UI/UX

Fork, branch, and submit a PR 🚀

---

## 📧 Contact
If you have questions or suggestions, please open an [issue](../../issues) or contact **Adon Mathew** at `adon.pmpm@gmail.com`.
