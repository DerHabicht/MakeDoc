#!/bin/bash

# TODO: Make this file path agnostic
ln -s $HOME/lib/MakeDoc/Makefile
ln -s $HOME/lib/MakeDoc/build.sh build
ln -s $HOME/lib/MakeDoc/todo.py todo

# TODO: Create a generic .gitignore file
# TODO: Create some basic macros
touch .texmacros
touch .htmlmacros
touch .docmacros

# TODO: Interactively create a makedoc file
touch .makedoc

# TODO: Create a basic LaTeX template file
