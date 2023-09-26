#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    # Initialize an empty dictionary to store the data
    data = {}
    # Loop through the users
    for user in users:
        id = user.get("id")
        user_data = []
        # Fetch the user's todos
        todos = requests.get(url + "todos", params={"userId": id}).json()
        # Loop through the todos and extract the required information
        for todo in todos:
            task_data = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
            }
            user_data.append(task_data)
            # Add the user's data to the dictionary
            data[id] = user_data
            # Write the data to the JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
