import random

if __name__ == '__main__':
    random.seed(1337)
    print(''.join(chr(random.randrange(256) ^ c) for c in bytes.fromhex('1EE4EA0944EC87A6FA604E1B') if random.randrange(2)))