r = input("Enter range:")
n = input("Enter number:")


def prime(k):
    c = 0
    for i in range(1, int(k)):
        if int(k) % i == 0:
            c = c + 1

    if c == 1:
        return True
    else:
        return False


if prime(n):
    print("NUMBER IS PRIME")
print("list of primes are:")
for i in range(1, int(r) + 1):
    if prime(i):
        print(i, end = ' ')
