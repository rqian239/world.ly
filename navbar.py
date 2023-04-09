import dash_bootstrap_components as dbc


def navbar():
    link_style = {'color': 'white'}
    nav_items = [
        ("Info Page", "/info_page"),
        ("About", "/about"),
        ("How to Use", "/how_to_use"),
        ("Start", "/app"),
    ]

    nav = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink(label, href=link_href, style=link_style)) for label, link_href in nav_items
        ],
        brand="world.ly",
        brand_href="/",
        sticky="top",
        color='primary',
        dark=True
    )

    return nav