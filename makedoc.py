#!/usr/bin/python3.6

"""MakeDoc
Copyright (C) 2018 Robert Herschel Hawk

Usage:
    makedoc
    makedoc generate [options] <directory>
    makedoc add <part>
    makedoc parse tasks [options]

Options:
    -h, --help                    Show this help.
    -t DOCTYPE, --type=DOCTYPE    Define type of document to generate.
                                  The generator can make the following types:
                                    - generic (default)
                                    - idd
    -p NAME, --project=NAME       Project name to pass to Taskwarrior.
    --taskwarrior                 Have the generator create initial TW tasks.
    --version                     Show version.
"""

from docopt import docopt

from generator import idd_add_part, initial_design_doc
from taskwarrior import parse_idd_tasks

VERSION = "MakeDoc 2.0.0-alpha"

if __name__ == '__main__':
    arguments = docopt(__doc__, version=VERSION)

    if arguments['generate']:
        if arguments['--type'] == 'idd':
            initial_design_doc(arguments['<directory>'])
    elif arguments['add']:
        idd_add_part(arguments['<part>'])
    elif arguments['parse']:
        if arguments['tasks']:
            if arguments['--type'] == 'idd':
                parse_idd_tasks(arguments['--project'])
            else:
                pass
