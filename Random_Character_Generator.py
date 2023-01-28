
# Level 5 Character Generator by EZ Connie

from random import seed
from random import randint
import random
import math

seed()
class player:
     race = ""
     class_ = ""
     #this variable has an underscore after the name because the word class is in the Python dictionary
     weapon = ""
     armor = ""
     gender = ""
     language = ["Common" ,""]
     STR = 0
     DEX = 0
     CON = 0
     INT = 0
     WIS = 0
     CHA = 0
     AC = 0
     shield = False
     HP = 0

#creating a player called character, and we define each variable that describes a player

character = player()

# Lists of Possibilities. This is how we choose randomly with random.choices(array)

races = ["Half-Elf", "Human", "Half-Orc", "Tiefling", "Elf", "Dragonborn", "Dwarf", "Gnome", "Halfling"]

classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
           "Warlock", "Wizard"]

martial_weapons = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul",
                   "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War pick", "Warhammer",
                   "Whip"]

simple_weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light hammer", "Mace", "Quarterstaff", "Sickle",
                  "Spear"]

one_handed_weapons = ["Club", "Dagger", "Handaxe", "Javelin", "Light hammer", "Mace", "Quarterstaff", "Sickle", "Spear",
                      "Battleaxe", "Flail", "Lance", "Longsword", "Morningstar", "Rapier",  "Scimitar", "Shortsword",
                      "Trident", "War pick", "Warhammer", "Whip"]

light_armor = ["Padded", "Leather", "Studded Leather"]

medium_armor = ["Hide", "Scale Mail", "Breastplate", "Half Plate"]

heavy_armor = ["Ring Mail", "Chain Mail", "Splint Plate"]

languages = ["Undercommon", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial",
             "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan" ]

languages_without_elvish = ["Undercommon", "Dwarvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial",
             "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan" ]

# Races Randomizer

character.race = random.choice(races)

'''Class Randomizer with weighted probability. Races with certain racial bonuses will be more likely to get a class
that benefits from their bonuses. For example a Half-Elf gets a bonus to charisma, and bards, warlocks, paladins and
sorcerers do more damage the higher their charisma. so a half-elf has an 80% chance to get a class they can thrive in
and a 20% chance to be something different'''

match character.race:
    case "Half-Elf":
        d100 = randint(0,100)
        if d100 <= 20:
            character.class_ = "Bard"
        elif 40 >= d100 > 20:
            character.class_ = "Paladin"
        elif 60 >= d100 > 40:
            character.class_ = "Sorcerer"
        elif 80 >= d100 > 60:
            character.class_ = "Warlock"
        else:
            character.class_ = classes[random.choice([0, 2, 3, 4, 5, 7, 8, 11])]
    case "Human":
        character.class_=random.choice(classes)
    case "Half-Orc":
        d100 = randint(0, 100)
        if d100 <= 30:
            character.class_ = "Barbarian"
        elif 60 >= d100 > 30:
            character.class_ = "Fighter"
        else:
            character.class_ = classes[random.choice([1, 2, 3, 6, 5, 7, 8, 9, 10, 11])]
    case "Tiefling":
        d100 = randint(0, 100)
        if d100 <= 20:
            character.class_ = "Bard"
        elif 40 >= d100 > 20:
            character.class_ = "Paladin"
        elif 60 >= d100 > 40:
            character.class_ = "Sorcerer"
        elif 80 >= d100 > 60:
            character.class_ = "Warlock"
        else:
            character.class_ = classes[random.choice([0, 2, 3, 4, 5, 7, 8, 11])]
    case "Elf":
        d100 = randint(0, 100)
        if d100 <= 20:
            character.class_ = "Rogue"
        elif 40 >= d100 > 20:
            character.class_ = "Ranger"
        elif 60 >= d100 > 40:
            character.class_ = "Monk"
        else:
            character.class_ = classes[random.choice([0, 1, 2, 3, 4, 6, 9, 10, 11])]
    case "Dragonborn":
        d100 = randint(0, 100)
        if d100 <= 20:
            character.class_ = "Barbarian"
        elif 40 >= d100 > 20:
            character.class_ = "Fighter"
        elif 60 >= d100 > 40:
            character.class_ = "Paladin"
        else:
            character.class_ = classes[random.choice([1, 2, 3, 5, 7, 8, 9, 10, 11])]
    case "Dwarf":
        character.class_=classes[randint(0,11)]
    case "Halfling":
        d100 = randint(0, 100)
        if d100 <= 20:
            character.class_ = "Rogue"
        elif 40 >= d100 > 20:
            character.class_ = "Ranger"
        elif 60 >= d100 > 40:
            character.class_ = "Monk"
        else:
            character.class_ = classes[random.choice([0, 1, 2, 3, 4, 6, 9, 10, 11])]
    case "Gnome":
        d100 = randint(0, 100)
        if d100 <= 40:
            character.class_ = "Wizard"
        else:
            character.class_ = classes[random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,])]

