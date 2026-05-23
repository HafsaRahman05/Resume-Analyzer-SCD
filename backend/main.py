from fastapi import FastAPI
from routes import resume, user, jobs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Resume Analyzer",
    description="Resume Scoring, ATS Optimization & Job Recommendation System",
    version="1.0"
)

# ✅ Production-safe CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://resume-analyzer-scd.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(resume.router, prefix="/resume", tags=["Resume"])
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

@app.get("/")
def root():
    return {"message": "Resume Analyzer API is running 🚀"}
