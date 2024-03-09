
# numbers = []
# while True:
#        kalan = 10 - len(numbers)
#        number = int(input(f'Enter a number  (Remaining : {kalan}) : '))
#        numbers.append(number)
#        if len(numbers) == 10:
#               break

# print(numbers)

# sorted_list =  sorted(numbers)

# maximum = max(sorted_list)
# minimum = min(sorted_list)

# print(maximum,minimum)

##floyds triangle



# row_count = int(input('Enter a row for Floyds Triangle ...'))


# no = 1
# for i in range(1,row_count+1):

#        for j in range(1,i+1):
#               print(no, end = '  ')
#               no += 1
       
#        print()


#fibonacci

n = int(input('Enter a number for Fibionacci ...'))

for i in range(1,n+1):


       number = (i-1) + (i-2)
       print(number)