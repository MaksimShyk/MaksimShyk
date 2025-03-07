# -*- coding: utf-8 -*-
"""my-TASK-1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aoKVqohm7kxeRudb2vRDeha1U2r774by
"""

import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/bartpiel/files-for-classes/refs/heads/main/Workshop-1/country_profile_variables.csv')

#Show 10 random df1 rows.
df.sample(10)

# Produce the list of all df1 column names.
df.columns

#Use the loc function to provide major statistical indicators for columns from 'country' to 'Labour force participation (female/male pop. %)'.
df.loc[:,'country':'Labour force participation (female/male pop. %)']

#Create df2 consisting of 'country','Region','Surface area (km2)','Population in thousands (2017)','Population density (per km2, 2017)','Sex ratio (m per 100 f, 2017)','GDP: Gross domestic product (million current US$)','GDP per capita (current US$)','Unemployment (% of labour force)','Labour force participation (female/male pop. %)','Fertility rate, total (live births per woman)','Health: Total expenditure (% of GDP)','Individuals using the Internet (per 100 inhabitants)','CO2 emission estimates (million tons/tons per capita)' coming from df1.
df2=pd.read_csv('https://raw.githubusercontent.com/bartpiel/files-for-classes/refs/heads/main/Workshop-1/country_profile_variables.csv')

df2=df2.loc[0:229,'country':'CO2 emission estimates (million tons/tons per capita)']
df2

df2

# Rename columns in df2 as follows:
df2=df2.rename(columns={'country':'Country', 'Surface area (km2)':'Surface', 'Population in thousands (2017)' : 'Population', 'Population density (per km2, 2017)' : 'Population_density', 'Sex ratio (m per 100 f, 2017)' : 'Sex-ratio', 'GDP: Gross domestic product (million current US$)' : 'GDP', 'GDP per capita (current US$)' : 'GDP_per_capita', 'Unemployment (% of labour force)' : 'Unemployment', 'Labour force participation (female/male pop. %)' : 'Labour_force_participation', 'Individuals using the Internet (per 100 inhabitants)' : 'Internet_per_100', 'CO2 emission estimates (million tons/tons per capita)' : 'CO2_emission'
})

#Show the names of all columns in df2

df2.columns

# Show the last 10 rows in df2
df2.tail(10)

#. Create df2a consisting of rows 219 to 224 and columns from 'Country' to 'Sex-retio' from df2.
df2a=df2.loc[219:224, 'Country' : 'Sex-ratio']

df2a

#Create df2b consisting of rows 223, 225, 227 and columns 'Country', 'Surface', 'Population_density'.
df2b=df2.loc[[223, 225, 227], ['Country', 'Surface', 'Population_density']]
df2b

# Show all indicators for Poland in df2
 df2[df2['Country'] == 'Poland']

# Show all unique values ​​for Region in df2.
df2['Region']

# Create df3 based on df2, which consists of the Eastern European region, with a Population of over 7000 and a Population density of over 60.
df3=df2[(df2['Region']=='EasternEurope') & (df2['Population']> 7000) & (df2['Population_density']>60)]
df3.head()

#.Create histograms for Population and GDP per capita from df2.
df2.hist(column=['Population','GDP'])

#  Save df3 as EasternEurope.json with separated records.
df3[df3['Region']=='EasternEurope'][['Population', 'Population_density']].to_json('EasternEurope.json',orient='records')