from pymongo import MongoClient
import os

# Get MongoDB URL from Railway environment variables
MONGO_URL = os.getenv("MONGO_URL")

# Connect to MongoDB
client = MongoClient(MONGO_URL)

# Database
db = client["resume_analyzer"]

# Collections
users_collection = db["users"]
resumes_collection = db["resumes"]
jobs_collection = db["job_history"]

# Debug message
print("✅ MongoDB Connected Successfully")
