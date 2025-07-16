import pandas as pd

def processar_arquivos(input_files, output_file):
    dfs = []
    
    for input_file in input_files:
        df = pd.read_csv(input_file, delimiter=';', encoding='latin1')
        dfs.append(df)

    df_final = pd.concat(dfs, ignore_index=True)

    df_final.to_excel(output_file, index=False)

input_files = [
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Alunos3.csv",
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Dengue3.csv",
    "C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Onibus3.csv"
]

output_file = "C:\\Users\\gabri\\OneDrive\\Documentos\\Questão 1.xlsx"

processar_arquivos(input_files, output_file)
