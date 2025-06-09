Health = 3 # creating health system
Health_potion = 0
handbook = False
cure_potion = False
import random
#########################################################################################################################################################################
def Death_Checker():#checking if players health is equal to or less than zero
    global Health
    if Health <=0:
        Game_Over_Menu()
#########################################################################################################################################################################
def Enemy_Decider():#Used to decide on enemy encounter
    comp_Number = random.randint(1, 4)
    if comp_Number == 1:
            Enemy_Encounter_1()
    elif comp_Number == 2:
            Enemy_Encounter_2()
    elif comp_Number == 3:
            Enemy_Encounter_3()
    elif comp_Number == 4:
            Enemy_Encounter_4()
#########################################################################################################################################################################
def Enemy_Encounter_1():#enemy encounter Cat girl
    global Health#declaring we want to use global health variable
    global Health_potion#declaring we want to use global health variable
    Enemy_Health = 3 # creating the local variable enemy health
    Fight = True # setting up a while loop
    while Fight == True:
         print("------------------------------------------------------------------------------------------------------------------------------")
         print("The figure leaps out the darkness and your eyes adust to the sight of the creature")
         print("The creature seems to be in an oversized Hoodie and wearing a neon pair of headphone with cat ears at the top")
         print("The creature come forward and tries to swipe at you like a cat")
         print(f"You have {Health} hp left")
         print(f"The enemy has {Enemy_Health} hp left")
         print(f"You have {Health_potion} Health potions left")
         User_Input = input("Do Attack, Dodge or use a Health potion?: ")
         if User_Input == "attack":#first decision
             comp_Number = random.randint(1, 20)
             if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully jab the creature and it goes down but only for a moment")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You have slain the creature.")
                 Fight = False # ending the while loop
             else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack the creature but miss and the creature claws you and you step back.") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
         elif User_Input == "dodge":#second decision
                 comp_Number = random.randint(1, 20)
                 if comp_Number > 10:
                     print("------------------------------------------------------------------------------------------------------------------------------")
                     print("You successfully sidestep the creatures claw attack.")
                 elif comp_Number <= 10:
                     print("You attempt to dodge the creature attack but trip and the creature claws you and you step back.")
                     Health -= 1 # adjusting players health by minus 1
                     Death_Checker()
         elif User_Input == "health potion":#third decision
            Health_potion -= 1
            Health += 1
         else:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("Invalid selection try again.")
#########################################################################################################################################################################
def Enemy_Encounter_2():#enemy encounter squire
    global Health#declaring we want to use global health variable
    global Health_potion #declaring we want to use global health potion variable
    Enemy_Health = 5 # creating the local variable enemy health
    Fight = True # setting up a while loop
    while Fight == True:
         print("------------------------------------------------------------------------------------------------------------------------------")
         print("The figure leaps out the darkness and your eyes adust to the sight of the creature")
         print("The creature rises up and you immediately see the metallic armour, the blood shot eyes their blood stained sword, the squire hunches over and starts walking forward tightening its grip on the bloody sword")
         print("The creature comes forward while swinging its blade")
         print(f"You have {Health} hp left")
         print(f"The enemy has {Enemy_Health} hp left")
         print(f"You have {Health_potion} Health potions left")
         User_Input = input("Do Attack, Dodge or use a Health potion?: ")
         if User_Input == "attack": #first decision
             comp_Number = random.randint(1, 20)
             if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully strike the creature and it goes down but only for a moment")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You have slain the creature.")
                 Fight = False # ending the while loop
             else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack the squire but it swipes and strike you in the chest") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
         elif User_Input == "dodge":#second decision
                 comp_Number = random.randint(1, 20)
                 if comp_Number > 10:
                     print("------------------------------------------------------------------------------------------------------------------------------")
                     print("You successfully sidestep the squires sword strike.")
                 elif comp_Number <= 10:
                     print("You attempt to dodge the squires attack but trip and their sword swings down and strikes you")
                     Health -= 1 # adjusting players health by minus 1
                     Death_Checker()
         elif User_Input == "health potion":#third decision
            Health_potion -= 1
            Health += 1
         else:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("Invalid selection try again.")