# Weapon Randomizer. Depending on the class, we give them a weapon they can use. Martial classes get martial weapons,
# and mages get simple light weapons.

if character.class_ == "Paladin" or character.class_ == "Barbarian" or character.class_ == "Fighter" or character.class_ == "Ranger":
    character.weapon = martial_weapons[randint(0, len(martial_weapons))]
elif character.class_ == "Bard" or character.class_ == "Cleric" or character.class_ == "Rogue" or character.class_ == "Monk" or character.class_ == "Warlock":
    character.weapon = random.choice(simple_weapons)
elif character.class_ == "Sorcerer" or character.class_ == "Wizard":
    character.weapon = simple_weapons[random.choice([1, 7])]
elif character.class_ == "Druid":
    character.weapon = simple_weapons[random.choice([0, 1, 4, 7, 8, 9, 6])]

# Armor Randomizer. Depending on the class, we give them armor they can wear. Martial classes use medium or heavy armor, mages
# and monks use no armor, and classes that need to be fast and nimble wear light or medium armor

if character.class_ == "Paladin" or character.class_ == "Fighter":
    medium_or_heavy = randint(0, 6)
    if medium_or_heavy <= 3:
        character.armor = medium_armor[medium_or_heavy]
    else:
        character.armor = heavy_armor[medium_or_heavy - 4]
elif character.class_ == "Sorcerer" or character.class_ == "Wizard" or character.class_ == "Monk":
    character.armor = "no"
elif character.class_ == "Barbarian" or character.class_ == "Cleric" or character.class_ == "Ranger":
    medium_or_light = randint(0, 6)
    if medium_or_light <= 2:
        character.armor = light_armor[medium_or_light]
    else:
        character.armor = medium_armor[medium_or_light - 3]
elif character.class_ == "Bard" or character.class_ == "Rogue" or character.class_ == "Warlock":
    character.armor = light_armor[randint(0, 2)]
elif character.class_ == "Druid":
    medium_or_light = randint(0, 4)
    if medium_or_light <= 2:
        character.armor = light_armor[medium_or_light]
    else:
        character.armor = medium_armor[medium_or_light - 4]

# Gender Randomizer

character_gender = randint(1, 2)
if character_gender == 1:
    character.gender = "female"
else:
    character.gender = "male"

''' Languages. All characters can speak common. After that, depending on their race they can speak their race's language.
Humans whose main language is common can learn a random language, and Elves, in addition to knowing Elvish and Common
can learn one bonus language of their choice'''


if character.race == "Half-Elf":
    character.language[1] = "Elvish"
    character.language.append("")
    character.language[2] = random.choice(languages_without_elvish)
elif character.race == "Human":
    character.language[1] = random.choice(languages)
elif character.race == "Half-Orc":
    character.language[1] = "Orc"
elif character.race == "Tiefling":
    character.language[1] = "Infernal"
elif character.race == "Elf":
    character.language[1] = "Elvish"
    character.language.append("")
    character.language[2] = random.choice(languages_without_elvish)
elif character.race == "Dragonborn":
    character.language[1] = "Draconic"
elif character.race == "Dwarf":
    character.language[1] = "Dwarvish"
elif character.race == "Gnome":
    character.language[1] = "Gnomish"
elif character.race == "Halfling":
    character.language[1] = "Halfling"


