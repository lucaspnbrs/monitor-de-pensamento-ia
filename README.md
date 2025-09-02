📊 Monitor de Percepção Pública sobre IA no Piauí


📖 Descrição

Este projeto é um painel de dados interativo desenvolvido em Streamlit que monitora a percepção pública sobre o tema "Inteligência Artificial" no estado do Piauí. O dashboard coleta notícias de fontes públicas através de um feed RSS, processa os textos para análise de sentimento e apresenta os resultados de forma visual e intuitiva.
Este trabalho foi desenvolvido como solução para o case técnico proposto, com foco em habilidades de coleta de dados, análise, visualização e boas práticas de desenvolvimento.


✨ Recursos

Dashboard Interativo: Interface amigável para explorar os dados.
Métricas em Tempo Real: KPIs que resumem o cenário atual (total de notícias, percentual de sentimentos).
Análise de Sentimento: Gráfico de pizza que mostra a distribuição dos sentimentos (Positivo, Negativo, Neutro).
Nuvem de Palavras: Visualização dos termos mais frequentes nos títulos das notícias.
Filtragem Dinâmica: Filtro na barra lateral para analisar notícias por sentimento.
Tabela de Detalhes: Expansor que exibe a tabela completa com os dados coletados e classificados.


🛠️ Estrutura do Projeto

O repositório está organizado da seguinte forma:

├── src
│   ├── utils
│   │   ├── coletadados.py        # Módulo para coleta e processamento dos dados
│   │   └── analise_sentimento.py # Módulo com a lógica da análise de sentimento
├── |--- app.py # Script principal da aplicação Streamlit
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Este arquivo
└── DECISIONS.md            # Documentação das decisões técnicas


🚀 Como Executar?

Para executar este projeto localmente, siga os passos abaixo:

1. Clone o repositório:

git clone [https://github.com/lucaspnbrs/monitor-de-pensamento-ia]
cd seu-repositorio


2. Crie e ative um ambiente virtual (recomendado):

python -m venv venv
# Windows
.\venv\Scripts\Activate
# macOS/Linux
source venv/bin/activate


3. Instale as dependências:

pip install -r requirements.txt


4. Execute a aplicação Streamlit:

streamlit run app.py
Acesse http://localhost:8501 no seu navegador para ver o dashboard.


📦 Entregável de Dados (CSV)

Conforme solicitado no case, o projeto pode gerar um arquivo noticias_processadas.csv. Para criá-lo, execute o script de coleta diretamente a partir da pasta raiz do projeto:

python src/utils/coletadados.py
O arquivo será salvo em src/data/.


🔧 Tecnologias Utilizadas

Linguagem: Python 3
Dashboard: Streamlit
Manipulação de Dados: Pandas
Visualização de Dados: Plotly Express, Matplotlib, WordCloud
Coleta de Dados: Requests, XML ElementTree
