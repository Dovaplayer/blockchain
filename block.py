import json
import os
import hashlib


def get_hash(filename):
    file = open(os.curdir + '/blockchain/' + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def write_block(name, amount, to_whom, prev_hash=''):

    blockchain_dir = os.curdir + '/blockchain/'

    last_file = sorted(os.listdir(os.curdir + '/blockchain/'), key=int)[-1]
    #print(last_file)

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': get_hash(last_file)
    }

    with open(blockchain_dir + str(int(last_file) + 1), 'w') as file:
        json.dump(data, file, indent=4)


def main():
    write_block('Ivan', 2, 'Katya')


if __name__ == '__main__':
    main()