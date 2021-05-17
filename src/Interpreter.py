import os

import MorseFactory

actions = {
    "QUIT": 'Q',
    "FROM_MORSE": 'E',
    "TO_MORSE": 'M'
}

action_str = "\n\nTo quit press: " + actions["QUIT"] + \
             ", To translate from english to morse press: " + actions["TO_MORSE"] + \
             ", To interpret morse to english press: " + actions["FROM_MORSE"] + "\n"

# os.system('cls')
print("Welcome to Morse Code interpreter\nPlease Select an action:")

act = ""
while act != actions["QUIT"]:
    act = input(action_str).capitalize()
    if act == actions["FROM_MORSE"]:
        intp = MorseFactory.interpret(input("msg: "))
        print(intp)

    elif act == actions["TO_MORSE"]:
        MorseFactory.create_morse(input("msg: "))

    elif act != actions["QUIT"]:
        print("Invalid")

