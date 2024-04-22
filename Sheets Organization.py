import pandas as pd

def processar_arquivos(input_files, output_file):
    # Lista para armazenar os DataFrames de cada arquivo
    dfs = []
    
    # Iteração sobre os arquivos de entrada
    for input_file in input_files:
        # Ler o arquivo CSV com ponto e vírgula como delimitador e encoding latin1
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)

    # Concatenar os DataFrames em um único DataFrame
    df_final = pd.concat(dfs, ignore_index=True)

    # Escrever os dados processados em um arquivo XLSX sem índices
    df_final.to_excel(output_file, index=False)

# Lista de caminhos dos arquivos de entrada
input_files = [
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Alunos3.csv",
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Onibus3.csv"
]

# Caminho do arquivo de saída
output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Questão 1.xlsx"

# Chamada da função para processar os arquivos
processar_arquivos(input_files, output_file)
