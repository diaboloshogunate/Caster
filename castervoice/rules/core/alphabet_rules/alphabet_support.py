from dragonfly import Choice

from castervoice.lib.actions import Key, Text


def caster_alphabet():
    return {
        "anne"    : "a",
        "ben"     : "b",
        "carl"    : "c",
        "don"     : "d",
        "ed"      : "e",
        "frank"    : "f",
        "george"  : "g",
        "hot"     : "h",
        "ice"     : "i",
        "jim"    : "j",
        "king"    : "k",
        "lance"    : "l",
        "mike"    : "m",
        "nate"    : "n",
        "oak"     : "o",
        "pam"   : "p",
        "queen"   : "q",
        "rick"    : "r",
        "sam"     : "s",
        "todd"    : "t",
        "urn"     : "u",
        "vin"     : "v",
        "will"    : "w",
        "xray"      : "x",
        "yoke"    : "y",
        "Zed"     : "z",
    }


def get_alphabet_choice(spec):
    return Choice(spec, caster_alphabet())


def letters(big, dict1, dict2, letter):
    '''used with alphabet.txt'''
    d1 = str(dict1)
    if d1 != "":
        Text(d1).execute()
    if big:
        Key("shift:down").execute()
    letter.execute()
    if big:
        Key("shift:up").execute()
    d2 = str(dict2)
    if d2 != "":
        Text(d2).execute()


def letters2(big, letter):
    if big:
        Key(letter.capitalize()).execute()
    else:
        Key(letter).execute()


'''for fun'''


def elite_text(text):
    elite_map = {
        "a": "@",
        "b": "|3",
        "c": "(",
        "d": "|)",
        "e": "3",
        "f": "|=",
        "g": "6",
        "h": "]-[",
        "i": "|",
        "j": "_|",
        "k": "|{",
        "l": "|_",
        "m": r"|\/|",
        "n": r"|\|",
        "o": "()",
        "p": "|D",
        "q": "(,)",
        "r": "|2",
        "s": "$",
        "t": "']['",
        "u": "|_|",
        "v": r"\/",
        "w": r"\/\/",
        "x": "}{",
        "y": "`/",
        "z": r"(\)"
    }
    text = str(text).lower()
    result = ""
    for c in text:
        if c in elite_map:
            result += elite_map[c]
        else:
            result += c
    Text(result).execute()
