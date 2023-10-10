class Tile:
    
    def __init__(self, int_loc_x, int_loc_y, str_quadrant, str_island_name):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.str_quadrant = str_quadrant
        self.str_island_name = str_island_name
    
    def __str__(self):

        return (f"Here is {self.str_island_name} Island in the {self.str_quadrant} Quadrant of the map, coordinates [{self.int_loc_x},{self.int_loc_y}]")
    
    def pvp_tile_boss(self, tile_boss, user_player):

        if (tile_boss.int_hp <= 0):

            print(f"\nYou have already defeated {tile_boss.str_name} on {tile_boss.str_island} Island! Please continue to the next Island safely {user_player.str_name}\n")

        else:

            print(self)
            print(tile_boss)

            while (tile_boss.int_hp > 0):

                print(f"{tile_boss.str_name} currently has {tile_boss.int_hp} health points")
                tile_boss.int_hp = tile_boss.int_hp - user_player.int_launch_atk()
                print(f"After the vicious attack from {user_player.str_name}, {tile_boss.str_name} now has {tile_boss.int_hp} remaining!")
            
            print(f"\nCongratulations: you have defeated {tile_boss.str_name}\n")
            user_player.arr_tiles_islands_conquered.append(self.str_island_name)
            print(f"You have now conquered {user_player.arr_tiles_islands_conquered[-1]}")
        

         