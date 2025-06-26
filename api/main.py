import os
import shutil
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pipeline.process_resumes import ingest_resume, score_job_description, UPLOAD_DIR
from langchain.document_loaders import PyPDFLoader

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.post("/evaluate")
async def evaluate(
        resumes: List[UploadFile] = File(...),
        job_desc_text: str = Form(None),
        job_desc_file: UploadFile = File(None),
        weight: float = Form(1.0),
        top_k: int = Form(5),
):
    # Determine job description
    if job_desc_text:
        job_desc = job_desc_text
    elif job_desc_file:
        ext = job_desc_file.filename.lower().split('.')[-1]
        data = await job_desc_file.read()
        if ext == 'pdf':
            tmp = f"/tmp/{job_desc_file.filename}"
            with open(tmp, 'wb') as f:
                f.write(data)
            loader = PyPDFLoader(tmp)
            docs = loader.load()
            job_desc = "\n".join(d.page_content for d in docs)
        else:
            job_desc = data.decode('utf-8')
    else:
        raise HTTPException(status_code=400, detail="Provide job description via text or file.")

    # Ingest resumes
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    for f in resumes:
        dest = os.path.join(UPLOAD_DIR, f.filename)
        with open(dest, 'wb') as buf: buf.write(await f.read())
        ingest_resume(dest)

    # Score
    results = score_job_description(job_desc, top_k)
    weighted = [{"resume_id": rid, "score": round(score * weight, 4)} for rid, score in results]
    return {"results": weighted}
