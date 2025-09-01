PALAVRAS_POSITIVAS = [
    "avanço", "crescimento", "inovação", "benefício", "melhora", "eficiência",
    "lança", "investe", "desenvolve", "fortalece", "positivo", "sucesso", "oportunidade"
]

PALAVRAS_NEGATIVAS = [
    "risco", "problema", "perigo", "crise", "ameaça", "desafio", "dificuldade",
    "falha", "crítica", "negativo", "preocupação", "impacto negativo"
]

def analisar_sentimento(texto):
    """
    Analisa o sentimento de um texto com base em listas de palavras.
    Retorna 'Positivo', 'Negativo' ou 'Neutro'.
    """
    texto_limpo = texto.lower()
    
    score_positivo = 0
    for palavra in PALAVRAS_POSITIVAS:
        if palavra in texto_limpo:
            score_positivo += 1
            
    score_negativo = 0
    for palavra in PALAVRAS_NEGATIVAS:
        if palavra in texto_limpo:
            score_negativo += 1
            
    if score_positivo > score_negativo:
        return "Positivo"
    elif score_negativo > score_positivo:
        return "Negativo"
    else:
        return "Neutro"