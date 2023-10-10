from class_player import Player
from class_tile import Tile 
from funcs import str_get_player_input, view_world_map, set_player_name, set_player_home_city, set_player_age, bool_is_game_complete, tile_validation
from data_storage import arr_world_map, arr_tile_bosses, dict_moves_in_y, dict_moves_in_x, arr_player_input_options, arr_tiles_islands_full_list

def play():

    bool_game_is_on = True 
    bool_game_is_complete = False 

    #Single run only
    test_player = Player(set_player_name(), set_player_home_city(), set_player_age())
    print(test_player)

    while ((bool_game_is_on == True) and (bool_game_is_complete == False)):

        #Everything below Exists inside 'while' game loop until declared otherwise
        #view_world_map(arr_world_map)
        
        print("-----------------------------------------------------------------------------------")

        test_player.player_tile_location(arr_world_map)
        test_player.player_tile_valid_directions(arr_world_map, dict_moves_in_y, dict_moves_in_x)
        
        test_player_input = str_get_player_input(arr_player_input_options)

        if test_player_input in ['North', 'NORTH', 'north', 'N', 'n', '^']:

            #Validate the tile
            int_north_x = test_player.int_loc_x + 0 
            int_north__y = test_player.int_loc_y + 1 

            try:
                valid_tile = arr_world_map[int_north_x][int_north__y]
                test_player.int_loc_x = valid_tile.int_loc_x
                test_player.int_loc_y = valid_tile.int_loc_y

                valid_tile_boss = arr_tile_bosses[valid_tile.int_loc_x][valid_tile.int_loc_y]
                valid_tile.pvp_tile_boss(valid_tile_boss, test_player)
            
            except IndexError:
                print("You cannot move North")
                continue

            #Check to see if the user_player has conquered all 9 islands
            bool_game_is_complete = bool_is_game_complete(arr_tiles_islands_full_list, test_player)
        elif test_player_input in ['East', 'EAST', 'east', 'E', 'e', '>']:

            #validate the tile
            int_east_x = 1
            int_east_y = 0 
            valid_tile = tile_validation(int_east_x, int_east_y, arr_world_map, test_player)

            if valid_tile == None:
                print("Keep on sailing")
            else:
                test_player.int_loc_x = valid_tile.int_loc_x
                test_player.int_loc_y = valid_tile.int_loc_y

                valid_tile_boss = arr_tile_bosses[valid_tile.int_loc_x][valid_tile.int_loc_y]
                valid_tile.pvp_tile_boss(valid_tile_boss, test_player)

            #Check to see if the user_player has conquered all 9 islands 
            bool_game_is_complete = bool_is_game_complete(arr_tiles_islands_full_list, test_player)
        elif test_player_input in ['South', 'SOUTH', 'south', 'S', 's', 'v']:

            #validate the tile
            int_south_x = 0 
            int_south_y = -1
            valid_tile = tile_validation(int_south_x, int_south_y, arr_world_map, test_player)

            if valid_tile == None:
                print("Keep on sailing")
            else:
                test_player.int_loc_x = valid_tile.int_loc_x
                test_player.int_loc_y = valid_tile.int_loc_y

                valid_tile_boss = arr_tile_bosses[valid_tile.int_loc_x][valid_tile.int_loc_y]
                valid_tile.pvp_tile_boss(valid_tile_boss, test_player)
                
            #Check to see if the user_player has conquered all 9 islands
            bool_game_is_complete = bool_is_game_complete(arr_tiles_islands_full_list, test_player)
        elif test_player_input in ['West', 'WEST', 'west', 'W', 'w', '<']:

            #validate the tile 
            int_west_x = -1 
            int_west__y = 0 
            valid_tile = tile_validation(int_west_x, int_west__y, arr_world_map, test_player)

            if valid_tile == None:
                print("Keep on sailing")
            else:
                test_player.int_loc_x = valid_tile.int_loc_x
                test_player.int_loc_y = valid_tile.int_loc_y

                valid_tile_boss = arr_tile_bosses[valid_tile.int_loc_x][valid_tile.int_loc_y]
                valid_tile.pvp_tile_boss(valid_tile_boss, test_player)

            #Check to see if the user_player has conquered all 9 islands 
            bool_game_is_complete = bool_is_game_complete(arr_tiles_islands_full_list, test_player)
        elif test_player_input in ['Inventory', 'INVENTORY', 'inventory', 'I', 'i']:
            #Reveal to the user_player their inventory 
            #Envisioning my loft conversion
            print("bleep")
        elif test_player_input in ['Quit', 'QUIT', 'quit', 'Q', 'q']:
            bool_game_is_on = False
        else:
            print("So misunderstood")
    
    if bool_game_is_complete == True:
        print("\nWell done on beating the game Sailor\n")
    else:
        print("\nYou'll be at sea again soon Sailor; rest for now\n")

play()


