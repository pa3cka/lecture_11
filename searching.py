import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """
    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name) #spoji cestu do adresara a nazov suboru

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)

    return seq[key]


def main():
    read_data(file_name='sequential.json', key='unordered_numbers')
    pass


if __name__ == '__main__':
    main()