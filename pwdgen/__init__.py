__version__ = open('.version', "rt").read().strip()

from .generators import password, ascii, alphanumeric, passphrase, numeric
