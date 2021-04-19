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




def linear_search(sequence, number):
    """
    Function finds positions and count of searched number.
    :param sequence: (list) list in which we are searching positions and count of number
    :param number: (int) input number
    :return: (dict) dict of positions and count of searched number
    """
    positions = list()
    count = 0

    idx = 0
    while idx < len(sequence):
        if sequence[idx] == number:
            positions.append(idx)
            count += 1
        idx += 1

    return {"positions": positions, "count": count}

    pass




def pattern_search(sequence, pattern):
    """
    Function finds positions of all searched patterns.
    :param sequence: (str) string in which we are searching patterns
    :param pattern: (str) searched pattern
    :return: (set) positions of pattern
    """
    positions_of_pattern = set()

    left_idx, right_idx = 0, len(pattern)

    while right_idx < len(sequence):
        if sequence[left_idx:right_idx] == pattern:
            positions_of_pattern.add(left_idx + len(pattern) // 2)
        left_idx += 1
        right_idx += 1

    return positions_of_pattern
    pass




def main():
    """
    Driver function.
    :return:
    """
    sequence = read_data(file_name='sequential.json', key='unordered_numbers')
    searched_number = input("Zadaj cislo.")
    result_1 = linear_search(sequence=sequence, number=int(searched_number))

    sequence = read_data(file_name='sequential.json', key='dna_sequence')
    result_2 = pattern_search(sequence=sequence, pattern='ATA')
    pass


if __name__ == '__main__':
    main()