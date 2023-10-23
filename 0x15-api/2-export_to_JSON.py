#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({user_id: [{
                "task": tool.get("title"),
                "completed": tool.get("completed"),
                "username": username
            } for tool in todos]}, json_file)
