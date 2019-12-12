#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

    
"""
Creating the races and classes from which we will be using to 
create our random characters. There have been many additions of 
races/classes within the years to D&D but for the purposes of 
this we will stick with the basic OG choices
"""
RACES = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Half-Elf', 
         'Half-Orc', 'Human', 'Tiefling']
CLASSES = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 
        'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

"""
Putting this outside of our functions first so we can make more 
customizations later on with the different race bonuses, hit die, etc.
"""
CHOOSE_RACE = random.choice(RACES)
CHOOSE_CLASS = random.choice(CLASSES)

""" 
The way ability scores in D&D are determined is you roll four 6-sided dice, 
add up the highest three dice and that is one of your ability scores. That
means the lowest possible score you can get is 3 and the highest is 18.
Ideally, depending on what class you are playing you would place your higher 
rolls in certain ability scores e.g. barbarians prioritize strength while 
wizards prioritize intelligence, but to avoid hardcoding 12 classes to make
optimum characters, we'll just keep them as is. Besides, D&D is an interactive
roleplaying game, and roleplaying a really intelligent barbarian or a bard
who can't really sing can make for some funny interactions and gameplay.
"""
STRENGTH = str(random.randint(3,18))
DEXTERITY = str(random.randint(3,18))
WISDOM = str(random.randint(3,18))
INTELLIGENCE = str(random.randint(3,18))
CONSTITUTION = str(random.randint(3,18))
CHARISMA = str(random.randint(3,18))

"""
Ability scores determine modifiers for when you make rolls in the game so 
higher ability scores means a higher modifier = higher chances at better 
rolls using a dictionary to determine these modifiers
"""
MODIFIERS = {'1' : '-5', '2' : '-4', '3' : '-4', '4' : '-3', '5' : '-3', '6' : 
             '-2', '7' : '-2', '8' : '-1', '9' : '-1', '10' : '0', '11' : '0', 
             '12' : '+1', '13' : '+1', '14' : '+2', '15' : '+2', '16' : '+3', 
             '17' : '+3', '18' : '+4', '19' : '+4', '20' : '+5', '21' : '+5', 
             '22' : '+6', '23' : '+6', '24' : '+7', '25' : '+7', '26' : '+8', 
             '27' : '+8', '28' : '+9', '29' : '+9', '30' : '+10'}


def name(): 
    """
    Creating a name for the character, still want to give player some 
    customization so this should not be random
    """
    print('What would you like your character name to be?')
    create_name = input()
    
def alignment(): 
    """
    Alignment in D&D is the moral compass of the character and determines what 
    kind of actions they would make. 
    """
    #a list of the alignments in D&D
    alignment_list = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 
                    'Lawful Neutral', 'Neutral', 'Chaotic Neutral', 
                    'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
    print(random.choice(alignment_list))

def character_race(): 
    """
    Print out character race
    """
    print(CHOOSE_RACE)
          
def character_class():
    """
    Function to print out our randomly chosen class
    """
    
    print(CHOOSE_CLASS)
    
def hit_points(): 
    """
    Need to create the amount of hit points the character has which is usually
    determined by the class and your constitution modifier. Barbarians, for
    example, roll a 12 sided die whereas a warlock rolls an 8 sided die for hit
    points.Now in my games, I have a custom rule where your health at level 1
    is the max number of your hit die that you roll plus 10 because no one 
    likes to play a character with 5 hit points and can be one hit killed by 
    an enemy. 
    """
    health = 0
    if CHOOSE_CLASS == 'Barbarian': 
        health = str(12 + 10)
        print('Hit Points:' + health)
        print()
    elif (CHOOSE_CLASS == 'Fighter' or CHOOSE_CLASS == 'Paladin' or 
         CHOOSE_CLASS == 'Ranger'): 
        health = str(10 + 10)
        print('Hit Points:' + health)
        print()
    elif (CHOOSE_CLASS == 'Bard' or CHOOSE_CLASS == 'Cleric' or 
            CHOOSE_CLASS == 'Druid' or CHOOSE_CLASS == 'Monk' or 
            CHOOSE_CLASS == 'Rogue' or CHOOSE_CLASS == 'Warlock'):
        health = str(8 + 10)
        print('Hit Points:' + health)
        print()
    elif (CHOOSE_CLASS == 'Sorcerer' or CHOOSE_CLASS == 'Wizard'):
        health = str(6 + 10)  
        print('Hit Points:' + health)
        print()
        
