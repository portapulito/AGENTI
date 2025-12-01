# LangGraph UI from LLM

A simple, educational example of "Generative UI" using Python and LangGraph.
This project demonstrates how to use an LLM to generate complete HTML pages based on user prompts, orchestrated by a simple graph.

## Description

This tool takes a user description (e.g., "A dashboard for my personal tasks") and generates a single-file HTML page with internal CSS. It uses:
- **LangGraph**: To orchestrate the flow (User Input -> Generate -> Post-process -> Save).
- **LangChain**: To interact with the LLM (OpenAI/Anthropic/etc.).
- **Python**: For the core logic and CLI runner.

## Prerequisites

- Python 3.11+
- An OpenAI API Key (or compatible)

## Installation

1. Clone the repository (if not already done).
2. Navigate to the project directory:
   ```bash
   cd langgraph-ui-from-llm
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the `langgraph-ui-from-llm` directory with your API key:

```env
OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o  # Optional, defaults to gpt-4o
```

## Usage

### CLI Mode

Run the CLI script:

```bash
python -m src.runner
```

Follow the prompts:
1. Enter a description of the UI you want to generate.
2. Wait for the generation to complete.
3. Open the generated file (path will be printed) in your browser.

### Web Server Mode

1. Start the server:
   ```bash
   uvicorn src.server:app --reload
   ```
2. Open your browser to:
   [http://localhost:8000](http://localhost:8000)
3. Enter a description in the sidebar and click "Generate UI".
4. The generated page will appear in the main view.

## Project Structure

- `src/`: Source code
  - `server.py`: FastAPI server
  - `graph.py`: LangGraph logic
  - `prompts.py`: System instructions
  - `llm_client.py`: LLM wrapper
- `static/`: Frontend files
- `outputs/`: Generated HTML files (CLI mode only)

## Notes

- The project uses **LangGraph** to manage the generation state.
- It is designed to be educational and easily extendable.
- The frontend is pure HTML/JS (no build step required).
