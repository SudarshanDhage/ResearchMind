"""CLI launcher. Canonical pipeline lives in backend/."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "backend"))

from pipeline import run_research_pipeline  # noqa: E402

if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic, verbose=True)
