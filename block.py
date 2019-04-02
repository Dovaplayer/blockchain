import json
import os
import hashlib


blockchain_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_integrity():
    files = sorted(os.listdir(os.curdir + '/blockchain/'), key=int)
    result = []

    for file in files[1:]:
        f = open(blockchain_dir + file)
        h = json.load(f)['hash']

        prev_file = str(int(file) - 1)
        #print(prev_file)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        result.append({'block': prev_file, 'status': res})

    return result


def write_block(name, amount, to_whom, prev_hash=''):

    #blockchain_dir = os.curdir + '/blockchain/'

    last_file = sorted(os.listdir(blockchain_dir), key=int)[-1]
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
    #write_block('Iffrfran', 100000, 'Katgrya')
    print(check_integrity())


if __name__ == '__main__':
    main()