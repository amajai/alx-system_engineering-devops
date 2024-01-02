#!/usr/bin/python3
"""
module to gather data from an API to CSV
"""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    user_todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    user_data = requests.get(user_url.format(user_id)).json()
    user_todos_data = requests.get(user_todos_url.format(user_id)).json()
    username = user_data["username"]
    with open('{}.csv'.format(user_id), "w", encoding='utf-8') as f:
        for todo in user_todos_data:
            csv_data = '"{}","{}","{}","{}"\n' \
                .format(user_id, username, todo['completed'], todo['title'])
            f.write(csv_data)
