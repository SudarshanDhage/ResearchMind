# ResearchMind Final Year Project Report Starter

## Title
ResearchMind: A Hybrid Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering

## Project Idea Chosen
The proposed project idea is a **multi-agent research assistant** inspired in part by the IEEE paper **MASQRAD (Multiagent Actor-Critic Generative AI for Query Resolution and Analysis)**. From MASQRAD, the project borrows the idea of specialized agents with distinct responsibilities and a reviewer/critic stage. However, the proposed work differs in application focus and technical contribution.

ResearchMind is intended for **topic-based research report generation**. Instead of only transforming ambiguous queries into analytical outputs, the proposed system will follow a complete academic-assistant workflow:

1. Search the web for current information.
2. Read and scrape the most relevant source.
3. Apply a **TextCNN-based source filter** to classify gathered text as reliable or unreliable.
4. Generate a structured research report.
5. Critique and score the generated report.

This addition of a CNN module addresses the criticism that many student projects only combine external APIs. In the proposed system, DeepSeek and Tavily will serve as supporting components, while the **TextCNN source-quality classifier will represent the main machine learning contribution of the project**.

## 1. Introduction
The rapid growth of online information has made research both easier and more difficult. While the internet provides access to vast amounts of knowledge, users still face major problems in selecting trustworthy sources, reading large amounts of material, and organizing findings into a clear report. Manual research is often time-consuming, inconsistent, and difficult for students who need fast yet reliable summaries.

Recent progress in artificial intelligence, especially large language models and multi-agent workflows, has made it possible to automate parts of the research process. Instead of relying on a single model for every task, a multi-agent system divides the work into specialized roles such as searching, reading, writing, and reviewing. This improves structure, modularity, and explainability.

However, many existing research assistants still depend almost entirely on external APIs. They can search and generate text, but they do not include a locally controlled intelligence module that evaluates the reliability of information before using it in the report. To address this gap, this project proposes **ResearchMind**, a hybrid research assistant that combines API-driven agents with a **PyTorch TextCNN model** for source reliability classification.

The proposed system will follow a five-stage pipeline: Search Agent, Reader Agent, TextCNN Filter, Writer Agent, and Critic Agent. The system is planned as a full-stack application using React for the frontend, FastAPI for the backend, SQLite for report storage, LangChain/LangGraph for orchestration, and PyTorch for the CNN model. The TextCNN filter is expected to provide the main originality of the project by deciding whether retrieved web content appears reliable enough to be used in report writing.

## 2. Problem Statement
Current research workflows suffer from three major limitations:

- manual searching and summarization require significant time and effort,
- generated reports may include low-quality or unreliable web content,
- many AI assistants act only as wrappers around APIs without a meaningful local intelligence component.

Therefore, there is a need for a system that not only automates web research and report generation, but also includes a local machine learning model to assess source quality before synthesis.

## 3. Objectives
The main objectives of the project are:

- To design a multi-agent research assistant for automated topic exploration.
- To develop a full-stack application with React, FastAPI, and SQLite.
- To train a **TextCNN** model for classifying retrieved text as reliable or unreliable.
- To use the CNN output as a filtering step before report generation.
- To generate a structured research report and a critic-based evaluation.
- To provide a transparent workflow that users can inspect step by step.

## 4. Proposed Methodology
### 4.1 Search Agent
The Search Agent will accept a user topic and gather recent web results using Tavily. It will return titles, URLs, and snippets.

### 4.2 Reader Agent
The Reader Agent will select the most relevant result and extract readable content from the target page using web scraping techniques.

### 4.3 TextCNN Source Filter
The scraped and searched text will be passed through a **TextCNN** classifier. The model will be trained using labeled reliable and unreliable text samples. It will use word embeddings, parallel convolution filters of different kernel sizes, max-pooling, dropout, and a final fully connected layer to predict source reliability.

### 4.4 Writer Agent
CNN-accepted text will be prioritized for report generation. The writer agent will create a structured output containing Introduction, Key Findings, Conclusion, and Sources.

### 4.5 Critic Agent
The critic agent will review the final report and provide a score, strengths, areas to improve, and a one-line verdict.

## 5. Original Contribution
The main novelty of this project is the **proposed integration of a TextCNN source-quality filter inside a multi-agent research pipeline**. This is expected to make the system different from a simple API mashup.

Expected original points:

- a custom PyTorch TextCNN model for source-quality classification,
- a CNN decision stage before report generation,
- report generation guided by CNN-approved passages,
- a full-stack workflow with transparent stage-by-stage output.

## 6. IEEE Paper Support
The project can be justified using the following IEEE papers:

1. **MASQRAD** — supports the multi-agent actor/critic idea.
2. **SECNN sentence classification paper** — supports TextCNN for text classification.
3. **MCNN-LSTM news classification paper** — supports deep learning on news/web text.
4. **CNN fake news detection paper** — supports reliability filtering of web content.

## 7. Flow Diagram Section
Insert the project flow diagram here.

Suggested caption:

**Figure 1. Proposed ResearchMind workflow showing Search Agent, Reader Agent, TextCNN source filter, Writer Agent, Critic Agent, and database support.**

If image generation is enabled later in Cursor, use the prompt saved in `docs/flow_diagram_prompt.md`.

## 8. Conclusion of Starting Section
ResearchMind is proposed as a hybrid AI research assistant that combines multi-agent orchestration with a CNN-based source reliability stage. This architecture is expected to improve trust, add originality, and provide a stronger final-year project contribution than using APIs alone.
