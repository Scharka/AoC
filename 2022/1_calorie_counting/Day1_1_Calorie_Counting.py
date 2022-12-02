def calorie_counting(data):
    elfs = data.split("\n\n")
    maximum = 0
    for i in elfs:
        calories = i.split("\n")
        calories = [int(x) for x in calories]
        calories = sum(calories)
        if calories > maximum:
            maximum = calories
    return maximum

with open("data.txt") as file:
    data = file.read()

print(calorie_counting(data))