#########################################################################################################################################################################
def Enemy_Encounter_3():#enemy encounter slime
    global Health#declaring we want to use global health variable
    global Health_potion #declaring we want to use global health potion variable
    Enemy_Health = 2 # creating the local variable enemy health
    Fight = True # setting up a while loop
    while Fight == True:
         print("------------------------------------------------------------------------------------------------------------------------------")
         print("The figure leaps out the darkness and your eyes adust to the sight of the creature")
         print("The creature is a small mass, it has translucent green skin and seems to leave a slimy puddle when it moves")
         print("The creature come writhing over")
         print(f"You have {Health} hp left")
         print(f"The enemy has {Enemy_Health} hp left")
         print(f"You have {Health_potion} Health potions left")
         User_Input = input("Do Attack, Dodge or use a Health potion?: ")
         if User_Input == "attack": #first decision
             comp_Number = random.randint(1, 20)
             if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully strike the creature but its gelatinous body goes back to it original shape")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You have slain the creature.")
                 Fight = False # ending the while loop
             else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack the creature but you attack slides right off its slimy pulsating body") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
         elif User_Input == "dodge":#second decision
                 comp_Number = random.randint(1, 20)
                 if comp_Number > 10:
                     print("------------------------------------------------------------------------------------------------------------------------------")
                     print("You successfully step away from the creatures path.")
                 elif comp_Number <= 10:
                     print("You attempt to dodge the creatures lunge forward but you slip and its wriggly body strikes your chest")
                     Health -= 1 # adjusting players health by minus 1
                     Death_Checker()
         elif User_Input == "health potion":#third decision
            Health_potion -= 1
            Health += 1
         else:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("Invalid selection try again.")
#########################################################################################################################################################################
def Enemy_Encounter_4():#enemy encounter spider
    global Health#declaring we want to use global health variable
    global Health_potion #declaring we want to use global health potion variable
    Enemy_Health = 4 # creating the local variable enemy health
    Fight = True # setting up a while loop
    while Fight == True:
         print("------------------------------------------------------------------------------------------------------------------------------")
         print("The figure leaps out the darkness and your eyes adust to the sight of the creature")
         print("The creatures legs comes into focus first its 8 hairy, slender legs make a excruciating noise on the cobblestone the only other noticeable feature of the creature is its main body that is as black as night with the only expectance being its 2 narrow red eyes pinned on you")
         print("The creature comes crawling over towards you")
         print(f"You have {Health} hp left")
         print(f"The enemy has {Enemy_Health} hp left")
         print(f"You have {Health_potion} Health potions left")
         User_Input = input("Do Attack, Dodge or use a Health potion?: ")
         if User_Input == "attack": #first decision
             comp_Number = random.randint(1, 20)
             if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully strike the spiders on it body and it hisses and jumps backwards")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You have slain the creature.")
                 Fight = False # ending the while loop
             else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack the creature but the spider jumps forward lands on you and bites you") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
         elif User_Input == "dodge":#second decision
                 comp_Number = random.randint(1, 20)
                 if comp_Number > 10:
                     print("------------------------------------------------------------------------------------------------------------------------------")
                     print("You successfully back away from the spiders jump")
                 elif comp_Number <= 10:
                     print("You attempt to dodge the creatures attack but slip and the creatures fangs cling on to your leg")
                     Health -= 1 # adjusting players health by minus 1
                     Death_Checker()
         elif User_Input == "health potion":#third decision
            Health_potion -= 1
            Health += 1
         else:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("Invalid selection try again.")
#########################################################################################################################################################################
def NPC_1():#creating npc dialogue
    global Health_potion
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You open your mouth to speak but the desponded figure speaks and says:")
    print("So what brings you to this place")
    User_Input = input("Do you come seeking something, or someone? ")
    if User_Input == "Something":#something response
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("Well sorry to say but these here halls have been picked clean of its treasures, all that is left now is the remnants of a time long forgotten")
    elif User_Input == "Someone":#something response
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("Well you came to the wrong place no one has been here in a very ... long time.")
    else:
            print("Invalid selection try again.")
            NPC_1()
    print("As you ponder what he has said he reaches out with three flasks and say:")
    print("Take these they will help you in your journey")
    Health_potion += 3
    print(f"You have, {Health_potion} health potions left.")
    print("The stranger retreats back to silence and stays sat there without motion.")
    print("You decide to move along.")
    Corridor_3()#going to corridor 2
