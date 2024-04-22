import pandas as pd

def processar_arquivo(input_files, output_file):
    # Lista para armazenar os DataFrames de cada arquivo
    dfs = []
    for input_file in input_files:
        # Ler o arquivo CSV com ponto e vírgula como delimitador e encoding latin1
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)
    
    # Fazer a junção (merge) dos DataFrames usando uma junção externa (outer join)
    df_final = pd.merge(dfs[0], dfs[1], on=['Nome', 'Nome da Mae', 'Nome do Pai', 'Data de Nascimento', 'ID'], how='outer')
    
    # Excluir linhas que não possuem informação na coluna 'Data da Dengue'
    df_final = df_final.dropna(subset=['Data da Dengue'])
    
    # Verificar e excluir linhas duplicadas
    df_final = df_final.drop_duplicates(subset=['Nome', 'Nome da Mae', 'Nome do Pai'])
    
    # Selecionar colunas necessárias
    df_final = df_final[['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue']]
    
    # Escrever os dados processados no arquivo de saída
    df_final.to_excel(output_file, index=False)

# Lista de caminhos dos arquivos de entrada
input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Alunos3.csv"
]

# Caminho do arquivo de saída
output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 4.xlsx"

# Chamada da função para processar os arquivos
processar_arquivo(input_files, output_file)
