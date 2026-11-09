import csv
from datetime import datetime

risk_register = []

def assess_risk(asset, likelihood, impact):
    score = likelihood * impact

    if score >= 20:
        level = "Critical"
        recommendation = "Immediate action required"
    elif score >= 12:
        level = "High"
        recommendation = "Prioritize risk mitigation"
    elif score >= 6:
        level = "Medium"
        recommendation = "Apply security controls"
    else:
        level = "Low"
        recommendation = "Monitor the risk"

    print("\n--- Cyber Risk Assessment ---")
    print(f"Asset: {asset}")
    print(f"Risk Score: {score}/25")
    print(f"Risk Level: {level}")
    print(f"Recommendation: {recommendation}")
    risk_register.append({
        "Asset": asset,
        "Likelihood": likelihood,
        "Impact": impact,
        "Risk Score": score,
        "Risk Level": level,
        "Recommendation": recommendation,
        "Date": datetime.now().strftime("%Y-%m-%d")
    })


print("Welcome to Cyber Risk Assessment Tool")

asset = input("Enter asset name: ")

while True:
    try:
        likelihood = int(input("Likelihood (1-5): "))
        impact = int(input("Impact (1-5): "))

        if 1 <= likelihood <= 5 and 1 <= impact <= 5:
            break

        print("Please enter numbers between 1 and 5.")
    except ValueError:
        print("Please enter valid whole numbers.")

assess_risk(asset, likelihood, impact)

with open("risk_register.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "Asset", "Likelihood", "Impact",
        "Risk Score", "Risk Level",
        "Recommendation", "Date"
    ])
    writer.writeheader()
    writer.writerows(risk_register)

print("Risk register saved successfully!")