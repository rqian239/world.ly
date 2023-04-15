import dash
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

import plotly.graph_objs as go

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

import components.dropdown as dropdown
import ids
import functions
import data
import graphs.scatter_plot as scatter_plot

nav = navbar()
ftr = footer()

#query_string = '(SELECT year, life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM ( SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM ( SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC ) ) WHERE YEAR > 1950 AND YEAR < 2020 ) ORDER BY life_expectancy_change_compared_to_last_5_years FETCH FIRST 5 ROWS ONLY) UNION ALL (SELECT year, life_expectancy_change_compared_to_last_5_years FROM (SELECT year, ROUND(life_expectancy - past_5_yrs_avg_life_expectancy,4) life_expectancy_change_compared_to_last_5_years FROM (SELECT year, life_expectancy, AVG(life_expectancy) OVER(ORDER BY year DESC ROWS BETWEEN 1 FOLLOWING AND 5 FOLLOWING) past_5_yrs_avg_life_expectancy FROM (SELECT year, AVG(life_expectancy_at_birth) life_expectancy FROM LifeExpectancy GROUP BY year ORDER BY YEAR DESC)) WHERE YEAR > 1950 AND YEAR < 2020) ORDER BY life_expectancy_change_compared_to_last_5_years DESC FETCH FIRST 5 ROWS ONLY)'
query_string = 'SELECT education.code, education.entity, education.year, education.percentage_with_tertiary_education percentage_with_tertiary_education, income.gross_national_income_per_capita per_capita_income FROM ShareOfThePopulationWithCompletedTertiaryEducation education, GrossNationalIncomePerCapita income WHERE education.code = income.code AND education.year = income.year AND education.year = \'2010\' '
query_string_for_animation = 'SELECT education.code, education.entity, education.year, education.percentage_with_tertiary_education percentage_with_tertiary_education, income.gross_national_income_per_capita per_capita_income FROM ShareOfThePopulationWithCompletedTertiaryEducation education, GrossNationalIncomePerCapita income WHERE education.code = income.code AND education.year = income.year'
#query_string_for_map_2_metrics = 'WITH countries_contributing_to_75_percent_of_global_CO2_emissions AS ( SELECT code, entity, CO2_emissions_metric_tons FROM ( SELECT entity, code, CO2_emissions_metric_tons,  SUM(CO2_emissions_metric_tons) over(ORDER BY CO2_emissions_metric_tons DESC) running_sum FROM CarbonFootprint WHERE year = 2020 AND entity != \'World\' ORDER BY CO2_emissions_metric_tons DESC ) WHERE running_sum < (SELECT CO2_emissions_metric_tons*0.75 FROM CarbonFootprint WHERE entity = \'World\' AND year = \'2020\') )  SELECT entity country, code, (Electricity_from_coal_in_TWh + Electricity_fom_gas_in_TWh + Electricity_from_nuclear_in_TWh + Electricity_from_hydro_in_TWh +Electricity_from_solar_in_TWh + Electricity_from_oil_in_TWh + Electricity_from_wind_in_TWh + Electricity_from_bioenergy_in_TWh) total_electricity_production_in_TWh, CO2_emissions_metric_tons,     Case         WHEN Electricity_from_coal_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Coal\'         WHEN Electricity_fom_gas_in_TWh > Electricity_from_coal_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_solar_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_oil_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_wind_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Gas\'         WHEN Electricity_from_nuclear_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Nuclear\'         WHEN Electricity_from_hydro_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Hydroelectric\'         WHEN Electricity_from_solar_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Solar\'         WHEN Electricity_from_oil_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Oil\'         WHEN Electricity_from_wind_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_bioenergy_in_TWh THEN \'Wind\'         WHEN Electricity_from_bioenergy_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_wind_in_TWh AND Electricity_from_bioenergy_in_TWh > Electricity_from_coal_in_TWh THEN \'Bioenergy\'         END AS primary_electricity_source FROM (     SELECT c.CO2_emissions_metric_tons, c.code, c.entity, Electricity_from_coal_in_TWh, Electricity_fom_gas_in_TWh, Electricity_from_nuclear_in_TWh, Electricity_from_hydro_in_TWh, Electricity_from_solar_in_TWh, Electricity_from_oil_in_TWh, Electricity_from_wind_in_TWh, Electricity_from_bioenergy_in_TWh, Other_renewables_excluding_bioenergy_in_TWh     FROM countries_contributing_to_75_percent_of_global_CO2_emissions c, ElectricityProductionBySource e     WHERE e.year = 2020 AND e.code = c.code )'
query_string_for_map_2_metrics = 'WITH countries_contributing_to_75_percent_of_global_CO2_emissions AS ( SELECT year, code, entity, CO2_emissions_metric_tons     FROM     (     SELECT cf1.year, entity, code, CO2_emissions_metric_tons,  SUM(CO2_emissions_metric_tons) over(PARTITION BY year ORDER BY CO2_emissions_metric_tons DESC) running_sum     FROM CarbonFootprint cf1     WHERE entity != \'World\'     ORDER BY CO2_emissions_metric_tons DESC     ) cf1 WHERE running_sum < (SELECT CO2_emissions_metric_tons*0.9 FROM CarbonFootprint WHERE entity = \'World\' AND year = cf1.year) )  SELECT year, code, entity country, (Electricity_from_coal_in_TWh + Electricity_fom_gas_in_TWh + Electricity_from_nuclear_in_TWh + Electricity_from_hydro_in_TWh + Electricity_from_solar_in_TWh + Electricity_from_oil_in_TWh + Electricity_from_wind_in_TWh) total_electricity_production_in_TWh, CO2_emissions_metric_tons,     Case         WHEN Electricity_from_coal_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_wind_in_TWh THEN \'Coal\'         WHEN Electricity_fom_gas_in_TWh > Electricity_from_coal_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_solar_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_oil_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_wind_in_TWh THEN \'Gas\'         WHEN Electricity_from_nuclear_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_wind_in_TWh THEN \'Nuclear\'         WHEN Electricity_from_hydro_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_wind_in_TWh THEN \'Hydroelectric\'         WHEN Electricity_from_solar_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_wind_in_TWh THEN \'Solar\'         WHEN Electricity_from_oil_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_wind_in_TWh THEN \'Oil\'         WHEN Electricity_from_wind_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_coal_in_TWh THEN \'Wind\'         END AS primary_electricity_source FROM (     SELECT e.year, c.CO2_emissions_metric_tons, c.code, c.entity, Electricity_from_coal_in_TWh, Electricity_fom_gas_in_TWh, Electricity_from_nuclear_in_TWh, Electricity_from_hydro_in_TWh, Electricity_from_solar_in_TWh, Electricity_from_oil_in_TWh, Electricity_from_wind_in_TWh, Electricity_from_bioenergy_in_TWh, Other_renewables_excluding_bioenergy_in_TWh     FROM countries_contributing_to_75_percent_of_global_CO2_emissions c, ElectricityProductionBySource e     WHERE e.code = c.code AND e.year = c.year ) ORDER BY year'

