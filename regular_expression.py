#basic of reugular 
"""import re
string = 'search inside of this text this please !'

pattern = re.compile('search inside of this text  please !')
#a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)
print(c)
print(b)
#print(a.span())
#print(a.start()) #for where the string was started
#print(a.end()) #for where the string was ended
#print(a.group())#its shows the word that we reach """


import re 


pattern = re.compile(r'search\s')
string = 'search inside this of this text please! Prasad'

print('search' in string)

a = (pattern.search(string))
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string) 

print(c)