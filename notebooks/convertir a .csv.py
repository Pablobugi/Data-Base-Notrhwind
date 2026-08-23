import sqlite3
import pandas as pd

conn = sqlite3.connect("data/Northwind.db")

# Exportar cada tabla a CSV
tablas = ['Customers', 'Orders', 'OrderDetails', 'Products', 'Categories', 'Employees', 'Shippers', 'Suppliers']

for tabla in tablas:
    df = pd.read_sql_query(f"SELECT * FROM {tabla}", conn)
    df.to_csv(f'C:\\Users\\pabue\\OneDrive\\Documentos\\Aprendiendo SQL\\{tabla}.csv', index=False)
    print(f"✅ {tabla} exportada")

conn.close()