from getpass import getpass
import math
from time import time,sleep
import hashlib

u_p_dict = {}
def read_file():
    global u_p_dict
    uFile_U = open("usersC.txt", "r")
    users = uFile_U.readline()
    uFile_U.close()
    uFile_P = open("passwordsC.txt", "r")
    passw = uFile_P.readline()
    uFile_P.close()

    u_1 = users.split(',')
    p_1 = passw.split(',')
    

    for u,p in zip(u_1,p_1):
        u_p_dict[u] = p


    

def check_user(userN):
    if userN == "":
        return False
    if userN in u_p_dict:
        
        return False
    else:
        
        return True


def signup():
    user_N = input("enter username: ")
    if check_user(user_N) == False:
        print("username already exists")
        return signup()    
    else:
        pass
    
    pass_w = input("enter password: ")
    conf_p = input("confirm password: ")
    
    if (check_user(user_N) == True) and (pass_w != conf_p):
        print("password is not the same as above")
        return signup()

    elif (check_user(user_N) == True) and (pass_w == conf_p):
        if len(pass_w) < 8 or ',' in pass_w:
            print("password either too short or there is an invalid character there")
            return signup()
        else:
            pass
        enc = conf_p.encode()
        hash0 = hashlib.md5(enc).hexdigest()

        with open("usersC.txt", "a") as uFile_U:
            uFile_U.write(user_N+",")
            uFile_U.close()
        with open("passwordsC.txt", "a") as uFile_P:
            uFile_P.write(hash0+",")
            uFile_P.close()

        print("registration successful")
        return
    else:
        print("unexpected error")
        return signup()


def login():
    userName = input("enter username: ")
    passWord = input("enter password: ")
    read_file()
    if userName not in u_p_dict():
        return login()

    else:
        for i,j in u_p_dict.items():
            if userName == i and passWord == j:
                return True
            else:
                continue
                


if __name__ == '__main__':#main "method"
    read_file()
    signup()
    
