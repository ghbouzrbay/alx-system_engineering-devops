#!/usr/bin/python3
"""script that fetches info about a given employee using an api
and exports it in json format
"""
import json
import requests
import sys


baseurl = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    userid = sys.argv[1]
    userurl = '{}/users?id={}'.format(baseurl, userid)
    response = requests.get(userurl)
    data = response.text
    data = json.loads(data)
    username = data[0].get('username')
    tasksurl = '{}/todos?userId={}'.format(baseurl, userid)
    response = requests.get(tasksurl)
    tasks = response.text
    tasks = json.loads(tasks)
    dictionarykey = str(userid)
    builder = {dictionarykey: []}
    for task in tasks:
        f_jsondata = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        builder[dictionarykey].append(f_jsondata)
    encoded_jsondata = json.dumps(builder)
    with open('{}.json'.format(userid), 'w', encoding='UTF8') as myFile:
        myFile.write(encoded_jsondata)