#########################################################################################################################################################################
def NPC_2_Peace():
    global handbook
    global cure_potion
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You approach the figure and try and open your mouth to speak but before you can the figure eyes turn to you and suddenly he starts speaking in a very worried, and quick pace")
    print("Book... Book... Do you have my book? I need it back. You know its not safe to keep it away from me. I can feel it calling...")
    if handbook == True:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You remember the book you found and stowed away earlier on and proceed to reach for it in your satchel")
        print("As soon as you bring the book out the figure eyes seem to lighten up, the figure almost pounces towards and snatches the book out of your hand")
        print("My book . . . My book Thank you stranger i have been without Book for so long, here take this as token of my gratitude")
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The creature roots around in his satchel that was beside him at the fountain and pulls out a flask with some unknown purple liquid in")
        print("Use this if you are in perilous situation, but be warned you will only have one chance with this ")
        cure_potion = True
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You have no idea what the creature is talking about and soon enough the creature stops looking at you and slumps away")
        print("My book . . . My book where is my book")
        print("The creature seems to be silently crying, so you decide to leave the creature in peace")
        Corridor_5()
#########################################################################################################################################################################
def NPC_2_Fight():
    Enemy_Health = 5
    global Health#declaring we want to use global health variable
    global Health_potion#declaring we want to use global health variable
    Fight = True # setting up a while loop
    while Fight == True:
     print("------------------------------------------------------------------------------------------------------------------------------")
     print("The creatures eye transfixed upon you after a moment the creature leaps towards you snarling saying:")
     print("My Book . . . My Book you stole my book you shall die")
     print(f"You have {Health} hp left")
     print(f"The enemy has {Enemy_Health} hp left")
     print(f"You have {Health_potion} Health potions left")
     User_Input = input("Do Attack, Dodge or use a Health potion?: ")
     if User_Input == "attack":#first decision
        comp_Number = random.randint(1, 20)
        if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully strike the creature and the creature back down but only for a moment")
                print("My Book, My book give it now!")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You strike the creature and it falls down but before dying you can hear the creature last words be:")
                 print("My book . . . My book i want my Book . . . . . ")
                 print("The creature is dead")
                 Fight = False # ending the while loop
        else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack but your sword falls short and the creature jabs you in your stomach")
                 print("My Book, My Book i cannot live without it!") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
     elif User_Input == "dodge":#second decision
         comp_Number = random.randint(1, 20)
         if comp_Number > 10:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("You successfully sidestep the creatures attack")
          print("My Book, My book calls to me!")
         elif comp_Number <= 10:
          print("You attempt to dodge the creatures attack but trip and the creature jabs your throat")
          print("My Book, My book you stole")
          Health -= 1 # adjusting players health by minus 1
          Death_Checker()
     elif User_Input == "health potion":#third decision
         Health_potion -= 1
         Health += 1
     else:
      print("------------------------------------------------------------------------------------------------------------------------------")
      print("Invalid selection try again.")
#########################################################################################################################################################################
def Game_Over_Menu():#creating game over menu
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("Game over")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("Would you like to try again?")
    User_Input = input("Yes or No: ")
    if User_Input == "yes":
        global Health
        global Health_potion
        Health += 3 
        Health_potion == 0
        Start_Menu()
    elif User_Input == "no":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Ok goodbye")
        exit()
    else:
        print("Invalid selection try again.")
        Game_Over_Menu()
#########################################################################################################################################################################
def Start_Menu():#creating start menu
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("Hello Brave Adventurer do you wish to enter a word filled with challenge and intrigue")
    User_Input = input("Yes/No: ")
    if User_Input == "Yes":
        Corridor_1()
    elif User_Input == "No":
        print("Ok Goodbye")
        exit()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
    Start_Menu()
#########################################################################################################################################################################
def Corridor_1():#creating corridor 1
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You wake up in a small room, the rooms floor and walls seem to be made out of cracked stone there are broken beams along the ceiling and a single lone lanterns hangs in the middle of the ceiling")
    print("On the walls you also notice what seems to be broken shackles and moss. Whatever this place was its been a while since its seen any life")
    print("As you stand up you notice a short dagger by your side and your clothes seems to be slightly worn, you have a slight headache but are well enough to think and see clear.")
    print("You see that their are 3 doors around you, one to the Right, one to the Left and one that leads Forward.")
    User_Input = input("What way do you want go: ")
    comp_Number = random.randint(1, 3)
    if comp_Number == 1:
        Left_Room_1()
    elif comp_Number == 2:
        Right_Room_1()
    else:
        Forward_Room_1()
