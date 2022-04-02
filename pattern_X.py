for row in range(7):
    for col in range(7):
        if ((row==0) and (col>0 and col<6)) :
            print("*", end=" ")
        else:
            print(end="  ") 
    print() 