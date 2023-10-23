#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""

import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    name = data[0].get('name')
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)
    completed = 0
    total_tasks = len(tasks)
    tasks_cmp = []
    for task in tasks:

        if task.get('completed'):
            tasks_cmp.append(task)
            completed += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in tasks_cmp:
        print("\t {}".format(task.get('title')))
