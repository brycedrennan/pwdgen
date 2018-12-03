import string
from functools import partial

from randomlineaccess import IndexedOpen

from pwdgen.wordlist import LazyString
from .rand import sample_with_replacement
from .wordlist import get_wordlist_path

ASCII_CHARACTERS = string.ascii_letters + string.digits + string.punctuation
ALPHANUMERIC_CHARACTERS = string.ascii_letters + string.digits

EMOJI_CHARACTERS = []
EMOJI_RANGES = [
    (0x1F300, 0x1F322),
    (0x1F324, 0x1F393),
    (0x1F39E, 0x1F3F0),
    (0x1F400, 0x1F4FD),
    (0x1F600, 0x1F64F),
    (0x1F680, 0x1F6C5),
    (0x1F910, 0x1F93A),
    (0x1F947, 0x1F96F),
]

for s, e in EMOJI_RANGES:
    for chr_code in range(s, e):
        EMOJI_CHARACTERS.append(chr(chr_code))
EMOJI_CHARACTERS = "".join(EMOJI_CHARACTERS)

ALL_CHARACTERS = ASCII_CHARACTERS + EMOJI_CHARACTERS

_PASSPHRASE_CHARACTERS_TO_REMOVE = {ord(c): None for c in "'\n\r"}


def password(length=100, characters=ALL_CHARACTERS, join_char=""):
    return join_char.join(sample_with_replacement(characters, length))


def passphrase(length=8, wordlist=LazyString(get_wordlist_path)):
    with IndexedOpen(str(wordlist)) as wordlist_file:
        return password(length, wordlist_file, join_char="-").translate(_PASSPHRASE_CHARACTERS_TO_REMOVE)


def eff_passphrase(length=8):
    from .eff_wordlist import EFF_WORDS

    return password(length, EFF_WORDS, join_char="-")


ascii_lowercase = partial(password, characters=string.ascii_lowercase)
ascii_upppercase = partial(password, characters=string.ascii_uppercase)
ascii = partial(password, characters=ASCII_CHARACTERS)
alphanumeric = partial(password, characters=ALPHANUMERIC_CHARACTERS)
numeric = partial(password, characters=string.digits)
hex = partial(password, characters=string.hexdigits)
emoji = partial(password, characters=EMOJI_CHARACTERS)
