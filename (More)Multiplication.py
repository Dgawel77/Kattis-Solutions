def startEndLine():
    print("+", end="")
    for _ in range(0, 3+4*len(num1)):
        print("-", end="")
    print("+")


def middleLine():
    print("| ", end="")
    for _ in range(0, STDlen):
        print("+---", end="")
    print("+ |")

5
def beginNumbers():
    print("|", end="")
    for number in num1:
        print("   " + number, end="")
    print("   |")


def box(SecondNum):
    # printPipeHere
    print("|" + PrintPipe(), end="")
    # firstLine with numbers
    printable = ""
    for FirstNum in num1:
        if (int(FirstNum) * int(SecondNum)) < 10:
            printable = "0"
        else:
            printable = str(int(FirstNum) * int(SecondNum))[0]
        print("|" + printable + " /", end="")
    print("| |")
    # nextLine
    print("| ", end="")
    for _ in num1:
        print("| / ", end="")
    print("|" + SecondNum + "|")
    # SecondLine with numbers
    # printPipehere
    print("|" + PrintPipe(), end="")
    for FirstNum in num1:
        if (int(FirstNum) * int(SecondNum)) < 10:
            printable = str(int(FirstNum) * int(SecondNum))[0]
        else:
            printable = str(int(FirstNum) * int(SecondNum))[1]
        print("|/ " + printable, end="")
    print("| |")


def PrintPipe():
    global PipeNumber
    if PipeNumber < len(StringProduct):
        PipeNumber -= 1
        return StringProduct[PipeNumber]
    else:
        PipeNumber -= 1
        return " "


def ProductLine():
    print("|", end="")
    for x in range(0, PipeNumber):
        print(PrintPipe() + " ", end="")
    print("   |")


while True:
    text = input().split()
    if text == ["0", "0"]:
        break
    num1 = text[0]
    num2 = text[1]
    STDlen = len(num1)
    product = int(num1) * int(num2)
    StringProduct = ""
    PipeNumber = (len(num1)+len(num2))*2
    for number in reversed(str(product)):
        StringProduct = StringProduct + str(number) + "/"
    startEndLine()
    beginNumbers()
    middleLine()
    for SecondNum in num2:
        box(SecondNum)
        middleLine()
    ProductLine()
    startEndLine()
