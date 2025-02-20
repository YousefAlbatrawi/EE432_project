# Task Manager Application

## Overview
The **Task Manager Application** is a Python-based tool designed to help users manage tasks efficiently. It provides a graphical user interface (GUI) built with the `tkinter` library and uses advanced data structures like **Linked Lists**, **Hash Tables**, and **Binary Search Trees (BST)** to organize and retrieve tasks. Whether you're a student, professional, or anyone looking to stay organized, this application offers a simple yet powerful way to manage your tasks.

---

## Features
### Task Management
- **Add Task**: Add a new task with a description, priority (High, Medium, Low), and status (completed or incomplete). This feature ensures that all your tasks are captured and organized effectively.
- **Search Task**: Search for tasks by description (case-insensitive). This allows you to quickly find specific tasks without scrolling through the entire list.
- **Display Tasks**: View tasks in **insertion order** (the order they were added) or **priority order** (High > Medium > Low). You can also filter tasks by status: **All**, **Completed**, or **Incomplete**.
- **Delete Task**: Remove a selected task from the list. This feature helps you keep your task list clean and up-to-date.

### Data Structures
- **Linked List**: Stores tasks in the order they are added, ensuring that the sequence of tasks is preserved.
- **Hash Table**: Enables fast searching by task description, making it easy to locate specific tasks.
- **Binary Search Tree (BST)**: Organizes tasks by priority, allowing for efficient retrieval and sorting of tasks based on their importance.

---

## Commands
### Task Operations
- **Add Task**: Enroll a new task into the task manager. Simply enter the task description, select the priority, and mark it as completed if needed.
- **Delete Task**: Remove a task from the task manager. Select the task you want to delete and confirm the action.
- **Search Task**: Find tasks by description. Enter a keyword, and the application will display all tasks containing that keyword.
- **Display Tasks**: Show tasks based on insertion order or priority, with optional filtering by status. Use the display mode and filter options to customize the view.

### Display Modes
- **Insertion Order**: Display tasks in the order they were added. This is useful for tracking the sequence of tasks.
- **Priority Order**: Display tasks sorted by priority (High > Medium > Low). This helps you focus on the most important tasks first.

### Filter Options
- **All**: Show all tasks, regardless of their status.
- **Completed**: Show only tasks that have been marked as completed.
- **Incomplete**: Show only tasks that are still incomplete.

---

## Testing Environment
A testing environment can be set up to experiment with the application. Follow these steps:
1. Ensure Python is installed on your system (Python 3.6 or higher recommended).
2. Download the Python script (`task_manager.py`).
3. Run the script using the command:
   ```bash
   python task_manager.py