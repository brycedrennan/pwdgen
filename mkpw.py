
from pwdgen import password, ascii, alphanumeric, passphrase, numeric

for gen in [password, ascii, alphanumeric, passphrase, numeric]:
    print(gen())
