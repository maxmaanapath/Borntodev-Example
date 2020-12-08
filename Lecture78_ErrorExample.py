inputNumber1 = int(input("Number :"))
inputNumber2 = int(input("Number 2 :"))
while True:
    result=0
    if inputNumber1 and inputNumber2 <= 0:
        print("Wrong Number!! Input again")
        inputNumber1 = int(input("Number :"))
        inputNumber2 = int(input("Number 2 :"))
    elif inputNumber1 and inputNumber2 > 0:
        result = inputNumber1/inputNumber2
print(result)