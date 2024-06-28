import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the datasets
cinematic_data_path = 'merged_data/merged_cinematic_data.csv'
economic_data_path = 'merged_data/population_economic_data.csv'

cinematic_data = pd.read_csv(cinematic_data_path)
economic_data = pd.read_csv(economic_data_path)

# Example mapping (This needs to be filled with all country codes)
country_code_mapping = {
    'AD': 'AND', 'AE': 'ARE', 'AF': 'AFG', 'AG': 'ATG', 'AI': 'AIA',
    'AL': 'ALB', 'AM': 'ARM', 'AN': 'ANT', 'AO': 'AGO', 'AQ': 'ATA',
    'AR': 'ARG', 'AS': 'ASM', 'AT': 'AUT', 'AU': 'AUS', 'AW': 'ABW',
    'AZ': 'AZE', 'BA': 'BIH', 'BB': 'BRB', 'BD': 'BGD', 'BE': 'BEL',
    'BF': 'BFA', 'BG': 'BGR', 'BH': 'BHR', 'BI': 'BDI', 'BJ': 'BEN',
    'BM': 'BMU', 'BN': 'BRN', 'BO': 'BOL', 'BR': 'BRA', 'BS': 'BHS',
    'BT': 'BTN', 'BW': 'BWA', 'BY': 'BLR', 'BZ': 'BLZ', 'CA': 'CAN',
    'CD': 'COD', 'CF': 'CAF', 'CG': 'COG', 'CH': 'CHE', 'CI': 'CIV',
    'CK': 'COK', 'CL': 'CHL', 'CM': 'CMR', 'CN': 'CHN', 'CO': 'COL',
    'CR': 'CRI', 'CU': 'CUB', 'CV': 'CPV', 'CW': 'CUW', 'CY': 'CYP',
    'CZ': 'CZE', 'DE': 'DEU', 'DJ': 'DJI', 'DK': 'DNK', 'DM': 'DMA',
    'DO': 'DOM', 'DZ': 'DZA', 'EC': 'ECU', 'EE': 'EST', 'EG': 'EGY',
    'ER': 'ERI', 'ES': 'ESP', 'ET': 'ETH', 'FI': 'FIN', 'FJ': 'FJI',
    'FO': 'FRO', 'FR': 'FRA', 'GA': 'GAB', 'GB': 'GBR', 'GD': 'GRD',
    'GE': 'GEO', 'GF': 'GUF', 'GH': 'GHA', 'GI': 'GIB', 'GL': 'GRL',
    'GM': 'GMB', 'GN': 'GIN', 'GP': 'GLP', 'GQ': 'GNQ', 'GR': 'GRC',
    'GT': 'GTM', 'GU': 'GUM', 'GW': 'GNB', 'GY': 'GUY', 'HK': 'HKG',
    'HN': 'HND', 'HR': 'HRV', 'HT': 'HTI', 'HU': 'HUN', 'ID': 'IDN',
    'IE': 'IRL', 'IL': 'ISR', 'IN': 'IND', 'IQ': 'IRQ', 'IR': 'IRN',
    'IS': 'ISL', 'IT': 'ITA', 'JM': 'JAM', 'JO': 'JOR', 'JP': 'JPN',
    'KE': 'KEN', 'KG': 'KGZ', 'KH': 'KHM', 'KM': 'COM', 'KN': 'KNA',
    'KP': 'PRK', 'KR': 'KOR', 'KW': 'KWT', 'KY': 'CYM', 'KZ': 'KAZ',
    'LA': 'LAO', 'LB': 'LBN', 'LC': 'LCA', 'LI': 'LIE', 'LK': 'LKA',
    'LR': 'LBR', 'LS': 'LSO', 'LT': 'LTU', 'LU': 'LUX', 'LV': 'LVA',
    'LY': 'LBY', 'MA': 'MAR', 'MC': 'MCO', 'MD': 'MDA', 'ME': 'MNE',
    'MG': 'MDG', 'MH': 'MHL', 'MK': 'MKD', 'ML': 'MLI', 'MM': 'MMR',
    'MN': 'MNG', 'MO': 'MAC', 'MQ': 'MTQ', 'MR': 'MRT', 'MT': 'MLT',
    'MU': 'MUS', 'MV': 'MDV', 'MW': 'MWI', 'MX': 'MEX', 'MY': 'MYS',
    'MZ': 'MOZ', 'NA': 'NAM', 'NC': 'NCL', 'NE': 'NER', 'NG': 'NGA',
    'NI': 'NIC', 'NL': 'NLD', 'NO': 'NOR', 'NP': 'NPL', 'NR': 'NRU',
    'NZ': 'NZL', 'OM': 'OMN', 'PA': 'PAN', 'PE': 'PER', 'PF': 'PYF',
    'PG': 'PNG', 'PH': 'PHL', 'PK': 'PAK', 'PL': 'POL', 'PT': 'PRT',
    'PW': 'PLW', 'PY': 'PRY', 'QA': 'QAT', 'RO': 'ROU', 'RS': 'SRB',
    'RU': 'RUS', 'RW': 'RWA', 'SA': 'SAU', 'SB': 'SLB', 'SC': 'SYC',
    'SD': 'SDN', 'SE': 'SWE', 'SG': 'SGP', 'SI': 'SVN', 'SK': 'SVK',
    'SL': 'SLE', 'SM': 'SMR', 'SN': 'SEN', 'SO': 'SOM', 'SR': 'SUR',
    'ST': 'STP', 'SV': 'SLV', 'SY': 'SYR', 'SZ': 'SWZ', 'TC': 'TCA',
    'TD': 'TCD', 'TG': 'TGO', 'TH': 'THA', 'TJ': 'TJK', 'TM': 'TKM',
    'TN': 'TUN', 'TO': 'TON', 'TR': 'TUR', 'TT': 'TTO', 'TV': 'TUV',
    'TZ': 'TZA', 'UA': 'UKR', 'UG': 'UGA', 'US': 'USA', 'UY': 'URY',
    'UZ': 'UZB', 'VA': 'VAT', 'VC': 'VCT', 'VE': 'VEN', 'VG': 'VGB',
    'VI': 'VIR', 'VN': 'VNM', 'VU': 'VUT', 'WS': 'WSM', 'YE': 'YEM',
    'ZA': 'ZAF', 'ZM': 'ZMB', 'ZW': 'ZWE'
}

