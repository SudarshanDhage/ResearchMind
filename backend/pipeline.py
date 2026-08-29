from agents import (
    build_reader_agent,
    build_search_agent,
    critique_report,
    write_report,
)
from cnn.filter import filter_for_writer


def last_text(result) -> str:
    messages = result.get("messages") or []
    if not messages:
        return ""
    last = messages[-1]
    content = getattr(last, "content", None)
    if content is None and isinstance(last, dict):
        content = last.get("content", "")
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, dict):
                parts.append(part.get("text") or "")
            else:
                parts.append(str(part))
        return "".join(parts)
    return str(content or "")


def run_research_pipeline(topic: str, verbose: bool = False) -> dict:
    """Run Search -> Reader -> TextCNN -> Writer -> Critic."""
    if verbose:
        print("\n" + "=" * 50)
        print("step 1 - search agent is working ...")
        print("=" * 50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    search = last_text(search_result)

    if verbose:
        print("\nsearch result", search)
        print("\n" + "=" * 50)
        print("step 2 - Reader agent is scraping top resources ...")
        print("=" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [(
            "user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{search[:800]}",
        )]
    })
    reader = last_text(reader_result)

    if verbose:
        print("\nscraped content:\n", reader)
        print("\n" + "=" * 50)
        print("step 3 - TextCNN is scoring source quality ...")
        print("=" * 50)

    research_combined, cnn = filter_for_writer(topic, search, reader)

    if verbose:
        print("\nCNN filter\n", cnn["summary"])
        print("\n" + "=" * 50)
        print("step 4 - Writer is drafting the report ...")
        print("=" * 50)

    report = write_report(topic, research_combined)

    if verbose:
        print("\nFinal Report\n", report)
        print("\n" + "=" * 50)
        print("step 5 - critic is reviewing the report")
        print("=" * 50)

    critic = critique_report(report)

    if verbose:
        print("\ncritic report\n", critic)

    return {
        "topic": topic,
        "search": search,
        "reader": reader,
        "cnn": cnn["summary"],
        "cnn_verdict": cnn["verdict"],
        "report": report,
        "critic": critic,
    }


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic, verbose=True)