def ability_scores(): 
    """
    Creating our bonuses depending on which race that was randomly chosen for 
    us. Since this is just a basic program that I would only use for new 
    players or occasions where I need a super quick character, we're just going
    focus on the modifiers for strength and dexterity since those are the most 
    common abilites that show up for ability checks
    """
    
    print("ABILITY SCORES: ")
    if CHOOSE_RACE == 'Dragonborn': 
        strength_bonus = str(2)
        #creating final ability score with bonus added
        true_strength = str(int(STRENGTH) + int(strength_bonus))
        true_dexterity = DEXTERITY
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        true_constitution = CONSTITUTION
        charisma_bonus = str(1)
        true_charisma = str(int(CHARISMA) + int(charisma_bonus))
        #races have special innate abilities
        racial_traits = ['Draconic Ancestry', 'Breath Weapon', 
                             'Damage Resistance']
    elif CHOOSE_RACE == 'Dwarf': 
        strength_bonus = str(2)
        true_strength = str(int(STRENGTH) + int(strength_bonus))
        true_dexterity = DEXTERITY
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        constitution_bonus = str(2)
        true_constitution = str(int(CONSTITUTION) + int(constitution_bonus))
        true_charisma = CHARISMA
        racial_traits = ['Darkvision', 'Dwarven Resilience',
                        'Dwarven Combat Training', 'Stonecunning']
    elif CHOOSE_RACE == 'Elf': 
        true_strength = STRENGTH
        dexterity_bonus = str(2)
        true_dexterity = str(int(DEXTERITY) + int(dexterity_bonus))
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        true_constitution = CONSTITUTION
        true_charisma = CHARISMA
        racial_traits = ['Darkvision', 'Keen Senses', 'Fey Ancestry', 
                        'Trance']
    elif CHOOSE_RACE == 'Gnome': 
        true_strength = STRENGTH
        true_dexterity = DEXTERITY
        true_wisdom = WISDOM
        intelligence_bonus = str(2)
        true_intelligence = str(int(INTELLIGENCE) + int(intelligence_bonus))
        true_constitution = CONSTITUTION
        true_charisma = CHARISMA
        racial_traits = ['Darkvision', 'Gnome Cunning']
    elif CHOOSE_RACE == 'Half-Elf':
        strength_bonus = str(1)
        true_strength = str(int(STRENGTH) + int(strength_bonus))
        dexterity_bonus = str(1)
        true_dexterity = str(int(DEXTERITY) + int(dexterity_bonus))
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        true_constitution = CONSTITUTION
        charisma_bonus = str(2)
        true_charisma = str(int(CHARISMA) + int(charisma_bonus))    
        racial_traits = ['Darkvision', 'Fey Ancestry', 'Skill Versatility']
    elif CHOOSE_RACE == 'Halfling': 
        true_strength = STRENGTH
        dexterity_bonus = str(2)
        true_dexterity = str(int(DEXTERITY) + int(dexterity_bonus))
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        true_constitution = CONSTITUTION
        true_charisma = CHARISMA
        racial_traits = ['Lucky', 'Brave', 'Halfling Nimbleness']
    elif CHOOSE_RACE == 'Half-Orc': 
        strength_bonus = str(2)
        true_strength = str(int(STRENGTH) + int(strength_bonus))
        true_dexterity = DEXTERITY
        true_wisdom = WISDOM
        true_intelligence = INTELLIGENCE
        constitution_bonus = str(1)
        true_constitution = str(int(CONSTITUTION) + int(constitution_bonus))
        true_charisma = CHARISMA
        racial_traits = ['Darkvision', 'Menacing', 
                        'Relentless Endurance', 'Savage Attacks']
    elif CHOOSE_RACE == 'Human': 
        strength_bonus = str(1)
        true_strength = str(int(STRENGTH) + int(strength_bonus))
        dexterity_bonus = str(1)
        true_dexterity = str(int(DEXTERITY) + int(dexterity_bonus))
        wisdom_bonus = str(1)
        true_wisdom = str(int(WISDOM) + int(wisdom_bonus))
        intelligence_bonus = str(1)
        true_intelligence = str(int(INTELLIGENCE) + int(intelligence_bonus))
        constitution_bonus = str(1)
        true_constitution = str(int(CONSTITUTION) + int(constitution_bonus))
        charisma_bonus = str(1)
        true_charisma = str(int(CHARISMA) + int(charisma_bonus))
        racial_traits = ['Extra Language']
    elif CHOOSE_RACE == 'Tiefling':
        true_strength = STRENGTH
        true_dexterity = DEXTERITY
        true_wisdom = WISDOM
        intelligence_bonus = str(1)
        true_intelligence = str(int(INTELLIGENCE) + int(intelligence_bonus))
        true_constitution = CONSTITUTION
        charisma_bonus = str(2)
        true_charisma = str(int(CHARISMA) + int(charisma_bonus))
        racial_traits = ['Darkvision', 'Hellish Resistance', 
                              'Infernal Legacy'] 
    
    for key in MODIFIERS: 
        if key == true_strength: 
            #format of printout: Strength: 14 (modifier)
            print('Strength: {} ({})'.format(true_strength, 
                                             MODIFIERS[true_strength]))
        else: 
            pass
    
    for key in MODIFIERS: 
        if key == true_dexterity: 
            print('Dexterity: {} ({})'.format(true_dexterity, 
                                                MODIFIERS[true_dexterity]))
        else: 
            pass
    
    for key in MODIFIERS: 
        if key == WISDOM: 
            print('Wisdom: {} ({})'.format(true_wisdom, 
                                                MODIFIERS[true_wisdom]))
        else: 
            pass
    
    for key in MODIFIERS: 
        if key == true_intelligence: 
            print('Intelligence: {} ({})'.format(true_intelligence, 
                                                MODIFIERS[true_intelligence]))
        else: 
            pass
            
    for key in MODIFIERS: 
        if key == true_constitution: 
            print('Constitution: {} ({})'.format(true_constitution, 
                                             MODIFIERS[true_constitution]))
        else: 
            pass
        
    for key in MODIFIERS: 
        if key == true_charisma: 
            print('Charisma: {} ({})'.format(true_charisma, 
                                             MODIFIERS[true_charisma]))
        else: 
            pass
    print()
    print('Racial Traits:')
    print(racial_traits)
    
def main():
    name()
    alignment()
    character_race()
    character_class()
    hit_points()
    ability_scores()

