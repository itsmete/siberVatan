#lesson 5 first commit


##VARIABLES & TYPES
number1 = 14
numberr2 = "14"
number3 = 2.4
is_true = False

# print(type(number1) , type(numberr2),type(number3),type(is_true))


number4 = 5
# print(type(number4))
number4_changed = float(number4)
# print(type(number4_changed))

# print(int(is_true))


##INPUTS

# username = input('Input an username\n')
# print(f'Welcome , {username} !')

#ex

# n1 = int(input('Enter a number.. \n'))
# n2= int(input('Enter a another number.. \n'))

# result = n1+n2

# print(f'{n1} + {n2} = {result}')



def take_input():
                  global n1,n2                  
                  n1 = input('Enter a number.. \n')
                  n2 = input('Enter a another number.. \n')
                  
take_input()

try: 
                  result = int(n1)+int(n2)
                  print(f'{n1} + {n2} = {result}')
except ValueError:
        print('Enter a invalid value')
        take_input()

finally:
        print('end.')