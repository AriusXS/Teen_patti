from collections import Counter
from random import *

class Player:
    cards = { 
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "10":9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
    }

    pattern = ["spade", "diamond", "love", "club"]

    def __init__(self, name, cards=None, faces=None, colors=None, sorted_face_values=None, has_trial=None, has_run=None, has_double=None, has_color=None, has_jute=None, has_seen=False, has_quit=False):
        self.name = name
        self.cards = cards
        self.faces = faces
        self.colors = colors
        self.sorted_face_values = sorted_face_values
        self.has_trial = has_trial
        self.has_run = has_run
        self.has_double = has_double
        self.has_color = has_color
        self.has_jute = has_jute
        self.has_seen = has_seen
        self.has_quit = has_quit
    
    def __str__(self):
        return f"Name: {self.name}, cards: {self.cards}"

def main():
    global players_with_trial,players_with_double,players_with_run,players_with_color,players_with_jute,single_players, diff_players
    while True:
        try:
            num_players = int(input("How many players want to play? (only 2-10 are allowed): "))
            if num_players not in range(2, 11): raise ValueError
            break
        except ValueError:
            print("Please enter a valid number between 2-10")
            continue
    #Creating players and giving them different values
    players = [Player(f"Player {i+1}") for i in range(num_players)]
    for player in players:
        player.cards = card_gen()
        player.faces, player.colors, player.has_trial = trial(player.cards)
        player.has_run, player.sorted_face_values = run(player.faces)
        player.has_color = color(player.colors)
        player.has_jute = jute(player.faces)
        print(player)
    
    #Now, comparing players on different terms:
    players_with_trial = [player for player in players if player.has_trial]
    players_with_run = [player for player in players if player.has_run]
    players_with_color = [player for player in players if player.has_color]
    players_with_double = list(set(players_with_color) & set(players_with_run))
    players_with_jute = [player for player in players if player.has_jute]
    single_players = players.copy()
    diff_players = [players_with_trial,players_with_double,players_with_run,players_with_color,players_with_jute,single_players]
    diff_players = list(filter(lambda x: len(x) > 0, diff_players))
    print(win_generator(players))



"""defining random vairables here"""
deck = [f"{card}: {color}" for card in Player.cards.keys() for color in Player.pattern]

def card_gen():
    shuffle(deck)
    three_cards = sample(deck, 3)
    [deck.remove(card) for card in three_cards if card in deck]
    return three_cards

def trial(cards):
    faces = []
    colors = []
    for card in cards:
        face, color = card.split(": ")
        faces.append(face)
        colors.append(color)
    for i in range(2):
        if not faces[i] == faces[i+1]:
            return faces, colors, False
    return faces, colors, True


def run(faces):
    unsorted_face_values = []
    for face in faces:
        unsorted_face_values.append(Player.cards[face])    
    sorted_face_values = sorted(unsorted_face_values)  # descending: 10, 9, 4
    #sorted_face_values = sorted(unsorted_face_values)
    if Counter(["A", "2", "3"]) == Counter(faces):
        return True, sorted_face_values
    for i in range(2):
        if not sorted_face_values[i] == sorted_face_values[i+1] - 1:
            return False, sorted_face_values
    return True, sorted_face_values

def color(colors):
    for i in range(2):
        if not colors[i] == colors[i+1]:
            return False
    return True

def jute(face_only):
    return len(face_only) != len(set(face_only))

def win_generator(players):
    global players_with_trial,players_with_double,players_with_run,players_with_color,players_with_jute,single_players, diff_players
    for players_condition in diff_players:
        if not (winner_name:=single_winner(players_condition)):
            continue
        return winner_name
    return "Winner is None"

def single_winner(single_players):
    for i in range(3):
        equals = []

        player_values = {
        player: sorted(player.sorted_face_values, reverse=True)[i] for player in single_players
        }
        sorted_player_dict = dict(sorted(player_values.items(), key=lambda x: x[1], reverse=True))
        # Get the first (highest) value
        first_value = next(iter(sorted_player_dict.values()))
        # Collect all players with the same value
        highest_players = [
            (player, value)
            for player, value in sorted_player_dict.items()
            if value == first_value
        ]
        if len(highest_players) == 1:
            return highest_players[0][0].name
        else:
            single_players = [player for player, value in highest_players]
            continue
    return False


if __name__ == "__main__":
    main()