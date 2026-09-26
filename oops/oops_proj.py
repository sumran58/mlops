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
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=='4':
            pass
        else:
            pass

    def signup(self):
        email=input("enter your email here ->")
        pwd=input("enter your password here ->")
        self.username=email
        self.password=pwd
        print("you have successfully signed up !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by  pressing 1 ")
        else:
            uname=input("enter your email->")
            pwd=input("enter your pasword")
            if uname==self.username and pwd==self.password:
                print("you have signedin successfully !!")
            else:
                print("enter the correct credentials")
        print("\n")
        self.menu()

c=chatbook()
c