#!/usr/bin/python3
"""
module to gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"
    user_todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"

    user_data = requests.get(user_url.format(user_id)).json()
    user_todos_data = requests.get(user_todos_url.format(user_id)).json()

    total_tasks = len(user_todos_data)
    complete_tasks = []
    for todo in user_todos_data:
        if todo["completed"]:
            complete_tasks.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(user_data["name"], len(complete_tasks), total_tasks)
          )

    for done_task in complete_tasks:
        print("\t {}".format(done_task))
