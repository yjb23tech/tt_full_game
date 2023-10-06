def str_get_player_input(arr_input_options) -> str:

    for x, option in enumerate(arr_input_options, 1):
        print(f"Press {x}. {option}")
    print(" ")

    player_input = input("\nPlease choose from the options above:\n")
    return player_input


    

