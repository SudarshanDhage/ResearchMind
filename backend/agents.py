import os
from pathlib import Path

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

from tools import web_search, scrape_url

load_dotenv(Path(__file__).resolve().parent / ".env")
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_llm():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY is missing. Add it to your .env file.")
    return ChatOpenAI(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        temperature=0,
        api_key=api_key,
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    )


def build_search_agent():
    return create_agent(
        model=get_llm(),
        tools=[web_search],
        system_prompt=(
            "You are a research search agent. Always use the web_search tool. "
            "Return a concise summary that includes titles, URLs, and key facts."
        ),
    )


def build_reader_agent():
    return create_agent(
        model=get_llm(),
        tools=[scrape_url],
        system_prompt=(
            "You are a research reader agent. Pick the most relevant URL from the "
            "search results and always use the scrape_url tool. Return the useful extracted content."
        ),
    )


writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])


def write_report(topic: str, research: str) -> str:
    chain = writer_prompt | get_llm() | StrOutputParser()
    return chain.invoke({"topic": topic, "research": research})


critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])


def critique_report(report: str) -> str:
    chain = critic_prompt | get_llm() | StrOutputParser()
    return chain.invoke({"report": report})
