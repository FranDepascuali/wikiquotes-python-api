# import sys
# def _get_python_version():
#     version = sys.version_info
#     return (version.major, version.minor)
#
# python_version = _get_python_version()
#
# import os
#
# if python_version[0] == 2:
#     # In python 3.x, the default encoding is already utf8.
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
#
# def __is_visible_directory__(directory):
#     return not '.' in directory and not "__" in directory
#
# def __all_subdirectories__(directory):
#     return [x[0] for x in os.walk(wikiquotes_directory)]
#
# def _look_for(subdirectory_name, directories):
#     # We add list to support filter in python 3.x (because it returns an iterable)
#     # In python 2.x, list(list) behaves as identity (list([1,2]) is [1,2])
#     return list(filter(lambda subdirectory: subdirectory_name in subdirectory, directories))[0]
#
# for subdirectory in visible_subdirectories:
#     sys.path.append(subdirectory)

# languages_directory = _look_for("languages", visible_subdirectories)
# authors_directory = _look_for("authors", visible_subdirectories)
# logs_directory = _look_for("logs", visible_subdirectories)
# log_path = os.path.join(logs_directory, "debug.log")
