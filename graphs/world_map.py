import dash
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np

import plotly.graph_objs as go

from dash import html, dcc
from dash import dash_table
from components.navbar import navbar
from components.footer import footer

import components.dropdown as dropdown
import ids
import functions
import data

query_string_complex_globe_1 = 'WITH countries_contributing_to_75_percent_of_global_CO2_emissions AS ( SELECT year, code, entity, CO2_emissions_metric_tons     FROM     (     SELECT cf1.year, entity, code, CO2_emissions_metric_tons,  SUM(CO2_emissions_metric_tons) over(PARTITION BY year ORDER BY CO2_emissions_metric_tons DESC) running_sum     FROM CarbonFootprint cf1     WHERE entity != \'World\'     ORDER BY CO2_emissions_metric_tons DESC     ) cf1 WHERE running_sum < (SELECT CO2_emissions_metric_tons*0.9 FROM CarbonFootprint WHERE entity = \'World\' AND year = cf1.year) )  SELECT year, code, entity country, (Electricity_from_coal_in_TWh + Electricity_fom_gas_in_TWh + Electricity_from_nuclear_in_TWh + Electricity_from_hydro_in_TWh + Electricity_from_solar_in_TWh + Electricity_from_oil_in_TWh + Electricity_from_wind_in_TWh) total_electricity_production_in_TWh, CO2_emissions_metric_tons,     Case         WHEN Electricity_from_coal_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_coal_in_TWh > Electricity_from_wind_in_TWh THEN \'Coal\'         WHEN Electricity_fom_gas_in_TWh > Electricity_from_coal_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_solar_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_oil_in_TWh AND Electricity_fom_gas_in_TWh > Electricity_from_wind_in_TWh THEN \'Gas\'         WHEN Electricity_from_nuclear_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_nuclear_in_TWh > Electricity_from_wind_in_TWh THEN \'Nuclear\'         WHEN Electricity_from_hydro_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_hydro_in_TWh > Electricity_from_wind_in_TWh THEN \'Hydroelectric\'         WHEN Electricity_from_solar_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_solar_in_TWh > Electricity_from_wind_in_TWh THEN \'Solar\'         WHEN Electricity_from_oil_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_coal_in_TWh AND Electricity_from_oil_in_TWh > Electricity_from_wind_in_TWh THEN \'Oil\'         WHEN Electricity_from_wind_in_TWh > Electricity_fom_gas_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_nuclear_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_hydro_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_solar_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_oil_in_TWh AND Electricity_from_wind_in_TWh > Electricity_from_coal_in_TWh THEN \'Wind\'         END AS primary_electricity_source FROM (     SELECT e.year, c.CO2_emissions_metric_tons, c.code, c.entity, Electricity_from_coal_in_TWh, Electricity_fom_gas_in_TWh, Electricity_from_nuclear_in_TWh, Electricity_from_hydro_in_TWh, Electricity_from_solar_in_TWh, Electricity_from_oil_in_TWh, Electricity_from_wind_in_TWh, Electricity_from_bioenergy_in_TWh, Other_renewables_excluding_bioenergy_in_TWh     FROM countries_contributing_to_75_percent_of_global_CO2_emissions c, ElectricityProductionBySource e     WHERE e.code = c.code AND e.year = c.year ) ORDER BY year'
query_string_complex_globe_2 = 'SELECT l.code, l.entity, l.year, life_expectancy_at_birth, life_expectancy_percentile, public_health_expenditure_percentage_of_gdp-avg_public_health_expenditure_percentage_of_gdp difference_in_public_health_expenditure_percentage_of_gdp_to_years_average FROM (     SELECT *     FROM     (     SELECT code, year, entity, life_expectancy_at_birth,  ROUND(PERCENT_RANK() OVER(PARTITION BY YEAR ORDER BY life_expectancy_at_birth),2) life_expectancy_percentile     FROM LifeExpectancy     ORDER BY year     )     WHERE life_expectancy_percentile > 0.9 ) l LEFT OUTER JOIN (SELECT code,year, public_health_expenditure_percentage_of_gdp, AVG(public_health_expenditure_percentage_of_gdp) OVER(PARTITION BY YEAR ORDER BY public_health_expenditure_percentage_of_gdp) avg_public_health_expenditure_percentage_of_gdp FROM PublicHealthGovExpenditureShareGDP) h ON (l.code = h.code AND l.year = h.year)   '
query_string_complex_globe_3 = 'SELECT RealGdpPerCapita.code, RealGdpPerCapita.entity, RealGdpPerCapita.year, GDP_per_capita, GDP_per_capita_percent_growth, Energy_consumption_per_capita_in_kwh - avg_Energy_consumption_per_capita_in_kwh difference_in_per_capita_energy_use_in_kwh_compared_to_the_yearly_average FROM (     SELECT RealGdpPerCapita.code, RealGdpPerCapita.entity, RealGdpPerCapita.year, GDP_per_capita, GDP_per_capita_percent_growth     FROM     (         SELECT RealGdpPerCapita.code, RealGdpPerCapita.entity, RealGdpPerCapita.year, GDP_per_capita, AVG(GDP_per_capita) OVER(PARTITION BY continent, RealGdpPerCapita.year ORDER BY GDP_per_capita) max_real_gdp_per_capita_per_continent_and_year         FROM RealGdpPerCapita, Continents         WHERE RealGdpPerCapita.code = Continents.code     ) RealGdpPerCapita     LEFT OUTER JOIN GdpPerCapitaGrowth ON (GdpPerCapitaGrowth.code = RealGdpPerCapita.code AND GdpPerCapitaGrowth.year = RealGdpPerCapita.year)     WHERE GDP_per_capita = max_real_gdp_per_capita_per_continent_and_year ) RealGDPPerCapita LEFT OUTER JOIN (SELECT EnergyPerPerson.code, EnergyPerPerson.year, Energy_consumption_per_capita_in_kwh, AVG(Energy_consumption_per_capita_in_kwh) OVER(PARTITION BY EnergyPerPerson.YEAR, continent ORDER BY Energy_consumption_per_capita_in_kwh) avg_Energy_consumption_per_capita_in_kwh FROM EnergyPerPerson, Continents WHERE Continents.code = EnergyPerPerson.code AND Continents.year = EnergyPerPerson.year) EnergyPerPerson  ON RealGDPPerCapita.code = EnergyPerPerson.code AND RealGDPPerCapita.year = EnergyPerPerson.year ORDER BY YEAR '
query_string_complex_globe_4 = 'SELECT GNI.entity, GNI.code, GNI.year, (GNI_index_contribution + life_expectancy_index_contribution + primary_education_index_contribution + secondary_education_index_contribution + tertiary_education_index_contribution) HDI_index FROM     (     SELECT entity, code, year, (gross_national_income_per_capita/max_GNI_per_capita)/3 GNI_index_contribution     FROM         (         SELECT entity, code, year, gross_national_income_per_capita, MAX(gross_national_income_per_capita) OVER(PARTITION BY YEAR) max_GNI_per_capita         FROM GrossNationalIncomePerCapita         )     ) GNI,               (        SELECT entity, code, year, (life_expectancy_at_birth/max_life_expectancy)/3 life_expectancy_index_contribution     FROM         (         SELECT entity, code, year, life_expectancy_at_birth, MAX(life_expectancy_at_birth) OVER(PARTITION BY YEAR) max_life_expectancy         FROM LifeExpectancy         )     ) LifeExpectancy,                  (             SELECT entity, code, year, (primary_education_gross_enrollment_percent/max_primary_education_gross_enrollment_percent)/9 primary_education_index_contribution     FROM         (         SELECT entity, code, year, primary_education_gross_enrollment_percent, MAX(primary_education_gross_enrollment_percent) OVER(PARTITION BY YEAR) max_primary_education_gross_enrollment_percent         FROM GrossEnrollmentRatioInPrimaryEducation         )     ) primary,                  (         SELECT entity, code, year, (lower_secondary_education_completion_rate/max_lower_secondary_education_completion_rate)/9 secondary_education_index_contribution     FROM         (         SELECT entity, code, year, lower_secondary_education_completion_rate, MAX(lower_secondary_education_completion_rate) OVER(PARTITION BY YEAR) max_lower_secondary_education_completion_rate         FROM CompletionRateOfLowerSecondaryEducation         )     ) secondary,              (     SELECT entity, code, year, (percentage_with_tertiary_education/max_percentage_with_tertiary_education)/9 tertiary_education_index_contribution     FROM         (         SELECT entity, code, year, percentage_with_tertiary_education, MAX(percentage_with_tertiary_education) OVER(PARTITION BY YEAR) max_percentage_with_tertiary_education         FROM ShareOfThePopulationWithCompletedTertiaryEducation         )     ) tertiary WHERE GNI.code = LifeExpectancy.code AND GNI.year = LifeExpectancy.year AND GNI.code = primary.code AND GNI.year = primary.year AND GNI.code = secondary.code AND GNI.year = secondary.year AND GNI.code = tertiary.code AND GNI.year = tertiary.year ORDER BY year, HDI_index '

