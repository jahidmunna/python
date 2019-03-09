import matplotlib.pyplot as plt
# Import numpy as np
import numpy as np

# Generate data
gdp_cap = [i for i in range(2018,1800,-1)]
life_exp = np.random.randint(50, 100, size=2018-1800)
pop = list(np.random.randint(5, 100, size=2018-1800))

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop *=2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s=np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Display the plot
plt.show()
