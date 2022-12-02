def calorie_counting(data):
    elfs = data.split("\n\n")
    stocks = []
    for i in elfs:
        calories = i.split("\n")
        calories = [int(x) for x in calories]
        calories = sum(calories)
        stocks.append(calories)
    return sum(sorted(stocks, reverse=True)[0:3])

with open("data.txt") as file:
    data = file.read()

print(calorie_counting(data))
