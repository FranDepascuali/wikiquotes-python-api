import os
import sys

def __is_visible_directory__(directory):
    return not '.' in directory and not "__" in directory

def __all_subdirectories__(directory):
    return [x[0] for x in os.walk(wikiquotes_directory)]

wikiquotes_directory = os.path.abspath(os.path.join(os.path.dirname(__file__)))
visible_subdirectories = filter(__is_visible_directory__, __all_subdirectories__(wikiquotes_directory))

for subdirectory in visible_subdirectories:
    sys.path.append(subdirectory)
