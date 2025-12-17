from fastapi import FastAPI
from dotenv import load_dotenv
from api import upload, chat


load_dotenv()

app = FastAPI(title="RAG Application")


@app.get("/")
async def read_root():
    return {
        "status": "OK",
        "message": "Welcome to the RAG Application And FastAPI! Server is running."
        }



app.include_router(upload.router, prefix="/upload")
app.include_router(chat.router, prefix="/api")


