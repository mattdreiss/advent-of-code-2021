with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()

# part 1 setup
previous_value = None
count_increases_1 = 0

# part 2 setup
rolling_window = []
count_increases_2 = 0

for line in lines:
    value = int(line)

    # part 1 logic
    if previous_value is None:
        previous_value = value
        continue

    if value > previous_value:
        count_increases_1 = count_increases_1 + 1

    previous_value = value

    # part 2 logic
    rolling_window.append(value)
    length = len(rolling_window)

    if length < 4:
        continue

    if length > 4:
        rolling_window.pop(0)

    if rolling_window[3] > rolling_window[0]:
        count_increases_2 = count_increases_2 + 1

print(count_increases_1)
print(count_increases_2)
