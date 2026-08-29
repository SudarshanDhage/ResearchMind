# ResearchMind Viva FAQ

## 1. What is your project about?
ResearchMind is a proposed hybrid multi-agent research assistant. It is designed to search the web, read a relevant source, filter the content using a TextCNN model, generate a report, and then review that report using a critic agent.

## 2. What problem does it solve?
It addresses the difficulty of manual online research by automating search, reading, summarization, and review. It also tries to reduce unreliable source usage before report generation.

## 3. Why did you choose MASQRAD?
MASQRAD was chosen because it presents a role-based multi-agent structure with actor and critic logic. That concept is useful for designing writer and critic stages in our project.

## 4. Is your project the same as MASQRAD?
No. MASQRAD focuses on query resolution and analysis, while ResearchMind focuses on topic-based research report generation. The proposed system also adds a TextCNN reliability filter, which is not the main focus of MASQRAD.

## 5. What is the novelty in your project?
The novelty is the integration of a **TextCNN source reliability classifier** into the research pipeline. This means the project is not only using APIs, but also using a machine learning model for filtering source quality.

## 6. Why did you use TextCNN?
TextCNN is effective for sentence and document classification because it can capture local word patterns using convolution filters. It is also lighter and easier to explain than more complex transformer-based classifiers.

## 7. Why not use only DeepSeek for reliability checking?
If DeepSeek alone is used for everything, the project becomes mostly API orchestration. A local TextCNN adds an independent machine learning stage and gives the project a clearer research and implementation contribution.

## 8. What are the main modules of the system?
The main modules are:
- Search Agent
- Reader Agent
- TextCNN Source Filter
- Writer Agent
- Critic Agent
- Frontend and backend support modules

## 9. What does the Search Agent do?
It takes the user topic and retrieves web results such as titles, URLs, and snippets using a search API.

## 10. What does the Reader Agent do?
It selects the most relevant result and scrapes the page content to obtain deeper textual information.

## 11. What does the TextCNN do?
It classifies the collected text into reliable or unreliable categories. This helps the system decide which content should be used by the writer agent.

## 12. What does the Writer Agent do?
It generates a structured research report using the filtered text. The report typically includes introduction, key findings, conclusion, and sources.

## 13. What does the Critic Agent do?
It evaluates the generated report, provides a score, lists strengths and weaknesses, and gives suggestions for improvement.

## 14. Why is a critic stage important?
The critic stage improves quality assurance. Instead of directly accepting generated output, the system adds a review step for better transparency.

## 15. What technologies are used?
- React and Vite for frontend
- FastAPI for backend
- SQLite for storage
- LangChain and LangGraph for agent orchestration
- Tavily for web search
- BeautifulSoup for web scraping
- PyTorch for TextCNN

## 16. Why is it called a full-stack project?
Because it includes frontend, backend, database, AI orchestration, and a machine learning component.

## 17. What kind of data is used for the CNN?
The CNN is trained on labeled text examples that represent reliable and unreliable writing styles.

## 18. What are the two output classes of the CNN?
- Reliable
- Unreliable

## 19. Why do you need a database?
The database can store generated reports, topics, timestamps, and other pipeline outputs for later access.

## 20. Why use SQLite?
SQLite is simple, lightweight, and suitable for student projects and prototypes.

## 21. Why use FastAPI?
FastAPI is lightweight, fast, easy to structure, and well suited for connecting the backend with the frontend.

## 22. Why use React for frontend?
React helps create a clean user interface and makes the project look like a proper full-stack application.

## 23. What are the limitations of your proposed system?
- depends on external search API,
- may scrape only a limited number of sources,
- CNN quality depends on dataset quality,
- reliability filtering is based on text patterns rather than formal citation verification.

## 24. What future improvements are possible?
- larger training dataset,
- academic-paper PDF support,
- citation validation,
- multi-source aggregation,
- comparison with BERT or transformer classifiers.

## 25. What if the teacher asks, “What exactly did you contribute?”
A clear answer is:
"The contribution is a hybrid research assistant architecture where a locally trained TextCNN model is placed between the reading and writing stages to filter unreliable content before report generation. This moves the project beyond only API-based orchestration."

## 26. What if the teacher asks, “Why not just call this a chatbot?”
Because the system is not a single conversational model. It is a structured multi-stage workflow with different modules performing different tasks, including a separate CNN classifier.

## 27. What if the teacher asks, “Why is CNN suitable for text?”
CNN can detect important local phrase patterns such as sensational or formal academic wording. That makes it suitable for text classification tasks like fake-news and source-quality detection.

## 28. What if the teacher asks, “How is this better than direct summarization?”
Direct summarization can include unreliable or noisy content. This project proposes a filtering stage before writing, which can improve trustworthiness.

## 29. What if the teacher asks, “Can this be extended to IEEE papers only?”
Yes. The search and reading stages can later be restricted to trusted sources such as IEEE Xplore, digital libraries, or academic PDFs.

## 30. One-line summary for viva
ResearchMind is a proposed full-stack hybrid research assistant inspired by MASQRAD that adds a TextCNN-based source reliability filter before report generation.
