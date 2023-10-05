class Tile:
    
    def __init__(self, int_loc_x, int_loc_y, str_quadrant, str_island_name):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y 

        self.str_quadrant = str_quadrant
        self.str_island_name = str_island_name
    
    def __str__(self):

        return (f"Here is {self.str_island_name} Island in the {self.str_quadrant} Quadrant of the map, coordinates [{self.int_loc_x},{self.int_loc_y}]")
    
