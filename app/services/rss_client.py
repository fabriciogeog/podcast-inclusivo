import feedparser
from bs4 import BeautifulSoup
from . import cache
import time

def _strip_html(text: str) -> str:
    if not text:
        return ""
    return BeautifulSoup(text, "html.parser").get_text(separator=" ", strip=True)

def fetch_feed(url: str):
    """
    Busca e normaliza as entradas do feed RSS.
    Retorna lista de dicts com title, summary, link, published.
    """
    d = feedparser.parse(url)
    entries = []
    for e in d.entries:
        title = _strip_html(e.get("title", ""))
        summary = _strip_html(e.get("summary", e.get("description", "")))
        link = e.get("link", "")
        published = e.get("published", e.get("updated", ""))
        entries.append({
            "title": title,
            "summary": summary,
            "link": link,
            "published": published
        })
    return entries

def get_feeds_with_cache(url: str, ttl: int = 300):
    """
    Cache simples por URL para reduzir número de requests.
    """
    cached = cache.get(url)
    now = time.time()
    if cached:
        timestamp, data = cached
        if now - timestamp < ttl:
            return data
    data = fetch_feed(url)
    cache.set(url, data)
    return data
