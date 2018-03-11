import string
from functools import partial

from randomlineaccess import IndexedOpen

from pwdgen.wordlist import LazyString
from .rand import sample_with_replacement
from .wordlist import get_wordlist_path

ASCII_CHARACTERS = string.ascii_letters + string.digits + string.punctuation
ALPHANUMERIC_CHARACTERS = string.ascii_letters + string.digits
UNICODE_SYMBOLS = u"☺★✰✓ÆÖÛ÷ɣɥΘЖ∭☀☂☃☎☻♫✈❤"
ALL_CHARACTERS = ASCII_CHARACTERS + UNICODE_SYMBOLS
_PASSPHRASE_CHARACTERS_TO_REMOVE = {ord(c): None for c in u"'\n\r"}


def password(length=100, characters=ALL_CHARACTERS, join_char=""):
    return join_char.join(sample_with_replacement(characters, length))


def passphrase(length=8, wordlist=LazyString(get_wordlist_path)):
    with IndexedOpen(str(wordlist)) as wordlist_file:
        return password(length, wordlist_file, join_char='-').translate(_PASSPHRASE_CHARACTERS_TO_REMOVE)


ascii = partial(password, characters=ASCII_CHARACTERS)
alphanumeric = partial(password, characters=ALPHANUMERIC_CHARACTERS)
numeric = partial(password, characters=string.digits)
symbols = partial(password, characters=UNICODE_SYMBOLS)
