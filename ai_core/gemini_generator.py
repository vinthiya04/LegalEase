import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

class GeminiDocumentGenerator:

    def __init__(self):
        self.model = genai.GenerativeModel(
            os.getenv("MODEL_NAME", "gemini-3.8-flash")
        )

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        effective_date
    ):

        prompt = f"""
Generate a professional legal document.

Document Type:
{document_type}

Parties:
{parties}

Terms:
{terms}

Effective Date:
{effective_date}

Include:
1. Introduction
2. Terms and Conditions
3. Responsibilities
4. Confidentiality
5. Termination
6. Signature Section
"""

        response = self.model.generate_content(prompt)

        return response.text