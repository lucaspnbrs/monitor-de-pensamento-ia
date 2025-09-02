📝 Documento de Decisões Técnicas

Este arquivo documenta as principais decisões de arquitetura e implementação tomadas durante o desenvolvimento do projeto "Monitor de Percepção Pública sobre IA no Piauí".

1. Abordagem de Regras para Análise de Sentimento
Pergunta: Por que você escolheu a abordagem de regras para análise de sentimento (em vez de um modelo de ML ou uma ferramenta externa)?

Resposta: A abordagem de análise de sentimento baseada em regras, implementada no módulo src/utils/analise_sentimento.py, foi escolhida por três motivos estratégicos:

Simplicidade e Rapidez na Implementação: Para um projeto com escopo definido e prazo limitado, um sistema de regras é significativamente mais rápido de desenvolver do que treinar e implantar um modelo de Machine Learning.

Transparência e Depuração (Explainability): O método é 100% transparente. Se uma notícia for classificada incorretamente, é fácil rastrear a palavra-chave que causou a classificação.

Baixo Custo Computacional: A análise por regras não exige poder computacional intensivo, tornando a aplicação leve, rápida e barata de hospedar.

1.1. Alternativa Considerada (Não utilizada): Inicialmente, foi considerada a ideia de utilizar uma assistente via n8n para criar e analisar o sentimento das notícias. Embora essa abordagem oferecesse uma boa automação, optou-se pela solução interna (via regras) para manter a simplicidade da arquitetura e evitar uma dependência externa adicional no contexto deste projeto.

2. Tratamento de Erros e Falta de Notícias
Pergunta: Como você lidou com possíveis erros ou falta de notícias no feed RSS?

Resposta: O tratamento de erros foi considerado em duas frentes:

Na Coleta de Dados (src/utils/coletadados.py): A requisição HTTP é encapsulada em um bloco try...except para lidar com falhas de conexão. Além disso, uma estrutura match-case trata diferentes códigos de status da resposta HTTP, sempre retornando um DataFrame vazio em caso de falha.

Na Interface do Usuário (app.py): O dashboard verifica se o DataFrame de dados está vazio (if df.empty:). Se estiver, exibe uma mensagem de erro clara para o usuário (st.error) em vez de tentar renderizar os gráficos.

3. Uso de Inteligência Artificial no Desenvolvimento
Em conformidade com o princípio de transparência, este projeto utilizou um modelo de linguagem de IA (Google Gemini) como uma ferramenta de assistência ("copiloto"), auxiliando nas seguintes tarefas:

Refatoração e Melhoria de Código: Sugestão de melhorias em trechos de código existentes.

Geração de Documentação: Geração das versões iniciais do README.md e da estrutura deste próprio documento, o DECISIONS.md, que foram então revisados e ajustados.

Toda a lógica central do projeto foi concebida e executada pelo desenvolvedor. A IA atuou como uma ferramenta de produtividade.
