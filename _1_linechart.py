import matplotlib.pyplot as plt

# plt.plot(x, y) generates a line graph

# population of bears over years
x = [2017, 2018, 2019, 2020, 2021, 2022]
y = [100, 175, 350, 450, 400, 350]

plt.xlabel("Year")
plt.ylabel("# of Bears Over Years")
plt.title("Population Of Bears Over Years")

plt.plot(x, y)  # line graph
plt.show()
