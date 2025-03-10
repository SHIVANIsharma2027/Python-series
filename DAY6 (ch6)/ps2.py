marks1 = int(input("enter a marks: "))
marks2 = int(input("enter a marks: "))
marks3 = int(input("enter a marks: "))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and  marks1>=33 and marks2>=33 and marks3>=33):
    print("congratulational! you are passed", total_percentage)
    
else:
    print("your are fail, \n try again", total_percentage)    
