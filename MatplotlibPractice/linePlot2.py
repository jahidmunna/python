# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

year = [2018, 2017, 2016, 2015]
pop = [10, 8, 5, 4]

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Display the year where population (pop) is morethan 8 million
print(year[pop.index(8)])