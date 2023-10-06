from class_player import Player
from class_tile import Tile 
from funcs import str_get_player_input 
from data_storage import arr_world_map, dict_moves_in_y, dict_moves_in_x, arr_player_input_options 

test_player = Player("Yuri Orlov", "Odessa", 47)
print(test_player)

#x = 1
#while (x < 4):
    #print(f"{test_player.str_name} currently has an atk pwr of: {test_player.int_atk_pwr}")
    #print(f"{test_player.str_name} now has an atk pwr of: {test_player.int_launch_atk()}\n")
    #x += 1 

#for x in range(len(arr_world_map)):
    #for y in range(len(arr_world_map)):
        #print(arr_world_map[x][y])
    #print(" ")

test_player.player_tile_location(arr_world_map)
test_player.player_tile_valid_directions(arr_world_map, dict_moves_in_y, dict_moves_in_x)

test_player_input = str_get_player_input(arr_player_input_options)
print(f"Chosen action: {test_player_input}")