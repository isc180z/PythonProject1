def next_player(n):
    return abs(n-1)

def empty_grid():
    MTgrid = [['\n'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|'],['\n','|   ','|   ','|   ','|']]
    return MTgrid



def display(grid:list,message:str)->str:
    print(message)
    for i in range(0, len(mt)):
        for j in range(0, len(mt[i])):
            print(mt[i][j], end='')
    print("\n____________________")

def ask_position():
    coordx,coordy  = input('Enter the coordinates to the format : row,column')
