from enum import Enum
from hashlib import md5
from os import walk
from os.path import join
from re import finditer
from taskw import TaskWarrior
from taskw.exceptions import TaskwarriorError


TW = TaskWarrior()


class DocumentType(Enum):
    GENERIC = 0
    IDD = 1


def _read_todos_from_tex_file(filename, doctype=DocumentType.IDD):
    with open(filename, 'r') as f:
        text = f.read()

    todos = []
    for match in finditer(r'.*\\todo.*{(.*)}', text):
        todos.append(match.group(1))

    return todos


def _create_task(project, description):
    twi_hash = md5(description.upper().encode('utf-8')).hexdigest()
    task_id, _ = TW.get_task(twi_hash=twi_hash)

    if task_id:
        print(f'Task "{description}" has already been added. Skipping.')

    try:
        TW.task_add(description, project=project, twi_hash=twi_hash)
    except TaskwarriorError:
        print(f'Failed to add "{description}" for project "{project}"')


def new_doc_tasks(doctype=DocumentType.IDD):
    if doctype == DocumentType.GENERIC:
        pass
    elif doctype == DocumentType.IDD:
        pass


def parse_idd_tasks(project):
    if not project:
        pass

    todos = []
    for path, _, files in walk('.'):
        for f in files:
            if f.endswith('.tex'):
                todos.extend(_read_todos_from_tex_file(join(path, f)))

    for todo in todos:
        _create_task(project, todo)
