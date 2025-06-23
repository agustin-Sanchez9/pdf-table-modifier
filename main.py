import pdfplumber
import pandas as pd

dataframes = []
encabezado_fijo = ["Producto", "Pack/Caja", "Precio Uni.", "Precio Caja"]

with pdfplumber.open(r"C:\Users\agust\Desktop\mayorista-bebidas\lista\lista-modificar.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()

        for table in tables:
            if table and len(table) > 1:
                filas = table[1:]
                df = pd.DataFrame(filas, columns=encabezado_fijo)
                dataframes.append(df)

df_total = pd.concat(dataframes, ignore_index=True)

df_total.to_csv(r"C:\Users\agust\Desktop\mayorista-bebidas\lista\lista-modificar.csv")

print("program has ended.")
