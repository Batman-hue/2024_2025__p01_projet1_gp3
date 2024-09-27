def bin_dec_hex__to__bin_dec_hex (init_number, init_base, target_base) :
    pass
    target_number = None
    return target_number

from utils import *
from data import *

def get_infos ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
        bin_dec_hex__to__bin_dec_hex (init_number, \
                                      init_base, \
                                        target_base)
    
print(get_infos ())