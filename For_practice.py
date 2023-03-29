"""Program for defining zeros in factorization
def factorial(n):
#    if (n==1) and (n==0):
#        return 1
#    else:
#        return n*(n-1) 
#def factorialTrailingZeroes(number):
#    count=0
    i=5
    while(number//i!=0):
        count+=int(number/i)
        i=i*5
    return count

print(factorialTrailingZeroes(1000)"""

"""print("Enter your favourite number")
num=int(input())
for i in range(1,11):
    print(f"{num}*{i}=",num*i)

print("Choose the words that are given below:\n'S'\n'C'\n'D'\n'G'")
c=input()
if c=='S':
    print("Satisfaction")
elif c=='C':
    print("Configuration")
elif c=='D':
    print("Donkey")
elif c=='G':
     print("Gauri")

import time 
a=time.strftime("%H %M %S")
print(a)


l=input()
r=input()
k=input()
count=0
for i in range(int(l),int(r)):
    if (i%int(k))==0:
        count+=1"""

"""print("Enter a number")
num=[int(input())]
add=0
for i in num:
    add=int(num[0]+num[0+1])"""

#Error Handling in program 
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")
#try:
#    num = int(input("Enter an integer: "))
#    a = [6, 3]
#    print(a[num])
#except ValueError:
#    print("Number entered is not an integer.")
    
#except IndexError:
#  print("Index Error")
    
"""def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

#  finally:
#    print("I am always executed")
  # print("I am always executed")

#x = func1()
#print(x)


    a=int(input("ENter any value between 5 and 9"))
try:
 a=int(input("ENter any value between 5 and 9"))
   
 if(a<5 or a>9):
   raise  ValueError('Your value is not between 5 and 9')
except:
   if a!='Quite':
    print(a)"""

"""my_list=[1,2,3,4,5]
for i in range(len(my_list)):
    print(i)"""

"""class Hiring:
    def __init__(self, Qualifications, Experience):
        self.Qualifications=Qualifications
        self.Experience=Experience

    def Interview(self):
        print('What is your Qualification and Experience...?')
        print(self.Qualifications)
        print(self.Experience)
    
class Selection(Hiring):
    def Sel(self, apptitude):
        print('What is your scoore in apptitude....?')
        self.apptitude=apptitude
        print(self.apptitude)
#Hired=Hiring('B.Tech', 'Fresher')
#Hired=Selection('B.Tech', 'Fresher')
class AllQ(Selection, Hiring):
    def all_q(self, Qualifications, Experience, apptitude):
        self.Qualifications=Qualifications
        self.Experience=Experience
        self.apptitude=apptitude
       

HI=AllQ.all_q('B.Tech', 'Fresher')
print(HI('90'))"""


"""# Example input data
X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y = [1,0,1,0,1]
  
# Train a model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)
print(model) 
# Make a prediction
prediction = model.predict([[6,7]])[0]
print(prediction)"""
