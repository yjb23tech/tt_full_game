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


    

