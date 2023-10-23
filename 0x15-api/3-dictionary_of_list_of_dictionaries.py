#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            user.get("id"): [{
                "task": tool.get("title"),
                "completed": tool.get("completed"),
                "username": user.get("username")
            } for tool in requests.get(base_url + "todos",
                                       params={"userId": user.get("id")}).json()]
            for user in users}, json_file)
