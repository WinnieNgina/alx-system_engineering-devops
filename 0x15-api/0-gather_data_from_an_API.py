#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    # .json() converts json string in to a dictionary
    todo = requests.get(url + "todos", params={"userId": id}).json()
    completed = []
    for dos in todo:
        if dos.get("completed") is True:
            completed.append(dos.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    for i in completed:
        print("\t {}".format(i))
