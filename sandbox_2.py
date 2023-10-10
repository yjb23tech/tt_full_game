from data_storage import arr_world_map, arr_tile_bosses 
from class_player import Player

print(" ")
for x in range(len(arr_tile_bosses)):
    for y in range(len(arr_tile_bosses)):
        print(arr_tile_bosses[x][y])
    print(" ")
print(" ")

#for tile_boss in arr_tile_bosses:
    #print(f"{x}. {tile_boss}")
    #x += 1 
#print(" ")

#Post validation sequence in main game loop

test_player = Player("Yuri Orlov", "Odessa", 47)
print(test_player)

#The user_player's potential new tile location is tested; and can throw an IndexError if invalid
#Below, we're assuming that the tile returned is valid and a part of the 3 x 3 grid world_map 
valid_tile = arr_world_map[test_player.int_loc_x][test_player.int_loc_y]

#Associated tile_boss with the validated tile is then returned and held in a easy to use variable 
valid_tile_boss = arr_tile_bosses[valid_tile.int_loc_x][valid_tile.int_loc_y]

#Here, you're fighting the tile_boss for the first time and the battle sequence should ensue as normal
valid_tile.pvp_tile_boss(valid_tile_boss, test_player)
#Here, you've already defeated the tile_boss; this is checked initially and once confirmed, no fight sequence should take place
valid_tile.pvp_tile_boss(valid_tile_boss, test_player)


