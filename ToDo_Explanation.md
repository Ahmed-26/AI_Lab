# To-Do List (Dynamic)

**Name:** Ahmed Rasheed  
**Roll no:** SU92-BSDSM-F24-021

---

## Code Explanation

This Python code implements a simple, interactive To-Do list system that runs in the terminal. The user can add, remove, and view tasks dynamically. The program continues to prompt the user for actions until they choose to exit.

### How the Code Works

1. **Task Storage:**

   - All tasks are stored in a list called `tasks`.

2. **Display Function:**

   - The `show_tasks()` function prints the current list of tasks. If there are no tasks, it notifies the user.

3. **Main Loop:**

   - The program runs an infinite loop, showing options to the user:
     - Add Task
     - Remove Task
     - Show Tasks
     - Exit
   - The user selects an option by entering a number (1-4).

4. **Adding a Task:**

   - If the user selects '1', they are prompted to enter a new task, which is then added to the `tasks` list.

5. **Removing a Task:**

   - If the user selects '2', the current tasks are displayed.
   - The user is asked to enter the number of the task to remove.
   - The code checks if the input is valid and removes the selected task.

6. **Showing Tasks:**

   - If the user selects '3', the current list of tasks is displayed.

7. **Exiting:**

   - If the user selects '4', the program prints a closing message and exits the loop.

8. **Input Validation:**
   - The code checks for invalid options and handles errors (like entering a non-number when removing a task).

---

## What the Code is Doing

- The code provides a simple way to manage a list of tasks from the terminal.
- It allows the user to add as many tasks as they want, remove any task by its number, and view the current list at any time.
- The program is interactive and continues running until the user chooses to exit.
- All actions and errors are clearly communicated to the user.

This makes it a practical example of a dynamic, menu-driven To-Do list in Python.

---

## Example Session / Output

```
Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 1
Enter new task: Buy groceries
Task added.

Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 1
Enter new task: Finish assignment
Task added.

Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 3
Your To-Do List:
1. Buy groceries
2. Finish assignment

Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 2
Your To-Do List:
1. Buy groceries
2. Finish assignment
Enter task number to remove: 1
Removed: Buy groceries

Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 3
Your To-Do List:
1. Finish assignment

Options: 1) Add Task  2) Remove Task  3) Show Tasks  4) Exit
Choose an option (1-4): 4
To-Do Task System Closed.
```
