for row in range(7):
    for col in range(4):
        if (col==0) or (col==3 and row!=0  and row!=3 and row!=4 and row!=5 and row!=6) or ((row ==0 or row==3 )) and (col>0 and col<3) :
            print("*", end=" ")
        else:
            print(end="  ") 
    print() 
