def next_player(n):
    return abs(n-1)

def empty_grid():
    MTgrid = [['\n'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|']]
    return MTgrid



def display(grid:list,message:str)->str:
    print(message)
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            print(grid[i][j], end='')
    print("\n____________________")

def ask_position():
    coordx,coordy  = input().split()
    if coordx <= '0' or coordy <= '0' or coordx >= '4' or coordy >= '4':
        coordx, coordy = input('Please use coordinates between 1 and 3 included using the format : row column').split()
    return (int(coordx), int(coordy))

def initialize()->list:
    empty = empty_grid()
    print('Enter the coordinates of your first boat using the format : row column')
    boat1 = ask_position()
    print('Enter the coordinates of your second boat using the format : row column')
    boat2 = boat1
    while boat2 == boat1:
        boat2 = ask_position()