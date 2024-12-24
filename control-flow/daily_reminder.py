

# #* Prompt for a Single Task:

#! ASK THE USER TO INPUT A TASK DESCRIPTION AND SAVE IT INTO A TASK VARIABLE
task = input("Enter your task:")

#! PROMPT FOR THE TASK’S PRIORITY (HIGH, MEDIUM, LOW)
priority = input("Priority (high/medium/low):")

#! IN A TIME_BOUND VARIABLE, ASK IF THE TASK IS TIME-BOUND (YES OR NO)
time_bound = input("Is it time-bound? (yes/no):")

#//Add
error_message = "something went wrong!"
first_part = f"{task} is a {priority} priority task"

#! USE A MATCH CASE STATEMENT TO REACT DIFFERENTLY BASED ON THE TASK’S PRIORITY.
match priority:
    case "high":
        reminder = "that requires immediate attention today!"
    case "medium":
       reminder = "schedule it for later"
    case "low":
        reminder = "Consider completing it when you have free time."
    case _ :
        message = error_message

#! WITHIN THE MATCH CASE OR AFTER, USE AN IF STATEMENT TO MODIFY THE REMINDER IF THE TASK IS TIME-BOUND.
if time_bound == "yes":
    reminder = "that requires immediate attention today!"
elif time_bound == "no":
    reminder = "Consider completing it when you have free time."
else:
    message = error_message 

message = (f"Reminder: '{task}' is a {priority} priority task. that requires immediate attention today!" 
           if time_bound == "yes" else "Consider completing it when you have free time.")
print("Reminder: ", reminder)
print(message)

# task = input("Enter your task: ")
# priority = input("priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# match priority:
#     case "high":
#         reminder = f"'{task}' is a {priority} priority task "
#     case "medium":
#         reminder = f"'{task}' is a {priority} priority task "
#     case "low":
#         reminder = f"'{task}' is a {priority} priority task "
#     case _:
#         reminder = "Invalid priority entered. Please use high, medium, or low."

#     if time_bound == "yes":
#         reminder += "that requires immediate attention today!"
#     elif time_bound == "no":
#         reminder += ". Consider completing it when you have free time."
#     else:
#         reminder += ". Time sensitivity was not specified correctly."

# print("\nReminder:")
# print(reminder)
