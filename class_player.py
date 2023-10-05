class Player:

    def __init__(self, str_name, str_home_city, int_age):

        self.str_name = str_name 
        self.str_home_city = str_home_city
        self.int_age = int_age

        self.int_loc_x = 1
        self.int_loc_y = 1

        self.tiles_conquered = []
        self.tiles_collected_treasure = []
    
    def __str__(self):

        return (f"Name: {self.str_name} Home City: {self.str_home_city} Age: {self.int_age}")


    



        