# ⚖️ LegalEaseAI

LegalEaseAI is an AI-powered legal document generator that helps users create legal documents quickly using Google's Gemini AI model.

## Features

- Generate legal documents using AI
- FastAPI backend
- Streamlit frontend
- Gemini AI integration
- Download generated documents
- Easy-to-use interface

## Project Structure

LegalEaseAI/

├── frontend/
│   └── app.py

├── backend/
│   ├── main.py
│   ├── routes.py
│   └── models.py

├── ai_core/
│   └── gemini_generator.py

├── utils/
│   ├── formatter.py
│   ├── pdf_generator.py
│   ├── docx_generator.py
│   └── sanitizer.py

├── assets/
│   └── logo.png

├── exports/
├── .env
├── requirements.txt
└── README.md

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
APP_NAME=LegalEaseAI
APP_ENV=development
HOST=127.0.0.1
PORT=8000
```

## Run Backend

```bash
uvicorn backend.main:app --reload
```

Swagger Docs:
http://127.0.0.1:8000/docs

## Run Frontend

```bash
streamlit run frontend/app.py
```

## Technologies Used

- Python
- FastAPI
- Streamlit
- Gemini AI
- Python-Docx
- FPDF
