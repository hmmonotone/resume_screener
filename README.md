# **AI-Powered Resume Screener (SaaS)**

An intelligent resume screening tool that parses and ranks resumes based on job descriptions, helping recruiters shortlist candidates efficiently.

---

## **Features**

* NLP-driven pipeline using **OpenAI** & **LangChain**
* **FastAPI** backend deployed on **AWS Lambda**
* Resume and metadata storage on **Amazon S3**
* **MongoDB** / **PostgreSQL** for candidate profiles and scoring data
* Responsive admin dashboard built with **Refine.dev**
* Real-time parsing & scoring with adjustable weightage parameters

---

## **Tech Stack**

* **Python**, **FastAPI**
* **OpenAI**, **LangChain**
* **AWS Lambda**, **Amazon S3**
* **MongoDB**, **PostgreSQL**
* **React**, **Refine.dev**
* **Docker**, **Docker Compose**

---

## **Setup Instructions**

1. Clone the repository:

   ```bash
   git clone https://github.com/hmmonotone/resume_screener.git
   cd resume_screener
   ```

2. Configure environment variables:
   Create a `.env` file in the root directory and add the necessary variables.

3. Build and start services:

   ```bash
   docker-compose up --build
   ```
