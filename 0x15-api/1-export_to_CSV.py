#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": id}).json()
    csv_filename = "{}.csv".format(id)
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for dos in todo:
            writer.writerow([id, username, dos.get(
                "completed"), dos.get("title")])
