# ResearchMind

A full-stack hybrid research assistant. Give it any topic. Agents search and scrape the web,
a **locally trained TextCNN** filters unreliable sources, then a writer and critic produce
a cited report.

This is not only API wrapping. DeepSeek/Tavily collect and write text. The original module is
the **TextCNN source-quality classifier** trained in this repo (`backend/cnn/`).

The app is split into:

- **React frontend** (`frontend/`) — topic input, live pipeline status, report view, history
- **FastAPI backend** (`backend/`) — REST API + SQLite saved reports
- **LangChain agents** — Search, Reader, Writer, Critic
- **TextCNN** — local PyTorch model that scores sources as reliable or unreliable

## Overview

ResearchMind runs a five-stage pipeline:

1. **Search Agent** — queries the web via Tavily.
2. **Reader Agent** — scrapes the most relevant page.
3. **TextCNN filter (original work)** — a trained convolutional network scores search/scrape text as reliable vs unreliable. The writer only trusts CNN-accepted text.
4. **Writer Chain** — drafts Introduction, Key Findings, Conclusion, Sources.
5. **Critic Chain** — scores the report and lists improvements.

## Architecture

```
multi-ai-agent-research-assistant/
├── backend/
│   ├── main.py        FastAPI REST API
│   ├── pipeline.py    Five-stage runner (includes CNN)
│   ├── agents.py      Search, reader, writer, critic
│   ├── tools.py       web_search (Tavily) and scrape_url
│   ├── database.py    SQLite report history
│   └── cnn/           TextCNN model, train script, checkpoint
├── frontend/          React + Vite UI
├── pipeline.py        CLI launcher for backend/pipeline.py
├── app.py             Optional Streamlit UI (backup)
└── requirements.txt
```

```
Topic
  │
  ▼
React UI ──POST /api/research──► FastAPI
  │                                │
  │                                ▼
  │                         Search Agent ──(Tavily)──► search results
  │                                │
  │                                ▼
  │                         Reader Agent ──(scrape)──► scraped content
  │                                │
  │                                ▼
  │                         TextCNN ──(local model)──► reliable / unreliable
  │                                │
  │                                ▼
  │                         Writer Chain ──► structured report
  │                                │
  │                                ▼
  │                         Critic Chain ──► score + feedback
  │                                │
  │                                ▼
  │                             SQLite
  ▼
Report + history  ◄──GET /api/reports── FastAPI
```

## Tech Stack

- **Frontend**: React, Vite
- **Backend**: FastAPI, Uvicorn
- **Database**: SQLite
- **Language model**: DeepSeek `deepseek-chat`
- **Orchestration**: LangChain, LangGraph
- **Web search**: Tavily
- **Scraping**: requests, BeautifulSoup4
- **Source filter**: PyTorch TextCNN (trained locally)

## API

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/api/health` | Health check |
| `POST` | `/api/research` | Run the pipeline and save the report |
| `GET` | `/api/reports` | List saved reports |
| `GET` | `/api/reports/{id}` | Load one saved report |

`POST /api/research` body:

```json
{ "topic": "Fusion energy progress" }
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- A DeepSeek API key
- A Tavily API key

### Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root (or in `backend/`):

   ```bash
   cp .env.example .env
   ```

   Then put your real keys in `.env`:

   ```
   DEEPSEEK_API_KEY=your-deepseek-key
   TAVILY_API_KEY=your-tavily-key
   ```

4. Train the local TextCNN (required once):

   ```bash
   cd backend
   python -m cnn.train
   cd ..
   ```

5. Install frontend dependencies:

   ```bash
   cd frontend
   npm install
   ```

## Usage

### Full-stack app (recommended)

Terminal 1 — backend (keep the virtualenv activated):

```bash
source .venv/bin/activate
cd backend
uvicorn main:app --reload --port 8000
```

Terminal 2 — frontend:

```bash
cd frontend
npm run dev
```

Open [http://localhost:5173](http://localhost:5173). Enter a topic, run the pipeline, and download the report as Markdown. Past reports are saved in SQLite and listed in the UI.

### Command line

```bash
cd backend
python pipeline.py
```

### Streamlit (optional backup UI)

```bash
streamlit run app.py
```

## Configuration

| Variable | Description |
| --- | --- |
| `DEEPSEEK_API_KEY` | API key for the DeepSeek chat model |
| `DEEPSEEK_MODEL` | Optional. Model name (default: `deepseek-chat`) |
| `DEEPSEEK_BASE_URL` | Optional. API base URL (default: `https://api.deepseek.com`) |
| `TAVILY_API_KEY` | API key for Tavily web search |
| `VITE_API_URL` | Optional. Frontend API base URL. Leave unset in local dev to use the Vite proxy (`/api` → port 8000). |

## License

This project is provided for portfolio and educational purposes.
