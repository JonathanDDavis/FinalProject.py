#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     10/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Player:
    def __init__(self, name, stats, alive):
        self.name = ""
        self.stats = stats
        self.alive = True

class rogue(Player):
    def __init__(self, name, stats, alive, skills, armor, weapons, spells):
        super(). __init__(id, name, stats, alive)
        self.rogueSkills = skills
        self.rogueArmor = armor
        self.rogueWeapons = weapons
        self.rogueSpells = spells

class ranger(Player):
    def __init__(self, name, stats, alive, skills, armor, weapons, spells):
        super(). __init__(id, name, stats, alive)
        self.rangerSkills = skills
        self.rangerArmor = armor
        self.rangerWeapons = weapons
        self.rangerSpells = spells

class cleric(Player):
    def __init__(self, name, stats, alive, skills, armor, weapons, spells):
        super(). __init__(id, name, stats, alive)
        self.clericSkills = skills
        self.clericArmor = armor
        self.clericWeapons = weapons
        self.clericSpells = spells
class warrior(Player):
    def __init__(self, name, stats, alive, skills, armor, weapons):
        super(). __init__(id, name, stats, alive)
        self.warriorArmor = armor
        self.warriorWeapons = weapons
        self.warriorSkills = skills

class mage(Player):
    def __init__(self, name, stats, alive, skills, armor, weapons, spells):
        super(). __init__(id, name, stats, alive)
        self.mageArmor = armor
        self.mageWeapons = weapons
        self.mageSkills = skills
        self.mageSpells = spells

class human(rogue):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.humanStatsBoost = statsBoost
        self.humanLanguage = language

class human(ranger):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.humanStatsBoost = statsBoost
        self.humanLanguage = language

class human(cleric):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.humanStatsBoost = statsBoost
        self.humanLanguage = language

class human(warrior):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.humanStatsBoost = statsBoost
        self.humanLanguage = language

class human(mage):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.humanStatsBoost = statsBoost
        self.humanLanguage = language

class dwarf(rogue):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.dwarfStatsBoost = statsBoost
        self.dwarfLanguage = language


class dwarf(ranger):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.dwarfStatsBoost = statsBoost
        self.dwarfLanguage = language

class dwarf(cleric):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.dwarfStatsBoost = statsBoost
        self.dwarfLanguage = language

class dwarf(warrior):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.dwarfStatsBoost = statsBoost
        self.dwarfLanguage = language

class dwarf(mage):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.dwarfStatsBoost = statsBoost
        self.dwarfLanguage = language

class elf(rogue):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.eldStatsBoost = statsBoost
        self.elfLanguage = language

class elf(ranger):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.eldStatsBoost = statsBoost
        self.elfLanguage = language

class elf(cleric):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.eldStatsBoost = statsBoost
        self.elfLanguage = language

class elf(warrior):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.eldStatsBoost = statsBoost
        self.elfLanguage = language

class elf(mage):
    def _init_(self, name, stats, alive, skills, armor, weapons, spells, statsBoost, language):
        super(). __init__(id, name, stats, alive, skills, armor, weapons, spells)
        self.eldStatsBoost = statsBoost
        self.elfLanguage = language



# Add skills and spells to all classes