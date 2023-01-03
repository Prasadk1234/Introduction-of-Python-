sum=0
while(True):
 userInput=input("Enter price of thr product: ")
 if(userInput!='m'):
    sum= sum + int(userInput)
    print(sum)
 else:
    print(f"Your total amount of all products is {sum} .\nThank you....")
    a=input("Enter you have to operate it again (y/n).....")
    if a=='y':
       print(userInput)
    else:
        break 
   