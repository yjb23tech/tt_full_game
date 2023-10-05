from class_player import Player
from class_tile import Tile 

test_player = Player("Yuri Orlov", "Odessa", 47)
print(test_player)

arr_world_map = [

    [Tile(0, 0, "South Western", "Dressrosa"), Tile(0, 1, "Western", "Wano"), Tile(0, 2, "North Western", "Skypeia")], 
    [Tile(1, 0, "Southern", "Fisman"), Tile(1, 1, "Central", "Romance Dawn"), Tile(1, 2, "Northern", "Zou")], 
    [Tile(2, 0, "South Eastern", "Alabasta"), Tile(2, 1, "Eastern", "Thriller Bark"), Tile(2, 2, "North Eastern", "Marineford")]
]

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