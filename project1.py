import string
import random
print("Enter the number of password do you won't....")
pr=input()
s1=string.ascii_letters
#print(s1)
s2=string.ascii_lowercase
#print(s2)
s3=string.ascii_uppercase
#print(s3)
s4=string.punctuation
#print(s4)
s5=string.octdigits
#print(s5)
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
s.extend(list(s5))
#print(s)
random.shuffle(s)
#print(s)
print("".join(s[0:int(pr)]))