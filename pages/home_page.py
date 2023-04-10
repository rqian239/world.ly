import dash
import dash_bootstrap_components as dbc

from dash import html
from dash import dcc
from navbar import navbar


nav = navbar()


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("world.ly", style={"font-size": "60px"}),
                        html.Br(),
                        # home page blurb
                        html.P(
                            """\
                            Welcome to world.ly!
                            This application gives you the power to discover complex insights into global demographic data.\n world.ly
                            allows you to study notable trends for the countries and metrics you choose. Explore and compare metrics from
                            various sectors like health, education, and economy.""",
                            style={"font-size": "20px"},
                        ),
                        dcc.Link(html.Button("Get Started", id="get-started-button", className="btn btn-lg btn-primary", type="button"), href="/app"),
                        
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        html.Img(src="https://media.discordapp.net/attachments/1073377990844624919/1094767143884697610/earth.gif",
                                 width="80%",
                                 height="auto")
                    ],
                    md=6,
                ),
            ]
        )
    ],
    className="mt-4",
)


def home_page():
    layout = html.Div([nav, body])
    return layout