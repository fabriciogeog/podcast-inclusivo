from fastapi import APIRouter, Query
from typing import List
from pydantic import BaseModel
from ..models.news_item import NewsItem
from ..services import rss_client, filters, summarizer
from .. import config

router = APIRouter(prefix="/news", tags=["news"])

class SearchResponse(BaseModel):
    query: str
    results: List[NewsItem]

@router.get("/search", response_model=SearchResponse)
def search(q: str = Query('', description='Query de busca')):
    q = q.strip()
    all_results = []

    # iterar nas fontes configuradas
    for src in config.SOURCES:
        feed_url = src.get("rss")
        try:
            entries = rss_client.get_feeds_with_cache(feed_url, ttl=config.FEED_CACHE_TTL)
        except Exception:
            # se falhar uma fonte, continue com as demais
            continue

        filtered = filters.filter_entries(entries, q)
        for e in filtered:
            item = {
                "title": e.get("title"),
                "link": e.get("link"),
                "summary": summarizer.summarize_text(e.get("summary", ""), max_sentences=2),
                "published": e.get("published"),
                "source": src.get("name")
            }
            all_results.append(item)

    # Retorna lista (pode estar vazia)
    return {"query": q, "results": all_results}
