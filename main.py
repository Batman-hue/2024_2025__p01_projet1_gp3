from utils import *
from data import *
from math import*

def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base) :
    if target_base == 2:
        if init_base == 10:
            target_number = dec_to_bin (init_number)
        else:
            target_number = dec_to_bin(hex_to_dec(init_number))
    if target_base == 10:
        if init_base == 2:
            target_number = bin_to_dec(init_number)
        else:
            target_number = hex_to_dec(init_number)
    if target_base == 16:
        if init_base == 2:
            dec_to_hex(bin_to_dec(init_number))
        else:
            dec_to_hex(init_number)
    if init_base == target_base:
        target_number = init_number
    return target_number

def get_infos ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
        bin_dec_hex__to__bin_dec_hex (init_number, \
                                      init_base, \
                                        target_base)
    
print(get_infos ())

def dec_to_bin (init_number):
    power = 0
    target_number = ""
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
    while power > 0:
        if 10 ** power <= init_number:
            target_number = target_number + 2 ** power
            init_number = init_number - 10 ** power
        power = power - 1
    return target_number 

conversion = dec_number_valid_chars + ["A", "B", "C", "D", "E", "F"]

def dec_to_hex (init_number):
    power = 0
    target_number = ""
    multiplicator = 0
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
        target_number = target_number + ((16 ** power) * conversion.index(i))
        power = power - 1
    return target_number