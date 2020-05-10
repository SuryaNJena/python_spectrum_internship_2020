def fib(n):
    a = 0
    b = 1
    for j in range(int(n) + 1):
        ad_sum = a + b
        if (ad_sum == int(n)) or (int(n) == 0):
            return True
            break
        a = b
        b = ad_sum
    return False


k = input("Enter a number=")
if fib(k):
    print("is Fibonacci")
else:
    print("not Fibonacci")
o = input("enter range=")
print("list of fibonacci in range are:")
for i in range(int(o)+1):
    if fib(i):
        print(i, end=' ')
