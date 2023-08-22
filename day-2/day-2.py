with open("./input.txt", "r") as f:
    puzzle = f.read()

puzzle = puzzle.split("\n")


def calculate_wrapper(dimensions):
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)


def calculate_ribbon(dimensions):
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    return min(2*l+2*w, 2*w+2*h, 2*h+2*l) + l*w*h


total_paper = 0
total_ribbon = 0
for i in puzzle:
    dimensions = i.split("x")
    total_paper += calculate_wrapper(dimensions)
    total_ribbon += calculate_ribbon(dimensions)

print(total_paper)
print(total_ribbon)
