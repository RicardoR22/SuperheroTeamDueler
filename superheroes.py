import random

class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.abilities = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        ability_list = self.abilities
        ability_list.append(ability)

    def add_armor(self, armor):
        armor_list = self.armors
        armor_list.append(armor)

    def attack(self):
        attack_total = 0
        if not self.abilities:
            print("No abilities")
        else:
            for ability in self.abilities:
                attack_damage = ability.attack()
                attack_total += attack_damage
        return attack_total

    def defend(self):
        total_defense = 0
        if not self.armors:
            print("No armor")
        else:
            for armor in self.armors:
                armor_defense = armor.defend()
                total_defense += armor_defense

        if self.health <= 0:
            total_defense = 0

        return total_defense

    def take_damage(self, damage_amt):
        self.health -= damage_amt

        if self.health <= 0:
            self.deaths += 1
            return 1

        return 0

    def add_kill(self, num_kills):
        self.kills += num_kills




class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = int(attack_strength)

    def attack(self):
        min_attack_strength = self.attack_strength // 2
        attack_value = random.randint(min_attack_strength, self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        weapon_attack = random.randint(0, self.attack_strength)
        return weapon_attack

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        if hero not in self.heroes:
            self.heroes.append(hero)
            #print("{} added to {}".format(hero.name, self.name))
        #else:
            #print("{} is already in {}".format(hero.name, self.name))

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 1
                #print("{} removed from {}".format(hero.name, self.name))
            #else:
                #print("{} is not in {}".format(hero.name, self.name))
        return 0

    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                #print("{} found in {}".format(hero.name, self.name))
                return hero
            #else:
                #print("{} is not in {}".format(hero.name, self.name))
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        attack_total = 0
        for hero in self.heroes:
            attack = hero.attack()
            attack_total += attack

        deaths = other_team.defend(attack_total)

        for hero in self.heroes:
            hero.add_kill(deaths)
        return deaths

    def defend(self, damage_amt):
        total_defense = 0
        for hero in self.heroes:
            defense = hero.defend()
            total_defense += defense

        excess_damage = damage_amt - total_defense
        return self.deal_damage(excess_damage)

    def deal_damage(self, damage):
        damage = damage / len(self.heroes)
        deaths = 0

        for hero in self.heroes:
             if hero.take_damage(damage) == 1:
                 deaths += 1
        return deaths

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        for hero in self.heroes:
            print("{}'s KD: {}/{}".format(hero.name, hero.kills, hero.deaths))

    # def update_kills(self):



class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = int(defense)

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        # Ask User for Team Name
        team_name = input("Choose a team name: ")
        # Create Team
        self.team_one = Team(team_name)
        print("Successfully created {}".format(team_name))
        team_one_heroes = 0
        while team_one_heroes < 1:
            # User Input for Hero Name
            hero_name = input("Add a Hero to your team: ")
            # Make Hero with User Input
            hero = Hero(hero_name)
            self.team_one.add_hero(hero)
            team_one_heroes += 1

        ability_name = input("Give your hero an ability! Enter Ability Name: ")
        ability_strength = input("Give your Ability a strength value! Enter Strength Value: ")
        hero_ability = Ability(ability_name, ability_strength)
        hero.add_ability(hero_ability)
        armor_name = input("Give your hero armor! Enter Armor Name: ")
        armor_strength = input("Give your armor defense value! Enter Defense Value: ")
        hero_armor = Armor(armor_name, armor_strength)
        hero.add_armor(hero_armor)



    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        # Ask User for Team Name
        team_two_name = input("Choose a team name: ")
        # Create Team
        self.team_two = Team(team_two_name)
        print("Successfully created {}".format(team_two_name))
        team_two_heroes = 0
        while team_two_heroes < 1:
            # User Input for Hero Name
            hero_two_name = input("Add a Hero to your second team: ")
            # Make Hero with User Input
            hero_two = Hero(hero_two_name)
            self.team_two.add_hero(hero_two)
            team_two_heroes += 1

        ability_name = input("Give your hero an ability! Enter Ability Name: ")
        ability_strength = input("Give your Ability a strength value! Enter Strength Value: ")
        hero_ability = Ability(ability_name, ability_strength)
        hero_two.add_ability(hero_ability)
        armor_name = input("Give your hero armor! Enter Armor Name: ")
        armor_strength = input("Give your armor defense value! Enter Defense Value: ")
        hero_armor = Armor(armor_name, armor_strength)
        hero_two.add_armor(hero_armor)

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        team_one_deaths = 0
        team_two_deaths = 0
        team_two_size = len(self.team_two.heroes)
        team_one_size = len(self.team_one.heroes)

        while team_two_deaths < team_two_size or team_one_deaths < team_one_size:
            team_one_deaths = self.team_one.attack(self.team_two)
            team_two_deaths = self.team_two.attack(self.team_one)


    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        print("Stats for Team One: ")
        self.team_one.stats()
        print("Stats for Team Two: ")
        self.team_two.stats()



if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

# if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
# #     hero2 = Hero("Batman")
# #     hero3 = Hero("Superman")
#     team = Team("Justice League")
#     team.add_hero(hero)
#     armor = Armor("leather", 100)
#     print("Armor defense amt: " + str(armor.defend()))
# #     team.add_hero(hero2)
# #     team.add_hero(hero3)
# #     # team.find_hero(hero)
#     team.remove_hero("Wonder Woman")
#     print(len(team.heroes))
# #     team.find_hero(hero)
# #     team.view_all_heroes()
# #     print(hero.attack())
# #     ability = Ability("Divine Speed", 300)
# #     #ability2 = Weapon("Sword", 150)
# #     #print("weapon damage: {}".format(ability2.attack()) )
# #     hero.add_ability(ability)
# #     print(hero.attack())
# #     new_ability = Ability("Super Human Strength", 800)
# #     hero.add_ability(new_ability)
# #     print(hero.attack())
