import dash
import dash_bootstrap_components as dbc

from dash import html, dcc
from dash import dash_table

from components.navbar import navbar
from components.footer import footer

from dash_iconify import DashIconify

import functions

nav = navbar()
ftr = footer()

# Total tuples query: should output > 250000
query_string = 'SELECT SUM(count) total_tuples FROM' \
                ' ( (SELECT COUNT(*) as count FROM LifeExpectancy) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PublicHealthGovExpenditureShareGDP) UNION ALL'\
                ' (SELECT COUNT(*) as count FROM AdultMortality) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MaternalMortality) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesFiveToNineInSoutheastAsianRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesFiveToNineInEuropeanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesFiveToNineInEasternMediterraneanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesFiveToNineInAmericasRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesFiveToNineInAfricanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInWesternPacificRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInSoutheastAsianRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInEuropeanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInEasternMediterraneanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInAmericasRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateAgesTenToFourteenInAfricanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ShareOfThePopulationWithCompletedTertiaryEducation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM GrossEnrollmentRatioInTertiaryEducation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM GrossEnrollmentRatioInPrimaryEducation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PrimaryCompletionRateOfRelevantAgeGroup) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM CompletionRateOfLowerSecondaryEducation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM GrossEnrollmentRatioInSecondaryEducation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM EnergyPerPerson) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ShareOfThePopulationWithAccessToElectricity) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM GasConsumptionByCountry) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ElectricityProductionBySource) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM FossilFuelPrimaryEnergy) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM AnnualNumberOfDeathsByCause) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ShareOfDeathsHomicides) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM LandArea) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ShareOfAdultsWhoAreOverweight) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM CrossCountryLiteracyRates) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PopulationAndDemography) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInWesternPacificRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInSoutheastAsianRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInEuropeanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInEasternMediterraneanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInAmericasRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM InfantMortalityRateInAfricanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInWesternPacificRegion) UNION ALL'\
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInEasternAsianRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInEuropeanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInEasternMediterraneanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInAmericasRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM MortalityRateChildrenUnderFiveInAfricanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInWesternPacificRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInSoutheastAsianRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInEuropeanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInEasternMediterraneanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInAmericasRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM NeonatalMortalityRateInAfricanRegion) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM RealGdpPerCapita) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM GdpPerCapitaGrowth) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM Continents) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM Internet_Users) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PrimarySchoolsWithInternetAccess) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM FoodAid) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ForestArea) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM AnnualDeforestation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM DrinkingWaterServiceCoverage) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM AvgYearlyPrecipitation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PopWithAccessToSafeDrinkingWater) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PopWithoutAccessToSafeDrinkingWater) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM ShareOfSmokers) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM AgriculturalIrrigation) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM PlasticPollution) UNION ALL' \
                ' (SELECT COUNT(*) as count FROM CarbonFootprint) )'


df = functions.query_db(query_string)
total_num_tuples = df['TOTAL_TUPLES'][0]


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.H1("Learn More About world.ly"),
                        html.Br(),
                        # home page blurb
                        html.P(
                            """\
                            world.ly is an easy-to-use web application that displays demographic data and allows you to study their trends.
                            """
                        ),
                        html.Br(),
                        html.Div(
                            children=[
                                dcc.Link(
                                    html.Button(
                                        "Get Started",
                                        id="get-started-button-about-page",
                                        className="btn btn-lg btn-primary get-started-button-about-page",
                                        type="button"
                                    ),
                                    href="/app"
                                )
                            ],
                            className="centered",
                        )
                    ],
                    className="centered",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3(f"Total number of data points (tuples) in our dataset: {total_num_tuples}"),
                    ]
                )
            ],
            className="centered",
            style={"margin-top": "100px"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Img(
                        src="assets\images\elements-silhouette-pixel-world-map-pixelated-vector.jpg",
                        width="100%",
                        height="auto",
                        className=""
                        )
                    ],
                    className="centered",
                ),
                dbc.Col(
                    [
                        html.H3("Metrics Used"),
                        html.Hr(),
                        html.P(
                            """\
                            Description of sectors chosen and corresponding metrics. Explain the relevance of metrics.
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 1 (Economy): Metrics in Sector 1 (GDP, average income, inflation, etc.)
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 2 (Health):  Metrics in Sector 2
                            """,
                        ),
                        html.Br(),
                        html.P(
                            """\
                            ◉   Sector 3 (Population): Metrics in Sector 3
                            """,
                        ),
                    ],
                ),
            ],
            style={"margin-top": "100px"},
        ),
        dbc.Row(
            [  
                dbc.Col(
                    [   html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H3("Data Visualization and Trend Analysis"),
                        html.Hr(),
                        html.P(
                            """\
                            Visualize trends with world.ly. Generate graphs, charts, and maps of your selected data. Description of the visualization tools here. Describe the kinds of charts and graphs.
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Line Graphs
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Tables
                            """,
                        ),
                        html.Br(), 
                        html.P(
                            """\
                            ◉   Maps
                            """,
                        ),
                    ],
                    className="left",
                ),
                dbc.Col(
                    [   
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        # Search for icons here: https://icon-sets.iconify.design/
                        # Replace the name of the icon in the icon="" field
                        DashIconify(
                            icon="mdi:graph-line",
                            width=100,
                            height=100,
                        ),

                        DashIconify(
                            icon="ph:globe-hemisphere-west-fill",
                            width=100,
                            height=100,
                        ),
                        
                        DashIconify(
                            icon="material-symbols:table-chart-outline",
                            width=100,
                            height=100,
                        ),
                    ],
                    className="centered",
                ),
            ],
        ),
    ],
    className="mt-4 body-flex-wrapper",
)


def about_page(app: dash.Dash):
    layout = html.Div([nav, body, ftr], className="make-footer-stick")
    return layout