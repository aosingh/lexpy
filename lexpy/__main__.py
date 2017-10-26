import sys
from io import IOBase

PYTHON_3 = sys.version_info[0] == 3
if PYTHON_3:
    file = IOBase