import pandas as pd

def processar_arquivo(input_files, output_file):
    # Lista para armazenar os DataFrames de cada arquivo
    dfs = []
    for input_file in input_files:
        # Ler o arquivo CSV com ponto e vírgula como delimitador e encoding latin1
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)
    
    # Concatenar os DataFrames
    df_final = pd.concat(dfs, ignore_index=True)

    # Verificar se há duplicatas de nomes com informações de ônibus
    df_final['Duplicata_Onibus'] = df_final.duplicated(subset=['Nome', 'Nome da Mae', 'Nome do Pai'], keep=False) & (~df_final['Ônibus'].isnull())

    # Excluir pessoas sem informações na coluna "Ônibus" ou duplicatas com ônibus
    df_final = df_final[(df_final['Data da Dengue'].notnull()) | (~df_final['Ônibus'].isnull()) | df_final['Duplicata_Onibus']]

    # Excluir pessoas sem informações na coluna "Data da Dengue"
    df_final = df_final[df_final['Data da Dengue'].notnull()]

    # Selecionar colunas necessárias
    df_final = df_final[['Nome', 'Data de Nascimento', 'Data da Dengue']]

    # Escrever os dados processados no arquivo de saída
    df_final.to_excel(output_file, index=False)

# Lista de caminhos dos arquivos de entrada
input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Onibus3.csv"
]

# Caminho do arquivo de saída
output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 2.xlsx"

# Chamada da função para processar os arquivos
processar_arquivo(input_files, output_file)
