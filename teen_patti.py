from collections import Counter
from random import *
from time import sleep

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

    def __init__(self, name, cards=None, faces=None, colors=None, sorted_face_values=None, has_trial=None, has_run=None, has_double=None, has_color=None, has_jute=None, side_show_num = 0, has_seen=False, has_quit=False):
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
        self.side_show_num = side_show_num
        self.has_seen = has_seen
        self.has_quit = has_quit
    
    def __str__(self):
        return f"Name: {self.name}, cards: {self.cards}"

def main():
    global players_with_trial,players_with_double,players_with_run,players_with_color,players_with_jute,single_players, diff_players, bool_value
    #write constant variables here if need be
    round = 0
    bool_value = {"yes": True, "no":False}
    new_players = players_maker() #player objects have been made
    players = list(new_players) #making new list, cuz i don't think i should be interfering with the original list...cuz it will get a lot messier down the line when in-game!
    diff_players = diff_players_gen(players)
    diff_players = list(filter(lambda x: len(x) > 0, diff_players))
    num_players = len(players)

    while num_players >= 2:
        players = [player for player in players if not player.has_quit]
        num_players = len(players)
        round+=1
        print("this is round", round)
        i=0
        
        while i < num_players:
            player = players[i]
            last_player = players[i-1]
            seen(player)
            if player.has_seen:
                quit(player, round)
                if player.has_quit:
                    players.pop(i)
                    num_players-=1
                    continue
                #if he didn't quit then this:
                #time for sideshow
                if last_player.has_seen:
                    if_side_show = side_show(player, last_player, round)
                    if not if_side_show:
                        i+=1
                        continue
                    if player.has_quit:
                        players.pop(i)
                        num_players-=1
                        '''if num_players==1:
                            return'''
                        break
                    else:
                        player.side_show_num = 0
                        players.pop(i-1)
                        num_players-=1
                        break
            else:
                bool_open = open(player, players)
                if bool_open:
                    return
                else:
                    i+= 1 
                    continue
                return

            i+=1
        #inner loop ends here
    return


def error(player_name):
    bool_error_msg = "you must enter 'yes' or 'no'!"
    print(f"{player_name}, {bool_error_msg}")


def players_maker():
    while True:
        try:
            num_players = int(input("How many players want to play? (only 2-10 are allowed) : "))
            if num_players not in range(2, 11): raise ValueError("Please enter a valid number between 2-10")
        except ValueError:
            print("Ops! There seems to be an error")
            continue
        players = [Player(f"Player {i+1}") for i in range(num_players)] #defining each player
        for player in players:
            player.cards = card_gen()
            player.faces, player.colors, player.has_trial = trial(player.cards)
            player.has_run, player.sorted_face_values = run(player.faces)
            player.has_color = color(player.colors)
            player.has_jute = jute(player.faces)
            print(player)
        return players

deck_main = [f"{card}: {color}" for card in Player.cards.keys() for color in Player.pattern] #need to make deck and then make a copy instead of messing with the original actual deck
deck = list(deck_main)
def card_gen():
    shuffle(deck)
    three_cards = sample(deck, 3)
    [deck.remove(card) for card in three_cards if card in deck]
    return three_cards

def diff_players_gen(players):
    #Now, comparing players on different terms:
    players_with_trial = [player for player in players if player.has_trial]
    players_with_run = [player for player in players if player.has_run]
    players_with_color = [player for player in players if player.has_color]
    players_with_double = list(set(players_with_color) & set(players_with_run))
    players_with_jute = [player for player in players if player.has_jute]
    single_players = players.copy()

    return players_with_trial, players_with_double, players_with_run, players_with_run, players_with_color, players_with_jute, single_players

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
    diff_players = diff_players_gen(players)
    diff_players = list(filter(lambda x: len(x) > 0, diff_players))
    for players_condition in diff_players:
        if not (winner:=single_winner(players_condition)):
            continue
        return winner
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
            return highest_players[0][0]
        else:
            single_players = [player for player, value in highest_players]
            continue
    return f"No one won"

def win_printer(player):
    print(f"{player.name} has won!!")


#blind specific functions
def seen(player):
    while True:
        try:
            if not player.has_seen:
                seen = input(f"{player.name}, do u want to see the cards? ('yes'|'no') ").strip().lower()
            else:
                return
            if not seen in bool_value:
                raise ValueError("only 'yes' or 'no' will do!")
            player.has_seen = bool_value[seen]
            if player.has_seen:
                print(player)
            return
        except ValueError as e:
            print(e)
            continue

def open(player, players):
    while True:
        try:
            if (ask:= input(f"{player.name}, do u want to open all's cards? ('yes'|'no')")) not in bool_value:
                raise ValueError("DO U WANNA OPEN OR NOT?")
            open = bool_value[ask]
            if not open:
                return
            for plyr in players:
                print(plyr)
                sleep(0.2)
            win_printer(win_generator(players))
            return True
        
        except ValueError as e:
            print(e)
            continue

def quit(player, round):
    while True:
        try:
            if (quit:= input(f"{player.name}Do you want to fold? ('yes'|'no') ").strip().lower()) not in bool_value:
                raise ValueError(f"{player.name}, u wanna quit; yes or no?")
            player.has_quit = bool_value[quit]
            if player.has_quit:
                print(f"{player.name} has quited in round {round}!!!!")
            return
        except ValueError as e:
            print(e)
            continue
  

def side_show(player, last_player, round):
    side_show_num = 0
    while True:
        side_show = None
        try:
            if not side_show:
                if (side_show := input(f"{player.name} do u wanna request a sideshow? (yes|no) ").strip().lower()) not in bool_value:
                    raise ValueError("Sideshow, yes or no!!!??? ")
            side_show_value = bool_value[side_show]
            #if sideshow exists then do this
            if not side_show_value:
                return False
            player.side_show_num+= 1
            if player.side_show_num < 3:
                if (side_show_request:= input(f"{last_player.name}, do u accept {player.name}'s sideshow? (yes|no) ")) not in bool_value:
                    raise ValueError(f"{last_player.name}, do u want side show or not?")
                side_show_request = bool_value[side_show_request]
                if not side_show_request:
                    return False
            if player.side_show_num == 3 or side_show_request:
                print(f"{last_player.name}, you are forced to accept this sideshow, cuz it's the third time!! ")
                sideshow_list = [player, last_player]
                side_show_winner = win_generator(sideshow_list)
                for side_shower in sideshow_list: #sideshower meaning players participated in this sideshow
                    if  side_shower != side_show_winner:
                        side_shower.has_quit = True
                        print(f"{player.name} has quit in round {round}.")
                print(side_show_winner.name, f"has won the sideshow in round {round}")
                return True
        

        except ValueError as e:
            print(e)
            continue


if __name__ == "__main__":
    main()


#Simley face, crying face.
#wtf is wrong with my code?
#sometimes it works the way i totally intend it to..sometimes.....it's a fucking mess..