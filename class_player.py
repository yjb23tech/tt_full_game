import random 

class Player:

    def __init__(self, str_name, str_home_city, int_age):

        self.str_name = str_name 
        self.str_home_city = str_home_city
        self.int_age = int_age

        self.int_loc_x = 0
        self.int_loc_y = 0

        self.int_atk_pwr = 1 

        self.tiles_conquered = []
        self.tiles_collected_treasure = []
    
    def __str__(self):

        return (f"Name: {self.str_name} Home City: {self.str_home_city} Age: {self.int_age}\n")
    
    def player_tile_location(self, arr_game_grid):

        player_current_tile = arr_game_grid[self.int_loc_x][self.int_loc_y]
        print(f"You're currently on {player_current_tile.str_island_name} in the {player_current_tile.str_quadrant} Quadrant of the map")
        print(f"Your current coordinates are: [{self.int_loc_x}, {self.int_loc_y}]")

    def int_launch_atk(self):

        self.int_atk_pwr = random.randint(10, 20)
        current_atk_pwr = self.int_atk_pwr 
        return current_atk_pwr 
    



    



        