from getpass import getpass
import math
from time import time,sleep
import hashlib


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
    u_p_dict = {}

    for u,p in zip(u_1,p_1):
        u_p_dict[u] = p

    print(f"{u_p_dict}")
    #start





def check_user(userN,passW):
    pass


def signUp():
    user_N = input("enter username: ")
    pass_w = getpass("enter password: ")
    conf_p = getpass("confirm password: ")

    if pass_w == conf_p:
        enc = conf_p.encode()
        hash0 = hashlib.md5(enc).hexdigest()
        print(hash0)

        with open("usersC.txt", "w") as uFile_U:
            uFile_U.write(user_N+"\n")
            uFile_U.close()
        with open("passwordsC.txt", "w") as uFile_P:
            uFile_P.write(hash0+"\n")
            uFile_P.close()

        print("registration successful")

    else:
        print("password is not the same as above")


if __name__ == '__main__':#main "method"
    read_file()
