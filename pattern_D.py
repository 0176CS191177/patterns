for row in range(6):
    for col in range(4):
        if(col==3 and row!=0 and row!=5) or col==0 or ((col==1 or col==2 ) and row!=1 and row!=2 and row!=3 and row!=4):
            print("*", end=" ")
        else:
            print(end="  ") 
    print() 