from class_player import Player
from class_tile import Tile 
from funcs import str_get_player_input, view_world_map, set_player_name, set_player_home_city, set_player_age 
from data_storage import arr_world_map, dict_moves_in_y, dict_moves_in_x, arr_player_input_options 

#Single run only
test_player = Player(set_player_name(), set_player_home_city(), set_player_age())
print(test_player)

#Everything below Exists inside 'while' game loop until declared otherwise
view_world_map(arr_world_map)

test_player.player_tile_location(arr_world_map)
test_player.player_tile_valid_directions(arr_world_map, dict_moves_in_y, dict_moves_in_x)

test_player_input = str_get_player_input(arr_player_input_options)
print(f"Chosen action: {test_player_input}")