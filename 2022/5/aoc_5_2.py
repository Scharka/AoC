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
        reversed_state[i].append(state[j*columns+i])

reversed_state_cleaned = [a[::-1] for a in reversed_state]

final = []
for i in reversed_state_cleaned:
    final.append(list(filter("-".__ne__, i)))

stock = final

orders = guide.split("\n")
for order in orders:
    how_many, source, destination = [int(x) for x in re.sub(r"move (\d+) from (\d+) to (\d+)", r"\1 \2 \3", order).split(" ")]
    source, destination = source-1, destination-1
    current_change = []
    for i in range(how_many):
        current_change.append(stock[source].pop())
    stock[destination] += current_change[::-1]

code = ""
for i in stock:
    code += i[-1]
print(code)

