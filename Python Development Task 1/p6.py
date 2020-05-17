opt = input("Enter OPTION\n"
            "+\n"
            "-\n"
            "x\n"
            "/or\\\n")
a = input ("Enter First Number")
b = input("Enter Second Number")
if opt == "+":
    print(int(a)+int(b))
elif opt == "-":
    print(int(a)-int(b))
elif opt == "x":
    print(int(a)*int(b))
else:
    print(int(a)/int(b))