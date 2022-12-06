import re

with open("data.txt") as file:
    data = file.read()

print(data[0:50])


def index_end_of_first_foursome(txt_string, length_of_start_pocket):
    def has_unique_chars(sequence):
        if len(list(set(sequence))) == len(sequence):
            return True

    for i in range(0, len(txt_string)):
        foursome = txt_string[i:i+length_of_start_pocket]
        if has_unique_chars(foursome):
            return i+length_of_start_pocket


print(index_end_of_first_foursome(data, 4))
print(index_end_of_first_foursome(data, 14))

