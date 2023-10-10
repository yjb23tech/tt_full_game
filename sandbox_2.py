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

valid_tile = arr_world_map[2][1]
valid_tile_boss = arr_tile_bosses[2][1]

#Here, you're fighting the tile_boss for the first time and the battle sequence should ensue as normal
valid_tile.pvp_tile_boss(valid_tile_boss, test_player)
#Here, you've already defeated the tile_boss; this is checked initially and once confirmed, no fight sequence should take place
valid_tile.pvp_tile_boss(valid_tile_boss, test_player)


