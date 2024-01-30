#!/usr/bin/python3
"""
Check student .CSV output of user information
"""

import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
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


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
