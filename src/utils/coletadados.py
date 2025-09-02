import requests
import pandas as pd
import xml.etree.ElementTree as ET
""" from utils.analise_sentimento import analisar_sentimento """
from .analise_sentimento import analisar_sentimento
import re

def limpar_descricao(html_text):
    """Remove tags HTML da descrição para deixar o texto limpo."""
    try:
        clean_text = re.sub(r'<.*?>', '', html_text)
        clean_text = re.sub(r'&nbsp;&nbsp;.*', '', clean_text)
        return clean_text.strip()
    except:
        return html_text
    
def coletar_dados():
    url = "https://news.google.com/rss/search?q=Inteligência+Artificial+Piauí&hl=pt-BR&gl=BR&ceid=BR:pt-419"

    try:
        response = requests.get(url)

        match response.status_code:
            case 200:
                print("Conexão bem-sucedida! Processando os dados...")
                root = ET.fromstring(response.content)
                
                noticias = []
                for item in root.findall('.//item')[:15]: 
                    titulo = item.find('title').text
                    link = item.find('link').text
                    descricao = item.find('description').text
                    
                    noticias.append({
                        'titulo': titulo,
                        'link': link,
                        'descricao': descricao
                    })
                
                df = pd.DataFrame(noticias)
                return df

            case 400:
                print("Erro na requisição Verifique a URL.")
                return pd.DataFrame()

            case 404:
                print("Fonte de dados não encontrada.")
                return pd.DataFrame()
            
            case _: 
                print(f"Erro inesperado ao acessar a URL. Status Code: {response.status_code}")
                return pd.DataFrame()

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return pd.DataFrame()


def obter_dados_processados():
    """Gerencia o processo: coleta e depois aplica a análise."""
    df = coletar_dados()
    if not df.empty:

        df['descricao'] = df['descricao'].apply(limpar_descricao)
        
        df['sentimento'] = df['titulo'].apply(analisar_sentimento)
    return df


if __name__ == "__main__":
    print("--- Iniciando teste do fluxo completo (Coleta e Processamento) ---")
    
    dados_finais = obter_dados_processados()

    if not dados_finais.empty:
        print("\nProduto final (dados processados) gerado com sucesso!")
        
        print(dados_finais.head()) 
        
        dados_finais.to_csv("src/data/noticias_processadas.csv", index=False)
        print("\nArquivo 'noticias_processadas.csv' salvo na pasta 'src/data'!")
    else:
        print("\nFalha ao coletar ou processar os dados.")