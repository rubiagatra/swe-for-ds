import os

import numpy as np
import time


def foo():
    pass


def do_blah_thing():
    pass


# Correct:
if foo == "blah":
    do_blah_thing()

# Wrong:
if foo == "blah": do_blah_thing()
