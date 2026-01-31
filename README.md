# 🚀 Resume Analyzer – SCD Project

An **AI-powered Resume Analyzer** developed as part of the **Software Construction & Development (SCD)** course.  
This full-stack web application analyzes resumes, calculates ATS-based scores, optimizes resumes, and recommends relevant remote jobs based on extracted skills.

---

## 📌 Project Overview

The **Resume Analyzer** helps job seekers improve their resumes and find better job opportunities by:

- Extracting resume content from **PDF / DOCX**
- Calculating a **detailed resume score**
- Optimizing resumes for **ATS (Applicant Tracking Systems)**
- Recommending **real-world remote jobs**
- Displaying results using a clean, interactive frontend

The project follows **modular architecture**, **separation of concerns**, and **API-based design**, aligned with SCD best practices.

---

## ✨ Features

### 📄 Resume Upload & Parsing
- Supports **PDF** and **DOCX** formats
- Extracts text using reliable document parsers

### 📊 Resume Scoring System
Resume is scored out of **100** based on:
- Skills relevance
- Work experience
- Education
- ATS keyword compatibility

### ✨ ATS Resume Optimization
- Improves weak action verbs
- Adds missing skills
- Formats resume for ATS readability
- Generates structured, ATS-friendly content

### 💼 Job Recommendations
- Fetches live remote jobs using **Remotive API**
- Matches job descriptions with resume skills
- Calculates relevance percentage
- Stores job search history in MongoDB

### 📈 Visual Dashboard
- Resume score visualization using **Chart.js**
- Tab-based UI for smooth navigation

---

## 🛠 Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Vanilla JS)  
- Chart.js  
- Font Awesome  

### Backend
- FastAPI (Python)
- Pydantic
- MongoDB
- PyMongo
- pdfplumber
- python-docx
- Requests

---

## 🏗 Project Structure
```
Resume-Analyzer-SCD/
│
├── backend/
│ ├── main.py # FastAPI entry point
│ ├── database.py # MongoDB connection
│ ├── requirements.txt
│ │
│ ├── models/
│ │ └── user.py
│ │
│ ├── routes/
│ │ ├── resume.py
│ │ ├── jobs.py
│ │ └── user.py
│ │
│ ├── services/
│ │ ├── resume_parser.py
│ │ ├── resume_scoring.py
│ │ ├── ats_optimizer.py
│ │ └── job_fetcher.py
│ │
│ └── uploads/
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md
```


---

## 🔄 How the System Works

1. User uploads a resume (PDF/DOCX)
2. Backend extracts resume text
3. Resume is analyzed and scored
4. ATS optimization suggestions are generated
5. Relevant remote jobs are fetched and matched
6. Results are displayed on the frontend dashboard

---

## 🌐 API Endpoints

### Resume APIs
- `POST /resume/upload` – Upload & extract resume text  
- `POST /resume/score` – Calculate resume score  
- `POST /resume/optimize` – Generate ATS-optimized resume  

### Job APIs
- `POST /jobs/recommend` – Recommend jobs based on resume skills  

### User APIs
- `POST /user/register` – Register a new user  

---

## 🧠 SCD Concepts Implemented

- Modular programming
- Separation of concerns
- RESTful API design
- MVC-inspired architecture
- Database integration
- External API usage
- Validation & error handling

---

## 🚀 Future Improvements

- User authentication & login
- Resume comparison feature
- Skill gap analysis
- Machine learning-based scoring
- Cloud deployment (AWS / Vercel)

---

## 👩‍💻 Author

**Hafsa Rahman**  
Software Engineering Student  
SCD Course Project  

---

## 📄 License

This project is developed for **academic and educational purposes only**.

