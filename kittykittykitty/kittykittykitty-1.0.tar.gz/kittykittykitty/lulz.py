# -*- coding: utf-8 -*-

# --------------------------------------------
# For the lulz
# --------------------------------------------

import colorama
from colorama import Fore, Back, Style


def meow():
    """Who's a good kitty?"""

    print("""
                                                   
                      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         
                    ▄▀            ▄       ▀▄       
                    █  ▄    ▄              █       
                    █            ▄█▄▄  ▄   █ ▄▄▄   
             ▄▄▄▄▄  █      ▀    ▀█  ▀▄     █▀▀ ██  
             ██▄▀██▄█   ▄       ██    ▀▀▀▀▀    ██  
              ▀██▄▀██        ▀ ██▀             ▀██ 
                ▀████ ▀    ▄   ██   ▄█    ▄ ▄█  ██ 
                   ▀█    ▄     ██    ▄   ▄  ▄   ██ 
                   ▄█▄           ▀▄  ▀▀▀▀▀▀▀▀  ▄▀  
                  █▀▀█████████▀▀▀▀████████████▀    
                  ████▀  ███▀      ▀███  ▀██▀      
                                                   

                    PRRRRR PPRRRRR PPPRRRRRR...
                    PACKAGE YOUR STUFF BRO!!!

        """)


def meow_with_color():
    """A good kitty with color!"""

    colorama.init()

    print(Fore.GREEN)
    meow()
    print(Style.RESET_ALL)

    colorama.deinit()


def main():
    meow_with_color()
