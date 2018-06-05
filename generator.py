from datetime import date
from os import getcwd, makedirs
from os.path import basename

import templates


def idd_add_part(part):
    mainfilename = basename(getcwd())
    print('Component Name:', end=' ')
    name = input()

    # Main LaTeX File
    with open(f'{mainfilename}.tex', 'r') as mainfile:
        maintext = mainfile.read().split(r'\bookmarksetupnext{level=part}')

    parttext = \
        templates.IDD_MAIN_PARTS.replace('%%%NAME%%%', name)
    parttext = parttext.replace('%%%SHORT_NAME%%%', part)
    maintext[0] = (maintext[0]
                   + parttext
                   + r'\bookmarksetupnext{level=part}' + '\n')
    fulltext = ''.join(maintext)
    with open(f'{mainfilename}.tex', 'w') as mainfile:
        mainfile.write(fulltext)

    # Components file
    with open('components.tex', 'a') as componentsfile:
        section = templates.IDD_COMPONENTS_SECTION
        section = section.replace('%%%COMPONENT_NAME%%%', name)
        section = section.replace('%%%SHORT_NAME%%%', part)
        componentsfile.write(section)

    makedirs(part)
    with open(f'{part}/spec.tex', 'w') as specfile:
        text = templates.IDD_SPECIFICATION
        text = text.replace('%%%SHORT_NAME%%%', part)
        specfile.write(text)

    with open(f'{part}/schema.tex', 'w') as specfile:
        text = templates.IDD_SCHEMA
        text = text.replace('%%%SHORT_NAME%%%', part)
        specfile.write(text)

    with open(f'{part}/processes.tex', 'w') as specfile:
        text = templates.IDD_PROCESSES
        text = text.replace('%%%SHORT_NAME%%%', part)
        specfile.write(text)

    with open(f'{part}/testing.tex', 'w') as specfile:
        text = templates.IDD_TEST_CASES
        text = text.replace('%%%SHORT_NAME%%%', part)
        specfile.write(text)


def initial_design_doc(dir):
    print('Project Name:', end=' ')
    name = input()
    print('Author Name:', end=' ')
    author = input()
    print('Author Initials:', end=' ')
    initials = input()

    makedirs(dir)
    with open(f'{dir}/Makefile', 'w') as makefile:
        makefiletext = \
            templates.IDD_MAKEFILE.replace('%%%SHORT_NAME%%%', dir)
        makefile.write(makefiletext)

    with open(f'{dir}/{dir}.tex', 'w') as main:
        maintext = \
            templates.IDD_MAIN.replace('%%%PROJECT_NAME%%%', name)
        maintext = \
            maintext.replace('%%%AUTHOR_NAME%%%', author)
        maintext = \
            maintext.replace('%%%SHORT_NAME%%%', dir)
        main.write(maintext)

    with open(f'{dir}/vhistory.tex', 'w') as vhistory:
        vhistorytext = \
            templates.IDD_VERSION_HISTORY.replace('%%%AUTHOR%%%', initials)
        vhistorytext = \
            vhistorytext.replace('%%%DATE%%%',
                                 date.today().strftime('%Y-%m-%d'))
        vhistory.write(vhistorytext)

    with open(f'{dir}/purpose.tex', 'w') as purpose:
        purpose.write(templates.IDD_PURPOSE)

    with open(f'{dir}/components.tex', 'w') as components:
        components.write(templates.IDD_COMPONENTS)
