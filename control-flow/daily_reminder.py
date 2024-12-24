task = input("Enter your task: ")
priority = input("priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"'{task}' is a high priority task "
    case "medium":
        message = f"'{task}' is a medium priority task "
    case "low":
        message = f"'{task}' is a low priority task "
    case _:
        message = "Invalid priority entered. Please use high, medium, or low."

    if time_bound == "yes":
        message += "that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
    else:
        message += "Invalid input for time-bound. Please enter yes or no."

print("Reminder: ", message)



