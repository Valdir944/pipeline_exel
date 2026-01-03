📌 Descrição do Projeto

Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python, responsável por:

Extrair dados de vendas a partir de um arquivo Excel

Realizar transformações de dados (limpeza, cálculo de métricas e conversão de datas)

Carregar os dados em um banco MySQL local

Evitar duplicação de registros

Criar a tabela automaticamente caso não exista

Todo o ETL foi desenvolvido em um único arquivo, seguindo boas práticas de engenharia de dados.


├── etl_vendas_mysql.py
├── vendas.xlsx
└── README.md


pip install pandas openpyxl mysql-connector-python
