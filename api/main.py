import os
import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL", "mongodb://db_mongo:27017")
mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client.blog_db


def get_mysql_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db_mysql"),
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER", "admin"),
        password=os.getenv("MYSQL_PASSWORD"),
        port=3306,
    )


@app.get("/posts")
async def get_posts():
    try:
        cursor = mongo_db.posts.find({}, {"_id": 0})
        posts = await cursor.to_list(length=100)
        return {"posts": posts}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"MongoDB unavailable: {exc}")


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
        raise HTTPException(status_code=503, detail=f"MySQL unavailable: {exc}")


@app.get("/health")
async def health():
    errors = []

    try:
        await get_posts()
    except HTTPException as exc:
        errors.append(f"posts: {exc.detail}")

    try:
        await get_users()
    except HTTPException as exc:
        errors.append(f"users: {exc.detail}")

    if errors:
        raise HTTPException(status_code=503, detail={"status": "error", "errors": errors})

    return {"status": "ok"}
