# ===============================
# Base Image
# ===============================
FROM python:3.10-slim

# ===============================
# Environment settings
# ===============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# Working directory inside container
# ===============================
WORKDIR /app

# ===============================
# Install system dependencies (lightweight)
# ===============================
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ===============================
# Copy dependency file first (for caching)
# ===============================
COPY requirements.txt .

# ===============================
# Install Python dependencies
# ===============================
RUN pip install --no-cache-dir -r requirements.txt

# ===============================
# Copy entire project
# ===============================
COPY . .

# ===============================
# Expose ports
# 8000 -> FastAPI
# 8501 -> Streamlit (future ready)
# ===============================
EXPOSE 8000
EXPOSE 8501

# ===============================
# Default command (Backend)
# ===============================
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
