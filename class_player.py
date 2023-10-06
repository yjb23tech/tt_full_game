import random 

class Player:

    def __init__(self, str_name, str_home_city, int_age):

        self.str_name = str_name 
        self.str_home_city = str_home_city
        self.int_age = int_age

        self.int_loc_x = 1
        self.int_loc_y = 2

        self.int_atk_pwr = 1 

        self.arr_tiles_islands_conquered = ['Drum Island', 'Skypeia', 'Fishman', 'Romance Dawn', 'Zou', 'Alabasta', 'Thriller Bark']
        self.arr_tiles_collected_treasure = []
    
    def __str__(self):

        return (f"\n\nName: {self.str_name} Home City: {self.str_home_city} Age: {self.int_age}\n")
    
    def player_tile_location(self, arr_game_grid):

        #Do I need to import the Tile class to be able to work with Tile objects? It doesn't appear so... 
        player_current_tile = arr_game_grid[self.int_loc_x][self.int_loc_y]
        print(f"\nYou're currently on {player_current_tile.str_island_name} in the {player_current_tile.str_quadrant} Quadrant of the map")
        print(f"Your current coordinates are: [{self.int_loc_x}, {self.int_loc_y}]\n")

    #My own creation aka Frankenstein's Monster; really proud of this method - it works well! 
    def player_tile_valid_directions(self, arr_game_grid, dict_directions_y, dict_directions_x):

        arr_valid_travel_strings = []
        arr_invalid_travel_strings = []

        for x in range(1):
            for y in range(-1, 2):

                tile_int_loc_x_valid_tbc = self.int_loc_x + x
                tile_int_loc_y_valid_tbc = self.int_loc_y + y

                try:

                    if tile_int_loc_y_valid_tbc < 0:
                        raise IndexError
                    
                    valid_tile = arr_game_grid[tile_int_loc_x_valid_tbc][tile_int_loc_y_valid_tbc]
                    valid_direction = dict_directions_y[x][y]

                    if valid_direction == 'Stay':
                        continue
                    else:
                        arr_valid_travel_strings.append(f"You can travel {valid_direction} to {valid_tile.str_island_name} Island")

                except IndexError:

                    invalid_direction = dict_directions_y[x][y]
                    arr_invalid_travel_strings.append(f"You cannot travel {invalid_direction}")
        
        for x in range(-1, 2):
            for y in range(1):

                tile_int_loc_x_valid_tbc = self.int_loc_x + x
                tile_int_loc_y_valid_tbc = self.int_loc_y + y 
            
            try:

                if tile_int_loc_x_valid_tbc < 0:
                    raise IndexError
                
                valid_tile = arr_game_grid[tile_int_loc_x_valid_tbc][tile_int_loc_y_valid_tbc]
                valid_direction = dict_directions_x[x][y]

                if valid_direction == 'No Movement':
                    continue
                else:
                    arr_valid_travel_strings.append(f"You can travel {valid_direction} to {valid_tile.str_island_name} Island")
            
            except IndexError:

                invalid_direction = dict_directions_x[x][y]
                arr_invalid_travel_strings.append(f"You cannot travel {invalid_direction}")

        for valid_travel_string in arr_valid_travel_strings:
            print(valid_travel_string)
        print(" ")

        #When at [1, 1] you can travel in all directions; quite nicely, no error is thrown - instead the 'for' loop simply doesn't run
        for invalid_travel_string in arr_invalid_travel_strings:
            print(invalid_travel_string)
        print(" ")

    def int_launch_atk(self):

        self.int_atk_pwr = random.randint(10, 20)
        current_atk_pwr = self.int_atk_pwr 
        return current_atk_pwr 
    



    



        