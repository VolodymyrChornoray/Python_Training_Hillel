from utils.reading_file import read_txt_file_as_str


def get_domains(filename: str) -> list:
    domains_text = read_txt_file_as_str(filename)
    for line in domains_text.split('\n'):
        if line:
            domain = line.replace('.', '')
            domains_list.append(domain)

    return domains_list


def get_names(filename: str) -> list:
    names_text = read_txt_file_as_str(filename)
    for line in names_text.split('\n'):
        if line:
            names = line.split('\t')[1]
            family_names_list.append(names)

    return family_names_list


def get_authors(filename: str) -> list:
    authors = read_txt_file_as_str(filename)
    for line in authors.split('\n'):
        if '-' in line:
            birthday_date = line.split('-')[0]
            birthday_list.append({"date": birthday_date})
    return birthday_list


domains_list = []
family_names_list = []
birthday_list = []

if __name__ == "__main__":
    filename = "domains.txt"
    filename = f"../Homework/{filename}"
    domains = get_domains(filename)
    print(domains)

    filename = "names.txt"
    filename = f"../Homework/{filename}"
    names = get_names(filename)
    print(names)

    filename = "authors.txt"
    filename = f"../Homework/{filename}"
    birthday = get_authors(filename)
    print(birthday)
