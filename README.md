# 📊 Monitor de Percepção Pública sobre IA no Piauí

Este projeto tem como objetivo **monitorar notícias sobre Inteligência Artificial no Piauí** em fontes públicas (Google News RSS), aplicando uma **análise de sentimento baseada em regras** e exibindo os resultados em um **dashboard interativo com Streamlit**.

---

## 🚀 Funcionalidades
- 🔎 **Coleta automática** de notícias via RSS do Google News.  
- 🧹 **Limpeza de texto** para remover HTML e caracteres indesejados.  
- 🙂 **Classificação de sentimento** (Positivo, Negativo ou Neutro) baseada em palavras-chave.  
- 📊 **Dashboard em Streamlit** com:
  - Gráfico de pizza → distribuição de sentimentos.  
  - Nuvem de palavras → termos mais frequentes.  
  - Tabela interativa → detalhes das notícias.  
- ⚠️ **Aviso de limitação** no rodapé (transparência na análise).  

---

## 📂 Estrutura do Projeto
├── src/
| |-- utils/
|    |-- analise_sentimento.py # Função de análise de sentimento
|    |-- coletadados.py # Coleta + pré-processamento
|--- app.py
|--- venv/
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── DECISIONS.md # Documentação das decisões técnicas
