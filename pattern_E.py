for row in range(7):
    for col in range(4):
        if (col==0 )or( col==3 and row!=1 and row!=2 and row!=4 and row!=5) or ((row ==0 or row==3 or row==6)) and (col>0 and col<3) :
            print("*", end=" ")
        else:
            print(end=" ") 
    print() 