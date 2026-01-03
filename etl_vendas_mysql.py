import pandas as pd
import mysql.connector

MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'database': 'dw_vendas'
}

def extract_excel(file_path):
    df = pd.read_excel(file_path)
    print("✔ Dados extraídos do Excel")
    return df

def transform(df):
    # Remove registros inválidos
    df.dropna(inplace=True)

    # Cria métrica
    df['total_venda'] = df['quantidade'] * df['preco']

    # Converte data
    df['data_venda'] = pd.to_datetime(df['data_venda'])

    print("✔ Dados transformados")
    return df

def load_mysql(df):
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    # Cria tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id_venda INT PRIMARY KEY,
            produto VARCHAR(100),
            quantidade INT,
            preco DECIMAL(10,2),
            total_venda DECIMAL(10,2),
            data_venda DATE
        )
    """)

    # Insert com controle de duplicados
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO vendas (id_venda, produto, quantidade, preco, total_venda, data_venda)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                quantidade = VALUES(quantidade),
                preco = VALUES(preco),
                total_venda = VALUES(total_venda),
                data_venda = VALUES(data_venda)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    print("✔ Dados carregados no MySQL")

def run_etl():
    df = extract_excel('vendas.xlsx')
    df = transform(df)
    load_mysql(df)

run_etl()
