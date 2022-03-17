#PasswordGenerator_and_Saver

#modules
import string
import random
import os
import pickle


#prog
print("\t\tGENERATE YOUR PASSWORD RIGHT AWAY")
print("\t\t---------------------------------")
print("CREDITS: SUBARNA SUTRADHAR")
print("--------------------------")
"asking info"
"""Password has min 8 letters
(4char and 4numerics and a special char)"""

"""class passwrd:
    def __init__(self,name,appname,password):
        self.nm=name
        self.apnm=appname
        self.psd=password
    def showme(self):
        print(self.apnm,' ',self.psd)"""


#--------------------------------------
def create_char(charlen):
    return random.sample(string.ascii_letters,charlen)

def create_num(numlen):
    digits=[]
    for i in range(numlen):
        digits.append(str(random.randint(0,9)))

    return digits


def create_spec(spec):
    specialchar=[]
    for i in range(spec):
        specialchar.append(random.choice("_@#$%*"))
    return specialchar
d={}
def info():
    
    file1=open(fl1,'wb')
    appname=input("\nEnter the organization name: ")
    charlen=int(input("Enter the number of character you want: "))
    numlen=int(input("Enter the number of numerics you want: "))
    spec=int(input("Enter the number of special character you want: "))
    password_values=create_char(charlen) + create_spec(spec) + create_num(numlen)

    L=list(password_values)
    a=L[0]
    L.remove(a)
    L1=[]
    c=a.upper()
    L1.append(c)
    for i in L:
        b=i.lower()
        L1.append(b)
    password=""
    for ele in L1:
        password+=ele 

    d[appname]=password
    #ii=passwrd(name,appname,password)
    pickle.dump(d,file1,pickle.HIGHEST_PROTOCOL)
    file1.close()

def addmore():
    appname=input("\nEnter the organization name: ")
    charlen=int(input("Enter the number of character you want: "))
    numlen=int(input("Enter the number of numerics you want: "))
    spec=int(input("Enter the number of special character you want: "))
    password_values=create_char(charlen) + create_spec(spec) + create_num(numlen)

    L=list(password_values)
    a=L[0]
    L.remove(a)
    L1=[]
    c=a.upper()
    L1.append(c)
    for i in L:
        b=i.lower()
        L1.append(b)
    password=""
    for ele in L1:
        password+=ele 

    d[appname]=password

ans="y"
while ans=="y":
    #viewing already created password
    name=input("Enter the name: ")
    fl1="{}.dat".format(name)
    if os.path.exists(fl1):
        file1=open(fl1,'rb')
        try:
            while True:
                i=pickle.load(file1)
                print("\nUsername: ",name)
                print("\n")
                print("The Passwords saved for this username are")
                print("-----------------------------------------")
                for ii in i:
                    print(ii," ",i[ii])

                
        except EOFError:
            pass
        d=i
        file1.close()
        ans1=input("\nWanna add more password?(y/n) ")
        if ans1=="y" or ans=="Y":
            file2=open(fl1,"wb")
            addmore()
            pickle.dump(d,file2,pickle.HIGHEST_PROTOCOL)
            file2.close()
            file3=open(fl1,"rb")
            try:
                while True:
                    i=pickle.load(file3)
                    print("\nEditted Responses Are")
                    print("---------------------")
                    for iii in i:
                        print(iii," ",i[iii])
            except EOFError:
                pass
            print("\nThanks For Using This Prog")
            break

        else:
            break
    else:
        info()
        """file1=open(fl1,'wb')
        appname=input("Enter the organization name: ")
        charlen=int(input("Enter the number of character you want: "))
        numlen=int(input("Enter the number of numerics you want: "))
        spec=int(input("Enter the number of special character you want: "))
        password_values=create_char(charlen) + create_spec(spec) + create_num(numlen)
        password=''.join(password_values)

        L=list(password_values)
        a=L[0]
        L.remove(a)
        L1=[]
        c=a.upper()
        L1.append(c)
        for i in L:
            b=i.lower()
            L1.append(b)
        password=""
        for ele in L1:
            password+=ele 

        d[appname]=password
        #ii=passwrd(name,appname,password)
        pickle.dump(d,file1,pickle.HIGHEST_PROTOCOL)
        file1.close()"""
        ans=input("Continue? ")
