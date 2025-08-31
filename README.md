# Poem Generator with LangChain and Ollama

This project is a poetry generation application that uses LangChain, FastAPI, and Ollama to create poems based on user-provided topics. It consists of a FastAPI backend server and a Streamlit frontend interface.

## Prerequisites

- Python 3.10 or higher
- Ollama installed on your system (for local LLM)
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheJaiSrivastava/poem-generator.git
cd poem_generator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install langserve langchain-core langchain-ollama fastapi uvicorn streamlit requests
```

## Setting up Ollama

1. Install Ollama by following the instructions at [Ollama's official website](https://ollama.ai/).
2. Pull and run your preferred model (e.g., llama2):
```bash
ollama pull llama2
```

## Running the Application

1. Start the FastAPI backend server:
```bash
# Navigate to the apifolder directory
cd apifolder
uvicorn app:app --reload
```
The API will be available at `http://localhost:8000`

2. In a new terminal, start the Streamlit frontend:
```bash
# Make sure you're in the apifolder directory
streamlit run client.py
```
The web interface will be available at `http://localhost:8501`

## Project Structure

```
.
├── apifolder/
│   ├── app.py          # FastAPI backend server
│   └── client.py       # Streamlit frontend interface
└── README.md
```

## API Endpoints

- `POST /poem/invoke`: Generate a poem based on a given topic
  - Input: JSON object with a "topic" field
  - Output: JSON object containing the generated poem

## Usage

1. Open your web browser and go to `http://localhost:8501`
2. Enter a topic in the text input field
3. The application will generate a poem based on your topic using the Ollama LLM

## Troubleshooting

1. If you get "module not found" errors, ensure all required packages are installed:
```bash
pip install -r req.txt
```

2. If Uvicorn isn't recognized, ensure you've activated your virtual environment

3. If you can't connect to the API, make sure both the FastAPI server and Ollama are running




