# Corrected Synopsis Text for PDF Report

Use this content to replace the mismatched sections in **AI-Driven Multi-Agent(2).pdf**.
It matches what is actually built in the `multi-ai-agent-research-assistant` project.

---

## Suggested Title (optional update)

**ResearchMind: A Hybrid Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering**

Alternative (keep PDF title style):

**AI-Driven Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering**

---

## 1. Introduction (REPLACE ENTIRE SECTION)

Artificial Intelligence (AI) has rapidly evolved from single-model systems to more advanced systems capable of understanding natural-language queries, generating responses, and supporting information analysis. Multi-Agent AI systems extend this capability by using multiple specialized AI agents that cooperate to perform different tasks and improve the overall quality of the final result [1].

In a multi-agent architecture, different agents can be assigned different responsibilities such as searching, reading, writing, and reviewing. The MASQRAD framework demonstrates this approach by using multiple Generative AI agents, including an Actor AI, Critic AI, and Expert Analysis AI, to resolve ambiguous user queries and generate useful insights [1].

Research today involves searching large volumes of online information. Manual research is time-consuming and difficult to organize. AI can assist in searching, reading, writing, and reviewing research content. However, many existing research assistants depend almost entirely on external APIs. They can search and generate text, but they do not include a locally controlled intelligence module that evaluates whether retrieved web content is reliable enough to be used in a final report.

To improve the trustworthiness of AI-generated research outputs, Convolutional Neural Network (CNN)-based text classification techniques such as TextCNN can be used to extract important local features from text and classify content as reliable or unreliable. Prior studies such as MDCNN and NE ZHA-TextCNN demonstrate the application of CNN/TextCNN-based approaches for text classification tasks [3], [5]. Another important challenge in Generative AI systems is the generation of incorrect or unsupported information, commonly referred to as AI hallucination. Detecting and reducing such errors is important for improving the reliability of AI-generated results [6].

Therefore, our proposed system combines the Multi-Agent AI approach of MASQRAD with a locally trained TextCNN model for **source reliability filtering**. The system accepts a research topic from the user, gathers web information through specialized agents, filters low-quality or suspicious content using TextCNN, generates a structured research report, and evaluates the report using a critic agent. This hybrid design adds a machine learning contribution beyond simple API integration.

---

## 2. Problem Statement (REPLACE — minor correction)

To develop a Multi-AI-Agent Research Assistant that integrates a multi-agent Actor–Critic framework with a TextCNN-based approach to efficiently process research topics, retrieve relevant web information, validate source reliability, reduce inaccurate outputs, and generate reliable and structured research reports.

---

## 4. Research Gaps (REPLACE ENTIRE SECTION)

The challenges faced by the existing approaches are listed below.

- Existing Multi-Agent AI systems such as MASQRAD focus mainly on query resolution and analysis, but they do not include a dedicated TextCNN-based **source reliability filter** inside a research report generation workflow [1].
- Many AI research assistants depend only on external APIs for search and text generation, without a locally trained model to evaluate whether scraped web content is trustworthy before synthesis.
- MDCNN and NE ZHA-TextCNN mainly apply CNN to news and long-text classification, but their use for filtering web research sources inside a multi-agent pipeline is limited [3], [5].
- Hallucination detection studies focus on translation and generation errors, but do not directly solve the problem of low-quality or clickbait web pages entering a research assistant pipeline [6].
- Therefore, there is a need for an integrated system combining Multi-Agent AI and TextCNN to improve source evaluation, reduce unreliable content before report writing, and generate more trustworthy structured research outputs [1], [6].

---

## 5. Objectives (REPLACE ENTIRE SECTION)

The main objectives of this research are listed below.

- To develop a Multi-AI Agent Research Assistant for automated topic-based research.
- To implement multiple specialized AI agents for web searching, content reading, report writing, and report review.
- To develop and integrate a locally trained TextCNN model for classifying retrieved web text as **reliable** or **unreliable**.
- To filter or down-weight unreliable sources before report generation.
- To generate structured research reports containing Introduction, Key Findings, Conclusion, and Sources.
- To implement a Critic Agent that scores the generated report and identifies strengths and areas for improvement.
- To present the complete system through a full-stack application using React, FastAPI, and SQLite.

---

## 6. Proposed Methodology (REPLACE ENTIRE SECTION)

The proposed Multi-AI Agent Research Assistant accepts a research topic from the user and processes it through a five-stage pipeline of specialized AI components.

**Step 1 — Search Agent:** The Search Agent accepts the user topic and gathers recent web results using the Tavily search API. It returns titles, URLs, and short snippets related to the topic.

**Step 2 — Reader Agent:** The Reader Agent selects the most relevant result from the search output and extracts readable text from the selected webpage using web scraping (requests and BeautifulSoup).

**Step 3 — TextCNN Source Filter:** The search snippets and scraped page text are passed to a locally trained TextCNN model. The model predicts whether the collected text appears **reliable** or **unreliable** based on local n-gram patterns learned during training. Only CNN-accepted passages are prioritized for report writing. If no source is accepted, the writer is warned to proceed cautiously.

