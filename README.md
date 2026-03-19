# 🦙 ollama-first

A locally-hosted LLM playground exploring the Llama 3.2 (1B) model through Python orchestration, streaming APIs. A hands-on exploration of running and orchestrating Large Language Models (LLMs) locally. This project serves as a foundational sandbox for integrating local AI into Python applications using the **Ollama** framework.



---

## 🚀 Project Overview

The goal of this project was to move beyond cloud-based APIs (like OpenAI) and establish a private, offline-first AI environment. I transitioned from manual REST API calls to mastering the official **Ollama Python Library**, verifying multiple edge cases and performance scenarios.

### Key Milestones Achieved:
* **Local Setup:** Configured a high-performance environment using the `llama3.2:1b` model for rapid testing.
* **API vs. Library:** Built initial prototypes using raw `requests` and evolved into using the native `ollama-python` library for cleaner, more robust code.
* **Streaming Logic:** Implemented real-time token streaming to create a "live typing" user experience.
* **Advanced Formatting:** Leveraged the `rich` library to create beautiful terminal dashboards, including custom tables for monitoring model memory (`ollama.ps()`).
* **Model Customization:** Experimented with `Modelfiles` via Python to create specialized AI personas.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.14 |
| **Orchestration** | [Ollama](https://ollama.com/) |
| **Primary Model** | `llama3.2:1b` |
| **Libraries** | `ollama`, `rich`, `requests` |

---

## 🧪 Scenarios Verified

1.  **JSON Serialization Fixes:** Resolved `TypeError: Object of type datetime is not JSON serializable` by correctly handling `model_dump(mode='json')`.
2.  **Streaming Generators:** Successfully captured and formatted data chunks from a streaming response.
3.  **Environment Isolation:** Managed dependencies within a Python Virtual Environment (`venv`).


---

## 📂 Project Structure

```text
ollama-first/
├── .venv/               # Virtual environment
├── start_ollama.py      # Main entry point for chat logic
├── new_model_ollama.py  # Script for creating custom models
├── requirements.txt     # Project dependencies
└── README.md            # You are here!
