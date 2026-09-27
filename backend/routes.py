from fastapi import APIRouter
from backend.models import DocumentRequest
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()

generator = GeminiDocumentGenerator()

@router.post("/generate")
def generate_document(data: DocumentRequest):

    document = generator.generate_document(
        data.document_type,
        data.parties,
        data.terms,
        data.effective_date
    )

    return {
        "document": document
    }