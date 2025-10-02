import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
apikeyfromenv = os.getenv("GOOGLE_API_KEY").strip()
genai.configure(api_key = apikeyfromenv)

def llm(prompt:str) -> str:
    model = genai.GenerativeModel("gemini-2.5-pro")
    chat = model.start_chat(history =[])
    response = chat.send_message(prompt, generation_config=genai.GenerationConfig(
        max_output_tokens=3072, temperature=0.7, top_p=0.8, top_k=64
    ))
    return response.text 