# Apply the mapping to the cinematic data
cinematic_data['Country_Code'] = cinematic_data['region'].map(country_code_mapping)

# Drop rows where the country code mapping was not found
cinematic_data = cinematic_data.dropna(subset=['Country_Code'])

# Re-group by the new country code and aggregate the votes and quality scores
cinematic_data_grouped = cinematic_data.groupby('Country_Code').agg(
    total_votes=('numVotes', 'sum'),
    average_quality_score=('averageRating', 'mean')
).reset_index()

# Step 3: Merge the Data
merged_data = pd.merge(cinematic_data_grouped, economic_data, on='Country_Code')

# Step 4: Compute Ranks and Hegemony
# Calculate the ranks
merged_data['population_rank'] = merged_data['Population'].rank(ascending=False)
merged_data['gdp_rank'] = merged_data['GDP'].rank(ascending=False)
merged_data['gdp_per_capita_rank'] = merged_data['GDP_per_Capital'].rank(ascending=False)
merged_data['total_votes_rank'] = merged_data['total_votes'].rank(ascending=False)
merged_data['average_quality_rank'] = merged_data['average_quality_score'].rank(ascending=False)

# Compute hegemony
merged_data['weak_hegemony'] = merged_data['gdp_rank'] - merged_data['total_votes_rank']
merged_data['strong_hegemony'] = merged_data['gdp_rank'] - merged_data['average_quality_rank']

# Scatter plot for GDP vs Total Votes
fig1 = px.scatter(merged_data, x='GDP', y='total_votes', size='Population', color='gdp_rank', 
                  hover_name='Country_Code', title='GDP vs Total Votes',
                  labels={'GDP': 'GDP', 'total_votes': 'Total Votes'},
                  size_max=50)

fig1.show()

# Bubble plot for GDP vs Average Quality Score
fig2 = px.scatter(merged_data, x='GDP', y='average_quality_score', size='Population', color='gdp_rank', 
                  hover_name='Country_Code', title='GDP vs Average Quality Score',
                  labels={'GDP': 'GDP', 'average_quality_score': 'Average Quality Score'},
                  size_max=50)

fig2.show()

# Heatmap for ranks
rank_data = merged_data[['Country_Code', 'population_rank', 'gdp_rank', 'gdp_per_capita_rank', 'total_votes_rank', 'average_quality_rank']]
fig3 = px.imshow(rank_data.set_index('Country_Code').T, title='Heatmap of Ranks')
# fig3.show()

# Parallel coordinates plot
fig4 = px.parallel_coordinates(merged_data, dimensions=['population_rank', 'gdp_rank', 'gdp_per_capita_rank', 'total_votes_rank', 'average_quality_rank'],
                               color='gdp_rank', title='Parallel Coordinates Plot of Ranks')
# fig4.show()

# Scatter plot for Weak Hegemony vs Strong Hegemony
fig5 = px.scatter(merged_data, x='weak_hegemony', y='strong_hegemony', size='Population', color='gdp_rank', 
                  hover_name='Country_Code', title='Weak Hegemony vs Strong Hegemony',
                  labels={'weak_hegemony': 'Weak Hegemony', 'strong_hegemony': 'Strong Hegemony'},
                  size_max=45)
fig5.show()