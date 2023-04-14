import dash
from dash import html, dcc

attribute_table_dict = {

    'Life Expectancy at Birth': 'life_expectancy_at_birth',
    'Public Health Expenditure Percentage GDP': 'PublicHealthGovExpenditureShareGDP',
    'Male Mortality Rate': 'AdultMortality',
    'Female Mortality Rate': 'AdultMortality',
    'Number of Maternal Deaths': 'MaternalMortality',
    'GDP per Capita': 'RealGdpPerCapita',
    'GDP per Capita Percent Growth': 'GdpPerCapitaGrowth',
    'Gross National Income': 'GrossNationalIncomePerCapita',
    'Total Primary Completion Rate': 'PrimaryCompletionRateOfRelevantAgeGroup',
    'Gross Enrolment Ratio': 'GrossEnrollmentRatioInSecondaryEducation',
    'Percent Access To Electricity': 'ShareOfThePopulationWithAccessToElectricity',
    'Gas Consumption in TWh': 'GasConsumptionByCountry',
    'Homicide Deaths': 'ShareOfDeathsHomicides',
    'Land Area in square km': 'LandArea',
    'Literacy Rate': 'CrossCountryLiteracyRates',

}


def render(app: dash.Dash) -> html.Div:

    return html.Div(children=[])
