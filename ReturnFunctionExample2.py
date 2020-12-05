def vatCalculate(totalPrice):
    return totalPrice+(totalPrice*7/100)

print(vatCalculate(int(input("Price (THB) : "))))