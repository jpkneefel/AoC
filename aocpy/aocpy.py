from IPython.display import display
import ipywidgets as widgets
import sys
import os
from os import listdir
from os.path import isfile, join
import re
import ast
from aocd.models import Puzzle


def init(day, year):
    num = re.compile(r"(\d+)")

    puzzle = Puzzle(year=year, day=day)

    global DATA
    DATA = {"input": puzzle.input_data, "example": puzzle.example_data}

    files = [f for f in listdir('.') if isfile(join('.', f))]
    pat = re.compile('(ex(\d)+.txt)')
    files = [f for f in files if pat.match(f)]

    global box
    box = widgets.Select(
        options=["input", "example"] + files,
        value='example',
        rows=4,
        description='Input file:',
        disabled=False
    )

    display(box)


def get_lines():
    name = box.value
    data = None
    if name in DATA:
        print("Done reading \"{name}\"".format(name=box.value))
        data = DATA[name].splitlines()
    else:
        data = open(name, 'r').read()
        print("Done reading \"{name}\"".format(name=box.value))
    return list(map(lambda l: l.rstrip(), data))


def print_bools(mat):
    for row in mat:
        print("".join(["." if x else "#" for x in row]))


def print_mat(mat):
    for row in mat:
        print("".join(row))


def add_tuple(a, b):
    return tuple(x + y for x, y in zip(a, b))
