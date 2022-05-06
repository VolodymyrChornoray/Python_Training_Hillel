import os


class WorkWithFolders:
    def __init__(self, path, my_str):
        self.path = path
        self.status = True
        self.sorting = self.create_folder_describe()
        self.my_str = my_str
        self.list_dir = self.create_folder_describe()
        self.dir_name = 'create_test_dir'
        self.new_folder_name = self.create_folder_describe()
        self.compare_and_create_objects()

    def create_folder_describe(self):
        list_dir = os.listdir(self.path)
        dirs_list = []
        files_list = []
        for filename in list_dir:
            filepath = os.path.join(self.path, filename)
            if os.path.isdir(filepath):
                dirs_list.append(filename)
            elif os.path.isfile(filepath):
                files_list.append(filename)
        return {'filenames': files_list, 'dirnames': dirs_list}

    def sort_folder_objects(self) -> dict:
        if self.status:
            self.sorting["filenames"].sort()
            self.sorting["dirnames"].sort()
        else:
            self.sorting["filenames"].sort(reverse=True)
            self.sorting["dirnames"].sort(reverse=True)
        return self.sorting

    def update_folder_objects(self):
        key = 'filenames' if "." in self.my_str else 'dirnames'
        self.list_dir[key].append(self.my_str)
        return self.list_dir

    def compare_and_create_objects(self):
        dir_list = os.listdir(self.dir_name)
        for value in self.new_folder_name["filenames"]:
            if not value in dir_list:
                with open(os.path.join(self.dir_name, value), 'w') as file:
                    file.close()
        for value in self.new_folder_name["dirnames"]:
            os.makedirs(os.path.join(self.dir_name, value), exist_ok=True)


worker = WorkWithFolders("../test_dir", "str.txt")

result1 = worker.create_folder_describe()
result2 = worker.sort_folder_objects()
result3 = worker.update_folder_objects()

print(f'\n#1\n{result1}\n\n#2\n{result2}\n\n#3\n{result3}\n\n')

worker.compare_and_create_objects()
