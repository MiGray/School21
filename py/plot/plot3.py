import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

x = (0, 10, 50)
y1 = x
y2 = [i**2 for i in x]


plt.title("Зависимости: y1=x, y=x^2")
plt.xlabel("x")
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y1, x, y2)
plt.show()