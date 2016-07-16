import sys
from os.path import join, dirname

PACKAGE_PATH = dirname(__file__)
LIB_PATHS = [
    join(PACKAGE_PATH, "win32"),
    join(PACKAGE_PATH, "win32", "lib")
]

for lib in LIB_PATHS:
    if lib not in sys.path:
        sys.path.append(lib)
