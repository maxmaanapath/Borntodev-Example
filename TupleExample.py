tupleExample = ("Magma","Somo","Tangmo")
print(tupleExample)
tupleExample2 = ("Bank","Eark")
tupleExample3 = tupleExample + tupleExample2 *2
print(tupleExample3)
print(tupleExample3[2])
print(tupleExample3[:2])
print("Somo" in tupleExample3)

for i in tupleExample3:
    print("Hello",i)