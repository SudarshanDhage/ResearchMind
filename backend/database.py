import sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "research.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                search TEXT,
                reader TEXT,
                cnn TEXT,
                cnn_verdict TEXT,
                report TEXT,
                critic TEXT,
                created_at TEXT NOT NULL
            )
            """
        )
        cols = {row["name"] for row in conn.execute("PRAGMA table_info(reports)")}
        if "cnn" not in cols:
            conn.execute("ALTER TABLE reports ADD COLUMN cnn TEXT")
        if "cnn_verdict" not in cols:
            conn.execute("ALTER TABLE reports ADD COLUMN cnn_verdict TEXT")
        conn.commit()


def save_report(
    topic: str,
    search: str,
    reader: str,
    report: str,
    critic: str,
    cnn: str = "",
    cnn_verdict: str = "",
) -> dict:
    created_at = datetime.now(timezone.utc).isoformat()
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO reports (topic, search, reader, cnn, cnn_verdict, report, critic, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (topic, search, reader, cnn, cnn_verdict, report, critic, created_at),
        )
        conn.commit()
        report_id = cursor.lastrowid
    return get_report(report_id)


def list_reports() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, topic, created_at FROM reports ORDER BY id DESC"
        ).fetchall()
    return [dict(row) for row in rows]


def get_report(report_id: int) -> dict | None:
    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT id, topic, search, reader, cnn, cnn_verdict, report, critic, created_at
            FROM reports WHERE id = ?
            """,
            (report_id,),
        ).fetchone()
    return dict(row) if row else None
