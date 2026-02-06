


import matplotlib.pyplot as plt

info = 0
warning = 0
error = 0

with open("system.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1

labels = ["INFO", "WARNING", "ERROR"]
counts = [info, warning, error]

plt.bar(labels, counts)
plt.xlabel("Log Type")
plt.ylabel("Count")
plt.title("System Log Analysis")
plt.show()
