###LESSON 15
##SUBCLASSES

from typing import Any


class Person():
       def __init__(self,name,surname,birthdate,address = 'null'):
              self.name = name
              self.surname = surname
              self.address = address
              self.birthdate = birthdate


       def who_am_i(self):
              print('Im a Person')

class Teacher(Person):
       def __init__(self, name, surname,birthdate, branch, address='null' ):
              super().__init__(name, surname, address,birthdate)
              self.branch = branch

       def who_am_i(self):
              print('Im a Teacher')


class Student(Person):

       def __init__(self, name, surname, birthdate, sinif, number, address='null'):
              super().__init__(name, surname, birthdate, address)
              self.sinif = sinif
              self.number = number

       def who_am_i(self):
              return super().who_am_i()



# p1 = Person('mete','cakit','26/09/2006','karabuk')

# s1 = Student('Mete','Cakir','23423','12/c','280')

# p1.who_am_i()

# s1.who_am_i()



class OperationManager():
       
       def __init__(self,number1,number2):
              self.number1 = number1
              self.number2 = number2
              self.islem = None
       

       def hesapla(self):
              pass



class Toplama(OperationManager):

       def __init__(self, number1, number2):
              super().__init__(number1, number2)


       def hesapla(self):
              return self.number1 + self.number2


class Cikarma(OperationManager):
       
       def __init__(self, number1, number2):
              super().__init__(number1, number2)

       def hesapla(self):
              return self.number1 - self.number2
       
class Carpma(OperationManager):

       def __init__(self, number1, number2):
              super().__init__(number1, number2)

       def hesapla(self):
              return self.number1 * self.number2
       
class Bolme(OperationManager):
       def __init__(self, number1, number2):
              super().__init__(number1, number2)
       
       def hesapla(self):
              return self.number1 / self.number2
       


res = Carpma(10,5).hesapla()
print(res)


