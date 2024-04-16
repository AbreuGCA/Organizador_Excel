import pandas as pd

# Função para ler o arquivo CSV e escrever em outro arquivo CSV
def processar_arquivo(input_file, output_file):
    # Ler o arquivo CSV com ponto e vírgula como delimitador
    df = pd.read_csv(input_file, delimiter=';')

    # Exibir as colunas presentes no DataFrame
    print("Colunas presentes no arquivo CSV:")
    print(df.columns)

    # Selecionar apenas as colunas desejadas: nome, data de nascimento e id
    df_final = df[['Nome', 'Data de Nascimento', 'ID']]

    # Escrever os dados processados em outro arquivo XLSX
    df_final.to_excel(output_file, index=False)

# Caminho do arquivo de entrada e saída
input_file = 'C:\\Users\\gabri\\Downloads\\Base de dados AV1\\Terceira geração de bases\\Equipe4\\Base de Alunos3.csv'
output_file = 'C:\\Users\\gabri\\OneDrive\\Documentos\\Questão 1.xlsx'

# Chamada da função para processar o arquivo
processar_arquivo(input_file, output_file)
