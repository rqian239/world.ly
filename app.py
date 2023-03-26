import dash
from dash import dash_table
import cx_Oracle
from dash import dcc
from dash import html
import pandas as pd

app = dash.Dash(__name__)

conn = cx_Oracle.connect(user='williamsobczak', password='REBY7TpizLTdOp5dZHa9qJS0',
                         dsn=cx_Oracle.makedsn('oracle.cise.ufl.edu', '1521',
                                              sid='orcl'))
cursor = conn.cursor()
sql_query = 'SELECT * FROM country FETCH FIRST 20 ROWS ONLY'
cursor.execute(sql_query)
results = cursor.fetchall()

df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
cursor.close()
conn.close()

app.layout = html.Div([
    html.H1('world.ly'),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'width': '50%'},
        style_cell={'textAlign': 'left', 'fontSize': 14}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
