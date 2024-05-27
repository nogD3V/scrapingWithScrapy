import streamlit as st
import pandas as pd
import sqlite3

#Conectar ao BD.
conn = sqlite3.connect('../data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Fechar a conexão com o banco de dados
conn.close()

st.markdown(
    """
    <h1 style='text-align: center;'>ML - PLAYSTATION 5</h1>
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

df_filtered = df[df['old_price_reais'] > 2499]

# Melhorar o layout com colunas para KPIs
col1, col2 = st.columns([1, 1])

# KPI 1: Número total de itens
with col1:
    st.subheader('Número Total de Itens')
    total_itens = df.shape[0]
    st.write(total_itens)

# Exibir a fonte dos dados na coluna ao lado
with col2:
    st.subheader('Fonte dos Dados')
    unique_sources = df['_source'].unique()
    for source in unique_sources:
        st.write(source)

# Adicionar espaço entre as seções
st.write("")
st.write("")

# Quais preços são comuns até a 10ª página
st.subheader('Preços mais encontrados até a 10ª página')
col = st.columns([1])[0]
top_10_pages_prices = df['old_price_reais'].value_counts().sort_values(ascending=False)
col.bar_chart(top_10_pages_prices)