def next_player(n):
    return abs(n-1)



def empty_grid():
    MTgrid = [['\n'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|']]
    return MTgrid



def display(grid:list,message:str)->:
    print(message)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            print(grid[i][j], end='')
    print("\n_______________")



def ask_position():
    coords  = input()
    print(coords)
    while len(coords) != 3 or coords[0] not in ["1","2","3"] or coords[2] not in ["1","2","3"] or coords[1] != ',':
        coords = input('Please use coordinates between 1 and 3 included using the format : row,column')
        print(coords)
    coordx,coordy = coords.split(',')
    return (int(coordx), int(coordy))



def initialize():
    grid = empty_grid()

    print('Enter the coordinates of your first boat using the format : row,column')
    boat1 = ask_position()
    print('Enter the coordinates of your second boat using the format : row,column')
    boat2 = boat1
    while boat2 == boat1:
        boat2 = ask_position()

    grid[boat1[0]][boat1[1]] = '| B '
    grid[boat2[0]][boat2[1]] = '| B '

    display(grid,"Here's how you placed your ships")



def turn(player:int, player_shots:list, opponent_grid:list):
    if player == 0:

