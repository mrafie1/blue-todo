# blue-todo
<img src="/app/src/icon.png" width="48">

A simple blue-themed Tkinter to-do application.

# Introduction

**Hello!** 👋

This is my first solo project and my first time practicing using Tkinter.

My goal was to be able to be able to create a simple to-do application that allows users to:
- Create tasks with titles and descriptions
- Have multiple tasks that users can scroll through, inspect (view their descriptions), complete, and delete
- Be able to track their task progress
- And most importantly, view periodically changing, random motivational messages :)

My other goal was to play around with markdown and create proper documentation for current and future projects!

# Installing & Running
Open your terminal and run the following command to install and run the app:

1. **Clone the repository**

   ```bash
   git clone https://github.com/mrafie1/blue-todo
   ```
2. **Navigate to the project directory**
   ```bash
   cd blue-todo
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Navigate to the app directory**
   ```bash
   cd app
   ```
5. **Run!**
   ```bash
   python app_final.py
   ```
   

# Features
## Creating tasks: titles and descriptions!

Users will be able to input task titles and their descriptions on the left side of the application. 

The application will detect and display an error screen when:
- Empty task title
- Title and description going over their respective character limit
![](documentation/potential_errors.gif)

## After creating a task: completing, deleting, and scrolling through tasks

After creating a task, the task will appear on the right side of the application, below any previous created tasks.
![](documentation/create_a_task.gif)

Users are then able to scroll through all of the tasks they've created, complete and delete tasks, and track their task progress on the left side of the application.
![](documentation/scroll_complete.gif)

## Inspecting tasks: returning to home, completing a task, and then removing it

By pressing the 'check notes!' button widget next to the desired task, users can:
- View task title and description
- Return to homepage
- Toggle complete
- Remove the task
![](documentation/inspect_complete_delete.gif)


# Conclusion
Thank you for reading through all of this documentation - this took way too much time to complete. I hope you enjoy the app!
