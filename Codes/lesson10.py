###LESSON 10

#recursive (öz yinemeli) fonksiypn : fonksiyon kendi icimnde kendini cagirabiliyorsa  "recursive" denir.
import re
import x


def factorial(x): #factorial of a number x
          if x == 0:   
                  return 1
          else:        
                    x * factorial(x-1)



#try- except

try:
        factorial(-10)
except Exception as error:
        print(f'Program has a {error} error')


try:
        x = int(input('enter number '))
        y = int(input('enter number '))
        print(x/Y)
except ValueError:
        print('yanlis deger girili')
except ZeroDivisionError:
        print('bir sayi 0a bolunmez')
except SyntaxError:
        print('Yazim yanlisi var')
except NameError:
        print('global olarak bu veri bulunamadi')
except Exception as err:
        print(f'Programda {err} hatası var')





def password_control(password):

        if len(password)<8:
                raise Exception(f"Password must be at least 8 characters")
        
        if not re.search(["[A-Z] [a-z] "], password):
                raise Exception('Passwrord must be contains [a-z] & [A-Z]')
        elif not any (char.isdigit() for char in password):
                raise Exception("Password must contain a digit")
        else:
                return 'password created succesfully'
        

