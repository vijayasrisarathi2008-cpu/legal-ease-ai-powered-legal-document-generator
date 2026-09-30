import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)


class GeminiDocumentGenerator:

    def __init__(self):
        self.model = genai.GenerativeModel(
            "gemini-1.5-pro"
        )

    def generate_document(
        self,
        document_type,
        parties,
        terms,
        dates
    ):

        prompt = f"""
You are a professional legal document assistant.

Create a structured {document_type}.

Parties:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Requirements:
- Use clear professional language.
- Include a title.
- Include parties.
- Include effective date.
- Include terms and conditions.
- Add appropriate sections.
- Add signature sections.
- Do not invent personal information.
- Clearly mention that the generated document
  should be reviewed by a qualified legal professional.

Generate only the legal document.
"""

        response = self.model.generate_content(prompt)

        return response.text
