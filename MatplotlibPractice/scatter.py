# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

gdp_cap = [i for i in range(2018,1800,-1)]
life_exp = np.random.randint(50, 100, size=2018-1800)

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)

# Add title
plt.title(title)

#ticks
plt.yticks([50,60,70,80,90,100], ["Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"])
# Show plot
plt.show()