
w1 ="Make a lot of money"
w2 = "buy now"
w3= "subscribe this"
w4= "click this"

a = input("enter your comment: ")
if((w1 in a) or (w2 in a) or (w3 in a) or (w4 in a)):
    print(" this is a spam comment.")
    
else:
    print(" continue this is not spam ")
        
