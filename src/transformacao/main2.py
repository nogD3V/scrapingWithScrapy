import pandas as pd

# Carregar o arquivo JSONL para um DataFrame
df = pd.read_json('../data/data.jsonl', lines=True)

# Função para remover parênteses de uma string
def remove_parenteses(string):
    if isinstance(string, str):
        return string.replace("(", "").replace(")", "")
    else:
        return string

# Aplicar a função ao campo desejado
df['reviews_amount'] = df['reviews_amount'].apply(remove_parenteses)

# Salvar o DataFrame modificado de volta para um arquivo JSONL
print(df.head())