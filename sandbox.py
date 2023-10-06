from class_player import Player
from class_tile import Tile 
from funcs import str_get_player_input, view_world_map, set_player_name, set_player_home_city, set_player_age 
from data_storage import arr_world_map, dict_moves_in_y, dict_moves_in_x, arr_player_input_options 

def play():

    bool_game_is_on = True 

    #Single run only
    test_player = Player(set_player_name(), set_player_home_city(), set_player_age())
    print(test_player)

    while (bool_game_is_on == True):

        #Everything below Exists inside 'while' game loop until declared otherwise
        #view_world_map(arr_world_map)
        
        test_player.player_tile_location(arr_world_map)
        test_player.player_tile_valid_directions(arr_world_map, dict_moves_in_y, dict_moves_in_x)
        
        test_player_input = str_get_player_input(arr_player_input_options)

        if test_player_input in ['North', 'NORTH', 'north', 'N', 'n', '^']:
            print("Blah")
        elif test_player_input in ['East', 'EAST', 'east', 'E', 'e', '>']:
            print("blah blah")
        elif test_player_input in ['South', 'SOUTH', 'south', 'S', 's', 'v']:
            print("blah blah blah")
        elif test_player_input in ['West', 'WEST', 'west', 'W', 'w', '<']:
            print("blah blah blah blah")
        elif test_player_input in ['Inventory', 'INVENTORY', 'inventory', 'I', 'i']:
            print("bleep")
        elif test_player_input in ['Quit', 'QUIT', 'quit', 'Q', 'q']:
            print("bloop")
            bool_game_is_on = False
        else:
            print("So misunderstood")

play()


