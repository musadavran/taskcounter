# ⏰ Mission Reminder CLI App

This is a simple command-line Python project where the user can input a task (mission), define a time duration in minutes, and get reminded to complete it. Once the time is up, the program asks whether the task is completed and logs the result accordingly.

## 📌 Features

- Add your task (mission)
- Set a countdown time (in minutes)
- Get notified when time is up
- Answer whether the task is completed or not
- Tracks completed tasks
- Gives additional time if needed

## 🚀 How It Works

1. User inputs a mission (task)
2. User sets how many minutes they need to complete the mission
3. The program waits for the specified duration
4. Once time's up, it asks:
   - Did you finish? → If yes: task is marked as completed
   - If no: gives 1 more minute, and asks again
5. Completed tasks are saved in a list and printed at the end

## 🧠 Example
What your mission?: Study for math exam
After how many minutes should I remind you?: 2

…waiting 2 minutes…

Did you finish yes or no?: yes

Tasks you have completed: [‘Study for math exam’]
## 📁 Files

- `mission.py`: Main script with the task management logic

## ✅ Requirements

- Python 3.x  
- No external libraries needed (uses built-in `time`)
