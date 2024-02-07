####LOOPS


numbers = [1,2,3,4,5,6,7,8]

'''for number in numbers:
          print(number)
'''



'''for number in numbers:
                  if number % 2 == 1 :
                          print(number)
                  else:
                          continue
'''



n = 0
numberlist = []
while n <= 5:
        number = int(input('enter a number ..\n '))
        numberlist.append(number)
        n += 1

for number in numberlist:
        print(number)



