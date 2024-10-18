from data import*

def ask_for_the_target_base ():
    target_base = input("Base dans laquelle le nombre doit être converti(en chiffre):  ")
    while not (is_a_valid_base (target_base)) == True:
        target_base = input ("Base incorrecte, veuillez réessayer:  ")
    return target_base


def ask_for_the_init_number (init_base):
    init_number = input ("Nombre choisi:  ")
    while not (is_a_valid_number (init_number,init_base)) == True:
        init_number = input ("Nombre incorrect, veuillez réessayer:  ")
    return init_number

def is_a_valid_number (number,base):
    flm = 0
    number = f"{number}"
    if base == "2":
        for i in number:
            if i in bin_number_valid_chars:
                flm = flm + 1
        if flm == len(number):
            return True
        else:
            return False
    if base == "10":
        for i in number:
            if i in dec_number_valid_chars:
                flm = flm + 1
        if flm == len(number):
            return True
        else:
            return False
    if base == "16":
        for i in number:
            if i in hex_number_valid_chars:
                flm = flm + 1
        if flm == len(number):
            return True
        else:
            return False
        
def ask_for_the_init_base ():
    init_base = input("Base d'origine du nombre (en chiffre):  ")
    while not (is_a_valid_base (init_base)) == True:
        init_base = input ("Base incorrecte, veuillez réessayer:  ")
    return init_base


def is_a_valid_base(base):
    if base == "2" or base == "10" or base == "16":
        return True
    else:
        return False

def dec_to_bin (init_number):
    power = 0 
    target_number = ""
    init_number = float(init_number)
    while True :
        if init_number >= 2 ** power :
            power = power + 1
        else:
            power = power - 1 
            break
        if init_number == 2 ** power :
            break
    while power > -1 :
        if init_number >= 2 ** power :
            init_number = init_number - 2 ** power
            target_number = target_number + "1"
            power = power - 1
        else:
            target_number = target_number + "0"
            power = power - 1
    return target_number

def bin_to_dec (init_number):
    power = len(f"{init_number}") - 1
    target_number = 0
    init_number = float(init_number)
    while power > -1:
        if 10 ** power <= init_number:
            target_number = target_number + 2 ** power
            init_number = init_number - 10 ** power
        power = power - 1
    return target_number 

def dec_to_hex (init_number):
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
            target_number = target_number + f"{conversion[multiplicator]}"
            init_number = init_number - multiplicator * 16 ** power
            power = power - 1
            multiplicator = 0
        if init_number < multiplicator * 16 ** power:
            multiplicator = multiplicator - 1
            target_number = target_number + f"{conversion[multiplicator]}"
            init_number = init_number - multiplicator * 16 ** power
            power = power - 1
            multiplicator = 0
        else:
            multiplicator = multiplicator + 1
        if multiplicator == 16:
            multiplicator = 0
            power = power - 1
    return target_number

def hex_to_dec(init_number):
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