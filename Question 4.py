import pandas as pd

def processar_arquivo(input_files, output_file):
    dfs = []
    for input_file in input_files:
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)
    
    df_final = pd.merge(dfs[0], dfs[1], on=['Nome', 'Nome da Mae', 'Nome do Pai', 'Data de Nascimento', 'ID'], how='outer')
    
    df_final = df_final.dropna(subset=['Data da Dengue'])
    
    df_final = df_final.drop_duplicates(subset=['Nome', 'Nome da Mae', 'Nome do Pai'])
    
    df_final = df_final[['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue']]
    
    df_final.to_excel(output_file, index=False)

input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Alunos3.csv"
]

output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 4.xlsx"

processar_arquivo(input_files, output_file)
