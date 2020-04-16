# Top 5 Confirmed cases.
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
countries = set(list(data['Country/Region']))

# countries = ['China', 'US','Italy', 'Spain', 'Germany', 'Iran', 'France', 'South Korea', 'United Kingdom', 'Switzerland']

# January data
January = data.loc[data['Date'] <= '2020-01-31'].groupby(['Country/Region'])['Confirmed'].sum().sort_values(ascending=False)[:5]
February = data.loc[(data['Date'] >= '2020-02-01') & (data['Date'] <= '2020-02-29')].groupby(['Country/Region'])['Confirmed'].sum().sort_values(ascending=False)[:5]
March = data.loc[(data['Date'] >= '2020-03-01') & (data['Date'] <= '2020-03-29')].groupby(['Country/Region'])['Confirmed'].sum().sort_values(ascending=False)[:5]
April = data.loc[(data['Date'] >= '2020-04-01') & (data['Date'] <= '2020-04-29')].groupby(['Country/Region'])['Confirmed'].sum().sort_values(ascending=False)[:5]

months = [January, February, March, April]
month_names = ['January', 'February', "March", "April"]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
fig.subplots_adjust(hspace=0.25, wspace=0.35)

for ax, month, month_name in zip(axes.flatten(), months, month_names):
    labels = list(month.keys())
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    rects1 = ax.bar(x - width/2, list(month), width)
    ax.set_title(month_name)
    ax.set_ylabel("Confirmed cases")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    autolabel(rects1)

fig.tight_layout()
plt.xlabel('Countries')
plt.ylabel('Confirmed cases')
plt.suptitle("Top 5 Countries with highest confirmed cases by each month")
plt.tight_layout()
plt.show()


# plt.savefig('img_trend2.pdf', bbox_inches='tight')

