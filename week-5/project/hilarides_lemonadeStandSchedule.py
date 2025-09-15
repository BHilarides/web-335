"""
Author: Ben Hilarides
Date: 09.14.25
Filename: hilarides_lemonadeStandSchedule.py
Description: This file demonstrates the use of both file header comments and normal
level comments
"""

# 1. Create a list of at least 5 tasks related to running a lemonade stand.
tasks = [
    "Buy Lemons and Sugar",
    "Set up Stand",
    "Prepare Lemonade",
    "Serve Customers",
    "Clean Up"
]

# 2. Use a for loop to iterate over the list of tasks and print them to the console window.
print("Lemonade Stand Tasks:")
for task in tasks:
    print(f"- {task}")

print("\nSchedule for the Week:")

# 3. Create a list of days (Sunday through Saturday)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# 4. Use a for loop to iterate over the list of days to display what the tasks are for each day.
for i, day in enumerate(days):
    if day in ["Saturday", "Sunday"]:
        print(f"{day}: Day off - Time to Rest!")
    else:
        task_for_day = tasks[i % len(tasks)]
        print(f"{day}: Today's task is '{task_for_day}'.")