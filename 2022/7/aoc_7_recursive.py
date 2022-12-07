import re

src = "data.txt"

with open(src) as file:
    terminal_content = file.read()

sizes_of_dir = {}

with open(src) as file:
    content = file.read()
    list_of_dirs = re.findall(r"\$ cd .*", content)
    # print(list_of_dirs)
    list_of_dirs = [re.sub(r"\$ cd (.*)", r"\1", i) for i in list_of_dirs]
    list_of_dirs = [i for i in list_of_dirs if i != ".."]
    # print(list_of_dirs)


def find_value_of_dir(terminal_content, dir_name):
    value = 0
    start_index = terminal_content.find(f"$ cd {dir_name}")

    limited_context = terminal_content[start_index:].splitlines()
    limited_context = limited_context[2:]
    #print(f"limited k. pro fir '{dir_name}': {limited_context}")
    # print("limited content")
    # print(limited_context)
    # print("----------")
    # print(len(limited_context))
    # print(start_index)
    # print(terminal_content[start_index:start_index+20])

    for line in limited_context:
        if "cd" not in line:

            # print(f"line is: {line}")
            if re.match(r"(\d+).*", line):
                value += int(re.findall(r"\d+", line)[0])

            if re.match(r"dir .*", line):
                name_of_dir = re.sub(r"dir(.*)", r"\1", line)
                name_of_dir = name_of_dir.strip()
                value += find_value_of_dir(terminal_content, name_of_dir)
        else:
            return value
    return value


total_size = 0

for i in list_of_dirs:
    value_of_dir = find_value_of_dir(terminal_content, i)
    print(f"value of dir '{i}' os {value_of_dir}")
    if value_of_dir <= 100000:
        total_size += value_of_dir

print(total_size)
