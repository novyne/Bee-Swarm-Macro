# This file makes the macros directory a Python package
import sys
import os

# Add the parent directory to Python path so macros can import from utils
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
