'''what else is remaining?:
1>show option for these unblind cunts ///// DONE ✅
2>introduce the concept of pot and bet value
    give each player a starting value of $400
    let user choose the pot value and add-up betting value
    use Player class to check and track each player's outgoing value
    then give all the value to winner
    then save it all in patti_data.txt or csv
    then load the values(remaining ones) from there in the next round....
    see? it gets better this way...i can even see for history....
    and write code definsively..so that at first(when the program is first run)...instead of deleting previous histories,
    start adding up new ones, and with date too...and use it to know if you should new assign values to players or load from previous data

    damm...I/O ni babbal use hune vayo ta haha....ajai 1 hapta lagla jasto xa 


3>count no of sideshow

idk what's wrong but...it certainly still contains a lot of bugs....
fix it...tespaxi balla no of sideshow=3 for forcing add gar(easy nai hunxa hola)
may be try removing a player after it has quit ani balla fix the bugs..or idk.....
i'm sleepy and i'm gonna sleep now!

fuck everything's wrong with my code T_T 




'''
bool_value = 0

"""make functions for a player's atributes....liie .has_seen and has_quit,"""
def quit(player):
    while True:
        try:
            if (quit:= input("Do you want to fold? ('yes'|'no') ").strip().lower()) not in bool_value:
                raise ValueError(f"{player.name}, u wanna quit; yes or no?")
            player.has_quit = bool_value[quit]
            if player
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
                return False
            for plyr in players:
                print(plyr)
                sleep(0.1)
            win_printer(win_generator(players))
            return True
        
        except ValueError as e:
            print(e)
            continue

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
            return
        except ValueError as e:
            print(e)
            continue

def side_show(player, last_player):
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
            if (side_show_request:= input(f"{last_player.name}, do u accept {player.name}'s sideshow? (yes|no) ")) not in bool_value:
                raise ValueError(f"{last_player.name}, do u want side show or not?")
            side_show_request = bool_value[side_show_request]
            if not side_show_request and player.side_show_num < 3:
                return False
            else:
                print(f"{last_player.name}, you are forced to accept this sideshow, cuz it's the third time!! ")
                sideshow_list = [player, last_player]
                side_show_winner = win_generator(sideshow_list)
                for side_shower in sideshow_list: #sideshower meaning players participated in this sideshow
                    if  side_shower != side_show_winner:
                        side_shower.has_quit = True
                        print(f"{player.name} has quit in round {round}.")
                    #if both have equal hands then...do something too
                print(side_show_winner.name)
                return True
        

        except ValueError as e:
            print(e)
            continue
            





'''

def diff_players_gen(players):
    #Now, comparing players on different terms:
    players_with_trial = [player for player in players if player.has_trial]
    players_with_run = [player for player in players if player.has_run]
    players_with_color = [player for player in players if player.has_color]
    players_with_double = list(set(players_with_color) & set(players_with_run))
    players_with_jute = [player for player in players if player.has_jute]
    single_players = players.copy()

    return players_with_trial, players_with_double, players_with_run, players_with_run, players_with_color, players_with_jute, single_players




def win_generator(players):
    diff_players = diff_players_gen(players)
    for players_condition in diff_players:
        if not (winner_name:=single_winner(players_condition)):
            continue
        return winner_name
    return "Winner is None"


"""
def win_generator(players):
    global players_with_trial,players_with_double,players_with_run,players_with_color,players_with_jute,single_players, diff_players
    for players_condition in diff_players:
        if not (winner_name:=single_winner(players_condition)):
            continue
        return winner_name
    return "Winner is None"
"""

=



    """
    things i know:
        i,my variables, already know which player has trial, color, run, jute
        i can decide the winner using functions...but not in  a pretty way
    """
    '''
    things this function needs to do:
        take players
        compare the players' by throwing the into trial, run, color, jute and single functions
        but return, by priority, if one person wins before anyone else


        the given code does all of this...but it's ugly as fuck!

        new plan:
            if trial then for pleyrs with trial, return the winner
            (sounds easy right? i think so...and i already have the means to do so...so yea, it shouldn't be that hard)
            then comes doubling:
            for players with both run and color, return the winner
            since all the player have color,(which doesn't hold any value if another person also has a doubling)
            we need to return the player with highest run value..and return None if run is draw!
            for players with run, winner is the one with highest value..but return None if there are two or more with same run
            for player with color, use single_winner function...ez!
            for players with jute, use single_winner function...ez!
            if nothing, use single_winner function....
            infact use single winner function everywhere...
            i just love the fact that i made single_winner functinon...it's soooooooooooo nice and works perfectly k
            i'm proud of myself for making it lol
        '''

