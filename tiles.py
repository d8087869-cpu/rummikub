import random

def create_pool():
    pool = []
    colors = ["R", "B", "C", "O"]
    for number in range(1,14):
        for color in colors:
            pool.append((number, color))
            pool.append((number, color))
    random.shuffle(pool)
    return pool


def is_valid_set(tiles):
    if len(tiles) < 3 or len(tiles) >13:
        return False
    
    numbers = [] 
    colors = []
    
    for tile in tiles:
        numbers.append(tile[0])
        colors.append(tile[1])    

    #check a group 
    if len(tiles) <= 4:
        same_number = True
        diffrent_color = True
        
        for number in numbers:
            if number != numbers[0]:
                same_number = False
        
        for color in colors:
            if colors.count(color) >1:
                diffrent_color =False
        if same_number and diffrent_color:
            return True
        
    
    #run check
    same_color = True
    for color in colors:
        if color != colors[0]:
            same_color = False
            
    if same_color:
        numbers.sort()
        
        for i in range(len(numbers) -1 ):
            if numbers [i + 1] != numbers[i] + 1:
                return False
            
        return True
    return False



def play_set(hand, table, indexes):
    played_tiles = []

    for index in indexes:
        played_tiles.append(hand[index])

    for index in sorted(indexes, reverse=True):
        hand.pop(index)

    table.append(played_tiles)

    return played_tiles