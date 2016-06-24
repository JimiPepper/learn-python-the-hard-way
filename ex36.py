GAME_FOLDER = 'game_folder\\'

def loadHeroes():
    heroes = () # returned tuple

    with open("%s%s" % (GAME_FOLDER, 'heroes.txt'), 'r') as heroes_file:
        for line in heroes_file:
            info = line.split(';')
            hero = ([
                info[0], # Name
                info[1], # Role
                int(info[2]), # HP
                int(info[3]), # Attack
                int(info[4]) # Defense
            ], )

            heroes = heroes + (hero,)

    return heroes

def game():
    loadHeroes()

game()
