import random

game_stats = {
    "level_up": 4567,
    "kingdom_coins": 10000,
    }
STATS = {
    "Level": 1,
    "Weapon": "knife",
    "xp": 0,
    "Coins": 0,
    }
monsters = {
    "Nyarlathotep": "monster1",
    "Azathoth": "monster2",
    "Dagon": "monster3",
    "Hastur": "monster4",
    }
randmon = random.choice(list(monsters.keys()))

player = input ("Welcome, Player, to Golden Castle. Before we begin, may I know what to call you?: ")

print("Alright then, " + player + ". Currently, you are in the trial zone, outside the kingdom walls of Avaral. To get into the kingdom, you need to get 10,000 coins. You currently have no coins. (You can check how many coins you have, along with how much xp you have, what level your at, and what weapon you have equipped, by typing STATS in all caps.) To get coins, you need to roam the forests outside of Avaral and fight random monsters you come across.")
fight = input("Explor the forests of Avaral? [Y]es/[N]o: ")

if fight == "Y":
    print ("You walk through the forests and come across " +randmon+ ". You kill the Eldritch beast and gain coins and xp. Good job!")
else:
    print ("You can't get into the kingdom without money, so either stand outside those walls forever and starve to death, or get your lazy butt in that forest and slay some Eldritch beasts!")
