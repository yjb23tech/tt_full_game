class Foe:

    def __init__(self, int_loc_x, int_loc_y, str_name, str_island):

        self.int_loc_x = int_loc_x
        self.int_loc_y = int_loc_y 
        self.str_name = str_name
        self.str_island = str_island 

        self.int_hp = 100
    
    def __str__(self):

        return (f"I am Captain {self.str_name} of {self.str_island} Island! LET'S FIGHT!\n")
    
