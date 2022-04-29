import os

DEBUG_MODE = True


def return_dict_name(path: str) -> dict:
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


def return_reverse_dict(result_1: dict, debug_mode=DEBUG_MODE) -> dict:
    if debug_mode:
        files_dirs_dict_sort = {'filenames': sorted(result_1['filenames']),
                                'dirnames': sorted(result_1['dirnames']),
                                }
    else:
        files_dirs_dict_sort = {'filenames': sorted(result_1['filenames'], reverse=True),
                                'dirnames': sorted(result_1['dirnames'], reverse=True),
                                }
    return files_dirs_dict_sort


def add_files_dirs(result_1: dict, file_name: str) -> dict:
    if '.' in file_name:
        add_new_files_dirs = {'filenames': result_1['filenames'] + [file_name]}
    else:
        add_new_files_dirs = {'dirnames': result_1['dirnames'] + [file_name]}

    return add_new_files_dirs


path = 'test_dir'
files_list = []
dirs_list = []
file_name = 'test.py'

result_1 = return_dict_name(path)
result_2 = return_reverse_dict(result_1, DEBUG_MODE)
result_3 = add_files_dirs(result_1, file_name)
