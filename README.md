Daily Calorie Tracker CLI

A simple and interactive Python Command Line Interface (CLI) tool that helps users track their daily calorie intake, calculate totals and averages, compare it with a daily calorie limit, and optionally save a report as a CSV file.

📌 Project Information

Name: Ankit Kumar
Roll No: 2501730109
Project Title: Mini Project – Daily Calorie Tracker CLI
Date: 7 November 2025

📖 Overview

This CLI-based Python program allows users to enter meals and their calorie values. It then calculates:

Total calories consumed

Average calories per meal

Whether the user is within or above their daily calorie limit

Users can also save the results in a CSV file, along with a timestamp.

✨ Features

✔️ Add multiple meals and calorie values

✔️ Automatic total and average calorie calculation

✔️ Check calorie limit status

✔️ Display data in a formatted table

✔️ Save results to a CSV file (calorie_tracker.csv)

✔️ Simple and user-friendly interface

📂 File Output Example (CSV)

If the user chooses to save, the file will contain:

Daily Calorie Tracker
Date & Time: 2025-11-07 14:35:10
Meal Name    Calorie Amount
Breakfast    320
Lunch        450
Snack        150
Total Calories:      920
Average per Meal:    306.67
Calorie Limit:       1000
Status:              You are within your daily calorie limit.

🛠️ How It Works

The program asks how many meals the user wants to track.

For each meal, it asks:

Meal name (Breakfast/Lunch/Snack/Dinner)

Calories consumed

User enters their daily calorie limit.

Program displays:

Meal list

Total calories

Average calories

Calorie status

Optionally saves the data to a CSV file.

▶️ How to Run

Make sure Python is installed, then run:

python calorie_tracker.py

📌 Requirements

Python 3.x

No external libraries needed (only uses built-in modules: csv, datetime)

📈 Sample Output
<------------Welcome Fellow Problem Solver!------------>

How many meals do you want to track? 3
Enter the Meal Name(Breakfast/Lunch/Snack/Dinner): Breakfast
Enter the Calories Amount: 300
Enter the Meal Name(Breakfast/Lunch/Snack/Dinner): Lunch
Enter the Calories Amount: 450
Enter the Meal Name(Breakfast/Lunch/Snack/Dinner): Snack
Enter the Calories Amount: 150

Enter Your Daily Calorie Limit: 1000

---------------------------------
     Daily Calorie Tracker
---------------------------------
Meal Name        Calories Amount
------------------------------------
Breakfast        300
Lunch            450
Snack            150
----------------------------------------------------
Total Calories:            900
Average per Meal:          300.0
Calorie Limit:             1000
Status:        You are within your daily calorie limit.
----------------------------------------------------
Do you want to save the result?(y/n): y

Results saved to file calorie_tracker.csv

📚 Learning Outcomes

Through this project, you practice:

Python lists

Loops

User input handling

File handling with CSV

Formatting console output

Basic calculations

Date and time usage

📧 Author

Ankit Kumar
Mini Project – Daily Calorie Tracker CLI
