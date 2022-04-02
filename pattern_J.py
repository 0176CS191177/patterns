for row in range(6):
    for col in range(5):
    
        if(col==2 and row!=5 )  or ((col==0 or col==1 or col==3 or col==4  ) and row!=1 and row!=2 and row!=3 and row!=4 and row!=5) or ( row==5 and col!=0  and col!=2 and col!=3 and col!=4) or(row==4 and col==0):
            print("*", end=" ")
        else:
            print(end="  ") 
    print() 