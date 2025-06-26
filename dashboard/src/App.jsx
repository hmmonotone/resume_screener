import React, { useState } from 'react';
import './style.css';
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [resumes, setResumes] = useState([]);
  const [jobDescText, setJobDescText] = useState('');
  const [jobDescFile, setJobDescFile] = useState(null);
  const [results, setResults] = useState([]);
  const [weight, setWeight] = useState(1.0);
  const [topK, setTopK] = useState(5);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = new FormData();
    resumes.forEach(r => form.append('resumes', r));
    if (jobDescFile) form.append('job_desc_file', jobDescFile);
    else form.append('job_desc_text', jobDescText);
    form.append('weight', weight);
    form.append('top_k', topK);

    const res = await fetch(`${API_URL}/evaluate`, { method: 'POST', body: form });
    const data = await res.json();
    setResults(data.results);
  };

  return (
    <div className="container">
      <h1>Resume Screener</h1>
      <form onSubmit={handleSubmit}>
        <label>Upload Resumes (PDF):</label>
        <input type="file" multiple accept=".pdf" onChange={e => setResumes(Array.from(e.target.files))} />

        <label>Job Description Text:</label>
        <textarea value={jobDescText} onChange={e => setJobDescText(e.target.value)} />

        <label>Or Upload Job Description (PDF/TXT):</label>
        <input type="file" accept=".pdf,.txt" onChange={e => setJobDescFile(e.target.files[0])} />

        <label>Weight:</label>
        <input type="number" step="0.1" value={weight} onChange={e => setWeight(parseFloat(e.target.value))} />

        <label>Top K:</label>
        <input type="number" value={topK} onChange={e => setTopK(parseInt(e.target.value))} />

        <button type="submit">Evaluate</button>
      </form>

      <h2>Results</h2>
      <table>
        <thead><tr><th>Resume ID</th><th>Score</th></tr></thead>
        <tbody>
          {results.map(r => (
            <tr key={r.resume_id}><td>{r.resume_id}</td><td>{r.score}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;