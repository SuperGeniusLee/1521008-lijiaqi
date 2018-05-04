#!/env/python3
# -*-encoding: utf-8-*-


def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(16):
        print("{} is prime? {}".format(i, is_prime(i)))