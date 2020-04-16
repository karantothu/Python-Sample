# Top 5 Confirmed cases.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import scipy.stats
import numpy as np
import scipy.stats as stats
import pylab as pl

fontP = FontProperties()
fontP.set_size('small')

file_name = 'assignment.xlsx'

data = pd.read_excel(file_name, columns=0, sheet_name="data_after_cleaning",
                     usecols=['Country/Region', 'Date', 'Confirmed', 'Deaths'])
# print(data.head())
dates = set(list(data['Date']))
confirmed = set(list(data['Confirmed']))
countries = set(list(data['Country/Region']))

data = data.groupby(['Country/Region'])['Deaths'].sum()
his = data.describe()

x_min = his['min']
x_max = his['max']

mean = his['mean']
std = his['std']

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x, mean, std)

plt.plot(x, y , color='r')

plt.grid()

plt.xlim(x_min,x_max)
# plt.ylim(0,0.25)

plt.title('Normal distribution curve of deaths rate across countries', fontsize=10)

plt.xlabel('Deaths')
plt.ylabel('Normal Distribution')

# plt.savefig("normal_distribution.png")
plt.show()