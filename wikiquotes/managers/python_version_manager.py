import sys

major = sys.version_info.major
minor = sys.version_info.minor
python_version = (major, minor)

def is_python_2():
    return python_version[0] == 2

def is_python_3():
    return python_version[0] == 3
