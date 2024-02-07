
'''a,b,c,d = 50,100,50,75

print(a<b)
print(a==b)
print(a!=b)
print(a>b)
print(a<=b)
print(a>=b)


username1 = "mete"
username2 = "alparslan"


result =  username1 == "mete"
print(result)
result =  username2 == "mete"
print(result)



username_input = str(input('Enter a username..\n'))

username1 = 'mete'
username2 = 'alparslan'



try: 
        usernames.index(username_input)
        print('username matched')
except ValueError:
        print("User is not in the list")




res1 = (username1 == username_input)
res2 = (username2 == username_input)

result = (res1 | res2)
print(result)
'''

'''
database = {
        "user1": 
                {
                'username':'itsmete',
                'email':'itsmete@itsmete.com',
                "password":"12345"
                },
        "user2":
        {
                'username':'alparslan',
                'email':'apo@email.com',
                'password':'6789'
        }
}'''


'''email_input = str(input('Enter a email..\n')).lower()


check1 = (email_input == database['user1']['email'])
check2 = (email_input == database['user2']['email'])

result =  ( check1 | check2 )

emailsplitted = email_input[:email_input.index('@')]

print(f'your login status is : {result}  {emailsplitted}')

'''

#email_input = str(input('Enter a email ...\n'))
#password_input = str(input('Enter a password ...\n'))

'''
database = {
        1 : {
                'username' : 'mete',
                'password' : '12345'
        }
}

class User:
        def __init__(self,id,username,password):
                self.id = id
                self.username=username
                self.password = password
        


class UserManager:

        def signup(username,password):
                user_temporate = User(id = random() , username= username, password=password)

                database.update({
                        user_temporate.id :{
                                'username': user_temporate.username,
                                'password' : user_temporate.password
                        }
                })


        def login(self,username):
                if  username in database and database[username]['password'] == password:
                        return "Logged In" + username'''
                  

'''numbers = [1,2,3,4,5]
        
if 5 in numbers:
        print('sd')

manager1 = UserManager()
#print(manager1.signup("admin","123"))

print(database)





vize = int(input('vize notu girin'))
final = int(input('final notu girin'))

print((vize*0.4) + (final*0.6) >50 )


number = int(input('enter a number'))

result =  number > 0 and number%2 ==0
print(reselt)
'''
'''


database = {
        1 : {
                'username' : 'mete',
                'password' : '12345'
        },

        2 : {
                'username' : 'alparslan',
                'password' : '7890'
        }
}


class User:
        def __init__(self,id,username,password) -> None:
                self.id = id
                self.username = username
                self.password = password



class UserManager:

        
        
        def signup(self,username_input : str , password_input : str):
                user_temp = User(id = randint(1,100),username=username_input,password=password_input)

                database.update({
                        user_temp.id : {
                                'username' : user_temp.username,
                                'password' : user_temp.password
                        }
                })

                return user_temp


        
'''
#manager1 = UserManager()

'''
manager1.signup(username_input='itsmete',password_input='sfdfsdsf')
print(database)'''

#print(database.values())
#print(manager1.login(usernameinput='mete'))





'''
veri = {
        'mete' : '12345',
        'alparslan' : '67890'
}



usernameinput = str(input('enter a username '))
passwordinput = str(input('enter a password '))


if usernameinput in veri:
        if veri[usernameinput] ==  passwordinput:
                print('giris basarili')
        else:
                print('hatalı şifre')
else:
        print('kullanıcı adi eslesmedi')





islem = int(input('İslem girininzi \n1-Toplama\n2-Cikarma\n3-Carpma\n4-Bolme\n'))
sayi1 = int(input('1.sayiyi giriniz .. \n'))
sayi2 = int(input('2.sayiyi giriniz .. \n'))


if islem == 1:
        result = sayi1 + sayi2
elif islem == 2:
        result = sayi1 - sayi2
elif islem == 3:
        result = sayi1 * sayi2
elif islem == 4:
        result = sayi1 / sayi2

print(result)
'''


