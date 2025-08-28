import matplotlib.pyplot as plt
temperature = [25, 48, 35, 20, 37, 30, 15]
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
plt.plot(days, temperature)
plt.xlabel("Days of the week")
plt.ylabel("Temperature (°C)")
plt.title("Weather")
plt.show()