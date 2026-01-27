import os
from fastapi import APIRouter , Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
router = APIRouter(prefix="/chat", tags=["ChatBot"])



class ChatReq(BaseModel):
    message: str

@router.post("/ask")
def ask_chatbot(data: ChatReq):
    prompt = f"""You are a cricket expert assistant.

Rules:
1. Answer ONLY cricket-related questions.
2. Automatically detect the user’s language:
   - If the user writes in Hinglish (mix of Hindi and English), reply in clear English.
   - If the user writes in English, reply in English.
   - If the user writes in Hindi (Devanagari script), reply in Hindi.
3. If the question is about a cricket player:
   - First give a short introduction (2–3 lines).
   - Then provide key statistics in a simple table format.
   - The table must include: Matches, Runs, Centuries (100s), Wickets.
4. Keep answers short, simple, and easy to understand.
5. Do not add unnecessary explanations or non-cricket topics.
6. If exact statistics are not available, clearly mention that the data is approximate.

Response format:
- Short player introduction
- Statistics table
- One-line summary


Question: {data.message}
Answer:
"""
    response = model.generate_content(prompt)
    return {"reply": response.text}
