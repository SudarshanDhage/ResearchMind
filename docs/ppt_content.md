# ResearchMind PPT

## Slide 1: Title Slide
**ResearchMind: A Hybrid Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering**

- Final Year Project
- Student Name(s)
- Guide Name
- Department / College

**Speaker note:**
This project proposes a hybrid AI research assistant that combines a multi-agent workflow with a locally controlled TextCNN model for source reliability filtering.

## Slide 2: Introduction
- Research today involves searching large volumes of web information.
- Manual research is time-consuming and difficult to organize.
- AI can assist in searching, reading, writing, and reviewing research content.
- However, many systems rely only on external APIs.

**Speaker note:**
The main issue is not only generating reports, but making sure the input sources are trustworthy before they are used.

## Slide 3: Problem Statement
- Online information is abundant but not always reliable.
- Students spend significant time searching and summarizing content.
- Existing AI assistants may include low-quality or noisy sources.
- Many student projects simply combine third-party APIs without adding a new technical contribution.

**Speaker note:**
So the problem is to create a research assistant that is automated, structured, and more trustworthy than a simple API-based summarizer.

## Slide 4: Motivation
- Need for faster academic topic exploration
- Need for structured report generation
- Need for source-quality checking before synthesis
- Need for a project with clear originality and machine learning contribution

## Slide 5: Selected Reference Paper
**Teacher-selected paper: MASQRAD**

- Full name: *Multiagent Actor-Critic Generative AI for Query Resolution and Analysis*
- Venue: **IEEE Transactions on Artificial Intelligence**, 2025
- Core idea: Actor, Critic, and Expert agents collaborate to improve output quality

**Relation to our idea:**
- Inspires the role-based agent structure
- Supports the writer + critic design
- Our project extends the idea toward topic research and report generation

## Slide 6: Proposed Project Idea
**ResearchMind** is proposed as a five-stage pipeline:

1. Search Agent
2. Reader Agent
3. TextCNN Source Filter
4. Writer Agent
5. Critic Agent

**Main originality:**
- includes a **locally trained TextCNN**,
- not limited to API use,
- combines agent orchestration with deep learning.

## Slide 7: Objectives
- To design a multi-agent research assistant for topic exploration
- To automate search, reading, writing, and review stages
- To develop a TextCNN model for source reliability classification
- To reduce unreliable content before report generation
- To present the system through a full-stack application

## Slide 8: System Architecture
**Flow:**
User -> React Frontend -> FastAPI Backend -> Search Agent -> Reader Agent -> TextCNN -> Writer Agent -> Critic Agent -> SQLite

**Add the flow diagram image here**

**Speaker note:**
This slide should show the end-to-end system flow. The TextCNN stage is the main contribution because it filters source quality before the writing stage.

## Slide 9: Search Agent
- Accepts the topic from the user
- Uses Tavily API to collect web results
- Returns titles, URLs, and snippets
- Acts as the information discovery stage

## Slide 10: Reader Agent
- Selects the most relevant result
- Scrapes page content using BeautifulSoup
- Extracts readable text from the selected webpage
- Provides deeper content for the next stage

## Slide 11: TextCNN Source Filter
- Receives search and scraped text
- Predicts whether text is **reliable** or **unreliable**
- Helps reduce noisy, promotional, or clickbait-like content
- Passes reliable content to the writing stage

**Why this matters:**
This stage makes the project more than API integration by adding a locally controlled machine learning module.

## Slide 12: CNN Model Details
- Model: **TextCNN**
- Embedding dimension: **64**
- Kernel sizes: **3, 4, 5**
- Filters: **64**
- Dropout: **0.5**
- Output classes: **reliable / unreliable**

**Simple explanation:**
The model checks short patterns of 3 to 5 words at a time and learns whether the writing style looks trustworthy or suspicious.

## Slide 13: Expected Training Setup
- Framework: **PyTorch**
- Dataset type: labeled reliable and unreliable text samples
- Data split: training and validation
- Output: reliability score used before report writing

**Possible evaluation metrics:**
- Accuracy
- Precision
- Recall
- F1-score

## Slide 14: Writer Agent
- Uses CNN-approved content as input
- Generates a structured research report
- Output sections:
  - Introduction
  - Key Findings
  - Conclusion
  - Sources

## Slide 15: Critic Agent
- Reviews the generated report
- Assigns a score
- Lists strengths
- Identifies areas to improve
- Gives a final one-line verdict

**Speaker note:**
This stage improves transparency and quality by evaluating the generated report instead of directly returning it.

## Slide 16: Full Workflow
1. User enters topic
2. Search Agent gathers web results
3. Reader Agent scrapes detailed text
4. TextCNN checks source reliability
5. Writer Agent generates report
6. Critic Agent evaluates report
7. Results are displayed and stored

## Slide 17: Tools and Technologies
- Frontend: React, Vite
- Backend: FastAPI, Uvicorn
- Database: SQLite
- Orchestration: LangChain, LangGraph
- LLM: DeepSeek (deepseek-chat)
- Web Search: Tavily
- Web Scraping: BeautifulSoup
- Deep Learning: PyTorch TextCNN

## Slide 18: Advantages
- Automates topic research workflow
- Uses specialized agents for each stage
- Adds a local deep learning component
- Improves trust through source filtering
- Can be extended for academic or domain-specific use

## Slide 19: Limitations
- Search depends on external web API
- Reliability is judged from text patterns, not full citation verification
- One-page deep scraping may miss some sources
- Model quality depends on training data quality

## Slide 20: Future Scope
- Larger labeled dataset for TextCNN
- Compare TextCNN with BERT-based models
- Multi-source aggregation instead of one-page scraping
- Add PDF ingestion for IEEE papers
- Add citation validation and plagiarism checks
- Support domain-specific research modes

## Slide 21: Conclusion
ResearchMind is proposed as a hybrid research assistant that combines multi-agent AI with a TextCNN-based source filtering stage. Inspired by MASQRAD, the project extends the idea into topic-based research report generation and aims to provide stronger originality than an API-only assistant.

## Slide 22: Thank You
**Thank You**

Questions?
