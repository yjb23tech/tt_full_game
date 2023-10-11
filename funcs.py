from class_tile import Tile
from data_storage import arr_world_map

def view_world_map(arr_game_grid):
    for x in range(len(arr_game_grid)):
        for y in range(len(arr_game_grid)):
            print(arr_game_grid[x][y])
        print(" ")

def display_world_map(arr_game_grid):

    print(" ")
    for x in range(len(arr_game_grid)):
        for y in range(len(arr_game_grid[x])):
            print(arr_game_grid[x][y], end="")
        print(" ")
    print(" ")

def update_world_map(arr_game_grid, selected_tile):

    arr_game_grid[selected_tile.int_quadrant_label_loc_1][selected_tile.int_quadrant_label_loc_2] = "X"
    arr_game_grid[selected_tile.int_quadrant_label_loc_1][(selected_tile.int_quadrant_label_loc_2) + 1] = " "

def str_get_player_input(arr_input_options) -> str:

    for x, option in enumerate(arr_input_options, 1):
        print(f"Press {x}. {option}")
    print(" ")

    player_input = input("\nPlease choose from the options above:\n")
    print(" ")
    return player_input

def set_player_name():

    str_player_name = input("\nWhat is your name Sailor?\n")
    return str_player_name 

def set_player_home_city():
    
    str_player_home_city = input("\nWhere are you from Sailor?\n")
    return str_player_home_city 

def set_player_age():

    int_player_age = int(input("\nAnd how old are you Sailor?\n"))
    return int_player_age 

def bool_is_game_complete(arr_tiles_islands_all, user_player) -> bool:

    arr_tiles_islands_unconquered = []

    for island in arr_tiles_islands_all:
        if island in user_player.arr_tiles_islands_conquered:
            continue
        else:
            arr_tiles_islands_unconquered.append(island)
    
    if (len(arr_tiles_islands_unconquered) == 0):

        print("\nCongratulations: you've successfully conquered all 9 islands\n")
        x = 1
        for island in user_player.arr_tiles_islands_conquered:
            print(f"{x}. {island}")
            x += 1 
        
        return True
    
    else:

        print("\nYou still have the following islands to conquer:\n")
        for z, island in enumerate(arr_tiles_islands_unconquered, 1):
            print(f"{z}. {island}")
        print(" ")
        return False

def tile_validation(int_move_x, int_move_y, arr_game_grid, user_player) -> Tile:

    potential_tile_int_loc_x = user_player.int_loc_x + int_move_x
    potential_tile_int_loc_y = user_player.int_loc_y + int_move_y

    try:

        if ((potential_tile_int_loc_x < 0) or (potential_tile_int_loc_y < 0)):
            raise IndexError

        queried_tile = arr_game_grid[potential_tile_int_loc_x][potential_tile_int_loc_y]
        return queried_tile
    except IndexError:
        print("You cannot move in this direction")
        return None
    


    



    

