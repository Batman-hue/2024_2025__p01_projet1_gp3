from data import check_char_number_validity

def is_a_valid_number(number):
    i = 0
    is_a_valid_char = True 
    while is_a_valid_char == True and i <= len (number):
        is_a_valid_char = check_char_number_validity (number [i])
        i = i + 1
    return is_a_valid_char

def ask_for_the_init_number():
    init_number = input ("Entrez votre nombre: ")
    while not (is_a_valid_number):
        init_number= input("Nombre incorrect; réessayez: ")
    return init_number









