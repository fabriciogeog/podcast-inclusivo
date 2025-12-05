# 📘 ERS — Especificação de Requisitos de Software
## Aplicativo de Busca Acessível de Notícias sobre Inclusão e Acessibilidade
Versão: 1.0  
Data: _preencher_  
Autores: _preencher_

---

# 1. Introdução

## 1.1. Propósito
Este documento especifica os requisitos do Aplicativo de Apoio à Produção de Podcast Inclusivo, destinado a usuários cegos ou com baixa visão que necessitam de uma ferramenta confiável, simples e acessível para encontrar notícias relevantes sobre inclusão e acessibilidade.

Serve como referência para:
- Desenvolvimento do app e backend;
- Comunicação entre desenvolvedores e partes interessadas;
- Validação e testes;
- Evolução do produto.

## 1.2. Escopo
O sistema consiste em:
- App Android com navegação totalmente acessível;
- API backend responsável pela busca, filtragem e entrega de notícias a partir de fontes confiáveis;
- Recursos suplementares como filtros, favoritos, compartilhamento e resumos.

## 1.3. Definições e Abreviações
| Termo | Definição |
|-------|-----------|
| API | Interface de Programação de Aplicações |
| RSS | Formato de distribuição de notícias |
| MVP | Versão Mínima Viável |
| TTS | Text-to-Speech |
| TalkBack | Leitor de tela do Android |
| ERS | Especificação de Requisitos de Software |

## 1.4. Referências
- Questionário respondido pelo usuário-alvo.
- WCAG 2.1 — Diretrizes de Acessibilidade.
- Google Accessibility Guidelines.

---

# 2. Descrição Geral

## 2.1. Perspectiva do Produto
O sistema será composto por dois módulos:

### Frontend Mobile
- App Android desenvolvido inicialmente em Kivy (Python).
- Interface minimalista compatível com TalkBack.

### Backend
- API FastAPI.
- Hospedagem gratuita via Deta Space ou Render.

## 2.2. Funcionalidades de Alto Nível
- Pesquisa de notícias (texto e voz);
- Exibição acessível de resultados;
- Abertura, salvamento e compartilhamento de notícias;
- Resumos (texto e áudio) em versões futuras;
- Filtros temáticos.

## 2.3. Perfil do Usuário
- Cego total, 28 anos;
- Usuário avançado de tecnologia;
- Usa TalkBack intensivamente;
- Pesquisa notícias diariamente;
- Produz podcast semanal.

## 2.4. Restrições
- Backend deve operar com custo zero;
- Interface deve cumprir requisitos de acessibilidade;
- Dados móveis limitados.

## 2.5. Dependências
- Internet;
- Fontes externas de notícias;
- TTS do Android (futuro).

---

# 3. Requisitos Funcionais

## 3.1. Essenciais (MVP)
- RF01 — Pesquisa por texto.
- RF02 — Consulta a fontes confiáveis.
- RF03 — Exibição acessível em lista.
- RF04 — Abertura das notícias.
- RF05 — Salvar notícias.
- RF06 — Compartilhar notícias.
- RF07 — Total compatibilidade com TalkBack.
- RF08 — Filtros temáticos.

## 3.2. Intermediários
- RF09 — Pesquisa por voz.
- RF10 — Resumo automático em texto.
- RF11 — Histórico.

## 3.3. Avançados
- RF12 — Resumo em áudio.
- RF13 — Preferências inteligentes.
- RF14 — Notificações diárias.

---

# 4. Requisitos Não Funcionais

## 4.1. Usabilidade
- Interface minimalista e linear;
- Operável 100% sem visão.

## 4.2. Desempenho
- Resposta ideal < 3s;
- Baixo consumo de dados.

## 4.3. Segurança
- Armazenamento local seguro;
- Não coleta dados sensíveis.

## 4.4. Portabilidade
- Android 8+.

## 4.5. Confiabilidade
- Backend estável em plataforma gratuita.

---

# 5. Requisitos de Acessibilidade
- RA01 — Labels obrigatórios.
- RA02 — Navegação sequencial.
- RA03 — Interface sem ruído visual.
- RA04 — Leitura automática do foco.
- RA05 — Feedback sonoro.
- RA06 — Operação completa via leitor de tela.

---

# 6. Priorização (MoSCoW)
| Categoria | Requisitos |
|----------|------------|
| Must | RF01–RF08, RNF01–RNF08, RA01–RA06 |
| Should | RF09–RF11 |
| Could | RF12–RF14 |

---

# 7. Fluxo Básico do MVP
1. Tela inicial: busca por texto/voz.  
2. Resultados: abrir, salvar, compartilhar.  
3. Favoritos: lista de itens salvos.  
4. Configurações: temas e acessibilidade.

---

# 8. Considerações Finais
Este documento fornece os requisitos completos necessários para o desenvolvimento, validação e evolução do aplicativo.