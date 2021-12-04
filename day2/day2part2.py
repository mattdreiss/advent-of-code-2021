with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

aim = 0
x = 0
y = 0

for line in lines:
    command = line.split()
    direction = command[0]
    magnitude = int(command[1])

    if direction == "up":
        aim -= magnitude
    elif direction == "down":
        aim += magnitude
    elif direction == "forward":
        x += magnitude
        y += aim * magnitude

print("horizontal position", x)
print("depth position", y)
print("product", x * y)
