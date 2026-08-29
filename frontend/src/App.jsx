import { useCallback, useEffect, useMemo, useState } from "react";
import ReactMarkdown from "react-markdown";
import { getHealth, getReport, listReports, runResearch } from "./api";

const STEPS = [
  { key: "search", num: "01", title: "Search Agent", desc: "Gathers recent web information" },
  { key: "reader", num: "02", title: "Reader Agent", desc: "Scrapes & extracts deep content" },
  { key: "cnn", num: "03", title: "TextCNN Filter", desc: "Local CNN scores source reliability" },
  { key: "writer", num: "04", title: "Writer Chain", desc: "Drafts the report from CNN-approved text" },
  { key: "critic", num: "05", title: "Critic Chain", desc: "Reviews & scores the report" },
];

const EXAMPLES = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"];

function stepStatus(running, runningIndex, result, index) {
  if (result) return "done";
  if (!running) return "waiting";
  if (index < runningIndex) return "done";
  if (index === runningIndex) return "running";
  return "waiting";
}

function formatDate(iso) {
  if (!iso) return "";
  try {
    return new Date(iso).toLocaleString();
  } catch {
    return iso;
  }
}

export default function App() {
  const [topic, setTopic] = useState("");
  const [running, setRunning] = useState(false);
  const [runningIndex, setRunningIndex] = useState(0);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [history, setHistory] = useState([]);
  const [backendOk, setBackendOk] = useState(null);

  const loadHistory = useCallback(async () => {
    try {
      await getHealth();
      setBackendOk(true);
      const rows = await listReports();
      setHistory(rows);
    } catch {
      setBackendOk(false);
    }
  }, []);

  useEffect(() => {
    loadHistory();
  }, [loadHistory]);

  useEffect(() => {
    if (!running) return undefined;
    const timer = setInterval(() => {
      setRunningIndex((i) => Math.min(i + 1, STEPS.length - 1));
    }, 4000);
    return () => clearInterval(timer);
  }, [running]);

  async function onRun(event) {
    event.preventDefault();
    const value = topic.trim();
    if (!value) {
      setError("Please enter a research topic first.");
      return;
    }
    setError("");
    setResult(null);
    setRunning(true);
    setRunningIndex(0);
    try {
      const data = await runResearch(value);
      setResult(data);
      await loadHistory();
    } catch (err) {
      setError(err.message || "Research failed.");
    } finally {
      setRunning(false);
    }
  }

  async function openHistoryItem(id) {
    setError("");
    try {
      const data = await getReport(id);
      setResult(data);
      setTopic(data.topic || "");
    } catch (err) {
      setError(err.message || "Could not load report.");
    }
  }

  function downloadReport() {
    if (!result?.report) return;
    const blob = new Blob([result.report], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `research_report_${result.id || Date.now()}.md`;
    a.click();
    URL.revokeObjectURL(url);
  }

  const statuses = useMemo(
    () => STEPS.map((step, index) => stepStatus(running, runningIndex, result, index)),
    [running, runningIndex, result],
  );

  return (
    <div className="page">
      <header className="hero">
        <div className="hero-eyebrow">Multi-Agent AI System</div>
        <h1>
          Research<span>Mind</span>
        </h1>
        <p className="hero-sub">
          Four specialized AI agents collaborate — searching, scraping, writing,
          and critiquing — to deliver a polished research report on any topic.
        </p>
      </header>

      <div className="divider" />

      <main className="layout">
        <section>
          <form className="input-card" onSubmit={onRun}>
            <label htmlFor="topic">Research Topic</label>
            <input
              id="topic"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              placeholder="e.g. Quantum computing breakthroughs in 2025"
              disabled={running}
            />
            <button type="submit" disabled={running}>
              {running ? "Running pipeline…" : "Run Research Pipeline"}
            </button>
          </form>

          <div className="chips">
            <span className="chips-label">TRY</span>
            {EXAMPLES.map((ex) => (
              <button
                key={ex}
                type="button"
                className="chip"
                disabled={running}
                onClick={() => setTopic(ex)}
              >
                {ex}
              </button>
            ))}
          </div>

          {backendOk === false && (
            <p className="error">
              Backend is not reachable. Start it with: cd backend && uvicorn main:app --reload --port 8000
            </p>
          )}
          {error && <p className="error">{error}</p>}

          <div className="history">
            <div className="section-heading">Past reports</div>
            {backendOk === false ? (
              <p className="muted">History unavailable until the backend is running.</p>
            ) : history.length === 0 ? (
              <p className="muted">No saved reports yet.</p>
            ) : (
              <ul>
                {history.map((item) => (
                  <li key={item.id}>
                    <button type="button" onClick={() => openHistoryItem(item.id)}>
                      <strong>{item.topic}</strong>
                      <span>{formatDate(item.created_at)}</span>
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </section>

        <section>
          <div className="section-heading">Pipeline</div>
          {STEPS.map((step, index) => {
            const state = statuses[index];
            return (
              <div key={step.key} className={`step-card ${state}`}>
                <div className="step-header">
                  <span className="step-num">{step.num}</span>
                  <span className="step-title">{step.title}</span>
                  <span className={`step-status ${state}`}>
                    {state === "done" ? "done" : state === "running" ? "running" : "waiting"}
                  </span>
                </div>
                <div className="step-desc">{step.desc}</div>
              </div>
            );
          })}
        </section>
      </main>

      {result && (
        <>
          <div className="divider" />
          <div className="section-heading">Results</div>

          <details className="raw">
            <summary>Search Results (raw)</summary>
            <pre>{result.search}</pre>
          </details>

          <details className="raw">
            <summary>Scraped Content (raw)</summary>
            <pre>{result.reader}</pre>
          </details>

          {result.cnn && (
            <article className="feedback-panel">
              <div className="panel-label green">TextCNN Source Filter (local model)</div>
              <pre>{result.cnn}</pre>
              {result.cnn_verdict && (
                <p className="muted">Verdict: {result.cnn_verdict}</p>
              )}
            </article>
          )}

          <article className="report-panel">
            <div className="panel-label orange">Final Research Report</div>
            <div className="markdown">
              <ReactMarkdown>{result.report}</ReactMarkdown>
            </div>
            <button type="button" className="download" onClick={downloadReport}>
              Download Report (.md)
            </button>
          </article>

          <article className="feedback-panel">
            <div className="panel-label green">Critic Feedback</div>
            <div className="markdown">
              <ReactMarkdown>{result.critic}</ReactMarkdown>
            </div>
          </article>
        </>
      )}

      <footer className="notice">
        ResearchMind · FastAPI + React + SQLite · TextCNN + LangChain agents
      </footer>
    </div>
  );
}
