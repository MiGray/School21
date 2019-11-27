import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

x = (0, 10, 50)
y = x

plt.title("Линейная зависимость y=x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x,y, "r--")
plt.show()