import mysql.connector
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_mysql_connection():
    return mysql.connector.connect(
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER", "admin"),
        password=os.getenv("MYSQL_PASSWORD"),
        port=3306,
        host=os.getenv("MYSQL_HOST", "db_mysql"),
    )

def get_mongo_db():
    client = MongoClient(f"mongodb://{os.getenv('MONGO_HOST', 'db_mongo')}:27017/")
    return client["blog_db"], client

@app.get("/users")
async def get_users():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateurs")
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"utilisateurs": records}
    except mysql.connector.Error as exc:
        raise HTTPException(status_code=503, detail=f"Database unavailable: {exc}")

@app.get("/posts")
async def get_posts():
    try:
        db, client = get_mongo_db()
        posts = list(db.posts.find({}, {"_id": 0}))
        client.close()
        return {"posts": posts}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"MongoDB unavailable: {exc}")

@app.get("/health")
async def health():
    errors = []

    try:
        await get_users()
    except HTTPException as exc:
        errors.append(f"users: {exc.detail}")

    try:
        await get_posts()
    except HTTPException as exc:
        errors.append(f"posts: {exc.detail}")

    if errors:
        raise HTTPException(status_code=503, detail={"status": "error", "errors": errors})

    return {"status": "ok"}
