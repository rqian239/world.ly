import dash
import dash_bootstrap_components as dbc
from dash import html


def footer():

    ftr = html.Div(
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    html.P([
                        html.Span("Your Company or Name ", className="mr-2"),
                        html.A("Privacy Policy", href="#", className="mr-2"),
                        html.A("Terms of Service", href="#", className="mr-2"),
                    ]),
                    className="text-center mt-4"
                )
            ),
            fluid=True,
        ),
        className="p-3 bg-light"
    )

    return ftr