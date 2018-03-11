from pwdgen import alphanumeric, ascii, passphrase, numeric


def test_main():
    for gen in [ascii, alphanumeric, passphrase, numeric]:
        gen()
