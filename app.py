from fastapi import FastAPI, Form 
from fastapi.responses import FileResponse
import psycopg2
import os

app = FastAPI()
def get_db_conn():
    return psycopg2.connect(
        host = os.environ.get("DB_HOST", "db"),
        database = os.environ.get("DB_NAME", "mydatabase"),
        user = os.environ.get("DB_USER", "admin"),
        password = os.environ.get("DB_PASSWORD", "root")


    )
@app.on_event("startup")
def startup():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100)
                )
                """)
    conn.commit()
    conn.close()
    
    cur.close()
@app.get("/")
def read_root(name: str):
    conn = get_db_conn()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()
    except Exception as e:
        return {"eror":str(e)}
    finally:
        cur.close()
        conn.close()
    return {"status": "Ready", "message": f"User {name} added to the db"}
    
    
    

    