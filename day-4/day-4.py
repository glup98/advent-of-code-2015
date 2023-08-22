import hashlib


def mine_adventcoin(secret_key, num_of_zeros=5):
    number = 1
    target = '0' * num_of_zeros

    while True:
        data = secret_key + str(number)
        result_hash = hashlib.md5(data.encode()).hexdigest()

        if result_hash.startswith(target):
            return number

        number += 1


secretKey = "bgvyzdsv"
print(mine_adventcoin(secretKey))
print(mine_adventcoin(secretKey, 6))
