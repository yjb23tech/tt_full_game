arr_tile_quadrants_unconquered = [

    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "N", "W", " ", " ", "*", " ", " ", " ", "N", " ", " ", " ", "*", " ", " ", " ", "N", "E", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "W", " ", " ", " ", "*", " ", " ", " ", "C", " ", " ", " ", "*", " ", " ", " ", "E", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " ", " ", " ", "S", "W", " ", " ", "*", " ", " ", " ", "S", " ", " ", " ", "*", " ", " ", " ", "S", "E", " ", " ", "*"], 
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*"], 
    ["*", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *", " *"] 

]

print(" ")
for x in range(len(arr_tile_quadrants_unconquered)):
    for y in range(len(arr_tile_quadrants_unconquered[x])):
        print(arr_tile_quadrants_unconquered[x][y], end="")
    print(" ")
print(" ")