**Step 4 — Writer Agent:** The Writer Agent uses CNN-approved content as input and generates a structured research report with the following sections: Introduction, Key Findings, Conclusion, and Sources.

**Step 5 — Critic Agent:** The Critic Agent reviews the generated report, assigns a score, lists strengths, identifies areas to improve, and provides a final one-line verdict.

The complete workflow is orchestrated through LangChain-based agents and chains, exposed through a FastAPI backend, displayed in a React frontend, and stored in a SQLite database for history and inspection.

**TextCNN Model Details:**
- Model type: Kim-style TextCNN
- Embedding dimension: 64
- Kernel sizes: 3, 4, 5
- Number of filters: 64
- Dropout: 0.5
- Output classes: reliable / unreliable
- Framework: PyTorch
- Training data: labeled reliable and unreliable text samples
- Validation accuracy achieved: approximately 90%

---

## 7. System Architecture (UPDATE CAPTION / DESCRIPTION)

**Figure 1: System Architecture**

Suggested flow for the diagram:

```
User
  ↓
React Frontend (Vite)
  ↓
FastAPI Backend
  ↓
Search Agent (Tavily)
  ↓
Reader Agent (Web Scraping)
  ↓
TextCNN Source Filter (Local PyTorch Model)
  ↓
Writer Agent (DeepSeek)
  ↓
Critic Agent (DeepSeek)
  ↓
SQLite Database
  ↓
Report + History displayed to User
```

Caption:

**Figure 1. ResearchMind workflow showing Search Agent, Reader Agent, TextCNN source filter, Writer Agent, Critic Agent, and SQLite storage.**

---

## 9. Software Requirements (REPLACE / UPDATE)

- Frontend: React, Vite
- Backend: FastAPI, Uvicorn
- Database: SQLite
- AI Orchestration: LangChain
- Large Language Model: DeepSeek (deepseek-chat)
- Web Search: Tavily API
- Web Scraping: requests, BeautifulSoup4
- Deep Learning: PyTorch (TextCNN)
- Development Environment: VS Code
- Version Control: Git / GitHub

---

## 10. Expected Outcomes (REPLACE — align with build)

The system is expected to generate more trustworthy, accurate, and well-structured research reports compared with a basic search-and-summarize approach. It achieves this by using multiple specialized AI agents to perform tasks such as web information retrieval, content extraction, source evaluation, report generation, and report review.

The locally trained TextCNN module identifies potentially unreliable, promotional, or low-quality web text and either rejects it or warns the writer before synthesis. By evaluating source credibility before generating the final report, the system aims to reduce misinformation, improve factual consistency, and provide better-organized research findings. All intermediate outputs (search, scrape, CNN verdict, report, critic feedback) are stored and can be inspected by the user.

---

## 11. Scope (REPLACE ENTIRE SECTION)

The scope of the Multi-AI Agent Research Assistant is to develop an AI-based system that assists users in conducting topic-based web research. The system will:

- accept a research topic from the user through a web interface,
- search the web for relevant information,
- scrape and extract readable content from selected web pages,
- classify source text as reliable or unreliable using a locally trained TextCNN model,
- generate a structured research report using a Writer Agent,
- evaluate the report using a Critic Agent,
- store and display past reports using SQLite.

**Out of scope for the current implementation (future work):**
- academic paper-only search (IEEE Xplore, arXiv APIs),
- automatic comparison of multiple research papers,
- visual or scanned-document analysis using CNN,
- citation verification and plagiarism checking.

---

## 12. Applications (OPTIONAL SMALL UPDATE)

- Student topic exploration and report drafting
- Automated research report generation
- Literature-style summary from web sources
- Natural-language question answering on research topics
- Source-quality-aware AI writing assistance

---

## Short “Relation to MASQRAD” paragraph (for viva / intro)

Our project is inspired by the teacher-selected IEEE paper **MASQRAD**, which uses role-based agents including actor and critic components. We extend that idea toward **topic-based research report generation** and add a **locally trained TextCNN** as the main machine learning contribution. Unlike a simple API mashup, ResearchMind includes a PyTorch model that filters source reliability before writing.

---

## What to REMOVE from the old PDF

Do **not** keep these claims unless you actually build them later:

- TextCNN classifies the **user query**
- Natural Language-to-Visualization (Chat2VIS / nvBench) as the main project focus
- Research paper search, summarization, and **comparison** as implemented features
- TextCNN processing of **visual content or scanned documents**
- Query Processing Agent, Information Extraction Agent, Analysis Agent as separate implemented modules

---

## Copy checklist before submission

- [ ] Section 1 no longer focuses on visualization
- [ ] Section 4 gaps mention source filtering, not NL2VIS
- [ ] Section 5 objectives mention source reliability, not query classification
- [ ] Section 6 lists the 5-stage pipeline (Search → Reader → TextCNN → Writer → Critic)
- [ ] Section 9 includes Tavily, BeautifulSoup, PyTorch, LangChain
- [ ] Section 11 scope matches implemented features only
- [ ] Architecture diagram updated to match the 5-stage flow
- [ ] Student name spelling checked (Dhage Aarti Santosh)
