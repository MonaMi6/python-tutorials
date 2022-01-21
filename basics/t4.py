cond = 0
while cond < 10:
    print("1", cond)
    cond = cond + 3
print("done")

for c in [3, 2, 1]:
    print(c)
print("done!")

nomber = 1
while nomber <= 100:

    if nomber % 3 != 0 and nomber % 5 !=0:
        print(nomber)
    if nomber % 3 == 0:
        print("Xey")
    if nomber % 5 == 0:
        print("XO")    
    
    nomber = nomber + 1
    