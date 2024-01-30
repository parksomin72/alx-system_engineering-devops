#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_number_of_tasks(id):
    """ Check number of tasks in CSV """

    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Skip the header
        for _ in csv_reader:
            num_lines += 1

    if total_tasks == num_lines:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")


def check_user_info(id):
    """ Check user information """

    response = requests.get(users_url + str(id)).json()
    username = response[0]['username']

    with open(str(id) + ".csv", 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Skip the header
        for row in csv_reader:
            if row[0] != str(id) or row[1] != username:
                print("User ID or Username: Incorrect")
                return

    print("User ID and Username: OK")


def check_output_formatting(id):
    """ Check CSV formatting """

    response = requests.get(todos_url).json()
    with open(str(id) + ".csv", 'r') as f:
        csv_reader = csv.reader(f)
        output = list(csv_reader)

        count = 0
        flag = 0
        for i in response:
            if i['userId'] == id:
                url = users_url + str(i['userId'])
                usr_resp = requests.get(url).json()
                line = [str(i['userId']), usr_resp[0]['username'], str(i['completed']), i['title']]
                count += 1
                if line not in output:
                    print("Task {} Formatting: Incorrect".format(count))
                    flag = 1

        if flag == 0:
            print("Formatting: OK")


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # Check number of tasks
    check_number_of_tasks(user_id)

    # Check user info
    check_user_info(user_id)

    # Check output formatting
    check_output_formatting(user_id)
