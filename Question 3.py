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
    
    # Verificar se há duplicatas de nomes com informações de dengue
    df_final['Duplicata_Dengue'] = df_final.duplicated(subset=['Nome', 'Nome da Mae', 'Nome do Pai'], keep=False) & (~df_final['Data da Dengue'].isnull())
    
    # Excluir pessoas com informações de dengue, sem informações na coluna "Ônibus" ou duplicatas com dengue
    df_final = df_final[~((~df_final['Data da Dengue'].isnull()) | df_final['Ônibus'].isnull() | df_final['Duplicata_Dengue'])]
    
    # Selecionar colunas necessárias
    df_final = df_final[['Nome', 'Data de Nascimento', 'Ônibus']]
    
    # Escrever os dados processados no arquivo de saída
    df_final.to_excel(output_file, index=False)

# Lista de caminhos dos arquivos de entrada
input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Onibus3.csv"
]

# Caminho do arquivo de saída
output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 3.xlsx"

# Chamada da função para processar os arquivos
processar_arquivo(input_files, output_file)
