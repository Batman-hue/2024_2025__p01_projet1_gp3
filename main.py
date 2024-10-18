from math import*
from utils import*

def get_infos ():
    init_base = ask_for_the_init_base()
    init_number = ask_for_the_init_number(init_base)
    target_base = ask_for_the_target_base()
    print (dec_hex_bin_to_dec_hex_bin(init_base,init_number,target_base))
    return retry(input ("Voulez-vous refaire une convertion ? oui/non:   "))

def retry(answer):
    if  answer == "oui":
        return get_infos()
    elif answer == "non":
        return "Bonne journée ! "
    else:
        return retry(input ("Répondez par oui/non:   "))

def dec_hex_bin_to_dec_hex_bin(init_base,init_number,target_base):
    target_number = init_number
    if init_base == "2" and target_base == "10":
        target_number = bin_to_dec(init_number)
    if init_base == "2" and target_base == "16":
        target_number = dec_to_hex(bin_to_dec(init_number))
    if init_base == "10" and target_base == "2":
        target_number = dec_to_bin(init_number)
    if init_base == "10" and target_base == "16":
        target_number = dec_to_hex(init_number)
    if init_base == "16" and target_base == "2":
        target_number = dec_to_bin(hex_to_dec(init_number))
    if init_base == "16" and target_base == "10":
        target_number = hex_to_dec(init_number)
    return target_number

print(get_infos())