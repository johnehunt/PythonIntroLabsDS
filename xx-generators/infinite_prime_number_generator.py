
def infinite_prime_number_generator():
    prime_number = True
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                prime_number = False
                break
        if prime_number:
            yield num
        prime_number = True
        num += 1


def main():
    prime = infinite_prime_number_generator()
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))
    print(next(prime))


if __name__ == '__main__':
    main()
