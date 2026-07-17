# ResearchMind

A multi-agent AI research assistant. Give it any topic and four specialized agents
collaborate — searching the web, scraping the best sources, writing a structured
report, and critiquing the result — to produce a polished, cited research report.

## Overview

ResearchMind runs a fixed four-stage pipeline. Each stage hands its output to the next:

1. **Search Agent** — queries the web via Tavily for recent, reliable information on the topic.
2. **Reader Agent** — picks the most relevant URL from the search results and scrapes it for deeper content.
3. **Writer Chain** — combines the gathered research into a structured report (Introduction, Key Findings, Conclusion, Sources).
4. **Critic Chain** — reviews and scores the report, listing strengths and areas to improve.

The system runs on OpenAI's `gpt-4o-mini`, orchestrated with LangChain and LangGraph.
Stages 1 and 2 are tool-using agents; stages 3 and 4 are prompt chains.

## Architecture

```
multi-ai-agent-research-assistant/
├── app.py            Streamlit web UI (ResearchMind front end)
├── pipeline.py       Command-line pipeline runner
├── agents.py         Agent and chain definitions (search, reader, writer, critic)
├── tools.py          Agent tools: web_search (Tavily) and scrape_url (BeautifulSoup)
└── requirements.txt  Python dependencies
```

- **agents.py** builds the two tool-using agents (`build_search_agent`, `build_reader_agent`)
  and the two prompt chains (`writer_chain`, `critic_chain`).
- **tools.py** exposes the tools the agents call: `web_search` (Tavily API) and
  `scrape_url` (requests + BeautifulSoup, cleaned and truncated to 3000 characters).
- **pipeline.py** wires the four stages together for terminal use.
- **app.py** provides a styled Streamlit interface with live per-stage status,
  raw output panels, the final report, and a Markdown download.

## Tech Stack

- **Language model**: OpenAI `gpt-4o-mini`
- **Orchestration**: LangChain, LangGraph
- **Web search**: Tavily
- **Scraping**: requests, BeautifulSoup4
- **UI**: Streamlit
- **Config**: python-dotenv

## Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI API key
- A Tavily API key

### Setup

1. Clone the repository and enter the project directory:

   ```bash
   git clone https://github.com/sujit-al1809/multi-ai-agent-research-assistant.git
   cd multi-ai-agent-research-assistant
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API keys:

   ```
   OPENAI_API_KEY=your-openai-key
   TAVILY_API_KEY=your-tavily-key
   ```

## Usage

### Web app

Launch the Streamlit interface:

```bash
streamlit run app.py
```

Enter a topic, run the pipeline, and watch each stage complete. The final report can
be downloaded as a Markdown file.

### Command line

Run the pipeline directly in the terminal:

```bash
python pipeline.py
```

You will be prompted for a research topic, and each stage's output is printed as it runs.

## How It Works

```
Topic
  │
  ▼
Search Agent ──(web_search / Tavily)──► search results
  │
  ▼
Reader Agent ──(scrape_url / BeautifulSoup)──► scraped content
  │
  ▼
Writer Chain ──► structured research report
  │
  ▼
Critic Chain ──► score + strengths + areas to improve
```

## Configuration

| Variable | Description |
| --- | --- |
| `OPENAI_API_KEY` | API key for the OpenAI chat model |
| `TAVILY_API_KEY` | API key for Tavily web search |

Both are loaded from a `.env` file via python-dotenv and are required.

## License

This project is provided for portfolio and educational purposes.
