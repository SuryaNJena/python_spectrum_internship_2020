S1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
S2 = {1, 3, 4, 6, 8, 11, 22, 34, 51, 67}
s1 = S1.copy()
s2 = S2.copy()
for i in s1:
    for j in s2:
        if i == j:
            S1.discard(i)
print(S1)