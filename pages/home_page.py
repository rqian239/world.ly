from modules import *
from navbar import navbar

nav = navbar()


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("world.ly"),
                        # home page blurb
                        html.P(
                            """\
                            Welcome to world.ly!
                            This application allows to give you complex insights into global demographic data: world.ly
                            lets you study notable trends for countries and metrics you choose. Explore and compare metrics from
                            various sectors like health, education, and economy."""
                        )
                    ],
                    md=4,
                )
            ]
        )
    ],
    className="mt-4",
)


def home_page():
    layout = html.Div([nav, body])
    return layout