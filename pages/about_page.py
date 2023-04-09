import dash
import dash_bootstrap_components as dbc

from dash import html

from navbar import navbar

nav = navbar()

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
    className="mt-4",
)


def about_page():
    layout = html.Div([nav, body])
    return layout