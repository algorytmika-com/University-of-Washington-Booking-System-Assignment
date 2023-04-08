"""
    Dummy conftest.py for assignment07.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import pytest, sys, os
from pathlib import Path

#set enviroment ot recognize modules
folder = "/../src/assignment07"
sys.path.insert(0, Path(os.path.dirname(os.path.abspath(__file__)) + folder))