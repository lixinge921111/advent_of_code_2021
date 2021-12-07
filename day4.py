import pandas as pd

## day4, part1
with open("day4.txt", "r") as f:
    input_day4 = f.read().split("\n\n")
number_input = input_day4[0].split(",")
board_input = input_day4[1 : len(input_day4)]
int_number_input = [int(x) for x in number_input]


def remove_empty_string(list):
    if "" in list:
        list = [i for i in list if i != ""]
    else:
        pass
    return list


def generate_nested_list(string):
    array = []
    for i in range(0, 5):
        b_list = string.split("\n")[i].split(" ")
        b_list = remove_empty_string(b_list)
        new_list = [int(i) for i in b_list]
        array.append(new_list)
    return array


nested_board_input = [
    generate_nested_list(board_input[i]) for i in range(0, len(board_input))
]

date_cols = ["index", "input_number", "x_value", "y_value", "board_number"]
rows = []

for j in range(0, len(int_number_input)):
    for i in range(0, len(board_input)):
        input_number = int_number_input[j]
        result = np.argwhere(np.array(nested_board_input[i]) == input_number)
        if result.size != 0:
            index = j
            input_number = input_number
            x = result[0][0]
            y = result[0][1]
            board_number = i
            rows.append(
                {
                    "index": index,
                    "input_number": input_number,
                    "x_value": x,
                    "y_value": y,
                    "board_number": board_number,
                }
            )
data = pd.DataFrame(rows, columns=date_cols)

data_cols = ["bingo_index", "board_number"]
n_rows = []

for board_index in range(0, 99):
    for i in range(0, 4):
        board_data = data.loc[data["board_number"] == board_index]
        x_value_data = board_data.loc[board_data["x_value"] == i]
        y_value_data = board_data.loc[board_data["y_value"] == i]
        if len(x_value_data) == 5:
            x_last_index = max(x_value_data.loc[x_value_data["x_value"] == i, "index"])
        if len(y_value_data) == 5:
            y_last_index = max(y_value_data.loc[y_value_data["y_value"] == i, "index"])
        min_index = min(x_last_index, y_last_index)
        n_rows.append({"bingo_index": min_index, "board_number": board_index})
n_data = pd.DataFrame(n_rows, columns=data_cols)

r = []
for i in range(0, 99):
    board_n_data = n_data.loc[n_data["board_number"] == i]
    min_bingo_index = min(board_n_data["bingo_index"])
    r.append({"board_number": i, "bingo_index": min_bingo_index})
d = pd.DataFrame(r)

min_bingo_index_of_all = min(d["bingo_index"])
win_board = d.loc[d["bingo_index"] == min_bingo_index_of_all]
win_board

w_data = data.loc[data["board_number"] == 41]
w_data = w_data.loc[w_data["index"] <= min_bingo_index_of_all]
sum_input = sum(w_data["input_number"])
sum_input

win_board_str = board_input[41]


def return_total(win_board_str: str):
    total = 0
    for i in range(0, 5):
        w_list = remove_empty_string(win_board_str.split("\n")[i].split(" "))
        w_list = [int(i) for i in w_list]
        total = total + sum(w_list)
    return total


total = return_total(win_board_str)
result_p1 = (total - sum_input) * 64

##day4, part2
max_bingo_index_of_all = max(d["bingo_index"])
last_win_board = d.loc[d["bingo_index"] == max_bingo_index_of_all]
last_win_board

w_data = data.loc[data["board_number"] == 53]
w_data = w_data.loc[w_data["index"] <= max_bingo_index_of_all]
sum_input = sum(w_data["input_number"])

win_board_str = board_input[53]
total_last = return_total(win_board_str)
result_p2 = (total_last - sum_input + 57) * 59
