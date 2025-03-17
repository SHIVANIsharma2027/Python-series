def gr():
    a = int(input("enter first number: "))
    b = int(input("enter first number: "))
    c = int(input("enter first number: "))
    
    if(a>b and a>c):
        print(" a is greatest number.")
        return a
    elif(b>a and b>c):
        print(" b is greatest no. ")
    elif(c>a and c>b):
        print(" c is greatest no. ")        
print(gr())
gr()
