import random

game_stats = {
    "level_up": 350,
    "kingdom_coins": 10000,
    }
STATS = {
    "Level": 1,
    "Weapon": "knife" ,
    "xp": 0,
    "Coins": 0,
    }
player = input ("Welcome, Player, to Golden Castle. Before we begin, may I know what to call you?: ")

print ("Alright then, " + player + ". Currently, you are in the trial zone, outside the kingdom walls of Avaral. To get into the kingdom, you need to get 10,000 coins. You currently have no coins. you can check on your coins, xp, and level by typing STATS. Give it a try: ")
