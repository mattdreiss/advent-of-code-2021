with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    reports = [int(line, 2) for line in lines]

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for report in reports:
    i = 0
    num_of_bits = len(counts)
    while i < num_of_bits:
        counts[num_of_bits-1-i] += report >> i & 1
        i += 1

gamma_string = ""
epsilon_string = ""
for count in counts:
    if count > len(lines) / 2:
        gamma_string += "1"
        epsilon_string += "0"
    else:
        gamma_string += "0"
        epsilon_string += "1"

gamma = int(gamma_string, 2)
epsilon = int(epsilon_string, 2)
power = gamma * epsilon
print(gamma, bin(epsilon), power)

# part 2
most_common_first_bit = 1 if counts[0] > len(reports) / 2 else 0

