import pandas as pd
import sqlite3
from datetime import datetime

#Ler JSON.
df = pd.read_json('../../data/data.jsonl', lines=True)

#Fazer com que o pandas mostre todas as colunas.
pd.options.display.max_columns = None

#Adicionando a coluna _source com um valor fixo.
df['_source'] = "https://lista.mercadolivre.com.br/ps5"

#Adicionando a coluna _data_coleta com a data e horas atuais.
df['_data_coleta'] = datetime.now()

# Tratar colunas de texto.
text_cols = ['name', 'by']
for col in text_cols:
    df[col] = df[col].fillna('')

# Remover os parênteses das colunas 'reviews_amount'.
def remove_parenteses(string):
    if isinstance(string, str):
        return string.replace("(", "").replace(")", "")
    else:
        return string
    
# Aplicar a função ao campo desejado
df['reviews_amount'] = df['reviews_amount'].apply(remove_parenteses)

print(df.head())

# Conectar ao banco de dados SQLITE (ou criar um novo).
conn = sqlite3.connect('../../data/quotes.db')

# Salvar o dataframe no banco de dados SQLite.
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar a conexão com o bd.
conn.close()