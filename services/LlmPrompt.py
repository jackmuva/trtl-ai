import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def promptLlm(scrapedText: list[str]):
    messages=[
        {
            "role": "system",
            "content": "You will be provided with text from pages of my website delimited by triple quotes and a question. "
                       "Your task is to come up with ideas for topics to write email newsletter series on using the provided "
                       "text."
        },
    ]
    for text in scrapedText:
        messages.append({
            "role": "user",
            "content": f'"""{text}"""',
        })
    messages.append({
        "role": "user",
        "content": "What are your top 5 ideas?"
    })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )
    print(chat_completion)
    return chat_completion