df = functions.query_db(query_string)
df_animation = functions.query_db(query_string_for_animation)
df_map = functions.query_db(query_string_for_map_2_metrics)

def app_page(app: dash.Dash):

    # body = dbc.Container(
    #     [
    #         dbc.Row(
    #             [
    #                 dbc.Col(
    #                     [
    #                         html.H1("Main Application"),
    #                         html.P(
    #                             """\
    #                             This is where we put the data visualizations."""
    #                         ),
    #                         html.Div([
    #                             dash_table.DataTable(
    #                                 id='table',
    #                                 columns=[{"name": i, "id": i} for i in df.columns],
    #                                 data=df.to_dict('records'),
    #                                 style_table={'width': '50%'},
    #                                 style_cell={'textAlign': 'left', 'fontSize': 14}
    #                             )
    #                         ]),
    #                     ],
    #                     md=4,
    #                 )
    #             ]
    #         )
    #     ],
    #     className="mt-4 body-flex-wrapper",
    # )

    # fig = px.line(df, x="YEAR", y="BOTH_SEXES_MORTALITY_RATE", title='Adult Mortality Rate', color = 'COUNTRY')
    # fig.update_xaxes(title_text=(reformat_data_label("YEAR")))
    # fig.update_yaxes(title_text=(reformat_data_label("BOTH_SEXES_MORTALITY_RATE")))

    scatter_plot_section = scatter_plot.render()

    world_map_fig = px.scatter_geo(df, locations = 'CODE',
                        color='ENTITY',
                        hover_name='ENTITY',
                        size='PERCENTAGE_WITH_TERTIARY_EDUCATION',
                        projection='orthographic')
    world_map_fig.update_layout(width=1500, height=1000)

    world_map_section = dbc.Container(
        [
        # Add dropdown and buttons here
            dbc.Row(
                [
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    dcc.Graph(
                                        id='data-visualization',
                                        figure=world_map_fig
                                    ),
                                ],
                                # className="center-content"
                            )
                        ]
                    )
                ]
            ),
        ]
    )

    # #possibly add log_x=True, size_max=55,range_x=[100, 100000], range_y=[25, 90] to end of px.scatter
    # # ^^^for resizing graph and limit the bounds on x and y axis
    # animated_plot = px.scatter(df_animation, x='PERCENTAGE_WITH_TERTIARY_EDUCATION', y='PER_CAPITA_INCOME',
    #                             animation_frame='YEAR',
    #                             animation_group='ENTITY',
    #                             hover_name='ENTITY', color='ENTITY')
    # animated_plot.update_xaxes(title_text=(functions.reformat_data_label("PERCENTAGE_WITH_TERTIARY_EDUCATION")))
    # animated_plot.update_yaxes(title_text=(functions.reformat_data_label("PER_CAPITA_INCOME")))
    # animated_plot.update_layout(width=1500, height=1000)
    # animated_plot_section = dbc.Container(
    #     [
    #     # Add dropdown and buttons here
    #         dbc.Row(
    #             [
                
    #             ]
    #         ),
    #         dbc.Row(
    #             [
    #                 dbc.Col(
    #                     [
    #                         html.Div(
    #                             [
    #                                 dcc.Graph(
    #                                     id='data-visualization',
    #                                     figure=animated_plot
    #                                 ),
    #                             ],
    #                             # className="center-content"
    #                         )
    #                     ]
    #                 )
    #             ]
    #         ),
    #     ]
    # )

    world_map_fig_2_metrics = px.scatter_geo(df_map, locations = 'CODE',
                        animation_frame='YEAR',
                        animation_group='COUNTRY',
                        color='COUNTRY',
                        hover_name='COUNTRY',
                        size='CO2_EMISSIONS_METRIC_TONS',
                        projection='orthographic',
                        hover_data={'COUNTRY': True, 'TOTAL_ELECTRICITY_PRODUCTION_IN_TWH': True, 'CO2_EMISSIONS_METRIC_TONS': True, 'CODE': False, 'PRIMARY_ELECTRICITY_SOURCE': True})
    world_map_fig_2_metrics.update_layout(width=1500, height=1000)

    world_map_2_metrics_section = dbc.Container(
        [
        # Add dropdown and buttons here
            dbc.Row(
                [
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.H1("Countries Constituting the Majority of Global Greenhouse Gas Emissions along with their Total Electricity Generation Quantity (TWh) and Primary Source"),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                            html.Div(
                                [
                                    dcc.Graph(
                                        id='data-visualization',
                                        figure=world_map_fig_2_metrics

                                    ),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                ],
                                # className="center-content"
                            )
                        ],
                        className="centered"
                    )
                ]
            ),
        ]
    )
    layout = html.Div([nav, scatter_plot_section, world_map_section, world_map_2_metrics_section, ftr], className="make-footer-stick")
    return layout