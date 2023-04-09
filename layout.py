from dash import html

def create_layout(app: dash.Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1("app.title"),
            html.Hr()
        ]
    )