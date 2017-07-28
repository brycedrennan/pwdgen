import argparse

from pwdgen import password, ascii, alphanumeric, passphrase, numeric

generators = {
    'password': password,
    'ascii': ascii,
    'alphanumeric': alphanumeric,
    'passphrase': passphrase,
    'numeric': numeric
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", nargs='?', default=None)
    parser.add_argument("type", nargs='?', default='ascii')
    args = parser.parse_args()
    if args.length:
        print(generators[args.type](int(args.length)))
    else:
        for gen in [ascii, alphanumeric, passphrase, numeric]:
            print()
            print(gen())
        print()


if __name__ == '__main__':
    main()
