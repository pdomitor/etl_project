#!pip install ydata-profiling
#!pip install --upgrade typing_extensions

import sqlite3
import pandas as pd
from ydata_profiling import ProfileReport

# Conectar y cargar tabla
conn = sqlite3.connect("C:/Users/pdominguez/Desktop/ESCRITORIO/etl_project/data/product_sales.db")
df_sales = pd.read_sql("SELECT * FROM sales", conn)
df_product = pd.read_sql("SELECT * FROM product", conn)

# Crear el perfil
sales_profile = ProfileReport(df_sales, title="Sales Table Profiling Report", explorative=True)
product_profile = ProfileReport(df_product, title="Product Table Profiling Report", explorative=True)

# Exportar como HTML
sales_profile.to_file("utils/sales_profiling_report.html")
product_profile.to_file("utils/product_profiling_report.html")

conn.close()
