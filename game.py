from tiles import create_pool
from turn import read_player_move, find_computer_move, play_turn


def play_game():
    pool = create_pool()

    player_hand = []
    computer_hand = []

    for i in range(9):
        player_hand.append(pool.pop())
        computer_hand.append(pool.pop())

    table = []

    consecutive_passes = 0
    player_turn = True

    while True:

        print("\n========== RUMMIKUB ==========")

        print("\nTable:")

        if len(table) == 0:
            print("(empty)")
        else:
            for i in range(len(table)):
                print(f"[{i + 1}]", table[i])

        if player_turn:
            print("\nComputer tiles:", len(computer_hand))
            print("\nYour hand:")

            for i in range(len(player_hand)):
                print(f"[{i + 1}] {player_hand[i][0]}{player_hand[i][1]}")

            move = read_player_move(player_hand)

            result = play_turn(player_hand, pool, table, move)

            if result == "play":
                print("You played:", table[-1])

            elif result == "draw":
                print("You drew a tile.")

            else:
                print("You passed.")

            if len(player_hand) == 0:
                print("\nYou win!")
                break

        else:
            print("\nComputer's turn")

            move = find_computer_move(computer_hand)

            result = play_turn(computer_hand, pool, table, move)

            if result == "play":
                print("Computer played:", table[-1])

            elif result == "draw":
                print("Computer drew a tile.")

            else:
                print("Computer passed.")

            if len(computer_hand) == 0:
                print("\nComputer wins!")
                break

        if result == "pass":
            consecutive_passes += 1
        else:
            consecutive_passes = 0

        if consecutive_passes == 2:

            print("\nBoth players passed.")

            if len(player_hand) < len(computer_hand):
                print("You win!")

            elif len(computer_hand) < len(player_hand):
                print("Computer wins!")

            else:
                print("It's a tie!")

            break

        player_turn = not player_turn


if __name__ == "__main__":
    play_game()