##String Methods & Indexs

name = 'Mete'
surname = 'Cakir'
age = 18


test = 'METE CAKIR THE COMPANY'

user = [name,surname,age]

print(f' My name is {user[0]} {user[1]}.Im {[user[2]]} years old.')

print(test[-1:0:-1])

print(test.find('CAKIR'))

user = {
          'Name' : name,
          'Surname' : surname,
          'Age' : age
}


print(user['Name'])

print(f'My name is {user["Name"]} {user["Surname"]} .Im {user["Age"]} years old.')


text = f'My name is {name} {surname} .Im {age} years old.'


splitted_text = text.split()

age_in_text = splitted_text.index(str(age))

print(splitted_text[age_in_text])

print('.'.join(text))



print(text.startswith('M'))
print(text.startswith('C'))
print(text.endswith('k'))
print(text.endswith('.'))

replaced_text = text.replace('Mete','Cakir')
print(replaced_text)          

