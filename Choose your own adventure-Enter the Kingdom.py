import random
import time

game_stats = {
     "level_up": 35000,
     "kingdom_coins": 10000,
     }
STATS = {
     "Level": 1,
     "Weapon": "Knife",
     "xp": 0,
     "coins": 0,
     }
monsters = {
     "Nyarlathotep":"monster1",
     "Azathoth": "monster2",
     "Dagon": "monster3",
     "Hastur": "monster4",
     "Aiueb Gnshal": "monster5",
     "C'thalpa": "monster6",
     "Cxaxukluth": "monster7",
     "Kaajh'Kaalbh": "monster8",
     "Ycnàgnnisssz": "monster9",
     }


player = input("Welcome, player, to floating castle. Before we begin our journey, I need a name to call you by. Can't call you 'The Player' for the whole game."\
               " Type in the name you'd like to go by: ")
print("Alright then, " +player+ ". Your story begins just outside of the walls of the great city of Avaral. You came all the way from your home kingdom of Solvir to visit a friend of yours."\
       " Anamore was her name, and she resided in the castle of the royal family, and as she is one of the best witches in the country, acted as the head of magical research. You hadn't seen her"\
       " in quiet a bit of time, and had decided to come for a visit. When you came to the large gates of the kingdom, however, you found yourself faced with an entry fee of 10,000 coins that"\
       " didn't exist last time you visited. You unfortunately had used up all of your money on resources on your way here, so you had 0 coins on your person. to check how many coins you have at"\
       " any given momnet, along with how much xp, what weapon you have equipped, and what level your on, simply type STATS in all caps. Go ahead and give it a try.")

while True:
    stat = input("Type STATS: ")
    if stat == "STATS":
        print ("Great! Like knowing that your currently weaker then the weakest eldritch beast?")
        break
    else:
        print ("I'm not letting you leave until you check your stats")




print("Moving on, you heard through the grapevine that monsters"\
       " in the forests surounding Avaral drop coins when you fought them.")

time.sleep(2)

while True:
    monfight = random.choice(list(monsters.keys()))
    fight = input("Explore the forests of Avaral? [Y]es/[N]o: ")
    if fight == "y":
       STATS["xp"] = STATS["xp"] + random.choice(range(500,1000))
       STATS["coins"] = STATS["coins"] + random.choice(range(100,500))
       print ("You walk through the forests and come across " +monfight+ ". You kill the Eldritch beast and gain coins and xp. you now have " +str(STATS["coins"])+ \
              " coins and " +str(STATS["xp"])+ " xp. Good job!")
       else:
        print ("You can't get into the kingdom without money, so either stand outside those walls forever and starve to death, or get your lazy butt in that forest and slay some Eldritch beasts!")

  if STATS["xp"] == game_stats["level_up"]:
STATS["Level"] = STATS["Level"] + 1
    print("You went up one level! Your doing great sweety~")
else:
   print("Nothing happened. Your close though!")

if STATS["coins"] == game_stats["kingdom_coins"]:
    print("You have enough coins to get into the kingdom now! You can keep grinding for coins and xp t be able to level up and buy stuff in the kingdom market." \
          " Whenever your ready to head into the kingdom, type ENTER KINGDOM in all caps. You can come back to grind at any time.")      
else:
   print("keep going, you still need more coins to enter the kingdom")


#need to add that last section to the while loop
