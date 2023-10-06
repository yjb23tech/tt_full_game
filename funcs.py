def view_world_map(arr_game_grid):
    for x in range(len(arr_game_grid)):
        for y in range(len(arr_game_grid)):
            print(arr_game_grid[x][y])
        print(" ")

def str_get_player_input(arr_input_options) -> str:

    for x, option in enumerate(arr_input_options, 1):
        print(f"Press {x}. {option}")
    print(" ")

    player_input = input("\nPlease choose from the options above:\n")
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
            print(" ")
        else:
            arr_tiles_islands_unconquered.append(island)
    
    if (len(arr_tiles_islands_unconquered) == 0):

        print("Congratulations: you've successfully conquered all 9 islands\n")
        x = 1
        for island in user_player.arr_tiles_islands_conquered:
            print(f{x}. {island})
            x += 1 
        
        return True
    
    else:

        print("You still have the following islands to conquer:\n")
        for z, island in enumerate(arr_tiles_islands_unconquered, 1):
            print(f"{z} {island}")
        
        return False



    



    

