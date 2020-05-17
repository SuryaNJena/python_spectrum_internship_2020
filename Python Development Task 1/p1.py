def accept(a, b):
    def calc():
        return a + b

    return calc() + 5


x = int(input())
y = int(input())
print(accept(x, y))
