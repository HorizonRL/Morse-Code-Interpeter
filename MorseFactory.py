import winsound
import MorseSymbols
import time

frequency = 550
duration = 100


def morse_beep(kind: MorseSymbols.UnitOfTime):
    winsound.Beep(frequency, duration * kind.value)


def space(kind: MorseSymbols.UnitOfTime):
    time.sleep(kind.value * (duration / 1000))


def is_letter(d: str) -> bool:
    return d == "." or d == "-"


def play_morse(morse_str: str):
    for d in morse_str:
        if is_letter(d):
            kind = MorseSymbols.UnitOfTime.DIT if d == "." else MorseSymbols.UnitOfTime.DAH
            morse_beep(kind)
            space(MorseSymbols.UnitOfTime.SPACE_SINGLES)
        else:
            space(MorseSymbols.UnitOfTime.SPACE_WORDS)


def create_morse(msg: str):
    for c in msg:
        morse_str = MorseSymbols.SYMBOLS_DICT[str(c).capitalize()]
        print(morse_str, end=" ")
        play_morse(morse_str)


def interpret(morse_str: str) -> str:
    key_list = list(MorseSymbols.SYMBOLS_DICT.keys())
    val_list = list(MorseSymbols.SYMBOLS_DICT.values())
    msg = ""

    for d in morse_str.split(" "):
        pos = val_list.index(d)
        msg += key_list[pos]

    return msg