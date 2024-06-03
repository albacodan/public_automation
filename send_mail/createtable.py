import pandas as pd

# Leer los archivos CSV
csv_files = ['profesor_user_info.csv', 'alumno1_user_info.csv', 'alumno2_user_info.csv']
dfs = [pd.read_csv(file) for file in csv_files]

# Convertir cada DataFrame a una tabla HTML
html_tables = [df.to_html(index=False) for df in dfs]

# Unir las tablas HTML en una sola fila
html_combined = "<table><tr>"
for table in html_tables:
    html_combined += f"<td>{table}</td>"
html_combined += "</tr></table>"

# Guardar el HTML combinado en un archivo o imprimirlo
with open("combined_tables.html", "w") as file:
    file.write(html_combined)

# Alternativamente, puedes imprimir el HTML
print(html_combined)