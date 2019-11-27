import matplotlib.pyplot as plt

fruits = ("Яблоко", "Персик", "Апельсин", "Банан", "Дыня")
counts = [34, 25, 43, 31, 17]
plt.bar(fruits, counts)
plt.title("Фрукты")
plt.xlabel("Фрукты")
plt.ylabel("Количество")
plt.show()