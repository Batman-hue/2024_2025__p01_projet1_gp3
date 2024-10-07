from utils import*

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]
ask_for_the_init_base_text = "Quelle est la base du nombre ?  "
ask_again_for_the_init_base_text = "LA BASE "


def ask_for_the_init_base ():
    init_base = input(ask_for_the_init_base_text)
    while not (is_a_valid_base (init_base)) == True:
        init_base = input (ask_again_for_the_init_base_text)
    return init_base


def is_a_valid_base(base):
    i = 0
    is_a_valid_base = True
    while is_a_valid_base == True and i <= len (base) - 1:
        is_a_valid_base = check_base_base_validity (base[i])
        i = i + 1
    return is_a_valid_base

def check_base_base_validity(basen):
    return basen in hex_number_valid_chars