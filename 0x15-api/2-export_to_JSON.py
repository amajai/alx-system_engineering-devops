#!/usr/bin/python3
"""
module to gather data from an API to json
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    user_todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    user_data = requests.get(user_url.format(user_id)).json()
    user_todos_data = requests.get(user_todos_url.format(user_id)).json()

    username = user_data["username"]
    json_data = {user_id: []}
    for todo in user_todos_data:
        task_data = {}
        task_data['task'] = todo.get('title')
        task_data['completed'] = todo.get('completed')
        task_data['username'] = username
        json_data.get(user_id).append(task_data)

    with open('{}.json'.format(user_id), "w", encoding='utf-8') as f:
        f.write(json.dumps(json_data))
