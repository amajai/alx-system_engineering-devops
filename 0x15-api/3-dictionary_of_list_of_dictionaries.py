#!/usr/bin/python3
"""
module to gather data from an API to json
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    user_todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    users_data = requests.get(users_url).json()

    all_users = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        user_data = []

        user_todos_data = requests.get(user_todos_url.format(user_id)).json()

        for todo in user_todos_data:
            task_data = {}
            task_data['task'] = todo.get('title')
            task_data['completed'] = todo.get('completed')
            task_data['username'] = username
            user_data.append(task_data)
        all_users[user_id] = user_data

    with open('todo_all_employees.json', "w", encoding='utf-8') as f:
        f.write(json.dumps(all_users))
