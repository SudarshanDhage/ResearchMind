const API_BASE = import.meta.env.VITE_API_URL ?? "";

function errorMessage(detail, fallback) {
  if (!detail) return fallback;
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) {
    return detail
      .map((item) => item.msg || item.detail || JSON.stringify(item))
      .join(" ");
  }
  return JSON.stringify(detail);
}

async function handle(res) {
  if (!res.ok) {
    let detail;
    try {
      const body = await res.json();
      detail = body.detail;
    } catch {
      /* ignore */
    }
    throw new Error(errorMessage(detail, `Request failed (${res.status})`));
  }
  return res.json();
}

export function getHealth() {
  return fetch(`${API_BASE}/api/health`).then(handle);
}

export function runResearch(topic) {
  return fetch(`${API_BASE}/api/research`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ topic }),
  }).then(handle);
}

export function listReports() {
  return fetch(`${API_BASE}/api/reports`).then(handle);
}

export function getReport(id) {
  return fetch(`${API_BASE}/api/reports/${id}`).then(handle);
}
