with open("data.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]


def format_input(line):
    first, second = [item.split("-") for item in line.split(",")]
    first = [int(x) for x in first]
    second = [int(x) for x in second]
    return [first, second]


def is_fully_containing(list_w_2cand):
    first = list_w_2cand[0]
    second = list_w_2cand[1]
    if first[0] <= second[0] <= second[1] <= first[1]:
        return True
    elif second[0] <= first[0] <= first[1] <= second[1]:
        return True
    return False


total = 0

for i in data:
    candidates = format_input(i)
    if is_fully_containing(candidates):
        total += 1

print(total)

"""
def camp_cleanup(list_w_2cand):
    first = list_w_2cand[0]
    second = list_w_2cand[1]

    for i in data:
        lines += 1
        first, second = [item.split("-") for item in i.split(",")]
        first = [int(x) for x in first]
        second = [int(x) for x in second]
        print([first, second])
        if first[0] <= second[0] <= second[1] <= first[1]:
            total += 1
        if second[0] <= first[0] <= first[1] <= second[1]:
            total += 1
    print(lines)
    return total

"""

if __name__ == '__main__':
    pass