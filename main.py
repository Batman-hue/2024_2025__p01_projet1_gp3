def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base) :
    if init_base == target_base:
        return init_number
    target_number = None
    return target_number

from utils import *
from data import *
from math import*

def get_infos ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
        bin_dec_hex__to__bin_dec_hex (init_number, \
                                      init_base, \
                                        target_base)
    
print(get_infos ())

def from_dec_to_bin (init_number):
    power = 0
    while True :
        if init_number >= 2 ** power :
            power = power + 1
        elif init_number == 2 ** power :
            break
        else:
            power = power - 1 
            break
    while True :
        target_number = ""
        if init_number >= 2 ** power :
            target_number = target_number + "1"
            power = power - 1
        else:
            target_number = target_number + "0"
            power = power - 1
        if power < 0 :
            break
    return target_number
