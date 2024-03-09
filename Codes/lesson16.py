#lesson16
import os
path = os.getcwdb()
path = '/Users/itsmete/software/blockchain/Codes'
print(path)

directionlist = os.listdir()


for i in directionlist:
       print(i)


try:
       os.mkdir('NewFolder')
       print('Folder succesfully created.')
except FileExistsError:
       print('Folder is aldready exists')

newpath = os.path.join(path , 'NewFolder')
newpathfile = os.path.join(newpath , 'newfile.txt')

with open(newpathfile,'w') as f:
       f.write('hello world')


os.remove(newpathfile)
os.remove(newpath)