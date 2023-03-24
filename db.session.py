##  Session where we will work with our database (db) system in our application.

#   Library to use PostgreSQL  with Python 2
import psycopg2

#####################################################
# Creating the necessary tables for the project db. #
#####################################################

#   Before connecting, you must create a new db from your terminal with postgresSQL installed.
#   Use UsefulDB.txt to understand how to do it. 

#   $ createdb -U my_user -h localhost bills_management_api

#   Connect to the PostgreSQL server using the peer connection.
conn_postgre = psycopg2.connect(
    database="bills_management_api",
    user="bftormin",
    host="/var/run/postgresql",
    port="5432",
)

#   Creating the necessary tables
cur = conn_postgre.cursor()
#   Client table
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        idade INT NOT NULL,
        email VARCHAR(35) UNIQUE
    );
   '''
)
#   Bills table
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS contas (
        id SERIAL PRIMARY KEY,
        conta_nome VARCHAR(30) NOT NULL,
        conta_valor FLOAT NOT NULL,
        mes INT NOT NULL,
        ano INT NOT NULL
    );
   '''
)
#   Income table
cur.execute(
    '''
    CREATE TABLE IF NOT EXISTS rendimentos (
        id SERIAL PRIMARY KEY,
        rendimento_nome VARCHAR(50) NOT NULL,
        rendimeno_valor FLOAT NOT NULL,
        mes INT NOT NULL,
        ano INT NOT NULL
    );
   '''
)

#   Veryfing if the created tables have the expected headers (column names)
#       Clients table
cur.execute('SELECT * FROM clientes')
column_names_clientes = [desc[0] for desc in cur.description]

for row in cur:
    print(row)

print("Nome das colunas da tabela de clientes", column_names_clientes)

#       Bills table
cur.execute('SELECT * FROM contas')
column_names_bills = [desc[0] for desc in cur.description]

for row in cur:
    print(row)

print("Nome das colunas da tabela de contas", column_names_bills)

#       Incomes table
cur.execute('SELECT * FROM rendimentos')
column_names_incomes = [desc[0] for desc in cur.description]

for row in cur:
    print(row)

print("Nome das colunas da tabela de rendimentos", column_names_incomes)

conn_postgre.commit()

#   Close the database connection
cur.close()
conn_postgre.close()