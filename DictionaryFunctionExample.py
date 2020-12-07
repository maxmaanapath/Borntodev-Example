words = {"Bird":"มันคือนก","Dog":"มันคือสุนัข","Ant":"มันคือมด","Cat":"มันคือแมว","Zebra":"มันคือม้าลาย"}
print(words["Bird"])
print(type(words.keys()))
print(type(words.values()))

for i in words.keys():
    print(i)

for x in words.values():
    print(x)