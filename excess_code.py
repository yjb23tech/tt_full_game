#Should be stored in a data_storage file
arr_world_map = [

    [Tile(0, 0, "South Western", "Dressrosa"), Tile(0, 1, "Western", "Wano"), Tile(0, 2, "North Western", "Skypeia")], 
    [Tile(1, 0, "Southern", "Fisman"), Tile(1, 1, "Central", "Romance Dawn"), Tile(1, 2, "Northern", "Zou")], 
    [Tile(2, 0, "South Eastern", "Alabasta"), Tile(2, 1, "Eastern", "Thriller Bark"), Tile(2, 2, "North Eastern", "Marineford")]
]

#Should be stored in a data storage file
dict_moves_in_y = {

    0: {

        -1: "South", 
        0: "Stay", 
        1: "North"
    }
}

#Should be stored in a data_storage file 
dict_moves_in_x = {

    -1: {

        0: "West"
    }, 

    0: {

        0: "No Movement"
    }, 

    1: {

        0: "East"
    }
}

#Should be stored in a data_storage file
arr_player_input_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'Press I to view your Invetory', 'Q to Quit the game']
