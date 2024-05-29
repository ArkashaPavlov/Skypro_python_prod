class User:
    def __init__(self,first_name, last_name):
        self.user_first = first_name
        self.user_last = last_name
    
    def sayFirst_name(self):
        print("my first name is ", self.user_first)

    def sayLast_name(self):
        print("my last name is ", self.user_last)

    def sayFull_name(self):
        print("my full name is ", self.user_first,self.user_last)