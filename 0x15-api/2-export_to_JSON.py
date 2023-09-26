#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": id}).json()
    data_to_dump = {id: []}
    for dos in todo:
        data_to_dump[id].append({
            "task": dos.get("title"),
            "completed": dos.get("completed"),
            "username": username
        })
        with open("{}.json".format(id), "w") as jsonfile:
            json.dump(data_to_dump, jsonfile)
