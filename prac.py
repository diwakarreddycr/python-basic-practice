class practice:
    # To display as output of different things
    def printing():
        print("Hello World!")#printing Hello World!
        print(12345)
        print("Hello World",end="!")
        print("string:",str(input("\nEnter string:")))
    #To do different arithmetic operations
    def arith_operations():
        num_1=int(input("Enter a Number:"))
        num_2=int(input("Enter a Number:"))
        sum=num_1+num_2
        if(num_1>num_2):
            sub=num_1-num_2
            div=num_1/num_2
            div2=num_1//num_2
            rem=num_1%num_2
        else:
            sub=(num_2)-int(num_1)
            div=num_2/num_1
            div2=num_2//num_1
            rem=num_2%num_1
        mult=num_1*num_2
        power=num_1**num_2
        print("num_1+num_2=",sum)
        print("substractin=",sub)
        print("num_1*num_2=",mult)
        print("division(/)=",div)
        print("division(//)=",div2)
        print("reminder(%)=",rem)
    #To find the area of a Triangle(A=½(base X height)
    def area_tri():
        base=float(input("Enter the value of base of Triangle:"))
        height=float(input("Enter the value of height of Triangle:"))
        area=(1/2)*(base*height)
        print(area)
    def fibb_series():
        x=0
        y=1
        temp=0
        n=int(input("Enter no.of values required in series:"))
        print("The series is ",end=": ")
        print(x,y,sep=",",end=",")
        for i in range(0,n):
            temp=x+y
            x=y
            y=temp
            if(i<n-1):
                print(y,end=",")
            else:
                print(y)
    def prime_numbers():
        x=int(input("Enter the value from:"))
        y=int(input("Enter the value to:"))
        def prime():
            for i in range(x,y):
                for j in range(2,i):
                    if(i%j==0):
                        break
                    else:
                        print(i,end=",")
                        break
        prime()
    #To get Christmass tree pattern:
    def chrismas_pattern():
        n=int(input())
        for i in range(n):
            for j in range(i,n):
                print(" ",end=" ")
            for j in range(i):
                print("*",end=" ")
            for j in range(i-1):
                print("*",end=" ")
            print()
        for i in range(1,n):
            for j in range(i+1,n):
                print(" ",end=" ")
            for j in range(i+1):
                print("*",end=" ")
            for j in range(i):
                print("*",end=" ")
            print()
        for i in range(n//2):
            for j in range(int(n*0.8)):
                print(" ",end=" ")
            for j in range(n//3):
                print("*",end=" ")
            print()
