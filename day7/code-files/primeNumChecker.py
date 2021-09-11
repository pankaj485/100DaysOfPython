
n = int(input("Check this number: "))
prime_checker(number=n)


def prime_checker(number):
    isPrime = True
    for num in range(2, number):
        if number % num == 0:
            isPrime = False

    if not isPrime:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
