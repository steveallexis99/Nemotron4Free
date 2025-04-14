# 🧠 Nemotron4Free

**Nemotron4Free** is a lightweight Python wrapper for the [NEMOTRON](https://nemotron.one) chat API. It allows you to send prompts and receive responses easily — with optional streaming support.

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


🔧 Parameters

| Parameter | Type   | Default | Description                                           | Model Supported        |
|-----------|--------|---------|-------------------------------------------------------|------------------------|
| `content` | `str`  | —       | Your prompt or message to the AI.                    | `nemotron70b`, `claude3_5`, `gpt4o` |
| `stream`  | `bool` | `False` | If `True`, prints the output live as it streams.      | `nemotron70b`, `claude3_5`, `gpt4o` |
| `model`   | `str`  | `nemotron70b` | Specifies which model to use. Can be `nemotron70b`, `claude3_5`, or `gpt4o`. | `nemotron70b`, `claude3_5`, `gpt4o` |

🧪 Example Output
```
User: Tell me a joke
AI: Why don't scientists trust atoms?
    Because they make up everything.
```

✨ Author
Created with ❤️ by Ramona-Flower

# ⭐ Feel Free to Star!

# 📄 License
Apache 2.0 License.
