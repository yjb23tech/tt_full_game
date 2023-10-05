class Tile:
    
    def __init__(self, int_loc_x, int_loc_y, str_quadrant, str_island_name):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.str_quadrant = str_quadrant
        self.str_island_name = str_island_name
    
    def __str__(self):

        return (f"You're in the {self.str_quadrant} of the map, coordinates [{self.int_loc_x},{self.int_loc_y}] and docked on {self.str_island_name} Island")
    
    