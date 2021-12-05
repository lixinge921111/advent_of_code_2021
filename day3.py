# day3, part1
with open("day3.txt", "r") as f:
    input_day3 = f.read().split(",")
binary_length = len(input_day3[0])
list_length = len(input_day3)
l = [i for i in range(0, binary_length)]


def get_gamma_digit(position: int):
    sum_number = 0
    list_length = len(input_day3)
    for i in range(0, list_length):
        sum_number = sum_number + int(input_day3[i][position])
        if sum_number > 500:
            gamma_digit = 1
        else:
            gamma_digit = 0
    return gamma_digit


def get_epsilon_digit(position: int):
    sum_number = 0
    list_length = len(input_day3)
    for i in range(0, list_length):
        sum_number = sum_number + int(input_day3[i][position])
        if sum_number > 500:
            epsilon_digit = 0
        else:
            epsilon_digit = 1
    return epsilon_digit


gamma = [get_gamma_digit(x) for x in l]
decimal_gamma = int("".join(map(str, gamma)), 2)
epsilon = [get_epsilon_digit(x) for x in l]
decimal_epsilon = int("".join(map(str, epsilon)), 2)
result_p1 = decimal_gamma * decimal_epsilon
result_p1

## day3, part2
def get_most_common_digit(iterative_list, position: int):
    sum_number = 0
    list_length = len(iterative_list)
    for i in range(0, list_length):
        sum_number = sum_number + int(iterative_list[i][position])
        if sum_number >= len(iterative_list) / 2:
            digit = 1
        else:
            digit = 0
    return digit


def get_least_common_digit(iterative_list, position: int):
    sum_number = 0
    list_length = len(iterative_list)
    for i in range(0, list_length):
        sum_number = sum_number + int(iterative_list[i][position])
        if sum_number >= len(iterative_list) / 2:
            digit = 0
        else:
            digit = 1
    return digit


def find_items_in_list(iterative_list, position: int):
    return iterative_list[position]


def iterate_over_list(iterative_list, position: int):
    digit = get_least_common_digit(iterative_list, position)
    new_list = [
        find_items_in_list(iterative_list, i)
        for i in range(0, len(iterative_list))
        if int(iterative_list[i][position]) == digit
    ]
    return new_list


j = 0
updated_list = input_day3.copy()
while j < 12:
    updated_list = iterate_over_list(updated_list, j)
    if len(updated_list) > 1:
        j = j + 1
        continue
    elif len(updated_list) == 1:
        print("only one left and digit at", j)
        break
    else:
        print("??", j)
        break

result_p2 = int("000111100110", 2) * int("101011100000", 2)
