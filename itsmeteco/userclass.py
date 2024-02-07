from random import *
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

        def signup(self,username_input,password_input):
                temp_user = User(id = randint(1,100),username = str(username_input),password=str(password_input))

                return temp_user
        
        def save_user_to_database(self,user : User):

                database.update({
                        user.id : {
                                'username' : user.username,
                                'password' : user.password
                        }
                })

        #with for looop
        def login(self,username,password):
                loginstatus = 0
                datalist = list(database.values())
                for  data in datalist:
                        if data['username'] == username:
                                if data['password'] == password:
                                        print('Login Succesfully')
                                        loginstatus = 1
                if loginstatus == 0 :
                        print('Not loginned') 
                

manager1 = UserManager()



manager1.save_user_to_database(manager1.signup(username_input='itsmete',password_input='corporation'))




manager1.login('mete','12345')





class userIterator:

        def __init__(self,database : dict):
                self.database = database
        

        def __iter__(self,database):

                pass
