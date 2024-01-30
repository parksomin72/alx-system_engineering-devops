#!/usr/bin/python3
"""Fetch and export employee todos info to CSV
"""
import requests
import csv
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


def export_to_csv(user_data, todos_data):
    user_id = user_data.get('id')
    username = user_data.get('username')
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed_status = str(task['completed'])
            task_title = task['title']
            csv_writer.writerow([user_id, username, task_completed_status, task_title])


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee id>")
        exit()

    employee_id = argv[1]
    user_data = fetch_user_data(employee_id)

    if not user_data:
        exit()

    todos_data = fetch_todo_data(employee_id)
    export_to_csv(user_data, todos_data)
    print(f"Data exported to {employee_id}.csv")
