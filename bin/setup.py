import sys
import os


def add_src_path():
    folders = ["..", "../src"]
    for folder in folders:
        src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), folder))
        if src_path not in sys.path:
            sys.path.append(src_path)
