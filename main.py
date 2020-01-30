#https://codereview.stackexchange.com/questions/100852/pok%C3%A9mon-style-battle-game

import random

moves = {"lick": range(18, 26),
         "lightning attack": range(10, 36),
         "heal": range(10, 20)}


class Character:
    """ Define our general Character which we base our player and enemy off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Character):
    """ The player, they start with 100 health and have the choice of three moves """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat move would you like to make? (lick , lightning attack, or Heal)"))

            if choice == "heal":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == "lick" or choice == "lightning attack":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Enemy(Character):
    """ The enemy, also starts with 100 health and chooses moves at random """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            moves_1 = ["lick", "thundershock", "heal", "heal", "heal", "heal", "heal"]
            cpu_choice = random.choice(moves_1)
        else:
            cpu_choice = random.choice(list(moves))
        if cpu_choice == "lick" or cpu_choice == "thundershock":
            damage = int(random.choice(moves[cpu_choice]))
            other.health -= damage
            print("\nThe pokimane attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
        if cpu_choice == "heal":
            self.health += int(random.choice(moves[cpu_choice]))
            print("\nThe pokimane uses heal and its health is now {0.health}.".format(self))


def battle(player, enemy):
    print("An enemy pokimane enters...")
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print("\nThe health of the pokimane is now {0.health}.".format(enemy))
        enemy.attack(player)
        if player.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(player))
    if player.health > 0:
        print("You defeated the other pokimane!!!!!!")
    if enemy.health > 0:
        print("You were defeated by the CPU!!!!!")

if __name__ == '__main__':
    battle(Player(), Enemy())