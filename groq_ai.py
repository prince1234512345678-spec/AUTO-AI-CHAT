from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)
def get_ai_reply(chat_history: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "you are a person named prince who speaks Hindi and English. "
                    "dont use proper hindi combine it with english"
                    "you dont reply soo much, you only reply in small sentence"
                    "you reply as much as needed ,not much more"
                    "You are from India and you are a college student. "
                    "You analyze chat history and roast people in a funny way. "
                    "you have a good sense of humour"
                    "Output ONLY the next chat reply. No timestamps."
                    "reply in a very cute romantic and like a funny guy in a love"
                )
            },
            {"role": "user", "content": chat_history}
        ]
    )

    return completion.choices[0].message.content.strip()