arr_tile_quadrants_unconquered = [

    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "N", "W", " ", " ", "*", " ", " ", " ", "N", " ", " ", " ", "*", " ", " ", " ", "N", "E", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "W", " ", " ", " ", "*", " ", " ", " ", "C", " ", " ", " ", "*", " ", " ", " ", "E", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "S", "W", " ", " ", "*", " ", " ", " ", "S", " ", " ", " ", "*", " ", " ", " ", "S", "E", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"] 

]

def display_world_map(arr_game_grid):

    print(" ")
    for x in range(len(arr_game_grid)):
        for y in range(len(arr_game_grid[x])):
            print(arr_game_grid[x][y], end="")
        print(" ")
    print(" ")

bool_game_is_on = True

while (bool_game_is_on == True):

    display_world_map(arr_tile_quadrants_unconquered)

    ui_test_cases = input("Run the tests:\n")

    if ui_test_cases == 'Test 1':
        arr_tile_quadrants_unconquered[2][4] = 'X'
        arr_tile_quadrants_unconquered[2][5] = " "
    elif ui_test_cases == 'Test 2':
        arr_tile_quadrants_unconquered[2][12] = 'X'
    elif ui_test_cases == 'Test 3':
        arr_tile_quadrants_unconquered[2][20] = 'X'
        arr_tile_quadrants_unconquered[2][21] = " "
    elif ui_test_cases == 'QUIT':
        print("Bye now")
        bool_game_is_on = False
    else:
        print("Run again")



