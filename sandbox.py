from class_player import Player
from class_tile import Tile 
from funcs import str_get_player_input, view_world_map
from data_storage import arr_world_map, dict_moves_in_y, dict_moves_in_x, arr_player_input_options 

test_player = Player("Yuri Orlov", "Odessa", 47)
print(test_player)

view_world_map(arr_world_map)

test_player.player_tile_location(arr_world_map)
test_player.player_tile_valid_directions(arr_world_map, dict_moves_in_y, dict_moves_in_x)

test_player_input = str_get_player_input(arr_player_input_options)
print(f"Chosen action: {test_player_input}")