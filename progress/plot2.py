import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('small')

file_name = 'assignment.xlsx'

data = pd.read_excel(file_name, columns=0, sheet_name="data_after_cleaning",
                     usecols=['Country/Region', 'Date', 'Confirmed'])
# print(data.head())
dates = set(list(data['Date']))
confirmed = set(list(data['Confirmed']))
# countries = set(list(data['Country/Region']))

countries = ['China', 'US','Italy', 'Spain', 'Germany', 'Iran', 'France', 'South Korea', 'United Kingdom', 'Switzerland']

fig, ax = plt.subplots(figsize=(10, 10))

for country in countries:
    ax.plot(data.loc[data['Country/Region'] == country]['Date'],
            data.loc[data['Country/Region'] == country]['Confirmed'], label=country)

ax.set_yscale('linear')
ax.set_title('Confirmed case trend in specific countries')
ax.legend(prop=fontP)
plt.xlabel('Dates')
plt.ylabel('Confirmed Cases')
# plt.show()
plt.savefig('img_trend2.pdf', bbox_inches='tight')

