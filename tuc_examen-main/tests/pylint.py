class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1


class Pikachu(Pokemon):
    def __init__(self, name, level, type):
        super().__init__(name, level)
        self.type = type

    def electric_attack(self):
        return f"{self.name} used Thunderbolt!"


class Bulbasaur(Pokemon):
    def __init__(self, name, level, type):
        super().__init__(name, level)
        self.type = type

    def grass_attack(self):
        return f"{self.name} used Vine Whip!"


# Exemple d'utilisation
pikachu = Pikachu("Pikachu", 5, "Electric")
bulbasaur = Bulbasaur("Bulbasaur", 5, "Grass")

print(pikachu.electric_attack())
print(bulbasaur.grass_attack())
