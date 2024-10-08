from data import*

ask_for_the_target_base_text = "Choissisez la base dans laquelle le nombre sera converti entre binaire, héxadécimal ou décimal:  "

ask_again_for_the_target_base_text = "Base incorrect; réessaie (ne pas mettre de majuscules):  "

bin_number_valid_chars = ["0", "1"]

dec_number_valid_chars = \
    bin_number_valid_chars \
  + ["2", "3", "4", "5", "6", "7", "8", "9"]

hex_number_valid_chars = \
    dec_number_valid_chars \
  + ["A", "B", "C", "D", "E", "F"] \
  + ["a", "b", "c", "d", "e", "f"]

def check_char_number_validity (char):
    return char in hex_number_valid_chars

ask_for_the_init_number_text = "Choisis un nombre:  "

ask_again_for_the_init_number_text = "Nombre incorrect; réessaie :  "

def check_char_number_validity (char):
    return char in hex_number_valid_chars 

def is_a_valid_number (number):
    i = 0
    is_a_valid_char = True
    while is_a_valid_char == True and i <= len (number) - 1:
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number ():
    init_number = input (ask_for_the_init_number_text)
    while not (is_a_valid_number (init_number)) == True:
        init_number = input (ask_again_for_the_init_number_text)
    return init_number

def ask_for_the_target_base ():
    answer_target_base = input (ask_for_the_target_base_text)
    while True:
        if answer_target_base == "binaire":
           target_base = 2
           break
        elif answer_target_base == "décimal":
           target_base = 10
           break
        elif answer_target_base == "héxadécimal":
            target_base = 16
            break
        else:
            answer_target_base = input(ask_again_for_the_target_base_text)
    return target_base