#########################################################################################################################################################################_
def Left_Room_1(): #trap room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You enter a room similar to the other with the only difference being more vines on the walls.")
    print("The room has row of shells to the side that are covered in a thick layer of dust, but on one of the shelf's a old chest ornate with gold lays there with the same amount of dust")
    print("There is also a door leading out")
    User_Input = input("Do you open the chest or go forward: ")
    if User_Input == "open chest":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You abroach the chest wearily and as you creak open the chest the ceiling above you revels several rows of arrows.")
        print("As you run towards the door the arrows rain down several of which manage to scrape you but, you manage to escape alive")
        print("------------------------------------------------------------------------------------------------------------------------------")
        global Health
        Health -= 1 # adjusting players health by minus 1
        print(f"You now have {Health} hp left")
        Death_Checker()
        Corridor_2()
    elif User_Input == "forward":
        Corridor_2()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Left_Room_1()
#########################################################################################################################################################################
def Right_Room_1(): #puzzle room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a room with a door blocking your way, you read on the door that if you wish to past you must answer this riddle")
    User_Input = input("I AM TALL WHEN YOUNG, BUT SHORT WHEN OLD WHAT AM I?: ")
    if User_Input == "candle":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The door swings open and you try to see what kind of mechanism could have achieved this but can see nothing, so you decide to press on.")
        Corridor_2()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The door doesn't move")
        Right_Room_1()
#########################################################################################################################################################################
def Forward_Room_1(): #lore room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You enter a room that seems to be a dilapidated jail cell, there are chains all around the room some broken others still intact")
    print("There are also faint scratch marks on the walls some seem to be tally marks others seem to be like they come from a beast")
    print("As you creep through the room the more chains appear broken but not just broken most seemingly shattered")
    print("It seems that what ever was held in this room was left here far longer then they thought")
    Corridor_2()
#########################################################################################################################################################################
def Corridor_2():
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a narrow corridor on the floor, moss and vines decorate the room")
    print("The corridor haas beams across the ceiling and the floor is made of seemingly cracked and cobbled stone slabs.")
    print("There are three doors around you seemingly as broken as the rest of this place., one to the Right, one to the Left and one that leads Forward.")
    User_Input = input("What way do you go: ")
    comp_Number = random.randint(1, 30)
    if comp_Number <= 10:
        Left_Room_2()
    elif comp_Number > 10 and comp_Number <= 20:
        Right_Room_2()
    else:
        Forward_Room_2()
#########################################################################################################################################################################
def Left_Room_2(): #lore room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("As soon as you enter the rom you immediately notice the shelf's of miscellaneous armour pieces helmets, boots and others")
    print("The armour seems to be scratched and slightly rusted but in the palm of one of the gloves is a old book")
    print("You undo the twine holding the book and notice most the pages have been either torn out or burned")
    print("You find one of the more intact pages and it reads:")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("May 16th The prisons have seen more than a double increase in the amount of criminals coming in, no one seems to know why but we all we know is that they have displayed repeated fits of anger and rage ")
    print("Some believe a plague has befallen the land others believe they are rebelling against the kings and his rule")
    print("We have also been informed that to prevent a grand scale escape, each level now requires a different to progress, and to not attempt to use the wrong key or there will be consequences")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("The page ends there the rest seemingly been torn out")
    print("You decide to keep the book and carry forward")
    global handbook
    handbook = True
    Corridor_3()
#########################################################################################################################################################################
def Right_Room_2(): # NPC 1
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You walk into a room that is brighter and seems like a sort of mess hall")
    print("In the room you see a campfire and a figure sitting by the fire seemingly staring into the embers.")
    print("You abroach the figure and see that is seems to be a person wearing a seemingly medieval attire.")
    User_Input = input("Do you wish to speak to the person?: ")
    if User_Input == "No":
        print("You decide to ignore the stranger and move along.")
        Corridor_3()
    elif User_Input == "Yes":
        NPC_1()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Right_Room_2()
#########################################################################################################################################################################
def Forward_Room_2():# key problem
    global Health
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You enter the room and see the way forward is blocked by a old door with a strange keyhole shape in the middle")
    print("One the floor there seems to be a pile of metallic armour and you notice that in there is a chain with three keys attached")
    print("The keys seems seems to each have different designs one of them has a spider on top, another has a skull on top and the last has a snake design on top")
    print("You think the keys can help open the door but you do not know what key will help the door, you look at the door for a clue but can only see an engraving that feature")
    User_Input = input("Do you use the spider, skull or Snake key ")
    if User_Input == "spider key":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The door open leading the way for you to continue")
        Corridor_3()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You insert the key and as you turn the key, the door opens up but so does the ceiling and darts start immediately flying out, you rush out the room but not before being hit byt a few")
        global Health
        Health -= 1
        print("------------------------------------------------------------------------------------------------------------------------------")
        print(f"You now have {Health} hp left")
        Corridor_3()
