from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)
db = client["resume_analyzer"]

users_collection = db["users"]
resumes_collection = db["resumes"]
jobs_collection = db["job_history"]
