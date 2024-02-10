###FUNCTIONS###

def greets():
                  name = input('enter a name .. \n')
                  print(f'Hello ! {name}')

#greets()


def func1(city = 'karabuk'):
       print(city)


# func1()
# func1('istanbul')


def collector(number):
       return number + 5




# result = collector(5)
# print(result)              



def collector2(n1,n2):
       return n1 + n2    
                                         
# print(collector2(5,10))


def func_tuple(*args, **kwargs):
       
       for item in args:
              print(item)



func_tuple(1,2,3,4,5,6,8)