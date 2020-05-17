n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the numbers\n"
                        "in list separated with space\n"
                        "without'[]': ").strip().split()))[:n]
b=[]
for i in range(len(a)-1):
    if a[i] % 2 == 0:
        b.append(a[i])
        a.remove(a[i])
print(a)
print(b)