'''Stat Roller. The way stats work in dungeons and dragons is simple. You roll a six-sided die 4 times. Then you
add the three highest values, and you have one stat. You do this 6 times, and then those 6 numbers that you rolled.
you can distribute however you want'''

rolls = [0,0,0,0,0,0]

i = 0
while i <= 5:
    dice_roll1 = randint(1, 6)
    dice_roll2 = randint(1, 6)
    dice_roll3 = randint(1, 6)
    dice_roll4 = randint(1, 6)
    rolls [i] = dice_roll4 + dice_roll3 + dice_roll2 + dice_roll1 - min(dice_roll4, dice_roll2, dice_roll3, dice_roll1)
    i += 1

# Now we need to distribute those stats.


rolls.sort(reverse=True) #we set the rolls in descending order, so we can assign the higher number (rolls[0]) to the
                         #most important stat, second higher to second important etc

if character.class_ == "Paladin" or character.class_ == "Barbarian" or character.class_ == "Fighter":
    #martial classes that have to hit hard get their most important stat, their strength, to be the highest roll
    character.STR = rolls[0]

    if character.class_ == "Paladin":
        #paladins cast spells and the higher the charisma, the stronger the spell, so second highest is the charisma stat
        character.CHA = rolls[1]
        #paladins are on the front lines, and they need a lot of health, so constitution has to be the next highest stat
        character.CON = rolls[2]
        #dexterity, wisdom, and intelligence are not important, so we just add them in the end
        character.DEX = rolls[3]
    else:
        character.CON = rolls[1]
        character.DEX = rolls[2]
        character.CHA = rolls[3]

    character.INT = rolls[5]
    character.WIS = rolls[4]

elif character.class_ == "Monk" or character.class_ == "Ranger" or character.class_ == "Rogue":
    #these classes have to be fast and nimble, so dexterity is the highest
    character.DEX = rolls[0]
    if character.class_ == "Rogue":
        character.CHA = rolls[1]
        character.CON = rolls[2]
        character.WIS = rolls[3]
        character.INT = rolls[4]
        character.STR = rolls[5]
    else:
        character.WIS = rolls[1]
        character.CON = rolls[2]
        character.STR = rolls[3]
        character.INT = rolls[4]
        character.CHA = rolls[5]

elif character.class_ == "Bard" or character.class_ == "Sorcerer" or character.class_ == "Warlock":
    #mages do more damage the higher their charisma
    character.CHA = rolls [0]
    if character.class_ == "Bard":
        character.DEX = rolls[1]
        character.CON = rolls[2]
        character.WIS = rolls[3]
        character.INT = rolls[4]
        character.STR = rolls[5]
    else:
        character.DEX = rolls[2]
        character.CON = rolls[1]
        character.WIS = rolls[4]
        character.INT = rolls[3]
        character.STR = rolls[5]

elif character.class_ == "Cleric" or character.class_ == "Druid":
    #these classes do more damage the higher their wisdom
    character.WIS = rolls[0]
    if character.class_ == "Cleric":
        character.STR = rolls[1]
        character.CON = rolls[2]
        character.INT = rolls[4]
        character.DEX = rolls[3]
        character.CHA = rolls[5]
    else:
        character.CON = rolls[1]
        character.DEX = rolls[2]
        character.STR = rolls[4]
        character.INT = rolls[3]
        character.CHA = rolls[5]

elif character.class_ == "Wizard":
    #wizards do more damage the higher their intelligence
    character.INT = rolls[0]
    character.CON = rolls[1]
    character.DEX = rolls[2]
    character.CHA = rolls[4]
    character.STR = rolls[5]
    character.WIS = rolls[3]


'''Now we assign racial bonuses. Every race has things they are genetically better at. Dwarfs are born with a stout 
disposition, and halflings who are 3 feet tall are more dexterous than other races'''



