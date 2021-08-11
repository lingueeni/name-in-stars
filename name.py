#code of A letter
for ctr in range(7):
    for ctr2 in range(5):
        if (ctr2==0 or ctr2==4)  or ((ctr==0 or ctr==3) and (ctr2>0 and ctr2<4)) :
            print("*",end="")
        else:
            print(end=" ")
    print()
print('\n')

#code of L letter
for ctr in range(7):
    for ctr2 in range(5):
        if ctr2==0 or (ctr==6 and ctr2>0):
            print("*",end="")
        else:
            print(end=" ")
    print()
print('\n')

#code of Y letter
for ctr in range(5):
    for ctr2 in range(5):
        if (ctr2==2 and ctr>1) or (ctr==ctr2 and ctr2<2) or (ctr==0 and ctr2==4) or (ctr==1 and ctr2==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
