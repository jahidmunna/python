# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

year = [2018, 2017, 2016, 2015]
pop = [554, 450, 374, 344]

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

