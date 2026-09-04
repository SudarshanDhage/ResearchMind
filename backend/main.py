import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

from database import get_report, init_db, list_reports, save_report


def _allowed_origins() -> list[str]:
    defaults = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ]
    extra = os.getenv("ALLOWED_ORIGINS", "")
    if not extra.strip():
        return defaults
    return defaults + [o.strip() for o in extra.split(",") if o.strip()]


@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield


app = FastAPI(title="ResearchMind API", version="1.0.0", lifespan=lifespan)

_origins = _allowed_origins()
_allow_all = "*" in _origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if _allow_all else _origins,
    allow_credentials=not _allow_all,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=1)

    @field_validator("topic")
    @classmethod
    def topic_not_blank(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Topic is required.")
        return cleaned


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/research")
def create_research(body: ResearchRequest):
    from pipeline import run_research_pipeline

    try:
        result = run_research_pipeline(body.topic)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    saved = save_report(
        topic=result["topic"],
        search=result["search"],
        reader=result["reader"],
        cnn=result.get("cnn", ""),
        cnn_verdict=result.get("cnn_verdict", ""),
        report=result["report"],
        critic=result["critic"],
    )
    if saved is None:
        raise HTTPException(status_code=500, detail="Report was generated but could not be saved.")
    return saved


@app.get("/api/reports")
def reports():
    return list_reports()


@app.get("/api/reports/{report_id}")
def report_detail(report_id: int):
    row = get_report(report_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Report not found.")
    return row
