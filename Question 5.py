import pandas as pd

def processar_arquivo(input_files, output_file):
    dfs = []
    for input_file in input_files:
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)
    
    for df in dfs:
        df['Data de Nascimento'] = df['Data de Nascimento'].astype(object)
    
    df_final = pd.merge(dfs[0], dfs[1], on=['Nome', 'Nome da Mae', 'Nome do Pai', 'Data de Nascimento', 'ID'], how='outer')
    
    df_duplicatas = df_final[df_final.duplicated(subset=['Nome', 'Nome da Mae', 'Nome do Pai'], keep=False)]
    
    df_final = df_final[~df_final.index.isin(df_duplicatas.index)]

    df_final = df_final.dropna(subset=['Ônibus'])

    df_final = df_final[['Nome', 'Data de Nascimento', 'ID', 'Ônibus']]
    
    df_final.to_excel(output_file, index=False)

input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Onibus3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Alunos3.csv"
]

output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 5.xlsx"

processar_arquivo(input_files, output_file)
