from modules import *
from navbar import navbar

nav = navbar()

body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Main Application HERE"),
                        # home page blurb
                        html.P(
                            """\
                            This is where we put all the data and graphs and stuff."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4",
)


def app_page():
    layout = html.Div([nav, body])
    return layout