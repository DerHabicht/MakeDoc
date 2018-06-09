from enum import Enum
from taskw import TaskWarrior


TW = TaskWarrior()


class DocumentType(Enum):
    GENERIC = 0
    IDD = 1


def new_doc_tasks(doctype=DocumentType.IDD):
    if doctype == DocumentType.GENERIC:
        pass
    elif doctype == DocumentType.IDD:
        pass
