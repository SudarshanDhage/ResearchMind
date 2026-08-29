# ResearchMind Idea Explanation

## Title
ResearchMind: A Hybrid Multi-Agent Research Assistant with TextCNN-Based Source Reliability Filtering

## Simple Introduction
Today, a large amount of information is available on the internet, but not all of it is reliable or easy to organize. Students often spend a lot of time searching for information, reading multiple websites, and preparing a proper summary or report. Because of this, there is a need for an intelligent system that can assist in the research process.

The basic idea of this project is to create a **research assistant** that can help in collecting information, understanding it, and preparing a structured output. Instead of depending on a single AI model for every task, the proposed idea uses multiple stages, where each stage performs a specific role.

## Reference Idea from Paper
The teacher-selected paper is **MASQRAD** from IEEE Transactions on Artificial Intelligence. That paper follows a multi-agent concept where different agents are assigned different responsibilities, such as generating output and reviewing it.

This inspired the proposed idea because it shows that task division among agents can improve quality and structure.

## Our Proposed Idea
The proposed idea is called **ResearchMind**.

It is planned as a research assistant that will work in the following way:

1. Search for information related to a topic.
2. Read and extract content from the selected source.
3. Check whether the content looks reliable.
4. Generate a structured research report.
5. Review the generated report.

So, the main idea is not just report generation, but **research assistance with source filtering and review**.

## What Makes the Idea Different
Many similar systems only use APIs to search or generate text. The proposed idea aims to go one step further by adding a **TextCNN-based reliability filter**.

This means:
- the system will not directly trust every scraped source,
- a deep learning model will be used to classify content as reliable or unreliable,
- only better-quality content will be preferred for report generation.

This makes the idea stronger and more original than a basic API-based assistant.

## One-Paragraph Version for Explanation
My project idea is to develop a hybrid multi-agent research assistant called ResearchMind. It is inspired by the IEEE paper MASQRAD, which uses different agents for different roles. In my proposed idea, the system will search for topic-related information, read useful web content, pass that content through a TextCNN-based reliability filter, generate a structured report, and then review it using a critic stage. The key difference is that the project is not only based on APIs, but also includes a machine learning component for source-quality checking.

## Very Short Viva Version
My idea is to build a research assistant that uses multiple stages like search, reading, writing, and review. The inspiration comes from MASQRAD, but I am extending it for topic-based research report generation. The new part in my idea is a TextCNN model that checks whether the source content is reliable before it is used.
