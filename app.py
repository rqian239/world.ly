import dash
from dash import dcc
from dash import html
import cx_Oracle

app = dash.Dash(__name__)

conn = cx_Oracle.connect(user='williamsobczak', password='REBY7TpizLTdOp5dZHa9qJS0', 
                         dsn=cx_Oracle.makedsn('oracle.cise.ufl.edu', '1521', 
                                              sid='orcl'))
cursor = conn.cursor()
sql_query = 'SELECT * FROM country FETCH FIRST 20 ROWS ONLY'
cursor.execute(sql_query)
results = cursor.fetchall()
cursor.close()
conn.close()

app.layout = html.Div([
    html.H1('Oracle SQL Server Connection'),
    html.Table([
        html.Thead(html.Tr([html.Th(col) for col in results[0]])),
        html.Tbody([
            html.Tr([
                html.Td(results[i][j]) for j in range(len(results[0]))
            ]) for i in range(len(results))
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
