from random import *

def next_player(n):
    return abs(n-1)



def empty_grid():
    MTgrid = [['\n_____________'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|']]
    return MTgrid



def display(grid:list,message:str):
    print(message)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            print(grid[i][j], end='')
    print("\n_____________")



def ask_position():
    coords  = input()
    print(coords)
    while len(coords) != 3 or coords[0] not in ["1","2","3"] or coords[2] not in ["1","2","3"] or coords[1] != ',':
        coords = input('Use coordinates between 1 and 3 included using the format : row,column\n')
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

    return grid

def turn(player:int, player_shots_grid:list, opponent_grid:list):
    if player == 0:
        display(player_shots_grid, "\nHistory of your previous shots :")
        print('Where will you shoot ?')
        shot = ask_position()
        while player_shots_grid[shot[0]][shot[1]] == '| x ' or player_shots_grid[shot[0]][shot[1]] == '| . ':
            print("You already shot there, ask somewhere else")
            shot = ask_position()
        if opponent_grid[shot[0]][shot[1]] == '| B ':
            player_shots_grid[shot[0]][shot[1]] = '| x '
            print('Hit, sunk !!')
        else:
            player_shots_grid[shot[0]][shot[1]] = '| . '
            print('Splash...')


    else:
        print("\nIt's the game master's turn")
        shot = (randint(1,3),randint(1,3))
        while player_shots_grid[shot[0]][shot[1]] == '| x ' or player_shots_grid[shot[0]][shot[1]] == '| . ':
            shot = (randint(1,3),randint(1,3))
        print(f'The game master shoots at position {shot[0]},{shot[1]}')
        if opponent_grid[shot[0]][shot[1]] == '| B ':
            player_shots_grid[shot[0]][shot[1]] = '| x '
            input('Hit, sunk !!')
        else:
            player_shots_grid[shot[0]][shot[1]] = '| . '
            input('Splash...')



def has_won(player_shots_grid:list)->bool:
    x = 0
    for i in player_shots_grid[1:4]:
        for j in i:
            if j == '| x ':
                x += 1
        if x == 2:
            return True
    return False


def battle_ship_game():
    botgrid = empty_grid()
    bot1 = (randint(1,3),randint(1,3))
    bot2 = bot1
    while bot2 == bot1:
        bot2 = (randint(1,3),randint(1,3))
    botgrid[bot1[0]][bot1[1]] = '| B '
    botgrid[bot2[0]][bot2[1]] = '| B '
    playergrid = initialize()
    turnindex = 0
    playershots = empty_grid()
    botshots = empty_grid()
    grids = ([playershots,botgrid],[botshots,playergrid])

    while not(has_won(playershots) or has_won(botshots)):
        turn(turnindex, grids[turnindex][0], grids[turnindex][1])
        turnindex = next_player(turnindex)

    if has_won(playershots):
        display(playershots,"\nYou won! :D")
    else:
        display(botshots,"\nYou lost! >:)")