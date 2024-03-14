def prime_checker(number):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count +=1
    
    if count > 2:
        print(f"{number} is not a prime number.")
    else:
        print(f"{number} is a prime number.")


def prime_checker(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


n = int(input("Check this number is prime: "))
prime_checker(number=n)