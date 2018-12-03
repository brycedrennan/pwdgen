import pytest

from pwdgen import password, ascii, alphanumeric, passphrase, numeric, emoji, ascii_lowercase, ascii_upppercase, hex, eff_passphrase

generators = [password, ascii, alphanumeric, passphrase, numeric, emoji, ascii_lowercase, ascii_upppercase, hex, eff_passphrase]


@pytest.mark.parametrize("generator", generators)
def test_main(generator):
    generator()
