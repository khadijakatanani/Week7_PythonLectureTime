import matplotlib.pyplot as plt

# a pie chart helps organize and
# show data as a percentage of a whole
# the parameter order is essential
# plt.pie(<corresponding continuous data collection>,
#         labels = <categorical data>,
#         autopct = "%0.2f%%")

# x = ["C", "C++", "Java", "Python", "PHP"]
# y = [23, 17, 35, 29, 12]

x = ["London", "Paris", "Rome", "New Delhi", "Berlin", "Ankara"] # cities
y = [100, 20, 10, 260, 80, 10] # number of Indian restaurants

explode = (0, 0, 0, 0.2, 0, 0)
plt.title("Pie title")

plt.pie(y, labels = x, autopct = "%0.2f%%", explode=explode)
plt.show()