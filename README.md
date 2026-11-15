## Installation and Usage

Requires Python and a running Ollama server exposed through Pinggy.
The server must have `embeddinggemma` and `qwen3:4b` installed.

```bash
python -m pip install -r requirements.txt
```

Create `.env` from `.env.example`, then set:

- `FIREBASE_API_KEY`: the Firebase project's Web API key.
- `OLLAMA_BASE_URL`: the current HTTPS Pinggy URL.

Enable Email/Password in Firebase Authentication.

```bash
python -m streamlit run app.py
```

## Known Limitations

- Answers are limited to the 20 guide entries.
- Top-3 retrieval may miss evidence for multi-part questions.
- Chat history is displayed but is not included in subsequent model prompts.
- Source-only answering is prompt-based and can still fail.
- Colab sessions and Pinggy tunnels may disconnect.
- Firebase token expiration is not automatically handled.

## AI Assistance

ChatGPT assisted with implementation guidance, debugging,
drafting the knowledge base, and preparing documentation
and the video outline.

## Demonstration Video

[Watch the demonstration](https://drive.google.com/file/d/18Ya2efguEIPEuygkyulf51SESQW8GIOi/view?usp=sharing)