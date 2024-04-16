import pandas as pd

def processar_arquivo(input_file, output_file):
    # Ler o arquivo Excel de entrada
    df = pd.read_excel(input_file)

    # Identificar as pessoas que tiveram dengue
    pessoas_com_dengue = set(df[df['Data da Dengue'].notnull()]['Nome'])

    # Filtrar as pessoas com base nas condições especificadas e remover duplicatas
    df_filtrado = df[~((df['Data da Dengue'].notnull()) | ((df['Nome'].isin(pessoas_com_dengue)) &
                       (df['Nome da Mae'].isin(df[df['Data da Dengue'].notnull()]['Nome da Mae'])) &
                       (df['Nome do Pai'].isin(df[df['Data da Dengue'].notnull()]['Nome do Pai']))))]

    # Remover duplicatas com base nos critérios especificados
    df_filtrado = df_filtrado.drop_duplicates(subset=["Nome", "Nome da Mae", "Nome do Pai"])

    # Escrever os dados processados no arquivo de saída
    df_filtrado.to_excel(output_file, index=False)

# Caminho do arquivo de entrada
input_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Conjunto Universo.xlsx"

# Caminho do arquivo de saída
output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 1.xlsx"

# Chamada da função para processar o arquivo
processar_arquivo(input_file, output_file)
