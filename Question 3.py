import pandas as pd

def processar_arquivo(input_files, output_file):
    dfs = []
    for input_file in input_files:
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)
    
    df_final = pd.concat(dfs, ignore_index=True)
    
    df_final['Duplicata_Dengue'] = df_final.duplicated(subset=['Nome', 'Nome da Mae', 'Nome do Pai'], keep=False) & (~df_final['Data da Dengue'].isnull())
    
    df_final = df_final[~((~df_final['Data da Dengue'].isnull()) | df_final['Ônibus'].isnull() | df_final['Duplicata_Dengue'])]
    
    df_final = df_final[['Nome', 'Data de Nascimento', 'Ônibus']]
    
    df_final.to_excel(output_file, index=False)

input_files = [
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Base de Onibus3.csv"
]

output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Planilhas\\Questão 3.xlsx"

processar_arquivo(input_files, output_file)
