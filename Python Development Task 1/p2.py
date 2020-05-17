word = input()
result = ""
for i in range(len(word)):
    if (word[i]).islower():
        result += word[i]
for i in range(len(word)):
    if (word[i]).isupper():
        result += word[i]
print(result)