if character.race == "Half-Elf":
#Half-Elves get +2 to charisma and then 2 more points for them to distribute however they want in two other different stats
    character.CHA += 2
    if character.class_ == "Barbarian" or character.class_ == "Fighter":
        character.STR += 1
        character.CON += 1
    elif character.class_ == "Bard" or character.class_ == "Sorcerer" or character.class_ == classes [10]:
        character.DEX += 1
        character.CON += 1
    elif character.class_ == "Paladin":
        character.STR += 1
        character.CON += 1
    elif character.class_ == "Cleric" or character.class_ == "Druid":
        character.WIS += 1
        character.CON += 1
    elif character.class_ == "Monk" or character.class_ == "Ranger":
        character.DEX += 1
        character.WIS += 1
    elif character.class_ == "Rogue":
        character.DEX += 1
        character.CON += 1
    elif character.class_ == "Wizard":
        character.INT += 1
        character.CON += 1

elif character.race == "Human":
    character.STR += 1
    character.DEX += 1
    character.CON += 1
    character.INT += 1
    character.WIS += 1
    character.CHA += 1
elif character.race == "Half-Orc":
    character.STR += 2
    character.CON += 1
elif character.race == "Tiefling":
    character.CHA += 2
    character.INT += 1
elif character.race == "Elf":
    character.DEX += 2
    character.INT += 1
elif character.race == "Dragonborn":
    character.STR += 2
    character.CHA += 1
elif character.race == "Dwarf":
    character.CON += 2
elif character.race == "Gnome":
    character.INT += 2
elif character.race == "Halfling":
    character.DEX += 2

#AC calculation. AC or Armor Class is a number that determines how hard it is to hit a character.

#These modifiers help with calculating hit points and armor class.
dex_mod = math.floor((character.DEX - 10)/2)
wis_mod = math.floor((character.WIS - 10)/2)
con_mod = math.floor((character.CON - 10)/2)

if character.class_ == "Monk":
    #monks wear no armor, and their AC depends on their wisdom and dexterity
    character.AC = 10 + dex_mod + wis_mod
else:
    match character.armor:
        case "Padded":
            character.AC = 11 + dex_mod
        case "Leather":
            character.AC = 11 + dex_mod
        case "Studded Leather":
            character.AC = 12 + dex_mod
            #leather armors put your AC at 12 + dexterity modifier, but the modifier cannot be more than 2
        case "Hide":
            if dex_mod >= 2:
                character.AC = 14
            else:
                character.AC = 12 + dex_mod
        case "Scale Mail":
            if dex_mod >= 2:
                character.AC = 16
            else:
                character.AC = 14 + dex_mod
        case "Breastplate":
            if dex_mod >= 2:
                character.AC = 16
            else:
                character.AC = 14 + dex_mod
        case "Half Plate":
            if dex_mod >= 2:
                character.AC = 17
            else:
                character.AC = 15 + dex_mod
        #plate armors just sets your AC to a specific number without being dependant on dexterity
        case "Ring Mail":
            character.AC = 14
        case "Chain Mail":
            character.AC = 16
        case "Splint Plate":
            character.AC = 17
        case "no":
            character.AC = 10 + dex_mod


#Shield. If the class can hold a shield and the weapon we picked is one-handed, we flip a coin and give a shield.
#Look at how beautiful nested code looks

if character.class_=="Barbarian"\
or character.class_=="Cleric" \
or character.class_=="Druid" \
or character.class_=="Fighter" \
or character.class_=="Paladin" \
or character.class_=="Ranger":
        if character.weapon in one_handed_weapons:
            shield_or_not = randint(1,2)
            if shield_or_not == 1:
                character.shield = True
                character.AC += 2



'''HP rolling. Different classes get different dice that determine their hit points. Barbarians that are a specialist
martial class determines their hit points by throwing 12-sided dice, while mages who do massive damage safely from afar
must have fewer hit points so they are balanced, so they throw 6-sided dice. In every dice throw you add the constitution
modifier of the character, and you throw the dice once every new level you climb. Finally, dice results cannot be less
than or half of the maximum, so if I throw a 12 sided die and it lands on 2, I will add 7 on my HP'''

roll = 0

