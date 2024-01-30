#!/usr/bin/python3
"""Fetch employee todos info and export into csv format
"""
import csv
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


def export_to_csv(employee_id, username, todos_data):
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, 'w', newline='\n') as csv_file:
        fieldnames = ["userId", "username", "completed", "title"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for task in todos_data:
            writer.writerow({
                "userId": employee_id,
                "username": username,
                "completed": str(task.get('completed')),
                "title": task.get('title')
            })


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee id>")
        exit()

    employee_id = argv[1]
    user_data = fetch_user_data(employee_id)

    if not user_data:
        exit()

    username = user_data.get('username')
    todos_data = fetch_todo_data(employee_id)

    export_to_csv(employee_id, username, todos_data)
    print(f"Data exported to {employee_id}.csv")
