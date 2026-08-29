# Project Synopsis

## Title
ResearchMind: A Hybrid Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering

## 1. Introduction
ResearchMind is a proposed AI-based research assistant intended to automate topic exploration, web reading, source filtering, report writing, and evaluation. The system is planned to combine multiple specialized agents with a TextCNN model to improve source trustworthiness before report generation.

## 2. Need for the Project
Most AI research assistants depend mainly on external APIs for search and text generation. While these systems are useful, they often lack a local intelligence component that can verify whether scraped web content is reliable enough to be used in a final report. As a result, low-quality pages, clickbait, or noisy web content may affect the quality of generated outputs.

## 3. Problem Definition
There is a need for an automated research assistant that:

- performs web-based topic research,
- extracts useful textual content,
- filters unreliable information,
- produces structured reports,
- and reviews the quality of the final result.

## 4. Proposed Solution
The proposed solution is a five-stage pipeline:

- Search Agent
- Reader Agent
- TextCNN Source Filter
- Writer Agent
- Critic Agent

The Search and Reader Agents will gather and extract data. The TextCNN will classify the text as reliable or unreliable. The Writer Agent will use approved content to produce a report, and the Critic Agent will evaluate it.

## 5. Objectives
- Design a full-stack research assistant.
- Develop a TextCNN for source-quality classification.
- Reduce unreliable content before report generation.
- Improve report quality using a critic stage.
- Maintain history using database support.

## 6. Tools and Technologies
- Frontend: React, Vite
- Backend: FastAPI, Uvicorn
- Database: SQLite
- AI orchestration: LangChain, LangGraph
- LLM: DeepSeek (deepseek-chat)
- Web search: Tavily
- Web scraping: BeautifulSoup
- Deep learning: PyTorch TextCNN

## 7. Methodology
1. User will enter a topic through the frontend.
2. Backend will trigger the Search Agent to collect web results.
3. Reader Agent will scrape detailed content.
4. TextCNN will score the collected text.
5. Writer Agent will draft the report.
6. Critic Agent will evaluate the report.
7. Report and metadata will be stored in the database.

## 8. Novelty
The project is not intended to remain at the level of API consumption. Its novelty lies in the **TextCNN reliability classifier** integrated inside the research workflow.

## 9. Expected Outcome
The system is expected to produce more trustworthy and better-structured research reports than a basic search-and-summarize pipeline by rejecting or down-weighting unreliable sources.

## 10. Reference Paper Chosen by Teacher
Teacher-selected paper: **MASQRAD (IEEE Transactions on Artificial Intelligence, 2025)**.

Relation to the chosen idea:
- MASQRAD provides the role-based multi-agent concept.
- ResearchMind extends that idea toward topic research and report generation.
- ResearchMind adds a CNN-based reliability module as the proposed new contribution.
