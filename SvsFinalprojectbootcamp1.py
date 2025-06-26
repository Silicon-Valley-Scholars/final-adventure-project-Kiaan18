import random
import time
import sys
def Pillars(guess):
    if Parkour == "left":
        print("You guessed it right! Time for the next challenge")
    else:
        print("You guessed wrong, a magical force sends you to the start of the obsticle and gives you another chance, dont mess it up")
xp = 0
print(" You have", xp, "points")
wepon = "sword"
player_name = input("What is your name?: ")

input("Hello "+player_name+", I am Ragni, King of the vast lands of Wynn, I request your help to fight the arising corruption south of the abandoned lands of Fruma, Do you choose to accecpt?: ")
if "yes":
    time.sleep(1)
    print("Great! to prove yourself i will give you some tasks to finish to declare your knighthood, you shall start now!")
    time.sleep(5)
    xp += 20
    print("Your gained", xp , "experience points")                                                                                                                                # Kill Zombies
    time.sleep(2)
    Kill = input("      You find a zombie to kill, would  you like to use your fist or your sword?: ")
    if Kill.lower() == "sword":
        print("You kill the zombie in 2 swings!")
    elif Kill.lower() == "fist":
        print("You kill the zombie in 14 hits")
    else:
        print("not an option, you run out of time and die")
        sys.exit()
    xpGain = random.randint(10,30)
    xp += xpGain
    print ("You gained", xpGain ," experience points")
    time.sleep(2)
    print("You have ", xp," total experience points")


    time.sleep(3)                                                                                              # Decrepit Sewers                                                                      
    print(" The king has tasked you with a quest, far west of the lands of Ragni remains the Decrepit sewers, layer of the Witherhead. He requires you to slay him and bring back his head")
    time.sleep(1)
    print ("Now be on your way!")
    time.sleep(7)
    print ("    Your arive at the Decrepit Sewers, but to enter you need a key!")
    time.sleep(1)
    print("      Right outside of the Sewers you see a key gardian! You must slay it for the key")
    time.sleep(1)
    Key = input("Would you like to use your fists or your sword to kill the Key gardian?: ")
    if Key.lower() == "sword":
        print(" You kill it in 27 hits! Barely")
        time.sleep(2)
        xpGain2 = random.randint(150,275)
        xp += xpGain2
        print("You gained", xpGain2," experience points" )
        print("You have", xp," total experience points")
    elif Key.lower() == "fist" or "fists":
        print(" Sorry, but this beast is too strong for just bare hands")
        time.sleep(1)
        print("You Die")
        sys.exit()
    else:
        print("That isnt an option! You run out of time and die")
        sys.exit()
    print(" You enter the Decrepit sewers, but before you can fight the Witherhead, you need to complete some obstacles and parkour, if you fail you restart")
    print ("There are 3 lines of pillars which you must jump on, but some of them are unstable and will cause you to fall, pick the right one to complete the obstacle")
    time.sleep(3)
    Parkour = input("choose which pillar to jump on! left, middle, or right.:")
    if Parkour.lower() == "left":
        print("You guessed it right! Time for the next challenge")
    else:
        print("You guessed wrong, a magical force sends you to the start of the obsticle and gives you another chance, dont mess it up")
        Parkour = input("choose which pillar to jump on! left, middle, or right.")
        Pillars("left")
    print("You finished the obsticle, now you enter the next room")
    xp += 100
    time.sleep(1)
    print("You gain 100 experience points")
    print("You have ", xp," experience total points and you unlock a new spell called Slam!")
    print("You see the Witherhead's lair, but there are skeletons gaurding the entrace, you have to face them")
    print("Its a 10 vs 1, you need to use your spell,")
    Spell = input(" use spell. Yes, No:")
    time.sleep(2)
    if Spell.lower() == "yes":
        print(" you use the spell and you slam your sword to the ground, uplifting the earth in a circular motion around you, knocking each skeleton off balance and weponless, now you just need to finish the job")
        print(" Great! Now its time to face the Witherhead")
    else:
        print("Without the spell you are outnumbered and you stand no chance, you try to fight but you die")
        sys.exit()
    print(" You enter the room, and see the witherhead, pure evil, you know that your newfound spell wont be enought to stop him")
    time.sleep(1)
    print("Then you remember, before entering the dungeon you picked up a glowing flower, now is the time to use it")
    time.sleep(2)
    print(" He is pure evil, the only way to destroy him is with the POWER OF FRIENSHIP!, you hand him the flower and ask to be his friend")
    time.sleep(1)
    print(" He has never experienced such kindness before, you can see the evil flushed out of him! But the king requested his skull, your are left between disobeying the king or betraying your newfound bestfriend! you have a choice to make")
    time.sleep(2)
    Choice =input(" Do you choose to betray your bestfriend, or the king? Best friend, King:")
    if Choice.lower() =="king":
         print(" You become an outlaw and live happily ever after with your newfound bestfriend")
    elif Choice.lower() == "best friend":
        print(" While the Witherhead isnt looking you stab him in the back, you walk back to the king with a heavy heart, and get accepted as a knight, BUT AT WHAT COST??")
    else:
        print("Not an option")
        sys.exit()

else:
    print("Dissapointing but fair, I shall send a carraige to carry you back to your home")