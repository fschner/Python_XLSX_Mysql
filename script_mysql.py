import pandas as pd
import pymysql

# Configuração da conexão com o MySQL
host = 'hostname' 
user = 'user' 
password = 'senha' 
database = 'base' 

# Conectando ao MySQL
cnx = pymysql.connect(host=host, user=user, password=password, database=database)

# Nome da planilha XLSX e nome da tabela MySQL
planilha_xlsx = 'sua_planilha.xlsx'
tabela_mysql = 'sua_tabela'

# Ler a planilha XLSX
df = pd.read_excel(planilha_xlsx)

# Inserir dados na tabela MySQL
cursor = cnx.cursor()

for index, row in df.iterrows():
    usuario = row['usuario']
    nome = row['nome']
    grp = row['grp']

    # Execute a inserção de dados na tabela MySQL
    cursor.execute("INSERT INTO {} (usuario, nome, grp) VALUES (%s, %s, %s)".format(tabela_mysql), (usuario, nome, grp))

# Commit e fechar a conexão
cnx.commit()
cnx.close()

print("Dados inseridos com sucesso na tabela MySQL.")
