# imports
from hashlib import sha256
from random import randint

# Variable
MAX_NONCE = 1000000000000000000000
difficulty = 6
new_hash = ""


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def transactions():
    n = 0
    while n < 3:
        sender = random_with_N_digits(5)
        receiver = random_with_N_digits(5)
        bitcoins = random_with_N_digits(2)
        transactions = str(sender) + "->" + str(receiver) + "->" + str(bitcoins)
        n = n + 1
        return transactions


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transaction, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):

        text = str(block_number) + transaction + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Ich habe den Block Fertig! So viele versuche habe ich benötigt {nonce}")

            return new_hash
    raise BaseException(f"Der Block wurde nicht fertig. {MAX_NONCE}")


if __name__ == '__main__':
    block_numbr = 1
    a = 0
    while a < 11:
        nexttransactions = transactions()
        block_numbr = block_numbr + 1
        previoushash = new_hash
        new_hash = mine(block_numbr, nexttransactions, previoushash,
                        difficulty)

        print(new_hash)
        a = a + 1