# Query the database and store the results in a dataframe
df_complex_1 = functions.query_db(query_string_complex_globe_1)
df_complex_2 = functions.query_db(query_string_complex_globe_2)
df_complex_3 = functions.query_db(query_string_complex_globe_3)
df_complex_4 = functions.query_db(query_string_complex_globe_4)

# Get unique country code combinations from complex 2 dataframe
unique_country_code_combos_2 = df_complex_2.groupby(['ENTITY', 'CODE']).size().reset_index().drop(0, axis=1)
unique_country_code_combos_2.drop_duplicates()
# print(unique_country_code_combos_2.head(30))

# Append the new rows to the dataframe in a loop to fill in the missing years in complex_2
for index, row in unique_country_code_combos_2.iterrows():
    entity = row['ENTITY']
    code = row['CODE']
    new_row = {'YEAR': 1753, 'CODE': code, 'ENTITY': entity, 'LIFE_EXPECTANCY_AT_BIRTH': None, 'LIFE_EXPECTANCY_PERCENTILE': None, 'DIFFERENCE_IN_PUBLIC_HEALTH_EXPENDITURE_PERCENTAGE_OF_GDP_TO_YEARS_AVERAGE': None}
    df_complex_2 = df_complex_2._append(new_row, ignore_index=True)

