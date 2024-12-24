task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
    case "low":

        if time_bound == "yes":
            reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
        elif time_bound == "no":
            reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please use high, medium, or low."

print(f"\nReminder: {reminder}")
