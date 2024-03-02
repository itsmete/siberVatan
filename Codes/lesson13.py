

'''
sayiListesi = [233,777,45,99999999,81,36,90,88,11,61]

def sayiKontrol(sayiListesi : list):

       equalnumbers = []

       for number in sayiListesi:
              
              noset = set()
              number_str = str(number)

              for n in number_str:
                     noset.add(n)
              
              if len(noset) == 1:
                     equalnumbers.append(number)
       


       return equalnumbers



res = sayiKontrol(sayiListesi)
print(res)
'''


#CLASSES



class User():

       address = 'null'
       def __init__(self,name,surname,address = address):
              self.name = name
              self.surname = surname
              self.address = address

       def greet(self):
              return f'hello my name is {self.name} {self.surname}, my address is {self.address}'
       


id1 = User('Mete','Cakir')


# print(f'{id1.name} {id1.surname} {id1.address}')


id2 = User(name='Alparslan', surname='Cakir', address = '123456')

print(id2.greet())

