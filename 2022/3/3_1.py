import string

with open("data.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]


def sum_of_priorities(data):
    sum = 0
    value_of_item = " " + string.ascii_lowercase + string.ascii_uppercase



    for i in data:
        half = len(i)//2
        first = list(set(i[:half]))
        second = list(set(i[half:]))
        mistake = [item for item in first if item in second]

        print(value_of_item.index(mistake[0]))
        sum += value_of_item.index(mistake[0])
    return sum


print(sum_of_priorities(data))

"""
print(first)
        print(second)
        if len(first) != len(second):
            print(False)
            
            
value_of_item = list(enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1))
"""