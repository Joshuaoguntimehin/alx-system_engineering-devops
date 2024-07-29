#!/usr/bin/python3
"""import statement"""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """ URL for fetching user data"""
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    """Fetch user data"""
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error fetching user data")
        return

    """ Extract user data"""
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # URL for fetching todos
    todos_url = f'https://jsonplaceholder.typicode.com/todos'

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error fetching todos data")
        return

    # Extract todos data
    todos_data = todos_response.json()

    # Filter todos for the specific employee
    employee_todos = [todo for todo in todos_data
                      if todo['userId'] == employee_id]

    # Calculate completed and total tasks
    total_tasks = len(employee_todos)
    completed_tasks = [todo for todo in employee_todos
                       if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Output the employee's TODO list progress
    print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done_tasks}/{total_tasks}): "
            )
    # Output the titles of completed tasks
    for todo in completed_tasks:
        print(f"\t {todo['title']}")


def main():
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid employee ID. Please enter an integer.")


if __name__ == "__main__":
    main()
