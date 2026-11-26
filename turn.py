from tiles import is_valid_set, play_set

def read_player_move(hand):
    while True:
        choice = input("Choose tile position or D to draw: ").strip()
        if choice == "D" or choice == "d":
            return None
        try:
            positions = choice.split()
            if len(positions) < 3:
                print("you must choose at least 3 tiles")
                continue
            
            indexes = []
            
            for position in positions:
                indexes.append(int(position) - 1)
            
            if len(indexes) != len(set(indexes)):
                print("cannot duplicate card position")
                continue
            
            valid_indexes = True
            
            for index in indexes:
                if index < 0 or index >= len(hand):
                    valid_indexes = False
            
            if not valid_indexes:
                print("invalid position")
                continue
            
            selected_tiles = []
            
            for index in indexes:
                selected_tiles.append(hand[index])
            
            if not is_valid_set(selected_tiles):
                print("invalid set. try again")
                continue
            
            return indexes
        except ValueError:
            print("please enter a valid number")
            
           
    
    
def find_computer_move(hand):
    best_indexes = []

    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):

                indexes = [i, j, k]

                selected_tiles = []

                for index in indexes:
                    selected_tiles.append(hand[index])

                if is_valid_set(selected_tiles):

                    for attempt in range(len(hand)):

                        for index in range(len(hand)):
                            if index not in indexes:

                                new_tiles = selected_tiles.copy()
                                new_tiles.append(hand[index])

                                if is_valid_set(new_tiles):
                                    selected_tiles = new_tiles
                                    indexes.append(index)

                    if len(indexes) > len(best_indexes):
                        best_indexes = indexes.copy()

    if len(best_indexes) == 0:
        return None

    return best_indexes



def play_turn(hand, pool, table, move):
    if move is not None:
        play_set(hand, table, move)
        return "play"

    if len(pool) > 0:
        tile = pool.pop()
        hand.append(tile)
        return "draw"

    return "pass"