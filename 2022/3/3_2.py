import string

with open("data.txt") as file:
    data = file.readlines()
    length = len(data)


def sum_of_priorities(length):
    file = open("data.txt", "r")
    sum = 0
    value_of_item = " " + string.ascii_lowercase + string.ascii_uppercase
    try:
        for j in range(99):
            for i in range(3):
                first = file.readline().strip()
                second = file.readline().strip()
                third = file.readline().strip()
                print(third)
                badge = [item for item in first if item in second if item in third]
                print(badge)
                sum += value_of_item.index(badge[0])
    except IndexError:
        file.close()
        return sum


print(sum_of_priorities(99))


"""

    for i in data:
        half = len(i)//2
        first = list(set(i[:half]))
        second = list(set(i[half:]))
        mistake = [item for item in first if item in second]

        print(value_of_item.index(mistake[0]))
        sum += value_of_item.index(mistake[0])

    file.close()
    return sum


print(first)
        print(second)
        if len(first) != len(second):
            print(False)


value_of_item = list(enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1))
"""