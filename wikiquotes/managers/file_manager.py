from functools import wraps
import os.path
import shutil

def ensure_file_exists(file_path):
    if not file_exists(file_path):
        raise IOError('File does not exist: %s' % file_path)

def ensure_directory_exists(directory_path):
    if not directory_exists(directory_path):
        raise IOError('Directory does not exist: %s' % directory_path)

def ensure_file_not_exists(file_path):
    if file_exists(file_path):
        raise IOError('File already exist: %s' % file_path)

def ensure_directory_not_exists(directory_path):
    if directory_exists(directory_path):
        raise IOError('Directory already exist: %s' % directory_path)

def file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)

def directory_exists(directory_path):
    return os.path.exists(directory_path) and os.path.isdir(directory_path)

def create_directory_if_not_exists(directory_path):
    if not directory_exists(directory_path):
        os.makedirs(directory_path)
        return

def delete_directory(directory_path):
    if directory_exists(directory_path):
        shutil.rmtree(directory_path, ignore_errors=True)

def delete_file(file_path):
    if file_exists(file_path):
        os.remove(file_path)

def last_component_of(file_path):
    return os.path.basename(file_path)

def directory_of(file_path):
    return os.path.dirname(file_path)

def list_relative_files_with_extension(directory, extension):
    return filter(lambda filename: filename.endswith(extension), os.listdir(directory))

def list_absolute_files_with_extension(directory, extension):
    relative_paths = list_relative_files_with_extension(directory, extension)
    return map(lambda relative_path: join(directory, relative_path), relative_paths)

def join(baseurl, path_to_append):
    ensure_directory_exists(baseurl)
    return os.path.join(baseurl, path_to_append)
