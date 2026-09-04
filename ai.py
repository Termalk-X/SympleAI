import requests

API_KEY = "API_KEY"

while True:
    prompt = input("Kamu: ")

    if prompt.lower() == "exit":
        break

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-oss-20b",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    print("AI:", data["choices"][0]["message"]["content"])