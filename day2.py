import re

# day2, part1
with open("day2.txt", "r") as f:
    input_day2 = f.read().split(", ")

horizontal = 0
depth = 0
for i in input_day2:
    if i.startswith("forward"):
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        forward_number = r.match(i)
        horizontal = horizontal + int(forward_number.group(2))
    elif i.startswith("down"):
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        down_number = r.match(i)
        depth = depth + int(down_number.group(2))
    else:
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        up_number = r.match(i)
        depth = depth - int(up_number.group(2))
course = horizontal * depth
course

# day2, part2
new_horizontal = 0
new_depth = 0
aim = 0

for i in input_day2:
    if i.startswith("forward"):
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        forward_number = r.match(i)
        new_horizontal = new_horizontal + int(forward_number.group(2))
        new_depth = new_depth + aim * int(forward_number.group(2))
    elif i.startswith("down"):
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        down_number = r.match(i)
        aim = aim + int(down_number.group(2))
    else:
        r = re.compile("([a-zA-Z]+)\s([0-9]+)")
        up_number = r.match(i)
        aim = aim - int(up_number.group(2))
new_course = new_horizontal * new_depth
new_course
