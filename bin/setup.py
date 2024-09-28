import sys
import os


def add_src_path():
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if src_path not in sys.path:
        sys.path.append(src_path)
