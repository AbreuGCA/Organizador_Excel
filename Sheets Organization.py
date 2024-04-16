import pandas as pd

def processar_arquivos(input_files, output_file):
    # Lista para armazenar os DataFrames de cada arquivo
    dfs = []
    
    for input_file in input_files:
        # Ler o arquivo CSV com ponto e vírgula como delimitador
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)

    # Concatenar os DataFrames
    df_final = pd.concat(dfs, ignore_index=True)
    
    # Filtrar os dados para cidadãos de XPTO que frequentaram a escola e não tiveram dengue
    df_filtrado = df_final[(df_final['Cidadão'] == 'XPTO') & (df_final['Frequentou Escola'] == 'Sim') & (df_final['Teve Dengue'] == 'Não')]

    # Escrever os dados processados em um único arquivo XLSX
    df_filtrado.to_excel(output_file, index=False)

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
