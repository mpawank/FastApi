import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

# Get MongoDB URI from environment variable (fallback to hardcoded for testing)
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://root:root@cluster0.h7ulqme.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Create MongoDB client
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Verify connection
try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ MongoDB connection error:", e)

# Database and collection references
db = client.todo_db
collection = db["todo_collection"]
