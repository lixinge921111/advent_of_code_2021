# day1, input
with open("day1.txt", "r") as f:
    input_day1 = f.read().split(", ")

# day1, part1
counter = 0
for i in range(0, len(list)):
    if list[i + 1] > list[i]:
        counter = counter + 1
        print("pair", list[i + 1], list[i])
    else:
        print("not increased")

# day1, part2
new_list = []
for i in range(0, len(list) - 2):
    total = list[i] + list[i + 1] + list[i + 2]
    new_list.append(total)

new_counter = 0
for i in range(0, len(new_list)):
    if new_list[i + 1] > new_list[i]:
        new_counter = new_counter + 1
        print("pair", new_list[i + 1], new_list[i])
    else:
        print("not increased")
new_counter
