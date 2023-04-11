import dash
import dash_bootstrap_components as dbc

from dash import html

from components.navbar import navbar
from components.footer import footer

nav = navbar()
ftr = footer()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("About"),
                        # home page blurb
                        html.P(
                            """\
                            This is the About Page content."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4 body-flex-wrapper",
)


def about_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout