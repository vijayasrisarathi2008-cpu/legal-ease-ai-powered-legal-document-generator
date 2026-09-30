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
You are a professional legal document drafting assistant.

Create a structured {document_type}.

Parties:
{parties}

Terms and Conditions:
{terms}

Effective Date:
{dates}

Requirements:
1. Create a professional title.
2. Clearly mention the parties.
3. Include the effective date.
4. Convert the given terms into suitable clauses.
5. Use clear and formal language.
6. Add signature sections.
7. Do not invent important personal information.
8. Format the output with clear headings.

Document:
"""

        response = self.model.generate_content(prompt)

        return response.text
