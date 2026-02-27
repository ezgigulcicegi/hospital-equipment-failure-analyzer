# Hospital Equipment Failure Analyzer
# Author: Ezgi
# Description: Basic analysis of hospital equipment failure data

equipment_failures = {
    "Ventilator": 5,
    "Infusion Pump": 8,
    "ECG Monitor": 3,
    "Defibrillator": 2
}

print("=== Hospital Equipment Failure Report ===\n")

total_failures = sum(equipment_failures.values())
average_failures = total_failures / len(equipment_failures)
most_problematic = max(equipment_failures, key=equipment_failures.get)

for equipment, failures in equipment_failures.items():
    print(f"{equipment}: {failures} failures")

print("\n-----------------------------------------")
print(f"Total Failures: {total_failures}")
print(f"Average Failures per Device: {round(average_failures, 2)}")
print(f"Most Problematic Device: {most_problematic}")
