"""Module pour la lecture de données dans un fichier CSV"""
#### Imports et définition des variables globales
import csv


FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding="utf8") as f:
        # lire le contenu du fichier et le retourner sous forme de liste de listes
        l = []
        with open(filename, mode='r', encoding="utf8") as f:
            r=csv.reader(f, delimiter=';')
            for i in r:
                l.append([int(x) for x in i])
    return l

def get_list_k(data, k):
    """retourne la liste d'index k dans data"""
    l = data[k]
    return l

def get_first(l):
    """retourne le premier élément de la liste l"""
    return l[0]

def get_last(l):
    """retourne le dernier élément de la liste l"""
    return l[-1]

def get_max(l):
    """retourne le maximum de la liste l"""
    return max(l)

def get_min(l):
    """retourne le minimum de la liste l"""
    return min(l)

def get_sum(l):
    """retourne la somme des éléments de la liste l"""
    return sum(l)


#### Fonction principale


def main():
    """programme principal qui a pour but de tester les fonctions secondaires"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
