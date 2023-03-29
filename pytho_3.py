"""class Employee:
    #BestEmployeeAward= True #class object attribute 
    def __init__(self, Name):
        self._Name=Name
        #Name=input("Enter Your Name")
        #print(Name)
        if(self):
            print(f"{self._Name}is the best employee in our office")
    def degree(self):
        print(f"{self._Name} have a BCS degree")
Employee1=Employee('Gauri ')
print(Employee1._Name)
#Employee1._Name='!!!!'
#print(Employee1.Name)
#a=Employee1.degree()
#print(a)"""

"""class Cat:
    species='mammal'
    def __init__(self, Name, Age):
        self.Name=Name
        self.Age=Age

ca1=Cat('Mani', 1)
cat2=Cat('Ruby', 2)
cat3=Cat('Salu', 4)

def get_oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {get_oldest_cat(ca1.Age,cat2.Age,cat3.Age)}")"""

#cls is known as class
 
 #Inheritance 
"""class employee:
    def Biomatric_Scan():
        print("Welcome Sir")

class Office(employee):
    def __init__(self, OfficeName, Address):
        self.OfficeName=OfficeName
        self.Address=Address
    
    def Print(self):
        print(f"{self.OfficeName} is the Office and address is{self.Address}")

class lunchHall(employee):
    pass

#a=Office()
#print(Office.Biomatric_Scan())
print(Office.Print(self=['Google','silicon vally']))"""

"""class User:
    def signIN(self):
        print("'i'm logged in ")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of{self.power}')

a=Wizard('Prasad',100)
print(a.attack())"""

"""class employee:
    def Accept(self):
        print("I'm in class accept 1 ")
        
class employee2:
    def Accept(self):
        print("I'm in class accept 2 ")
sl=employee()
sl2=employee2()

def Print_Employee(char):
    char.Accept()

Print_Employee(sl2)
Print_Employee(sl)"""

"""class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats=[Simon('simon', 1), Sally('sally', 2)]

my_pets=Pets(my_cats)

my_pets.walk()"""

"""class User(object):
    def __init__(self, email):
        self.email=email
    def sigh_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(self, email)
        self.name=name
        self.power=power
    def attaack(self):
        print(f'attacking with power of {self.power}')

#introspection 
wizard1=Wizard('Prasad', 20, 'prasad@gmail.com')
print(dir(wizard1))"""

#dudder methods
"""class Toys:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.dict={
            'Power'   :'Super',
            'Attitude':'Max',
            'Rich..?' :'Billinore'
        }
    def __str__(self):
        return f'{self.name}'
    def __call__(self):
        return 'I am IronMan'
    def __dir__(self):
        return 2
    def __delattr__(self):
        print('deleted!!')
    def __getattribute__(self,i):
        return self.dict[i]

action=Toys('IronMan', 2)

print(action.__str__())
print(action())
print(action.__dir__())
print(action.__delattr__())
print(action['Power'])"""

#Exercise 
"""class SuperList(list):
    def __len__(self):
        return 1000
super_list1=SuperList();

print(len(super_list1))
super_list1.append(10)
print(super_list1[0])
print(issubclass(list, object))"""

#multiple Inheritance 
"""class User():
    def sigh_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name=name
        self.power=power
    def attaack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name=name
        self.arrows=arrows
    
    def Check_Arrows(self):
        print(f'{self.arrows} remaining')
    
    def run(self):
        print('ran really fast')

class hybridbrog(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1=hybridbrog('Soham', 40, 80)
print(hb1.attaack())"""


