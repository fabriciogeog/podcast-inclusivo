from typing import List, Dict

def filter_entries(entries: List[Dict], query: str):
    """
    Filtra entries pelo conjunto de palavras da query (AND).
    Se query vazia, retorna entries inteiras.
    """
    q = (query or "").strip().lower()
    if not q:
        return entries
    keywords = [w for w in q.split() if w]
    results = []
    for e in entries:
        text = (e.get("title", "") + " " + e.get("summary", "")).lower()
        if all(k in text for k in keywords):
            results.append(e)
    return results
