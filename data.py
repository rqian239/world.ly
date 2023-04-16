attribute_table_dict = {
    # ATTRIBUTE TO TABLE
    'Life Expectancy At Birth' : 'LifeExpectancy',
    'Public Health Expenditure Percentage of GDP' : 'PublicHealthGovExpenditureShareGDP',
    # 'Male Mortality Rate' : 'AdultMortality',
    # 'Female Mortality Rate' : 'AdultMortality',
    'GDP per Capita' : 'RealGdpPerCapita',
    'GDP per Capita Percent Growth' : 'GdpPerCapitaGrowth',
    'Gross National Income Per Capita' : 'GrossNationalIncomePerCapita',
    'Secondary Education Gross Enrollment Percent' : 'GrossEnrollmentRatioInSecondaryEducation',
    'Percent Access to Electricity' : 'ShareOfThePopulationWithAccessToElectricity',
    'Gas Consumption in TWh' : 'GasConsumptionByCountry',
    'Land Area in Square km' : 'LandArea',
    'Literacy Rate' : 'CrossCountryLiteracyRates',
    'Percentage with Tertiary Education' : 'ShareOfThePopulationWithCompletedTertiaryEducation',
    'Tertiary Education Gross Enrollment Percent' : 'GrossEnrollmentRatioInTertiaryEducation',
    'Primary Education Gross Enrollment Percent' : 'GrossEnrollmentRatioInPrimaryEducation',
    'Lower Secondary Education Completion Rate' : 'CompletionRateOfLowerSecondaryEducation',
    'Energy Consumption Per Capita in KWh' : 'EnergyPerPerson',
    'Total Fossil Fuel Use in TWh' : 'FossilFuelPrimaryEnergy',
    'Percent of Adults Overweight' : 'ShareOfAdultsWhoAreOverweight',
    'Number of Internet Users' : 'Internet_Users',
    'Proportion of Primary Schools with Internet' : 'PrimarySchoolsWithInternetAccess',
    'Food Aid Received in 2016 million USD' : 'FoodAid',
    'Forest Area Square km' : 'ForestArea',
    'Deforestation Square km' : 'AnnualDeforestation',
    'Average Precipitation in mm' : 'AvgYearlyPrecipitation',
    'Number with Access to Drinking Water' : 'PopWithAccessToSafeDrinkingWater',
    'Number Without Access to Safe Drinking Water' : 'PopWithoutAccessToSafeDrinkingWater',
    'Percent of Population that Smokes' : 'ShareOfSmokers',
    'Percent of Agricultural Land Irrigated' : 'AgriculturalIrrigation',
    'Plastic Pollution kg' : 'PlasticPollution',
    'CO2 Emissions Metric Tons' : 'CarbonFootprint',
    'Number with Post Secondary Education' : 'PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In',
    'Number with Secondary Education' : 'PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In',
    'Number with Primary Education' : 'PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In',
    'Number with no Education' : 'PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In',
    # 'Number under Fourteen' : 'PopulationBreakdownByHighestLevelOfEducationAchievedForThoseAged15In',
    'Total Primary Education Completion Rate' : 'PrimaryCompletionRateOfRelevantAgeGroup',
    'Female Primary Education Completion Rate' : 'PrimaryCompletionRateOfRelevantAgeGroup',
    'Male Primary Education Completion Rate' : 'PrimaryCompletionRateOfRelevantAgeGroup',
    'Electricity from Coal in TWh' : 'ElectricityProductionBySource',
    'Electricity fom Gas in TWh' : 'ElectricityProductionBySource',
    'Electricity from Nuclear in TWh' : 'ElectricityProductionBySource',
    'Electricity from Hydro in TWh' : 'ElectricityProductionBySource',
    'Electricity from Solar in TWh' : 'ElectricityProductionBySource',
    'Electricity from Oil in TWh' : 'ElectricityProductionBySource',
    'Electricity from Wind in TWh' : 'ElectricityProductionBySource',
    'Electricity from Bioenergy in TWh' : 'ElectricityProductionBySource',
    'Other Renewables excluding Bioenergy in TWh' : 'ElectricityProductionBySource',
    'Number of deaths due to Executions' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Meningitis' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Alzheimers' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Parkinsons' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Nutitional deficiences' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Malaria' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Drowning' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Interpersonal violence' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Maternal disorders' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to HIV' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Drug use' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Tuberculosis' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Cardiovascular disease' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Lower respiratory infections' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Neonatal disorders' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Alcohol use' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Self harm' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Forces of nature' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Diarrheal diseases' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Hypothermia or hyperthermia' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Neoplasms' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Conflict or terrorism' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Diabetes mellitus' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Chronic kidney disorder' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Poisonings' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Protein malnutrition' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Terrorism' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Road injuries' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Chronic respiratory disease' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Cirrhosis and other liver disease' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Digestive disease' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Fire' : 'AnnualNumberOfDeathsByCause',
    'Number of deaths due to Acute hepatitis' : 'AnnualNumberOfDeathsByCause'
}