import re

def summarize_text(text: str, max_sentences: int = 2) -> str:
    """
    Summarizer simples: pega as primeiras max_sentences frases do texto.
    Limpeza básica por regex. Para versões futuras, trocar por modelo ML.
    """
    if not text:
        return ""
    sentences = re.split(r'(?<=[.!?])\\s+', text.strip())
    short = sentences[:max_sentences]
    return " ".join(short).strip()
