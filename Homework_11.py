import os
from typing import Tuple, Dict, Any

DEBUG_MODE = True


def return_dict_name(path) -> dict:
    list_dir = os.listdir(path)
    for filename in list_dir:
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            files_list.append(filename)
        else:
            dirs_list.append(filename)
    dict_name = {'filenames': files_list,
                 'dirnames': dirs_list,
                 }
    return dict_name


def return_reverse_dict(result_1, debug_mode=DEBUG_MODE) -> dict:
    global files_list, dirs_list
    for key, value in result_1.items():
        if key == 'filenames':
            files_list = value
        if key == 'dirnames':
            dirs_list = value
    if debug_mode:
        files_dirs_dict_sort = {'filenames': sorted(files_list),
                                'dirnames': sorted(dirs_list),
                                }
    else:
        files_dirs_dict_sort = {'filenames': sorted(files_list, reverse=True),
                                'dirnames': sorted(dirs_list, reverse=True),
                                }
    return files_dirs_dict_sort


def add_files_dirs(result_1: dict, file_name: str) -> Tuple[Dict[str, Any], str]:
    global files_list, dirs_list
    for key, value in result_1.items():
        if key == 'filenames':
            files_list = value
        if key == 'dirnames':
            dirs_list = value
    if os.path.isfile(file_name):
        files_list.append(file_name)
    if os.path.isdir(file_name):
        dirs_list.append(file_name)
    add_new_files_dirs = {'filenames': files_list,
                          'dirnames': dirs_list,
                          }
    return add_new_files_dirs, file_name


path = 'test_dir'
files_list = []
dirs_list = []
file_name = 'test.py'

result_1 = return_dict_name(path)
result_2 = return_reverse_dict(result_1, DEBUG_MODE)
result_3 = add_files_dirs(result_1, file_name)
