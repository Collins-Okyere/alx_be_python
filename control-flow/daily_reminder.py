task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a {priority} priority task "
    case "medium":
        reminder = f"'{task}' is a {priority} priority task "
    case "low":
        reminder = f"'{task}' is a {priority} priority task "
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low."

if time_bound == "yes":
    reminder += "that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += ". Time sensitivity was not specified correctly."

print(f"\nReminder: {reminder}")
