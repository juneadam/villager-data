"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    
    vill_list = []
    animal = []
    
    for villagers in open(filename):
        villagers = villagers.rstrip()
        vill_list.append(villagers.split('|'))

    for i,line in enumerate(vill_list):
        animal.append(vill_list[i][1])
        
    species = set(animal)
    return species

#all_species('villagers.csv')


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    vill_list = []
    
    for villager in open(filename):
        villager = villager.rstrip()
        vill_list.append(villager.split('|'))

    for i,ind in enumerate(vill_list):
        if search_string == "All":
            villagers.append(vill_list[i][0])
        elif vill_list[i][1] == search_string:
            villagers.append(vill_list[i][0])

    print(sorted(villagers))
    
    return sorted(villagers)

#get_villagers_by_species('villagers.csv')

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    vill_list = []
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    villagers_sorted_by_hobby = []
    
    for villager in open(filename):
        villager = villager.rstrip()
        vill_list.append(villager.split('|'))

    for i,ind in enumerate(vill_list):
        if vill_list[i][3] == "Fitness":
            fitness.append(vill_list[i][0])
        if vill_list[i][3] == "Nature":
            nature.append(vill_list[i][0])
        if vill_list[i][3] == "Education":
            education.append(vill_list[i][0])
        if vill_list[i][3] == "Music":
            music.append(vill_list[i][0])
        if vill_list[i][3] == "Fashion":
            fashion.append(vill_list[i][0])
        if vill_list[i][3] == "Play":
            play.append(vill_list[i][0])
    
    villagers_sorted_by_hobby.append(sorted(fitness))
    villagers_sorted_by_hobby.append(sorted(nature))
    villagers_sorted_by_hobby.append(sorted(education))
    villagers_sorted_by_hobby.append(sorted(music))
    villagers_sorted_by_hobby.append(sorted(fashion))
    villagers_sorted_by_hobby.append(sorted(play))

    return villagers_sorted_by_hobby

print(all_names_by_hobby('villagers.csv'))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
