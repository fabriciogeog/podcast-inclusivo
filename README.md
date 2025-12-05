A seguir está um **README.md profissional, completo, robusto e pronto para uso no GitHub**. Ele contempla:

✔ Badges
✔ Descrição executiva
✔ Objetivos
✔ Demonstração da arquitetura
✔ Instruções detalhadas de instalação e execução
✔ Estrutura do repositório
✔ Roadmap do projeto
✔ Contribuição
✔ Licença
✔ Acessibilidade
✔ Considerações técnicas sobre backend e app

O texto está formatado em Markdown e pode ser copiado diretamente para o arquivo `README.md` na raiz do repositório.

---

# 📰 Aplicativo Acessível de Notícias e Inclusão

**Versão:** 1.0
**Tecnologias:** Python, FastAPI, Kivy, RSS Parsing
**Plataforma alvo:** Android
**Objetivo:** Apoiar pessoas cegas e com baixa visão na coleta de notícias confiáveis sobre inclusão e acessibilidade.

---

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PYTHON-3.10+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/MOBILE-Kivy-6DA55F?style=for-the-badge&logo=kivy"/>
</p>

---

# 📌 Sobre o Projeto

Este projeto tem como propósito desenvolver um **aplicativo Android acessível** que permita a pessoas cegas ou com baixa visão buscar notícias de **fontes confiáveis**, especialmente relacionadas a:

* Inclusão
* Direitos das pessoas com deficiência
* Acessibilidade em serviços públicos e privados
* Tecnologia assistiva
* Participação social e esportiva
* Vida independente e cidadania

O aplicativo foi idealizado para ajudar um criador de conteúdo cego que produz podcasts semanais. Sua maior dificuldade: encontrar, com autonomia e rapidez, matérias relevantes e confiáveis na internet.

O projeto resolve essa barreira oferecendo:

✔ Busca unificada
✔ Conteúdo filtrado
✔ Interface acessível
✔ Resumo automático
✔ Baixíssimo uso de dados
✔ Autonomia ao usuário

---

# 🧩 Arquitetura do Sistema

```
                    ┌─────────────────────────┐
                    │       Usuário cego      │
                    │  App Android (Kivy)     │
                    └───────────┬────────────┘
                                │
                                ▼
                   ┌──────────────────────────┐
                   │  Backend - FastAPI       │
                   │  /status                 │
                   │  /news/search?q=...      │
                   └───────────┬──────────────┘
                               │
                               ▼
            ┌─────────────────────────────────────────┐
            │     Fontes RSS Confiáveis (G1, BBC, etc.)│
            └─────────────────────────────────────────┘
```

### Componentes principais:

| Componente       | Tecnologia                 | Responsabilidade                          |
| ---------------- | -------------------------- | ----------------------------------------- |
| **App Mobile**   | Kivy + Python              | Interface acessível, navegação, favoritos |
| **Backend API**  | FastAPI                    | Consulta RSS, filtragem e sumarização     |
| **Parser RSS**   | feedparser + BeautifulSoup | Normalização do conteúdo                  |
| **Cache**        | In-memory                  | Melhor desempenho                         |
| **Documentação** | Markdown                   | ERS, arquitetura e decisões               |

---

# 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI** (backend)
* **Kivy** (app Android)
* **RSS feedparser** (coleta)
* **BeautifulSoup4** (limpeza de HTML)
* **Uvicorn** (servidor dev)
* **Docker** (opcional para backend)

---

# 📁 Estrutura do Repositório

```
podcast-inclusivo/
├── app/
│   ├── main.py
│   ├── kv/
│   ├── screens/
│   └── requirements.txt
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── models/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── docs/
│   ├── ERS-Aplicativo-Acessivel.md
│   ├── arquitetura.md
│   ├── acessibilidade.md
│   └── roadmap.md
│
├── setup_envs.sh
├── setup_envs.ps1
├── .gitignore
└── README.md
```

---

# 🚀 Instalação e Execução

## 1) Backend (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

* Teste:

```
GET http://127.0.0.1:8000/status
GET http://127.0.0.1:8000/news/search?q=acessibilidade
```

---

## 2) Aplicativo Android (Kivy)

### Ambiente de desenvolvimento:

```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Gerar APK com Buildozer (Linux):

```bash
buildozer android debug
```

---

# 🔍 Endpoints Disponíveis

### `GET /status`

Retorna:

```json
{
  "status": "online",
  "message": "API operante",
  "version": "1.0.0"
}
```

### `GET /news/search?q={texto}`

Retorna:

* Título
* Link
* Resumo automático
* Fonte
* Data (quando disponível)

---

# ♿ Acessibilidade

O app foi desenhado seguindo diretrizes:

* Navegação linear
* Compatibilidade total com TalkBack
* Botões largos e claros
* Fluxo sem elementos escondidos
* Layout com foco em texto
* Ausência de gestos complexos

O backend também ajuda a acessibilidade:

* Remove HTML e publicidade
* Simplifica chamadas
* Suporta futuras integrações com TTS

---

# 🧭 Roadmap

### ✔ Fase 1 — MVP *(concluída)*

* Backend funcional
* Coleta RSS real
* Filtragem por palavra-chave
* Resumo automático
* App com teste de comunicação
* Estrutura geral do repositório

### 🔄 Fase 2 — App funcional

* Tela de busca
* Lista de resultados
* Favoritos persistentes
* Abertura de link no navegador
* Layout em `.kv`

### 🔜 Fase 3 — Recurso de voz (TTS/STT)

* Pesquisa por voz
* Leitura em voz das manchetes
* Resumos em áudio

### 🔮 Fase 4 — Inteligência e personalização

* Recomendação automática
* Classificação por categorias
* Ajuste inteligente de filtros
* Multiplataforma (Web / Desktop)

---

# 🤝 Como Contribuir

1. Faça um fork
2. Crie uma branch:

   ```bash
   git checkout -b feature/sua-feature
   ```
3. Commit suas mudanças:

   ```bash
   git commit -m "Descrição da mudança"
   ```
4. Push para o fork
5. Abra um Pull Request

---

# 📜 Licença

A definir (sugestão: MIT).

---

# 📩 Contato

Caso deseje discutir melhorias, ideias ou parcerias:

* **Fabricio** — Analista de Sistemas, instrutor de informática inclusiva
* **Tecnologias assistivas & inclusão digital**