# Fill all the NaN values with 0
df_complex_2.fillna(0, inplace=True)
# df_complex_2 = df_complex_2.sort_values(by='YEAR')
# print(df_complex_2.head(50))

world_map_for_complex_1 = px.scatter_geo(df_complex_1, locations = 'CODE',
                    animation_frame='YEAR',
                    animation_group='COUNTRY',
                    color='COUNTRY',
                    hover_name='COUNTRY',
                    size='CO2_EMISSIONS_METRIC_TONS',
                    projection='orthographic',
                    hover_data={'COUNTRY': True, 'TOTAL_ELECTRICITY_PRODUCTION_IN_TWH': True, 'CO2_EMISSIONS_METRIC_TONS': True, 'CODE': False, 'PRIMARY_ELECTRICITY_SOURCE': True})
world_map_for_complex_1.update_layout(width=1500, height=1000)

complex_1_map_section = dbc.Container(
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
                                    figure=world_map_for_complex_1

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

world_map_for_complex_2 = px.scatter_geo(df_complex_2, locations = 'CODE',
                    animation_frame='YEAR',
                    animation_group='ENTITY',
                    color='ENTITY',
                    hover_name='ENTITY',
                    size='LIFE_EXPECTANCY_AT_BIRTH',
                    projection='orthographic',
                    hover_data={'ENTITY': True, 'LIFE_EXPECTANCY_AT_BIRTH': True, 'LIFE_EXPECTANCY_PERCENTILE': True, 'CODE': False, 'DIFFERENCE_IN_PUBLIC_HEALTH_EXPENDITURE_PERCENTAGE_OF_GDP_TO_YEARS_AVERAGE': True})
world_map_for_complex_2.update_layout(width=1500, height=1000)

complex_2_map_section = dbc.Container(
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
                    html.H1("Countries in the 90+ percentile for life expectancy for each year, along with the difference in their public health expenditure compared to the year's average"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=world_map_for_complex_2

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

world_map_for_complex_3 = px.scatter_geo(df_complex_3, locations = 'CODE',
                    animation_frame='YEAR',
                    animation_group='ENTITY',
                    color='ENTITY',
                    hover_name='ENTITY',
                    size='GDP_PER_CAPITA',
                    projection='orthographic',
                    hover_data={'ENTITY': True, 'GDP_PER_CAPITA': True, 'GDP_PER_CAPITA_PERCENT_GROWTH': True, 'CODE': False, 'DIFFERENCE_IN_PER_CAPITA_ENERGY_USE_IN_KWH_COMPARED_TO_THE_YEARLY_AVERAGE': True})
world_map_for_complex_3.update_layout(width=1500, height=1000)

complex_3_map_section = dbc.Container(
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
                    html.H1("Country with Highest GDP for each Continent along with Corresponding Percent Growth in GDP and Difference in Per Capita Energy Use Compared to the Content's Average"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=world_map_for_complex_3
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

world_map_for_complex_4 = px.scatter_geo(df_complex_4, locations = 'CODE',
                    animation_frame='YEAR',
                    animation_group='ENTITY',
                    color='ENTITY',
                    hover_name='ENTITY',
                    size='HDI_INDEX',
                    projection='orthographic',
                    hover_data={'ENTITY': True, 'HDI_INDEX': True, 'CODE': False})
world_map_for_complex_4.update_layout(width=1500, height=1000)

complex_4_map_section = dbc.Container(
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
                    html.H1("HDI"),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                        html.Div(
                            [
                                dcc.Graph(
                                    id='data-visualization',
                                    figure=world_map_for_complex_4
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

def world_map_render():
    return complex_1_map_section

def world_map_2_render():
    return complex_2_map_section

def world_map_3_render():
    return complex_3_map_section

def world_map_4_render():
    return complex_4_map_section