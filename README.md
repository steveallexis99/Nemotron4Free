# 🧠 Nemotron4Free

**Nemotron4Free** is a lightweight Python wrapper for the [NEMOTRON](https://nemotron.one) chat API. It allows you to send prompts and receive responses easily — with optional streaming support.

# ⭐ Feel Free to Star!

> ⚠️ No authentication or API key is required — the NEMOTRON API currently accepts any request, so `Nemotron4Free` works without login or account setup.

---

## 🚀 Installation

Install from PyPI:

```bash
pip install Nemotron
```
Or from source:

```bash
git clone https://github.com/Ramona-Flower/Nemotron4Free.git
cd Nemotron4Free
pip install .
```

# 💡 Usage
Basic Example
```python
from Nemotron import ask

response = ask("What's the capital of France?")
print(response)
```
Streaming Output
```python

from Nemotron import ask

response = ask("Tell me a sci-fi story.", stream=True)
```

With stream=True, the response is printed live as it's received — and also returned as a full string at the end.


# 🧠 Model Selection
You can choose which model to use by passing the model parameter:

```python

from Nemotron import ask

response = ask("Hello, who are you?", stream=True, model="claude3_5") # nemotron70b by default
```
## Available Models

| Model Name      | Description                | Streaming Supported |
|-----------------|----------------------------|---------------------|
| `nemotron70b`   | Default model (Used by default) | ✅ (`stream=True`)  |
| `claude3_5`     | Anthropic Claude 3.5       | ✅ (`stream=True`)  |
| `gpt4o`         | OpenAI GPT-4 Omni          | ✅ (`stream=True`)  |

## Claude 3.5 need premium account !

🔧 Parameters

| Parameter | Type   | Default | Description                                           | Info        |
|-----------|--------|---------|-------------------------------------------------------|------------------------|
| `content` | `str`  | —       | Your prompt or message to the AI.                    | Work with `nemotron70b`, `claude3_5`, `gpt4o` |
| `stream`  | `bool` | `False` | If `True`, prints the output live as it streams.      | Work with`nemotron70b`, `claude3_5`, `gpt4o` |
| `model`   | `str`  | `nemotron70b` | Specifies which model to use. Can be `nemotron70b`, `claude3_5`, or `gpt4o`. | Nothing to say |
| `name`    | `str`  | `"test"`       | Your name (optional). This is not required for the API but can be included for context. | `Useful for claude` |
| `email`   | `str`  | `"test@gmail.com"` | Your email (optional). This is not required for the API but can be included for context. | `Useful for claude` | 


🧪 Example Output
```
User: Tell me a joke
AI: Why don't scientists trust atoms?
    Because they make up everything.
```

---

# 🖼️ Image Generation

Nemotron4Free also supports **image generation**. To use this feature, you must provide a **valid email address**. Without a valid email, the API will reject the request.

### Example: Generate an Image
```python
from Nemotron import generate_image

img_url = generate_image(
    prompt="A futuristic city in the clouds",
    model="black-forest-labs/flux-1.1-pro",
    ratio="16:9",
    format_="jpg",
    email="your_valid_email@example.com"  # Replace with a valid email
)

if img_url:
    print(f"Image URL: {img_url}")
else:
    print("Failed to generate the image. Please check your email or other parameters.")
```

### Available Models for Image Generation

| Model Name                        | Description                     |
|-----------------------------------|---------------------------------|
| `black-forest-labs/flux-dev`      | Development version of Flux     |
| `black-forest-labs/flux-pro`      | Professional version of Flux    |
| `black-forest-labs/flux-schnell`  | Fast version of Flux            |
| `black-forest-labs/flux-1.1-pro`  | Flux 1.1 Pro version            |
| `black-forest-labs/flux-schnell`  | Another fast version of Flux    |

### Parameters for Image Generation

| Parameter | Type   | Default | Description                                           |
|-----------|--------|---------|-------------------------------------------------------|
| `prompt`  | `str`  | —       | The description of the image you want to generate.    |
| `model`   | `str`  | —       | The model to use for image generation.               |
| `ratio`   | `str`  | `1:1`   | Aspect ratio of the image (e.g., `16:9`, `4:3`).     |
| `format_` | `str`  | `png`   | The format of the image (e.g., `jpg`, `png`).        |
| `email`   | `str`  | —       | A valid email address required for image generation. |

- ratio : `1:1 - 16:9 - 9:16 - 3:2 - 2:3`
---

# ✨ Author
Created with ❤️ by Ramona-Flower

# 📄 License
Apache 2.0 License.
