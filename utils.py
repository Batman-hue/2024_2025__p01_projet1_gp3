from data import*     # Importe les variables stockées dans le fichier data.



def ask_for_the_target_base ():     # Demande dans quelle base le nombre devra être converti.
    target_base = input("Base dans laquelle le nombre doit être converti(en chiffre):  ")
    while not (is_a_valid_base (target_base)) == True:     # Relance la demande si la réponse fournie n'est pas supportée par le programme.
        target_base = input ("Base incorrecte, veuillez réessayer:  ")
    return target_base


def ask_for_the_init_number (init_base):     # Demande quel est le nombre à convertir.
    init_number = input ("Nombre choisi:  ")
    while not (is_a_valid_number (init_number,init_base)) == True:     # Relance la demande si la réponse fournie n'est pas supportée par le programme.
        init_number = input ("Nombre incorrect, veuillez réessayer:  ")
    return init_number


def ask_for_the_init_base ():     # Demande dans quelle base le nombre fourni sera.
    init_base = input("Base d'origine du nombre (en chiffre):  ")
    while not (is_a_valid_base (init_base)) == True:     # Relance la demande si la réponse fournie n'est pas supportée par le programme.
        init_base = input ("Base incorrecte, veuillez réessayer:  ")
    return init_base



def is_a_valid_base(base):     # Vérifie si la base donnée est supportée par le programme.
    return base in valid_base


def is_a_valid_number (number,base):     # Vérifie si le nombre est valide dans la base donnée.
    number = f"{number}"
    if base == "2":
        for i in number:
            if not i in bin_number_valid_chars:
                return False
        return True
    if base == "10":
        for i in number:
            if not i in dec_number_valid_chars:
                return False
        return True
    if base == "16":
        for i in number:
            if not i in hex_number_valid_chars:
                return False
        return True



def dec_to_bin (init_number):     # Permet de convertir un nombre de base 10 en base 2.
    power = 0
    target_number = ""
    init_number = float(init_number)
    while init_number >= 2 ** power:
            power = power + 1
    while power > -1 :
        if init_number >= 2 ** power :
            init_number = init_number - 2 ** power
            target_number = target_number + "1"
        else:
            target_number = target_number + "0"
        power = power - 1
    return target_number


def bin_to_dec (init_number):     # Permet de convertir un nombre de base 2 en base 10.
    target_number = 0
    init_number = f"{init_number}"
    power = len(init_number) - 1
    for i in init_number:
            target_number = target_number + ((2 ** power) * (bin_number_valid_chars.index(i)))
            power = power - 1
    return target_number


def dec_to_hex (init_number):     # Permet de convertir un nombre de base 10 en base 16.
    power = 0
    target_number = ""
    multiplicator = 0
    init_number = float(init_number)
    while True :
        if init_number >= 16 ** power :
            power = power + 1
        else:
            power = power - 1 
            break 
        if init_number == 16 ** power :
            break
    while power > -1 :
        if init_number == multiplicator * 16 ** power:
            target_number = target_number + f"{hex_number_valid_chars[multiplicator]}"
            init_number = init_number - multiplicator * 16 ** power
            power = power - 1
            multiplicator = 0
        if init_number < multiplicator * 16 ** power:
            multiplicator = multiplicator - 1
            target_number = target_number + f"{hex_number_valid_chars[multiplicator]}"
            init_number = init_number - multiplicator * 16 ** power
            power = power - 1
            multiplicator = 0
        else:
            multiplicator = multiplicator + 1
        if multiplicator == 16:
            multiplicator = 0
            power = power - 1
    return target_number


def hex_to_dec(init_number):     # Permet de convertir un nombre de base 16 en base 10.
    target_number = 0
    init_number = f"{init_number}"
    power = len(init_number) - 1
    for i in init_number:
        if hex_number_valid_chars.index(i) > 15:
            target_number = target_number + ((16 ** power) * (hex_number_valid_chars.index(i) - 6))
            power = power - 1
        else:
            target_number = target_number + ((16 ** power) * hex_number_valid_chars.index(i))
            power = power - 1
    return target_number