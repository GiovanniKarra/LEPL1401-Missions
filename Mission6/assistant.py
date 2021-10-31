from sys import exit as close_program
import os


current_file = None  # le fichier avec lequel on travail
lines = []
text = ""
dictionary_mode = False  # bool pour vérifier si le fichier est en mode dictionnaire ou pas


def file(name):
    """
        @pre :
            name : string avec le nom du fichier qu'on cherche

        @post :
            assigne à "current_file" le fichier au nom "name"
    """

    try:
        global current_file
        global lines
        global text

        current_file = open(os.path.dirname(os.path.realpath(__file__)) + "\\" + name, "r")
        lines = current_file.readlines()
        text = "".join(lines)

        return f"Le fichier {name} a été sélectionné"

    except FileNotFoundError:
        return f"Aucun fichier {name} n'a été trouvé"


def info():
    """
        @post :
            return le nombre de lignes et de caractères dans current_file
    """

    if current_file is not None:
        global lines
        global text

        line_num = len(lines)
        characters_num = len(text)

        return f"Nombre de lignes : {line_num}\nNombre de caractères : {characters_num}"

    else:
        return "Aucun fichier n'est sélectionné"


def dictionary():
    """
        utilise current_file comme dictionnaire (liste de mots triés par ordre alphabétique)
    """

    global current_file
    global dictionary_mode

    if current_file is not None:
        dictionary_mode = not dictionary_mode
        return "Le mode dictionnaire a été " + "dés" * int(not dictionary_mode) + "activé !"

    else:
        return "Aucun fichier n'est sélectionné"


def search(word):
    """
        @pre :
            word : un mot qu'on cherche dans le dictionnaire (si le fichier est un dictionnaire)

        @post :
            return un bool selon si word est dans le dictionnaire ou pas
    """
    global dictionary_mode
    global lines

    if current_file is None:
        return "Aucun fichier n'est sélectionné"

    if not dictionary_mode:
        return "Impossible de faire une recherche, le fichier n'est pas en mode dictionnaire"

    sorted_lines = sorted(lines)

    first = 0
    last = len(sorted_lines) - 1

    while first <= last:

        middle = (first + last) // 2
        middle_word = "".join(x for x in sorted_lines[middle] if x.isalpha())

        if middle_word == word:
            return f"'{word}' est bien présent dans le dictionnaire !"

        elif middle_word < word:
            first = middle + 1

        else:
            last = middle - 1

    return f"'{word}' n'est pas présent dans le dictionnaire"


def sum(*numbers):
    """
        @pre :
            *numbers : plusieurs nombres qu'on voudrait additionner

        @post :
            return la somme de tout les nombres dans *numbers
    """

    sum = 0
    for num in numbers:
        sum += num

    return sum


def avg(*numbers):
    """
        @pre :
            *numbers : les nombres dont on voudrait connaitre la moyenne

        @post :
            return la moyenne de *numbers
    """

    return sum(*numbers) / len(numbers)


def help():
    """
        @post :
            return la liste de commandes
    """
    return "file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment\n"\
        "info: montre le nombre de lignes et de caractères du fichier\n"\
        "dictionary: utilise le fichier comme dictionnaire à partir de maintenant\n"\
        "search <word>: détermine si le mot est dans le dictionnaire\n"\
        "sum <number1>,...,<numbern>: calcule la somme des nombres spécifiés\n"\
        "avg <number1>,...,<numbern>: calcule la moyenne des nombres spécifiés\n"\
        "help: montre des instructions à l'utilisateur\n"\
        "exit: arrête l'outil"


def exit():
    """
        quitte l'application
    """

    close_program()


def get_command():
    cmd_dict = {"file": file, "info": info, "dictionary": dictionary, "search": search, "sum": sum,
                "avg": avg, "help": help, "exit": exit}

    user_input = input(">>> ").split(" ")
    cmd = user_input[0]

    if cmd == "sum" or cmd == "avg":
        try:
            arg = (int(i) for i in "".join(user_input[1:]).strip(" ").split(","))
            return cmd_dict[cmd](*arg)

        except ValueError:
            return "Erreur dans l'argument. L'argument doit contenir plusieurs nombres séparés par des virgules"

    elif cmd == "search" or cmd == "file":
        arg = " ".join(user_input[1:])
        return cmd_dict[cmd](arg)

    elif cmd == "help" or cmd == "exit" or cmd == "info" or cmd == "dictionary":
        return cmd_dict[cmd]()

    else:
        return "Commande inconnue"


if __name__ == "__main__":
    print(f"Bienvenu, {os.getlogin()} !")
    while True:
        print(get_command())
