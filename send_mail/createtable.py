'''
import pandas as pd

# Leer los archivos CSV
csv_files = ['send_mail/profesor_user_info.csv', 'send_mail/alumno1_user_info.csv', 'send_mail/alumno2_user_info.csv']
dfs = [pd.read_csv(file) for file in csv_files]

# Convertir cada DataFrame a una tabla HTML
html_tables = [df.to_html(index=False) for df in dfs]

# Unir las tablas HTML en una sola fila
html_combined = "<table><tr>"
for table in html_tables:
    html_combined += f"<td>{table}</td>"
html_combined += "</tr></table>"

# Guardar el HTML combinado en un archivo o imprimirlo
with open("send_mail/combined_tables.html", "w") as file:
    file.write(html_combined)

# Alternativamente, puedes imprimir el HTML
print(html_combined)
'''


'''
import pandas as pd

# Leer los archivos CSV
csv_files = ['send_mail/profesor_user_info.csv', 'send_mail/alumno1_user_info.csv', 'send_mail/alumno2_user_info.csv']
dfs = [pd.read_csv(file) for file in csv_files]

# Definir el estilo CSS para las tablas
style = """
<style>
    table {
        border-collapse: collapse;
        border: 1px solid black;
        width: 100%;
    }
    th {
        background-color: lightblue;
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
    td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
</style>
"""

# Convertir cada DataFrame a una tabla HTML con estilos personalizados
html_tables = []
for df in dfs:
    # Renombrar las columnas
    df.columns = ['maquina', 'usuario', 'privilegio']
    # Convertir DataFrame a HTML y agregar estilo
    html_table = df.to_html(index=False, classes='styled-table')
    html_tables.append(html_table)

# Unir las tablas HTML en una sola fila
html_combined = f"{style}<table><tr>"
for table in html_tables:
    html_combined += f"<td>{table}</td>"
html_combined += "</tr></table>"

# Guardar el HTML combinado en un archivo
with open("send_mail/combined_tables.html", "w") as file:
    file.write(html_combined)

# Alternativamente, puedes imprimir el HTML
print(html_combined)
'''



import pandas as pd

# Leer los archivos CSV
csv_files = ['send_mail/profesor_user_info.csv', 'send_mail/alumno1_user_info.csv', 'send_mail/alumno2_user_info.csv']
dfs = [pd.read_csv(file) for file in csv_files]

# Definir el estilo en línea para las tablas
table_style = "border-collapse: collapse; width: 100%;"
th_style = "background-color: lightblue; border: 1px solid black; padding: 8px; text-align: left;"
td_style = "border: 1px solid black; padding: 8px; text-align: left;"

# Convertir cada DataFrame a una tabla HTML con estilos en línea
html_tables = []
for df in dfs:
    # Renombrar las columnas
    df.columns = ['maquina', 'usuario', 'privilegio']
    # Convertir DataFrame a HTML
    html_table = df.to_html(index=False)
    # Agregar estilos en línea
    html_table = html_table.replace('<table border="1" class="dataframe">',
                                    f'<table style="{table_style}">')
    html_table = html_table.replace('<th>', f'<th style="{th_style}">')
    html_table = html_table.replace('<td>', f'<td style="{td_style}">')
    html_tables.append(html_table)

# Unir las tablas HTML en una sola fila
html_combined = "<table><tr>"
for table in html_tables:
    html_combined += f"<td>{table}</td>"
html_combined += "</tr></table>"

# Guardar el HTML combinado en un archivo
with open("send_mail/combined_tables.html", "w") as file:
    file.write(html_combined)

# Alternativamente, puedes imprimir el HTML
print(html_combined)
