# AI-Powered Resume Screener (SaaS)

An intelligent resume screening tool that parses and ranks resumes based on job descriptions, helping recruiters shortlist candidates efficiently.

## Features
- NLP-driven pipeline with OpenAI & LangChain
- FastAPI backend deployed on AWS Lambda
- Storage on Amazon S3
- MongoDB/PostgreSQL for profiles & scoring metadata
- Responsive admin dashboard (Refine.dev)
- Real-time parsing & scoring with adjustable weightage

## Tech Stack
- Python, FastAPI
- OpenAI, LangChain
- AWS Lambda, S3
- MongoDB/PostgreSQL
- React, Refine.dev
- Docker & Docker Compose

## Setup
1. Clone the repo:
   ```bash
git clone https://github.com/hmmonotone/resume_screener.git
cd resume_screener
3. Configure environment variables in `.env`.
4. Start services:
   ```bash
docker-compose up --build