#########################################################################################################################################################################
def Corridor_3():# 
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a narrow corridor on the floor, moss and vines decorate the room")
    print("The corridor has beams across the ceiling and the floor is made of seemingly cracked and cobbled stone slabs.")
    print("There are three doors around you seemingly as broken as the rest of this place., one to the Right, one to the Left and one that leads Forward.")
    User_Input = input("What way do you go: ")
    comp_Number = random.randint(1, 3)
    if comp_Number == 1:
        Left_Room_3()
    elif comp_Number == 2: 
        Right_Room_3()
    else:
        Forward_Room_3()
#########################################################################################################################################################################
def Left_Room_3(): # Enemy_Encounter
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You enter a room thats decrypted as the others but from the shadows you see movement")
    print("You look into the darkness and the figure comes closer and closer")
    User_Input= input("Do you Fight or Flee?: ")
    if User_Input == "fight":
        Enemy_Decider()
    elif User_Input == "flee":
        comp_Number = random.randint(1, 20)
        if comp_Number > 10:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("You manage to escape the monster.")
            Corridor_4()
        elif comp_Number < 10:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("You try to run but fail and the creature ascends upon you")
            Enemy_Decider()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Left_Room_3()
    Corridor_4()
#########################################################################################################################################################################
def Right_Room_3(): #lore room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to room that seems like an office, it features a desk, an old wooden seat and a few bookshelf's")
    print("On the desk you see a dagger that seems to be stained by old blood and a old piece of parchment that reads")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("To who ever reads this be warned the kingdom of Ironspire has fallen, the king has decreed a evacuation into the country side, the plague that has befallen the land has spread out of control.")
    print("All members of the kings royal knights have been ordered to help with the evacuation process and been also ordered to kill anyone that displays any of these symptoms")
    print("Fits of sudden anger and rage")
    print("Swollen pupils")
    print("erratic behavior")
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You try to read on but the rest of the page is covered in dried blood")
    print("You stow the page away and carry on")
    Corridor_4()
#########################################################################################################################################################################
def Forward_Room_3(): # trap potion
    global Health
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to what seems like another store room in the middle there is a table with a few dusty used flasks but there is one that has not been used")
    print("The liquid inside the flask seems to be a dark crimson color")
    User_Input = input("Do you drink the liquid or leave: ")
    if User_Input == "drink":
        comp_Number = random.randint(1, 20)
        if comp_Number <= 10:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("You dink the liquid and as you taste the last drop you feel ill and drop to the floor in pain")
            print("After a few minutes you are able to get up and leave the room leaving the empty bottle behind")
            Health -= 1
            print(f"You have {Health} hp left")
            Corridor_4()
        else:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("Invalid selection try again.")
            print("You drink the flask and as you finish it you feel stronger and better")
            Health += 2
            print(f"You have {Health} hp left")
            Corridor_4()
    elif User_Input == "Leave":
        Corridor_4()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
#########################################################################################################################################################################
def Corridor_4():
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a narrow corridor on the floor, moss and vines decorate the room")
    print("The corridor has beams across the ceiling and the floor is made of seemingly cracked and cobbled stone slabs.")
    print("There are three doors around you seemingly as broken as the rest of this place., one to the Right, one to the Left and one that leads Forward.")
    User_Input = input("What way do you want go: ")
    comp_Number = random.randint(1, 3)
    if comp_Number == 1:
        Left_Room_4()
    elif comp_Number == 2:
        Right_Room_4()
    else:
        Forward_Room_4()
#########################################################################################################################################################################
def Left_Room_4(): # enemy
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You enter the room there are boxes and barrels scattered about most turned over but some completely untouched.")
    print("As you walk though the room you seem to hear noises coming from all sides and as you look you can shadow solutes darting back and fourth ")
    User_Input= input("Do you Fight or Flee?: ")
    if User_Input == "fight":
        Enemy_Decider()
    elif User_Input == "flee":
        comp_Number = random.randint(1, 20)
        if comp_Number > 10:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("You manage to escape the monster.")
            Corridor_5()
        elif comp_Number < 10:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("You try to run but fail and the creature ascends upon you")
            Enemy_Decider()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Left_Room_4()
    Corridor_5()
