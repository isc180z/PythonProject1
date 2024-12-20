from random import *

def next_player(n):
    return abs(n-1)



def empty_grid():
    MTgrid = [['\n'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|']]
    return MTgrid



def display(grid:list,message:str):
    print(message)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            print(grid[i][j], end='')
    print("\n_______________")



def ask_position():
    coords  = input()
    print(coords)
    while len(coords) != 3 or coords[0] not in ["1","2","3"] or coords[2] not in ["1","2","3"] or coords[1] != ',':
        coords = input('Use coordinates between 1 and 3 included using the format : row,column')
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



def turn(player:int, player_shots_grid:list, opponent_grid:list):
    if player == 0:
        print('Where will you shoot ?')
        shot = ask_position()
        while player_shots_grid[shot[0]][shot[1]] == '| x ' or player_shots_grid[shot[0]][shot[1]] == '| . ':
            shot = (randint(1, 3), randint(1, 3))
        if opponent_grid[shot[0]][shot[1]] == '| B ':
            player_shots_grid[shot[0]][shot[1]] = '| x '
            print('Hit, sunk !!')
        else:
            player_shots_grid[shot[0]][shot[1]] = '| . '
            print('Splash...')



    else:
        shot = (randint(1,3),randint(1,3))
        while player_shots_grid[shot[0]][shot[1]] == '| x ' or player_shots_grid[shot[0]][shot[1]] == '| . ':
            shot = (randint(1,3),randint(1,3))
        if opponent_grid[shot[0]][shot[1]] == '| B ':
            player_shots_grid[shot[0]][shot[1]] = '| x '
            print('Hit, sunk !!')
        else:
            player_shots_grid[shot[0]][shot[1]] = '| . '
            print('Splash...')




k = {"Paul":["1m66","Ouvrier"]}
k["Paul"].append("nothing")
print(k["Paul"])

k["A"] = ["fruit"]
print(k["A"])

def has_won(player_shots_grid:list)->bool:
    x = 0
    for i in player_shots_grid:
        for j in i:
            if j == '| x ':
                x += 1
        if x == 2:
            return True
    return False


#def battle_ship_game():