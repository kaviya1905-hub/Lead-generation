import requests
import json
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://ollama:11434")

def generate_icp_questions(persona, industry):
    prompt = f"""
You are an ICP (Ideal Customer Profile) generator AI.

Generate exactly **7 short business related questions**
to understand a customer with persona = "{persona}"
working in industry = "{industry}".

Return output strictly as a numbered list like:

1. question one?
2. question two?
3. ...
7. question seven?
    """
    payload = {
    "model": "llama3.2:1b",
    "prompt": prompt,
    "stream": False,
    "num_predict": 200
}

    
    try:
        response = requests.post(f"{OLLAMA_HOST}/api/generate", json=payload, timeout=180)
        text = response.json().get("response", "").strip()

        questions = [q.strip() for q in text.split("\n") if q.strip() and q[0].isdigit()]
        return questions if len(questions) >= 3 else ["Question generation failed"]

    except Exception as e:
        print("LLM Error:", e)
        return ["Question generation failed"]
