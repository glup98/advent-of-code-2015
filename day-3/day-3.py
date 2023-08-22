def unique_houses(puzzle_path):
    #Leer puzzle
    with open(puzzle_path, "r") as f:
        puzzle = f.read()

    #Cordenadas
    x,y = 0,0
    houses = set()

    #Añadir la casa inicial al set de 'houses'
    houses.add((x,y))

    #Iterar sobre el puzzle
    for move in puzzle:
        if move == "^":
            y +=1
        elif move == "v":
            y -=1
        elif move ==">":
            x +=1
        elif move == "<":
            x -=1
        #Añadir la casa actual a la lista
        houses.add((x,y))

    print(houses)
    return len(houses)


def robot_santa(puzzle_path):
    #Leer puzzle
    with open(puzzle_path, "r") as f:
        puzzle = f.read()

    #Cordenadas
    santa_x,santa_y = 0,0
    robot_x,robot_y = 0,0

    #Añadir la casa inicial al set de 'houses'
    houses = set()

    #Añadir la casa inicial al set de 'houses'
    houses.add((santa_x,santa_y))
    print(list(enumerate(puzzle)))
    for i,move in enumerate(puzzle):
        if i%2== 0:
            if move == "^":
                santa_y +=1
            elif move == "v":
                santa_y -=1
            elif move ==">":
                santa_x +=1
            elif move == "<":
                santa_x -=1
            houses.add((santa_x,santa_y))
            
        else:
            if move == "^":
                robot_y +=1
            elif move == "v":
                robot_y -=1
            elif move ==">":
                robot_x +=1
            elif move == "<":
                robot_x -=1
            houses.add((robot_x,robot_y))

    # print(houses)
    return len(houses)

print(robot_santa("puzzle-input.txt"))

