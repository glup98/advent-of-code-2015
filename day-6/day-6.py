# Part 2
# Inicializamos la matriz de luces con brillo 0
lights = [[0 for _ in range(1000)] for _ in range(1000)]


def apply_instruction(instruction, x1, y1, x2, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if instruction == "turn on":
                lights[i][j] += 1
            elif instruction == "turn off":
                # No permitimos valores negativos
                lights[i][j] = max(0, lights[i][j] - 1)
            elif instruction == "toggle":
                lights[i][j] += 2


# Leer input
with open("./input.txt", "r") as f:
    puzzle = f.read().split("\n")

# Procesar cada línea del puzzle
for line in puzzle:
    if line.startswith("turn on"):
        instruction = "turn on"
        coords = line[len("turn on "):].split(" through ")
    elif line.startswith("turn off"):
        instruction = "turn off"
        coords = line[len("turn off "):].split(" through ")
    elif line.startswith("toggle"):
        instruction = "toggle"
        coords = line[len("toggle "):].split(" through ")
    else:
        continue

    x1, y1 = map(int, coords[0].split(","))
    x2, y2 = map(int, coords[1].split(","))

    apply_instruction(instruction, x1, y1, x2, y2)

# Calculamos el brillo total
total_brightness = sum(sum(row) for row in lights)
print(total_brightness)


# Part 1
# Inicializamos la matriz de luces
# lights = [[0 for _ in range(1000)] for _ in range(1000)]


# def apply_instruction(instruction, x1, y1, x2, y2):
#     for i in range(x1, x2+1):
#         for j in range(y1, y2+1):
#             if instruction == "turn on":
#                 lights[i][j] = 1
#             elif instruction == "turn off":
#                 lights[i][j] = 0
#             elif instruction == "toggle":
#                 lights[i][j] ^= 1


# # Leer input
# with open("./input.txt", "r") as f:
#     puzzle = f.read().split("\n")

# # Procesar cada línea del puzzle
# for line in puzzle:
#     if line.startswith("turn on"):
#         instruction = "turn on"
#         coords = line[len("turn on "):].split(" through ")
#     elif line.startswith("turn off"):
#         instruction = "turn off"
#         coords = line[len("turn off "):].split(" through ")
#     elif line.startswith("toggle"):
#         instruction = "toggle"
#         coords = line[len("toggle "):].split(" through ")
#     else:
#         continue

#     x1, y1 = map(int, coords[0].split(","))
#     x2, y2 = map(int, coords[1].split(","))

#     apply_instruction(instruction, x1, y1, x2, y2)

# # Contamos las luces encendidas
# count = sum(sum(row) for row in lights)
# print(count)
