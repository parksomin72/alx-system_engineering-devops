#!/usr/bin/python3
"""Fetch employee todos info
"""
import requests
from sys import argv


def fetch_user_data(employee_id):
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    return user_response.json()


def fetch_todo_data(employee_id):
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    return todos_response.json()


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee id>")
        exit()

    employee_id = argv[1]
    user_data = fetch_user_data(employee_id)

    if not user_data:
        exit()
    else:
        employee_name = user_data.get('name')

    todos_data = fetch_todo_data(employee_id)
    completed_tasks = [
    task['title'] for task in todos_data if task['completed']
    ]

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(todos_data)}):")

    for task_title in completed_tasks:
        print(f"\t {task_title}")
