import sys
import winsound
import MorseSymbols
import time
import pyttsx3

frequency = 550
duration = 160
txt_speech = pyttsx3.init()
txt_speech.setProperty('rate', 114)


def morse_beep(kind: MorseSymbols.UnitOfTime):
    winsound.Beep(frequency, duration * kind.value)


def space(kind: MorseSymbols.UnitOfTime):
    time.sleep(kind.value * (duration / 1000))


def is_letter(d: str) -> bool:
    return d == "." or d == "-"


def play_morse(morse_str: str):
    counter = 0

    for d in morse_str:
        if is_letter(d):
            print_morse(counter, morse_str, True)

            kind = MorseSymbols.UnitOfTime.DIT if d == "." else MorseSymbols.UnitOfTime.DAH
            morse_beep(kind)
            space(MorseSymbols.UnitOfTime.SPACE_SINGLES)

            print_morse(counter, morse_str, False)

        elif d == " ":
            space(MorseSymbols.UnitOfTime.SPACE_LETTERS)
        else:
            space(MorseSymbols.UnitOfTime.SPACE_WORDS)

        counter += 1


def print_morse(word_index: int, morse_str: str, is_color: bool):
    color = '\33[31m'
    if word_index == 0:
        if is_color:
            sys.stdout.write("\r" + color + morse_str[word_index] + '\33[0m')
        else:
            sys.stdout.write("\r" + morse_str[word_index])
    else:
        if is_color:
            sys.stdout.write("\r" + morse_str[:word_index] + color + morse_str[word_index] + '\33[0m')
        else:
            sys.stdout.write("\r" + morse_str[:word_index + 1])
    sys.stdout.flush()


def create_morse(msg: str):
    morse_str = ""
    for c in msg:
        morse_str += MorseSymbols.SYMBOLS_DICT[str(c).capitalize()] + " "

    txt_speech.say("The message is: ")
    txt_speech.runAndWait()
    play_morse(morse_str[:len(morse_str) - 1])


def interpret(morse_str: str) -> str:
    if not morse_str.isalnum():
        key_list = list(MorseSymbols.SYMBOLS_DICT.keys())
        val_list = list(MorseSymbols.SYMBOLS_DICT.values())
        msg = ""

        for d in morse_str.split(" "):
            pos = val_list.index(d)
            msg += key_list[pos]

        txt_speech.say(msg)
        txt_speech.runAndWait()
        return msg
