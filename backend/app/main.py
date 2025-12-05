from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import news as news_router

app = FastAPI(
    title="API - Acessibilidade Notícias",
    description="Backend para busca de notícias acessíveis",
    version="1.0.0"
)

# CORS: permitir acesso do app mobile (ajuste em produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# incluir router de notícias
app.include_router(news_router.router)

@app.get("/status")
def status():
    return {"status": "online", "message": "API operante", "version": "1.0.0"}

