"""
Name: Ankit Kumar
Roll no: 2501730109
Project-title: Mini Project Assignment: Daily Calorie Tracker CLI.
Date: 7 November 2025

welcome fellow problem solver, this is a  python script
"""
import csv
from datetime import datetime

print("<------------Welcome Fellow Problem Solver!------------>")

Meal_Name_List= []
Calorie_Amount_List= []

User_input =int(input("how many meal do you want to track?"))
for i in range(User_input):
    Meal_Name = input("Enter the Meal Name(Breakfast/Lunch/Snack/Dinner):")
    Meal_Name_List.append(Meal_Name)
    Calorie_Amount = float(input("Enter the Calories Amount:"))
    Calorie_Amount_List.append(Calorie_Amount)



# Calculations

total_Calorie_Amount = sum(Calorie_Amount_List)
avg_Calorie_Amount = total_Calorie_Amount/User_input

limit=float(input("\nEnter Your Daily Calorie Limit:"))

if total_Calorie_Amount > limit:
    status = "You have exceeded your daily calorie limit."

else:
    status = "You are within your daily calorie limit."


# Displaying the Result

print("\n---------------------------------")
print("     Daily Calorie Tracker")
print("---------------------------------")
print("Meal Name\tCalories Amount")
print("------------------------------------")

for meal, cal in zip(Meal_Name_List, Calorie_Amount_List):
    print(f"{meal:}\t{cal}")

print("----------------------------------------------------")
print(f"Total Calories:\t\t{total_Calorie_Amount}")
print(f"Average per Meal:\t{avg_Calorie_Amount:}")
print(f"Calorie Limit:\t\t{limit}")
print(f"Status:\t{status}")
print("----------------------------------------------------")


# Saving the Report

save = input("Do you want to save the result?(y/n):").lower()
if save == "y":
    file="calorie_tracker.csv"
    with open(file, "w") as csvfile:
        writer = csv.writer(csvfile)
        csvfile.write("Daily Calorie Tracker\n")
        csvfile.write(f"Date & Time :{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        csvfile.write("Meal Name\tCalories Amount\n")
        for meal, cal in zip(Meal_Name_List, Calorie_Amount_List):
            csvfile.write(f"{meal:}\t{cal}\n")
        csvfile.write(f"Total Calories:\t\t{total_Calorie_Amount}\n")
        csvfile.write(f"Average per Meal:\t{avg_Calorie_Amount}\n")
        csvfile.write(f"Calorie Limit:\t\t{limit}\n")
        csvfile.write(f"Status:\t\t{status}\n")
    print(f"\nResults saved to file{file}")
else:
    print("\nResults not saved")

print("\n--------------------------")
print("Thank You for using this program")














