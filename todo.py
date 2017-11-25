#!/usr/bin/python3.6

from re import search
from subprocess import run, PIPE
from os import getcwd

import json


def read_todos():
    todos = []

    output = run(["git", "grep", "-n", "TODO:"], stdout=PIPE, cwd=getcwd())
    result = output.stdout.decode()

    lines = result.split("\n")

    for line in lines:
        try:
            regex = search(r"(.+?):(\d+):.+TODO:\s([\w\s\'\",:;\.]+)", line)
            todo = {"file": regex.group(1),
                    "line": regex.group(2),
                    "task": regex.group(3).strip()}
            todos.append(todo)
        except AttributeError:
            pass

    return todos


def write_json(todos):
    with open("todos.json", "w") as todo_file:
        todo_file.write(json.dumps(todos, sort_keys=True, indent=2))


if __name__ == "__main__":
    todos = read_todos()
    write_json(todos)

