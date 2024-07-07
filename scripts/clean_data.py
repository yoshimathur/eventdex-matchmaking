import pandas as pd
import numpy as np

df = pd.read_csv('./data/Test MM  Seller data from wbenc.csv')

# DBA --> mostly null
# Join DBA to Company [DBA: _] seperated
# Drop DBA 
for i in range(len(df['Company'])):
    if type(df['DBA'][i]) == str: 
        updated_company = df['Company'][i] + f" [DBA: {df['DBA'][i]}]"
        df.iloc[i, df.columns.get_loc('Company')] = updated_company
df.drop('DBA', axis=1, inplace=True)

# merge Business Category
df['Business Category'] = df.apply(
    lambda row: ', '.join(filter(pd.notna, [row['Primary Business Category'], row['Secondary Business Category']])),
    axis=1
)
df.drop(['Primary Business Category', 'Secondary Business Category'], axis=1, inplace=True)

# merge NAICS Codes  
naics_code_columns = [f'NAICS Code {i}' for i in range(1, 10)]
df['NAICS Codes'] = df[naics_code_columns].apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)
df.drop(columns=naics_code_columns, axis=1, inplace=True)

# merge commodities
commodities_columns = [f'Commodities.{i}' for i in range(1, 5)]
commodities_columns.append('Commodities')
commodities = df[commodities_columns].apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)
df.drop(commodities_columns, axis=1, inplace=True)
df['Commodities'] = commodities

# merge location data 
loc_columns = ['Work Address 1', 'Work city', 'Work State', 'Work Country', 'Work Zip Code']
df['Location'] = df[loc_columns].apply(lambda row: ', '.join(row.dropna().astype(str)), axis=1)
loc_columns.append('Work Address 2')
loc_columns.append('Work Country.1')
df.drop(loc_columns, axis=1, inplace=True)

# merge references
df['References'] = df.apply(
    lambda row: ', '.join(filter(pd.notna, [row['References 1'], row['References 2']])),
    axis=1
)
df.drop(['References 1', 'References 2'], axis=1, inplace=True)

# merge scope of work
df['Scope of Work'] = df.apply(
    lambda row: ', '.join(filter(pd.notna, [row['Scope of Work 1'], row['Scope of Work 2']])),
    axis=1
)
df.drop(['Scope of Work 1', 'Scope of Work 2'], axis=1, inplace=True)

#drop year in business --> use business established date (no null values)
df.drop('Year in business', axis=1, inplace=True)

reordered_cols = ['Prefix', 'First Name', 'Last Name', 'Primary Email', 'Secondary Email',
       'Job Title', 'Mobile Number', 'Company', 'Business Category',
       'NAICS Codes', 'Commodities', 'Location', 'Geographical Region', 'Number of Employees',
       'Business Established Date', 'BBB Number', 'Business DUNS Number',
       'RPO', 'Distribution Country', 'Manufactures Country', 'Ethnicity', 'References', 'Scope of Work',
       'Revenue', 'Business Tax Id', 'Website URL', 'Business Description',
       'Keywords', 'Business Structure', 'Fax Number', 'Non WBENC Awards', 'Outside Facilities']
df = df[reordered_cols]

df.to_csv('./data/Cleaned Seller data.csv')