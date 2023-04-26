import matplotlib.pyplot as plt

# plt.bar() generates a bar graph for x
# and its corresponding numeric data for y

# bar plots are best used when showing comparison between categories.

x = ["London", "Paris", "Rome", "New Delhi", "Berlin", "Ankara"] # cities
y = [100, 20, 10, 260, 80, 10] # number of Indian restaurants

plt.title("Number of Indian restaurants for Each City - Bar Plot")
plt.xlabel("Cities")
plt.ylabel("Number of Indian restaurants")
plt.barh(x, sorted(y, reverse=True))
# plt.barh(x, y)
plt.show()
