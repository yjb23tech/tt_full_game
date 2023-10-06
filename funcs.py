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


    

