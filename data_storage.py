from class_tile import Tile

arr_world_map = [

    [Tile(0, 0, "South Western", "Drum Island"), Tile(0, 1, "Western", "Wano"), Tile(0, 2, "North Western", "Skypeia")],
    [Tile(1, 0, "Southern", "Fishman"), Tile(1, 1, "Central", "Romance Dawn"), Tile(1, 2, "Northern", "Zou")], 
    [Tile(2, 0, "South Eastern", "Alabasta"), Tile(2, 1, "Eastern", "Thriller Bark"), Tile(2, 2, "North Eastern", "Marineford")]
]

dict_moves_in_y = {

    0: {

        -1: "South", 
        0: "Stay", 
        1: "North"
    }
}

dict_moves_in_x = {

    -1: {

        0: "West"
    }, 

    0: {

        0: "No Movement"
    }, 

    1: {

        0: " East"
    }
}

arr_player_input_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'I to view your Inventory', 'Q to Quit the game']

