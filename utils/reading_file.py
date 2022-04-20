import os

DEBUG_MODE = True  # переменная, пишеться с большой буквы, чтобы показать, что она относиться ко всему вашему файлу(глобальная)


def read_txt_file_as_str(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    return data


# if __name__ == "__main__":
#     path = "../Homework"
#     filename = '_.txt'
#     data = read_txt_file_as_str(os.path.join(path, filename))
#     print(data)

