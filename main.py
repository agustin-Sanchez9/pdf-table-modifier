import pdfplumber
import pandas as pd

dataframes = []
encabezado_fijo = ["Producto", "Pack/Caja", "Precio Uni.", "Precio Caja"]

with pdfplumber.open("/home/ags/Descargas/LISTADO MAYORISTA JUNIO 25 (1).pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()

        for table in tables:
            if table and len(table) > 1:
                filas = table[1:]
                df = pd.DataFrame(filas, columns=encabezado_fijo)
                dataframes.append(df)

df_total = pd.concat(dataframes, ignore_index=True)

df_total.to_csv("/home/ags/Descargas/lista-mayorista.csv")

print("program has ended.")
