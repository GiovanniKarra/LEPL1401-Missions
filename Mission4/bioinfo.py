def is_adn(s):
    if s == "":
        return False

    for i in s:
        if i.lower() == "a" or i.lower() == "t" or i.lower() == "c" or i.lower() == "g":
            continue
        else:
            return False

    return True


def positions(s, p):
    s = s.lower()
    p = p.lower()
    length = len(s)
    pos_list = []
    for i in range(length):
        if s[i] == p[0]:
            if i + len(p) <= length and "".join([s[i + j] for j in range(len(p))]) == p:
                pos_list.append(i)

    return pos_list


def distance_h(s1, s2):
    if len(s1) != len(s2):
        return None

    distance = 0
    for i in range(len(s1)):
        if s1[i].lower() != s2[i].lower():
            distance += 1

    return distance


def distances_matrice(l):
    matrice = []
    for i in l:
        ligne = []
        for j in l:
            ligne.append(distance_h(i, j))

        matrice.append(ligne)

    return matrice