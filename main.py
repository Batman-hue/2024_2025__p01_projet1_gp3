from math import*
from utils import*


def get_infos ():
    init_base = ask_for_the_init_base()
    init_number = ask_for_the_init_number(init_base)
    target_base = ask_for_the_target_base()
    print (dec_hex_bin_to_dec_hex_bin(init_base,init_number,target_base))     # Envoie les informations de conversion à la fonction.
    return retry(input ("Voulez-vous refaire une convertion ? oui/non:   "))


def dec_hex_bin_to_dec_hex_bin(init_base,init_number,target_base):
    target_number = init_number
    if init_base == "2" and target_base == "10":
        target_number = bin_to_dec(init_number)      # De binaire vers décimal, envoie le nombre à convertir vers la fonction appropriée.
    if init_base == "2" and target_base == "16":
        target_number = dec_to_hex(bin_to_dec(init_number))      # De binaire vers hexadécimal, envoie le nombre à convertir vers la fonction appropriée.
    if init_base == "10" and target_base == "2":
        target_number = dec_to_bin(init_number)      # De décimal vers binaire, envoie le nombre à convertir vers la fonction appropriée.
    if init_base == "10" and target_base == "16":
        target_number = dec_to_hex(init_number)      # De décimal vers hexadécimal, envoie le nombre à convertir vers la fonction appropriée.
    if init_base == "16" and target_base == "2":
        target_number = dec_to_bin(hex_to_dec(init_number))      # De hexadécimal vers binaire, envoie le nombre à convertir vers la fonction appropriée.
    if init_base == "16" and target_base == "10":
        target_number = hex_to_dec(init_number)      # De hexadécimal vers décimal, envoie le nombre à convertir vers la fonction appropriée.
    return target_number



def retry(answer):     # Permet de refaire une conversion à la fin du code.
    if  answer == "oui":
        return get_infos()
    elif answer == "non":
        print("Bonne journée !")
        return 
    else:
        return retry(input ("Répondez par oui/non:   "))     # Relance la demande si la réponse fournie n'est pas supportée par le programme.



get_infos()