with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

x = 0
y = 0

for line in lines:
    command = line.split()
    direction = command[0]
    magnitude = int(command[1])

    if direction == "up":
        y -= magnitude
    elif direction == "down":
        y += magnitude
    elif direction == "forward":
        x += magnitude

print("horizontal position", x)
print("depth position", y)
print("product", x * y)
