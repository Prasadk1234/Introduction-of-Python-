#error Handling 
"""while True:
 try:
  age= int(input('what is your age'))
  print(age)
  10/age
  raise ValueError('hey cut it out')
 except ValueError:
    print('Please enter a number')
    continue

 except ZeroDivisionError:
    print('Please enter a age greater then 0')
    break
 else:
    break
 finally:
    print('Ok, finally done')
 print('Can you hear me?')"""
    
"""def sum(num1, num2):
    try:
     return num1+num2
    except (TypeError, ZeroDivisionError)as err:
        print(err)
print(sum('1',2))"""

