#!/usr/bin/python3

from glob import glob

def get_preproc_name(filename):
    """ Get the name of a .m4 file after preprocessing. """
    return filename[:-3]

if __name__ == "__main__":

    # Grab known-raw files
    filenames = []
    for filename in glob("*.m4"):
        filenames.append(filename)

    # Grab all source files
    for filename in glob("*.md"):
        # Filter out files that have been run through the preprocessor
        if filename not in list(map(get_preproc_name, filenames)):
            filenames.append(filename)

    # Read the source files
    text = ""
    for filename in filenames:
        with open(filename, 'r') as file:
            text += file.read()

    # Print the word count to the terminal
    print(len(text.split()))
