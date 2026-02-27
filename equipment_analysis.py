

from datetime import datetime


def analyze_equipment_failures(equipment_failures):
    if not equipment_failures:
        print("No equipment data available.")
        return

    print("=== Hospital Equipment Failure Report ===")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    total_failures = sum(equipment_failures.values())
    average_failures = total_failures / len(equipment_failures)

    most_problematic = max(equipment_failures, key=equipment_failures.get)
    most_failures = equipment_failures[most_problematic]
    percentage = (most_failures / total_failures) * 100

    # Sort devices by failures (descending)
    sorted_items = sorted(equipment_failures.items(), key=lambda x: x[1], reverse=True)

    for equipment, failures in sorted_items:
        print(f"{equipment}: {failures} failures")

    print("\n----------------------------------------")
    print(f"Total Failures: {total_failures}")
    print(f"Average Failures per Device: {round(average_failures, 2)}")
    print(f"Most Problematic Device: {most_problematic}")
    print(f"Failure Contribution: {round(percentage, 2)}%")


def main():
    equipment_failures = {
        "Ventilator": 5,
        "Infusion Pump": 8,
        "ECG Monitor": 3,
        "Defibrillator": 2
    }

    analyze_equipment_failures(equipment_failures)


if __name__ == "__main__":
    main()