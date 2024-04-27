class User_Account:
    def __init__(self, email , name , phone_number):
        self.email = email
        self.name = name
        self.phone_number = phone_number

    def change_email(self, new_email):
       self.email = new_email

    def change_name(self, new_name):
       self.name = new_name

    def change_phone_number(self, new_phone_number):
       self.phone_number = new_phone_number

User_Account1 = User_Account('Boston.Morales@email.com', 'Boston Morales', +998909999999)
User_Account2 = User_Account('Cash.Luna@email.com', 'Cash Luna', +99890999899)
User_Account3 = User_Account('Skylar Cuevas@email.com', 'Skylar Cuevas', +99890999799)   
User_Account4 = User_Account('Avi Wheeler@email.com', 'Avi Wheeler', +99890999699)
User_Account5 = User_Account('Kyra Gutierrez@email.com', 'Kyra Gutierrez', +99890999599) 

                       
User_Account1.change_email('Leo.Moon@email.com')
print(User_Account1.email)

User_Account1.change_name('Leo.Moon')
print(User_Account1.name)

User_Account1.change_phone_number('+998909999777')
print(User_Account1.phone_number)