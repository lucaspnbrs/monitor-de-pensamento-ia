📝 Documento de Decisões Técnicas
Este arquivo documenta as principais decisões de arquitetura e implementação tomadas durante o desenvolvimento do projeto "Monitor de Percepção Pública sobre IA no Piauí".

1. Por que você escolheu a abordagem de regras para análise de sentimento (em vez de um modelo de ML)?
A abordagem de análise de sentimento baseada em regras, implementada no módulo src/utils/analise_sentimento.py, foi escolhida por três motivos estratégicos alinhados aos objetivos do case:

Simplicidade e Rapidez na Implementação: Para um projeto com escopo definido e prazo limitado, um sistema de regras é significativamente mais rápido de desenvolver do que treinar, avaliar e implantar um modelo de Machine Learning. A lógica é direta: verificar a presença de palavras-chave em listas pré-definidas (PALAVRAS_POSITIVAS e PALAVRAS_NEGATIVAS).

Transparência e Depuração (Explainability): O método é 100% transparente. Se uma notícia for classificada incorretamente, é fácil rastrear exatamente qual palavra-chave causou a classificação, permitindo ajustes rápidos e precisos nas listas. Modelos de ML, especialmente os mais complexos, podem operar como "caixas-pretas", dificultando a interpretação dos resultados.

Baixo Custo Computacional: A análise por regras não exige poder computacional intensivo para treinamento nem consome muita memória ou CPU durante a execução. Isso torna a aplicação leve, rápida e barata de hospedar, sendo ideal para um painel simples em Streamlit.

Embora menos sofisticada, essa abordagem foi a mais eficiente e adequada para entregar um produto funcional e transparente dentro do contexto do desafio.

2. Como você lidou com possíveis erros ou falta de notícias no feed RSS?
O tratamento de erros e a resiliência da aplicação foram considerados em duas frentes principais: na coleta dos dados e na interface do usuário.

Na Coleta de Dados (src/utils/coletadados.py):

Falhas de Conexão: A requisição HTTP à URL do Google Notícias foi encapsulada em um bloco try...except requests.exceptions.RequestException. Isso garante que, em caso de problemas de rede ou DNS, a aplicação não quebre e, em vez disso, retorne um DataFrame vazio, registrando o erro no console.

Erros de HTTP: Utilizei uma estrutura match-case para tratar diferentes códigos de status da resposta HTTP (response.status_code). O código lida explicitamente com o sucesso (200), erros comuns como "Bad Request" (400) e "Not Found" (404), além de um caso genérico (_) para qualquer outro erro inesperado, sempre retornando um DataFrame vazio para sinalizar a falha.

Na Interface do Usuário (app.py):

Ausência de Dados: O dashboard verifica se o DataFrame retornado pela função carregar_dados() está vazio (if df.empty:). Se estiver, em vez de tentar renderizar os gráficos (o que causaria um erro), ele exibe uma mensagem clara e amigável para o usuário com st.error("❌ Não foi possível coletar notícias...") e interrompe a execução com st.stop().

Filtros Sem Resultados: Da mesma forma, se o usuário aplicar um filtro que não retorna resultados, uma mensagem de aviso (st.warning("⚠️ Nenhum dado encontrado...")) é exibida, mantendo a experiência do usuário fluida.

Essa abordagem dupla garante que o sistema seja robusto a falhas externas e que o usuário final sempre receba um feedback claro sobre o estado da aplicação.

3. Uso de Inteligência Artificial no Desenvolvimento
Em conformidade com o princípio de transparência, este projeto utilizou um modelo de linguagem de IA (Google Gemini) como uma ferramenta de assistência ao desenvolvimento. O papel da IA foi de um "copiloto", auxiliando nas seguintes tarefas:

Refatoração e Melhoria de Código: A IA sugeriu melhorias em trechos de código existentes, como a otimização de mensagens de erro e a refinação da lógica de tratamento de dados vazios no app.py.

Debugging: A IA foi fundamental para diagnosticar e solucionar o ModuleNotFoundError que ocorreu ao tentar executar o script de coleta de dados de forma isolada, sugerindo a correção para importações relativas e o comando de execução de módulos.

Geração de Documentação: A IA gerou as versões iniciais dos arquivos README.md e deste DECISIONS.md com base nos scripts fornecidos, que foram então revisados e ajustados.

Melhoria de Textos (Copywriting): A IA ajudou a refinar o texto do aviso de limitações exibido no rodapé do dashboard, tornando-o mais claro e profissional.

É importante ressaltar que toda a lógica central do projeto, a estrutura dos scripts e as decisões de implementação foram concebidas e executadas pelo desenvolvedor. A IA atuou como uma ferramenta de produtividade e consultoria, e não como a autora principal do código.