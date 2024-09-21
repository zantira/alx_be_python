#simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single,
#  priority task for the day based on time sensitivity.

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

#add time bound sensitivity

if time_bound == "yes":
    reminder += " that requires immediate action today!"
else:
    reminder += " consider completing it when you have free time."

print("Reminder:", reminder)
