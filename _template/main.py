import re
from enum import Enum
from copy import deepcopy
from pprint import pprint
from functools import reduce, cmp_to_key
from itertools import groupby, combinations, permutations
from time import time
from queue import PriorityQueue
from math import prod, ceil, comb, perm
from collections import defaultdict
from dataclasses import dataclass
from bisect import insort
import numpy as np
import string
import sys

file = sys.argv[1] if len(sys.argv) > 1 else "ex1"
lines = list(map(lambda l: l.rstrip(), open(file + ".txt").readlines()))

# ----------------------------------------------------------------------
# * Parsing(/setup)


# ----------------------------------------------------------------------
# * Part 1


# ----------------------------------------------------------------------
# * Part 2
