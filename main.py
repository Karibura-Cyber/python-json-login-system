import os.path
import json
import base64
import time
user = ''

def screen():
    os.system("cls")
    print(' |Command|▽ \n /login //For Login\n /reg //For Register\n /exit or /q //For Exit')

def help():
    print("\nCommand:\n\nhelp or h   //For Help\nreg         //For Register\nlogin       //For Login\nexit or /q  //For Exit\ndeluser     //for delete user\n\n")
def main():
    c = input("==> ")

    if c == '/login':
        user = input("Username: ")
        if os.path.isfile('data/data_{}.json'.format(user)):
            passwd = input("Password: ")
            adpasswd_bytes = passwd.encode('ascii')
            base64_bytes = base64.b64encode(adpasswd_bytes)
            base64_adpasswd = base64_bytes.decode('ascii')
            with open('data/data_{}.json'.format(user)) as json_file:
                prog_dict = json.load(json_file)
        
            if base64_adpasswd == prog_dict["passwd"]:
                print('\nWelcome {} | Login successfully /help'.format(user))
                while True:
                    i = input("[{}@{}]==> ".format(user,user))
                    if i == '/exit' or i == '/q':
                        exit()
                    
                    if i == '/deluser':
                        user = input("Username: ")
                        if os.path.isfile('data/data_{}.json'.format(user)):
                            passwd = input("Password: ")
                            adpasswd_bytes = passwd.encode('ascii')
                            base64_bytes = base64.b64encode(adpasswd_bytes)
                            base64_adpasswd = base64_bytes.decode('ascii')
                            with open('data/data_{}.json'.format(user)) as json_file:
                                prog_dict = json.load(json_file)
                            
                            if base64_adpasswd == prog_dict["passwd"]:
                                cf = input("Are you sure? [Y/N]: ")
                                if cf == 'Y' or cf == 'y':
                                    os.remove('data/data_{}.json'.format(user))
                                    print('Delete successfully')
                                    exit()
                                else:
                                    print('Canceled')
                        else:
                                print("Please Check your password")
                                
                    elif i == '/help' or i == '/h':
                        help()
                            
                    else:
                        print("Command Not found") 
            
                           
            else:
                print("Please Check your password!!!")        
        else:
            print("Cann't found data, please check your username or Register")

    elif c == '/reg':
        user = input("Username: ")
        passwd = input("Password: ")
        adpasswd_bytes = passwd.encode('ascii')
        base64_bytes = base64.b64encode(adpasswd_bytes)
        base64_adpasswd = base64_bytes.decode('ascii')
        for i in range(1):
            name = "data_{}.json".format(user)
            with open("data/{}".format(name), "w") as outfile:
                i = {"user": user, "passwd": base64_adpasswd} 
                json.dump(i, outfile)
        print("Register Succuessfully")

    elif c == '/autologin':
        ic = input("Setting [T/F]: ")
        if ic == 't' or ic == 'T':
            user = input("Username: ")
            passwd = input("Password: ")
            cpasswd = input("Confirm your password: ")
            passwd_bytes = passwd.encode('ascii')
            base64_bytes = base64.b64encode(passwd_bytes)
            base64_passwd = base64_bytes.decode('ascii')
            
            cpasswd_bytes = cpasswd.encode('ascii')
            base64_bytes = base64.b64encode(cpasswd_bytes)
            base64_cpasswd = base64_bytes.decode('ascii')

            with open('data/data_{}.json'.format(user)) as json_file:
                    prog_dict = json.load(json_file)
            if base64_passwd == base64_cpasswd == prog_dict["passwd"]:
                with open("data/config.json".format(user), "w") as outfile:
                    i = {"autologin": True, "user": user, "passwd": base64_cpasswd} 
                    json.dump(i, outfile)    
            else:
                print("No")
        elif ic == 'f' or ic == 'F':
            user = input("Username: ")
            passwd = input("Password: ")
            cpasswd = input("Confirm your password: ")
            passwd_bytes = passwd.encode('ascii')
            base64_bytes = base64.b64encode(passwd_bytes)
            base64_passwd = base64_bytes.decode('ascii')
            
            cpasswd_bytes = cpasswd.encode('ascii')
            base64_bytes = base64.b64encode(cpasswd_bytes)
            base64_cpasswd = base64_bytes.decode('ascii')

            with open('data/data_{}.json'.format(user)) as json_file:
                    prog_dict = json.load(json_file)
            if base64_passwd == base64_cpasswd == prog_dict["passwd"]:
                with open("data/config.json".format(user), "w") as outfile:
                    i = {"autologin": False, "user": "", "passwd": ""} 
                    json.dump(i, outfile)   
    else:
        print("User not found Please check your username of register first.") 

if os.path.isfile('data/config.json'):
    screen()
    main()
else:
    with open("data/config.json", "w") as outfile:
        i = {"autologin": False} 
        json.dump(i, outfile)
        print("config file has created please run again.")









