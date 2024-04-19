import random

def roll():
    min_value = 1
    max_value = 6
    roll_value= random.randint(min_value, max_value)

    return roll_value

players = input("How many players are playing (2 - 4): ")

while True:
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4 :
            break
        else:
            print("Players must be between 2 or 4")
    else:
        print("Invalid Input. Try again!")
        break

max_score = 50
players_score = [0 for _ in range(players)]


while max(players_score) < max_score:
    for player_idx in range(players):
        print("\n" "Player Number", player_idx + 1, "is your turn!")
        print("Your current score is", players_score[player_idx], "\n")
        currentscore = 0

        while True:
            play = input("Do you want to play (y): ")
            if play.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1. Your turn is over!")
                currentscore = 0
                players_score[player_idx] = 0
                break
            else:
                currentscore += value
                print("You rolled a", value)

            print("Your Score is", currentscore)
            
        players_score[player_idx] += currentscore
        print("Player Number", player_idx + 1, "You Total score is", players_score[player_idx])

max_score = max(players_score)
winner = players_score.index(max_score)
print("player Number", winner + 1, "is the winner with a score of:", max_score)