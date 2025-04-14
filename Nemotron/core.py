import requests
import json
import random
import string

random_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
random_string = ''.join(random.choice(random_letter) for _ in range(10))

URL = "https://nemotron.one/api/chat"

HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://nemotron.one",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://nemotron.one/chat/nemotron70b",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}


def ask(content: str, stream=False, model="nemotron70b",name=None, email=None) -> str:
    
    if name is None:
        name = random_string
    if email is None:
        email = random_string+"@gmail.com"
    payload = {
        "content": content,
        "imageSrc": "",
        "model": model,
        "conversationId": "",
        "user": {
            "name": name,
            "email": email
        },
    }

    response = requests.post(URL, headers=HEADERS, data=json.dumps(payload), stream=True)

    full_output = ""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            text = chunk.decode("utf-8")
            if stream:
                print(text, end="", flush=True)
            full_output += text

    return full_output
