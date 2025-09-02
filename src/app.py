import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from utils.coletadados import obter_dados_processados

st.set_page_config(
    page_title="Monitor de IA no Piauí",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Monitor de Percepção Pública sobre IA no Piauí")
st.subheader("Um painel interativo para acompanhar notícias, sentimentos e tendências sobre Inteligência Artificial no Piauí.")

st.divider()

@st.cache_data
def carregar_dados():
    df = obter_dados_processados()
    if 'data_publicacao' in df.columns:
        df['data'] = pd.to_datetime(df['data_publicacao'], errors='coerce')
    else:
        df['data'] = pd.to_datetime('today')  # fallback
    return df

df = carregar_dados()

if df.empty:
    st.error("❌ Não foi possível coletar notícias. Verifique a conexão ou a fonte de dados.")
    st.stop()

st.sidebar.header("🔍 Filtro por Sentimento")
sentimento = st.sidebar.selectbox(
    "Selecione o sentimento:",
    options=["Todos", "Positivo", "Negativo", "Neutro"],
    index=0
)

if sentimento != "Todos":
    df_filtrado = df[df['sentimento'] == sentimento]
else:
    df_filtrado = df

if df_filtrado.empty:
    st.warning("⚠️ Nenhum dado encontrado para o filtro selecionado.")
    st.stop()
else:
    st.success(f"✅ {len(df_filtrado)} notícias encontradas!")


st.markdown("## 📈 Métricas Gerais")
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)

total_noticias = df_filtrado.shape[0]
perc_positivo = (df_filtrado[df_filtrado['sentimento'] == 'Positivo'].shape[0] / total_noticias * 100) if total_noticias > 0 else 0
perc_negativo = (df_filtrado[df_filtrado['sentimento'] == 'Negativo'].shape[0] / total_noticias * 100) if total_noticias > 0 else 0

col_kpi1.metric(label="📰 Total de Notícias", value=f"{total_noticias}")
col_kpi2.metric(label="👍 Positivas", value=f"{perc_positivo:.1f}%")
col_kpi3.metric(label="👎 Negativas", value=f"{perc_negativo:.1f}%")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribuição de Sentimentos")
    contagem_sentimentos = df_filtrado['sentimento'].value_counts().reset_index()
    contagem_sentimentos.columns = ['sentimento', 'total']

    fig_pizza = px.pie(
        contagem_sentimentos,
        names='sentimento',
        values='total',
        color='sentimento',
        color_discrete_map={
            'Positivo': '#4CAF50',
            'Negativo': '#F44336',
            'Neutro': '#607D8B'
        }
    )
    fig_pizza.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pizza, use_container_width=True)

with col2:
    st.subheader("☁️ Termos Mais Frequentes")
    texto_completo = " ".join(titulo for titulo in df_filtrado['titulo'])

    stopwords_pt = set(STOPWORDS)
    stopwords_pt.update([
        "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com",
        "não", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como",
        "mas", "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "Piauí", "Teresina"
    ])

    if texto_completo.strip():
        wordcloud = WordCloud(
            background_color="white", width=800, height=400,
            colormap='viridis', stopwords=stopwords_pt
        ).generate(texto_completo)

        fig_nuvem, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig_nuvem, use_container_width=True)
    else:
        st.info("ℹ️ Não há texto suficiente para gerar a nuvem de palavras.")

st.divider()


with st.expander("📑 Ver detalhes das notícias"):
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1
    df_filtrado.index.name = "Nº"
    st.dataframe(df_filtrado)

st.caption("""
---
🔍 **Interprete com Cuidado:** A análise de sentimento é um ponto de partida automatizado. Para conclusões aprofundadas, considere o contexto de cada notícia, pois o sistema pode não detectar nuances como sarcasmo e ironia.
""")
