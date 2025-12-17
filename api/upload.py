# from core.session import generate_session_id
# from fastapi import APIRouter, UploadFile, File, HTTPException
# import os
# import shutil


# router = APIRouter()

# @router.post("/")
# async def upload_files(files:list[UploadFile] = File(...)):
#     """Endpoint to upload multiple files."""

#     session_id = generate_session_id()
#     temp_dir = f"temp/{session_id}"

#     os.makedirs(temp_dir, exist_ok=True)

#     saved_file=[]
#     for file in files:
#         file_path= os.path.join(temp_dir, file.filename)


#         with open(file_path, "wb") as f:
#            shutil.copyfileobj(file.file, f)

#         saved_file.append(file.filename)


#     return {
#         "status": "success",
#         "message": f"Files uploaded successfully for session {session_id}",
#         "session_id": session_id,
#         "filename": saved_file
#     }


    
from fastapi import APIRouter, UploadFile, File
import os, shutil

from core.session import generate_session_id
from services.loader import load_document
from services.chunker import chunk_text
from services.embeddings import embedding_text
from services.vector_store import upsert_chunks

router = APIRouter()


@router.post("/")
async def upload_files(files: list[UploadFile] = File(...)):
    session_id = generate_session_id()
    temp_dir = f"tmp/{session_id}"
    os.makedirs(temp_dir, exist_ok=True)

    all_chunks = []

    for file in files:
        file_path = os.path.join(temp_dir, file.filename)

        # 1. Save file
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # 2. Load text
        text = load_document(file_path)

        # 3. Chunk text
        chunks = chunk_text(text)

        all_chunks.extend(chunks)

    # 4. Generate embeddings
    embeddings = embedding_text(all_chunks)

    # 5. Store in Pinecone
    upsert_chunks(session_id, all_chunks, embeddings)

    return {
        "status": "success",
        "session_id": session_id,
        "chunks_stored": len(all_chunks),
        "filename": file.filename
    }
