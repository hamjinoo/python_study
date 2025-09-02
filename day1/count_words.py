import re
from collections import Counter
from pathlib import Path

def load_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No file: {path}")
    return p.read_text(encoding="utf-8", errors="ignore")

def normalize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9가-힣\s]", " ", text)  # 기호 제거
    text = re.sub(r"[은,는,이,가]", "", text)
    return [w for w in text.split() if len(w) >= 2]

def top_k(words: list[str], k: int = 10):
    return Counter(words).most_common(k)

if __name__ == "__main__":
    text = load_text("sample.txt")
    words = normalize(text)
    for word, cnt in top_k(words, 10):
        print(f"{word}\t{cnt}")