#########################################################################################################################################################################
def Right_Room_4(): #riddle room
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a room with a door blocking your way, you read on the door that if you wish to past you must answer this riddle")
    print("You think to yourself this is just lazy game design, but still read the riddle")
    User_Input = input("WHAT LOSES ITS HEAD IN THE MORNING BUT GETS IT BACK AT NIGHT?: ")
    if User_Input == "pillow":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The door swings open and you try to see what kind of mechanism could have achieved this but can see nothing, so you decide to press on.")
        Corridor_5()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("The door doesn't move")
        Right_Room_4()
#########################################################################################################################################################################
def Forward_Room_4():
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You walk into a smallish room, beams and moss cover most of the room but in  the middle there is something strange.")
    print("In the middle of them room stands a fountain made of stone, it is not very big but its placement inside this place is peculiar to say the least.")
    print("As you peer at the fountain or see something, a shadow of a person, the person who seems to be wearing a guard outfit but there is something different ent about it it seems like is covered in old blood")
    User_Input = input("Do you wish to speak to this person?: ")
    if User_Input == "No":
        print("You decide to ignore the stranger and move along.")
        Corridor_5()
    elif User_Input == "Yes":
        comp_Number = random.randint(1, 20)
        if comp_Number <= 15:
            NPC_2_Peace()
            Corridor_5()
        else:
            NPC_2_Fight()
            Corridor_5()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Right_Room_4()
#########################################################################################################################################################################
def Corridor_5():
    global Health_potion
    print("------------------------------------------------------------------------------------------------------------------------------")
    print("You come to a large door around you are decayed skelton or the remains of them, their rusted armour lays by and swords litter the ground")
    print(f"You a have {Health_potion} health potions left")
    User_Input = input("Do you want to look around for any potential items or open the door?").lower()
    if User_Input == "look around":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You look around the piles of dust and bones and cannot seem to find anything of use all the weapons and armour are too weathered to be used but you do manage to collect three health flasks.")
        Health_potion += 3
        print("------------------------------------------------------------------------------------------------------------------------------")
        print(" After your search, You decide to press on and you open the door.")
        Mini_Boss()
    elif User_Input == "open door":
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("You decide to press on and you open the door")
        Mini_Boss()
    else:
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("Invalid selection try again.")
        Corridor_5()
#########################################################################################################################################################################
def Mini_Boss():
    global Health#declaring we want to use global health variable
    global Health_potion#declaring we want to use global health variable
    Enemy_Health = 6 # creating the local variable enemy health
    Fight = True # setting up a while loop
    while Fight == True:
         print("------------------------------------------------------------------------------------------------------------------------------")
         print("As you enter the chamber you notice it to be very spacious.")
         print("The figure leaps out the darkness and your eyes adust to the sight of the creature")
         print("The creature seems to be in an oversized Hoodie and wearing a neon pair of headphone with cat ears at the top")
         print("The creature come forward and tries to swipe at you like a cat")
         print(f"You have {Health} hp left")
         print(f"The enemy has {Enemy_Health} hp left")
         print(f"You have {Health_potion} Health potions left")
         User_Input = input("Do Attack, Dodge or use a Health potion?: ")
         if User_Input == "attack":#first decision
             comp_Number = random.randint(1, 20)
             if comp_Number >= 10:
                print("------------------------------------------------------------------------------------------------------------------------------")
                print("You successfully jab the creature and it goes down but only for a moment")
                Enemy_Health -= 1
                if Enemy_Health <= 0:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You have slain the creature.")
                 Fight = False # ending the while loop
             else:
                 print("------------------------------------------------------------------------------------------------------------------------------")
                 print("You try to attack the creature but miss and the creature claws you and you step back.") 
                 Health -= 1 # adjusting players health by minus 1
                 Death_Checker()
         elif User_Input == "dodge":#second decision
                 comp_Number = random.randint(1, 20)
                 if comp_Number > 10:
                     print("------------------------------------------------------------------------------------------------------------------------------")
                     print("You successfully sidestep the creatures claw attack.")
                 elif comp_Number <= 10:
                     print("You attempt to dodge the creature attack but trip and the creature claws you and you step back.")
                     Health -= 1 # adjusting players health by minus 1
                     Death_Checker()
         elif User_Input == "health potion":#third decision
            Health_potion -= 1
            Health += 1
         else:
          print("------------------------------------------------------------------------------------------------------------------------------")
          print("Invalid selection try again.")
#########################################################################################################################################################################
Start_Menu()
