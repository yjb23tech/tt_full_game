from class_tile import Tile
from class_foe import Foe

arr_world_map = [

    [Tile(0, 0, "South Western", "Drum"), Tile(0, 1, "Western", "Wano"), Tile(0, 2, "North Western", "Skypeia")],
    [Tile(1, 0, "Southern", "Fishman"), Tile(1, 1, "Central", "Romance Dawn"), Tile(1, 2, "Northern", "Zou")], 
    [Tile(2, 0, "South Eastern", "Alabasta"), Tile(2, 1, "Eastern", "Thriller Bark"), Tile(2, 2, "North Eastern", "Marineford")]
]

arr_tile_bosses = [

    [Foe(0, 0, "Wapol", "Drum"), Foe(0, 1, "Kaido", "Wano"), Foe(0, 2, "Enel", "Skpeia")], 
    [Foe(1, 0, "Hody Jones", "Fishman"), Foe(1, 1, "Higuma", "Romance Dawn"), Foe(1, 2, "Jack the Drought", "Zou")], 
    [Foe(2, 0, "Sir Crocodile", "Alabasta"), Foe(2, 1, "Gecko Moria", "Thriller Bark"), Foe(2, 2, "Akainu", "Marineford")]

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

        0: "East"
    }
}

arr_player_input_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'I to view your Inventory', 'Q to Quit the game']

arr_tiles_islands_full_list = ['Drum Island', 'Wano', 'Skypeia', 'Fishman', 'Romance Dawn', 'Zou', 'Alabasta', 'Thriller Bark', 'Marineford']

