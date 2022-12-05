import re

with open("test_data.txt") as file:
    data = file.read()

state, guide = data.split("\n\n")

columns = len(re.findall("\d", state))
rows = state.count("\n")


state = re.sub("\[(\w)\]", r"\1", state)
state = state.replace("    ", "-")
state = state.replace(" ", "")
state = state.replace("\n", "")

reversed_state = [[] for i in range(columns)]

for j in range(rows):
    for i in range(columns):
        #print(f"j je: {j}, i je : {i}")
        #print(state[j*columns+i], end="")
        reversed_state[i].append(state[j*columns+i])

reversed_state_cleaned = [list(filter(lambda a: a != "-", a_list)) for a_list in reversed_state]
stock = reversed_state_cleaned

orders = guide.split("\n")

def code(a_stock):
    code = ""
    for i in stock:
        code += i.pop()
    return code


for order in orders:
    try:
        print(code(stock))
    except IndexError:
        print("pop from empty list")
    how_many, source, destination = [int(x) for x in re.sub(r"move (\d+) from (\d+) to (\d+)", r"\1 \2 \3", order).split(" ")]
    source, destination = source-1, destination-1
    for i in range(how_many):
        print(f"situace je následující:")
        print(f"stock: {stock}")
        print(f"source: {source}")
        element = stock[source].pop()
        stock[destination].append(element)



"""
print(state)
print(state[0])
print(reversed_state)
print(reversed_state[0])
print(reversed_state[0])
"""



"""

[B]                     [N]     [H]
[V]         [P] [T]     [V]     [P]
[W]     [C] [T] [S]     [H]     [N]
[T]     [J] [Z] [M] [N] [F]     [L]
[Q]     [W] [N] [J] [T] [Q] [R] [B]
[N] [B] [Q] [R] [V] [F] [D] [F] [M]
[H] [W] [S] [J] [P] [W] [L] [P] [S]
[D] [D] [T] [F] [G] [B] [B] [H] [Z]
 1   2   3   4   5   6   7   8   9


"""
