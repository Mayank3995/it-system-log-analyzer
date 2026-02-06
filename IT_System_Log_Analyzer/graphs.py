import matplotlib.pyplot as plt

info = 0
warning = 0
error = 0
risk_score = 0

threat_types = {
    "Unauthorized": 0,
    "Failed": 0,
    "Denied": 0
}

with open("system.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info += 1
            risk_score += 1

        elif "WARNING" in line:
            warning += 1
            risk_score += 5

        elif "ERROR" in line:
            error += 1
            risk_score += 10

        for key in threat_types:
            if key in line:
                threat_types[key] += 1

# GRAPH 1
plt.figure()
plt.bar(["INFO", "WARNING", "ERROR"], [info, warning, error])
plt.title("System Log Severity Analysis")
plt.xlabel("Log Type")
plt.ylabel("Count")
plt.show(block=True)

# GRAPH 2
plt.figure()
plt.bar(["Risk Score"], [risk_score])
plt.title("Overall System Risk Level")
plt.ylabel("Score")
plt.show(block=True)

# GRAPH 3
plt.figure()
plt.bar(threat_types.keys(), threat_types.values())
plt.title("Security Threat Distribution")
plt.xlabel("Threat Type")
plt.ylabel("Occurrences")
plt.show(block=True)

input("Press ENTER to exit...")