match character.class_:
    case "Barbarian":
        roll = randint(1, 12) + randint(1, 12) + randint(1, 12) + randint(1, 12)
        if roll <= 28:
            roll = 28
        character.HP = 12 + roll + 5 * con_mod
    case "Bard":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Cleric":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Druid":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Fighter":
        roll = randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)
        if roll <= 24:
            roll = 24
        character.HP = 10 + roll + 5 * con_mod
    case "Monk":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Paladin":
        roll = randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)
        if roll <= 24:
            roll = 24
        character.HP = 10 + roll + 5 * con_mod
    case "Ranger":
        roll = randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)
        if roll <= 24:
            roll = 24
        character.HP = 10 + roll + 5 * con_mod
    case "Rogue":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Warlock":
        roll = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        if roll <= 20:
            roll = 20
        character.HP = 8 + roll + 5 * con_mod
    case "Wizard":
        roll = randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)
        if roll <= 20:
            roll = 20
        character.HP = 6 + roll + 5 * con_mod
    case "Sorcerer":
        roll = randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)
        if roll <= 20:
            roll = 20
        character.HP = 6 + roll + 5 * con_mod



'''Ability Score Improvement for level 5. When a character reaches level 5 they get two additional points to distribute
however they see fit. The problem is that a stat cannot go higher than 20, so before we assign a point to a stat
we have to check if adding the point would surpass the 20 limit'''

if character.class_ == "Paladin" or character.class_ == "Barbarian" or character.class_ == "Fighter":
    ''' if the str is less than or equal to 18 we add both points in strength who is the most important stat.
        if the str is 19 we will put 1 point in str and 1 point in con, and if str is 20 we put both points
        in con. It is impossible for both con and str to be above 18 so we are good for now'''
    if character.STR <= 18:
        character.STR += 2
    elif character.STR == 19:
        character.STR += 1
        character.CON += 1
    elif character.STR == 20:
        character.CON += 2
elif character.class_ == "Monk" or character.class_ == "Ranger" or character.class_ == "Rogue":
    if character.DEX <= 18:
        character.DEX += 2
    elif character.DEX == 19:
        character.DEX += 1
        character.CON += 1
    elif character.DEX == 20:
        character.CON += 2
elif character.class_ == "Bard" or character.class_ == "Sorcerer" or character.class_ == "Warlock":
    '''Now because of the half-elf class that has +2 to CHA and then +1 to two more stats, it is possible
    that the CHA is equal to 20 and the second most important stat to also be 20. so we need to check
    both the charisma and the constitution before we assign stats'''
    if character.CHA <= 18:
        character.CHA += 2
    elif character.CHA == 19:
        character.CHA += 1
        character.CON += 1
    elif character.CHA == 20 and character.CON <= 18:
        character.CON += 2
    elif character.CHA == 20 and character.CON == 19:
        character.CON += 1
        character.DEX += 1
    elif character.CHA == 20 and character.CON == 20:
        character.DEX += 2
elif character.class_ == "Cleric" or character.class_ == "Druid":
    if character.WIS <= 18:
        character.WIS += 2
    elif character.WIS == 19:
        character.WIS += 1
        character.CON += 1
    elif character.WIS == 20:
        character.CON += 2
elif character.class_ == "Wizard":
    if character.INT <= 18:
        character.INT += 2
    elif character.INT == 19:
        character.INT += 1
        character.CON += 1
    elif character.INT == 20:
        character.CON += 2

# Result Printing

print()
if character.shield:
    print("Your character is a level 5 " + str(character.gender) + " " + str(character.race) + " " + str(character.class_) +
          ", wielding a " + str(character.weapon) + " and a shield, and wearing " + str(character.armor) + " armor.")
else:
    print("Your character is a level 5 " + str(character.gender) + " " + str(character.race) + " " + str(character.class_) +
          ", wielding a " + str(character.weapon) + ", and wearing " + str(character.armor) + " armor.")

print("Languages they speak: " + str(character.language))
print()
print ("STR: " + str(character.STR))
print ("DEX: " + str(character.DEX))
print ("CON: " + str(character.CON))
print ("INT: " + str(character.INT))
print ("WIS: " + str(character.WIS))
print ("CHA: " + str(character.CHA))
print()
print("AC = " + str(character.AC))
print()
print("HP = " + str(character.HP))


