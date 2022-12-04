with open("data.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]


def format_input(line):
    first, second = [item.split("-") for item in line.split(",")]
    first = [int(x) for x in first]
    second = [int(x) for x in second]
    return [first, second]


def is_overlapping(list_w_2cand):
    first = list_w_2cand[0]
    second = list_w_2cand[1]
    print(f"1: {first}, 2: {second}")
    first_range = list(range(first[0], first[1]+1))
    print(f"first range: {first_range}")
    second_range = list(range(second[0], second[1]+1))
    print(f"second_range: {second_range}")
    together = first_range + second_range
    if sorted(together) != sorted(list(set(together))):
        return True
    return False


total = 0

for i in data:
    candidates = format_input(i)
    if is_overlapping(candidates):
        total += 1

print(total)



if __name__ == '__main__':
    pass