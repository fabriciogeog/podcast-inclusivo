# config.py - configurações do backend

# Lista de fontes RSS confiáveis (personalize conforme necessário)
SOURCES = [
    {"name": "G1 - Brasil", "rss": "https://g1.globo.com/rss/g1/"},
    {"name": "BBC Brasil", "rss": "https://www.bbc.co.uk/portuguese/geral/rss.xml"},
    {"name": "Agência Brasil", "rss": "https://agenciabrasil.ebc.com.br/ultimas.xml"},
    {"name": "Folha - Últimas", "rss": "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml"}
]

# Tempo de cache em segundos (para reduzir requests em produção ajustar conforme necessário)
FEED_CACHE_TTL = 300  # 5 minutos
