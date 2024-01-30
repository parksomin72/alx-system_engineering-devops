#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress from a REST API.
"""

import requests
import sys

def gather_data(employee_id):
    """
    Gather and display information about an employee's TODO list progress.
    """
    # API endpoint URL
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

        # Parse JSON response
        todo_list = response.json()

        # Extract relevant information
        employee_name = todo_list[0]['username']
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])

        # Display information in the specified format
        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todo_list:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error accessing API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Retrieve employee ID from command-line argument
    employee_id = int(sys.argv[1])

    # Call the gather_data function with the provided employee ID
    gather_data(employee_id)

