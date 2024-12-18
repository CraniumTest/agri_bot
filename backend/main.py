from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.post("/ask_agri_bot/")
async def ask_agri_bot(query: str):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
