class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.logging=True
        self.menu()

    def menu(self):
        user_input=input("""enter to the chatbook how would you like to preoceed
                         1.press 1 to signin
                         2.press 2 to signup
                         3.press 3 ro write a post
                         4.press 4 to message a friend
                         5.press any other key to exit
                         
                         """)
        if user_input=="1":
            pass
        elif user_input=='2':
            pass
        elif user_input=="3":
            pass
        elif user_input=='4':
            pass
        else:
            pass

c=chatbook()
c