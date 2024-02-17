##lesson 11
## file reading&writing in python and module&library operations

# open('newfile.txt','w') 



'''
'w' = write (eger dosya yoksa olusturur ,icerigi silip ekleme yapar)
'r' = read 
'a' = append
'x' = create      
'''


file = open('newfile.txt', 'w')
print(file)
file.close()


# file_dizin = open('/Users/itsmete/software/blockchain/codes/newfile.txt','w')
# file_dizin.close()
# file = open('newfile.txt','w')
# file.write('test Mete Çakır')
# file.close()
# file = open('newfile.txt','a')
# file.write('\nnnnckirrr')
# file.close()


try:
       file2 = open('newfile.txt','x')
       file2.close()

except FileExistsError:
       print('Your file is already exists!')

