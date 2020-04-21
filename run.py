#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(username,password):
    """
    Function for creating new user accounts
    """
    new_user=User(username,password)
    return new_user

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def finding_user(username):
    return User.find_by_username(username)

def check_user_exists(user):
    user.check_user_exists()
def confirm_user(userName,passwrd):
    return User.confirm_user(userName,passwrd)

def sign_in_user(userName,passwrd):
    return User.confirm_user(userName,passwrd)

def confirm_new(username):
    return User.confirm_new(username)

def  create_app_credential(app_name,app_username,app_email,app_password):
    new_app_credential=Credential(app_name,app_username,app_email,app_password)
    return new_app_credential

def save_app_credential(credential):
    credential.savecredentials()

def delete_app_credential(credential):
    credential.delete_app_credential()

def search_App_credential(app_name):
    return Credential.find_by_appname(app_name)

def search_App_credentials(app_Name):
    return Credential.search_app_credentials(app_Name)

def display_all_apps():
    return Credential.display_all_apps()

def controls():
    print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : na - Add a new appcredential, dc-Display all credential, search - find a profile, del - delete a profile, logout- logout of session, ex - exit the application")
    print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
    short_code=input()
    return (short_code)
    
def main():
    print("WELCOME TO PASSWORD LOCKER")
    while True:
        print ("DO you have  an account? Y/N")
        acc=input().upper()
        if acc =="Y":
            print ("enter Username:")
            existing_acc=input()
            print("Enter Password:")
            existing_pass=input()
            login=confirm_user(existing_acc,existing_pass)
            if login==False:
                print("No credentials inserted" )
                return main() 
            else:
                while True:
                    return controls()
        elif acc =="N":
            print("ENter Your  username")
            new_username=input()
            print("Enter your desired password")
            new_password=input()
            new_user= confirm_new(new_username)
            # check if user exists
            if new_user== True:
                print("User ALready exists!!!!!")
                return main

            else:#succesful login and saving the new user
                while True:
                    # new_user_credentials=(new_username,new_password)
                    # ********************UNABLE TO SAVE USER!!!!1
                    print("Account succefully created")
                    return acc_functions()
                    
    
def acc_functions():
    
    while True:
        print("\033[1m PROFILE CONTROLS:- "+'\033[0m'+"Use these short codes : na - Add a new appcredential, dc-Display all credential, search - find a profile, del - delete a profile, logout- logout of session, ex - exit the application")
        print("\033[1m ACCOUNT CONTROLS:- "+'\033[0m'+"Use these short codes : acp - Change your account password, delete - Delete your account")
        short_code=input()
        if short_code=="na":
            print("Fill the neccessary fields below to create a new app_credential;")
            print("nb--Fill all spaces with asterics")
            print("ENTER APPNAME/SITENAME**....eg:Instagram")
            new_App_Name_Entered=input()

            check_new_app_name=search_App_credential(new_App_Name_Entered)
        
            print("ENTER USERNAME FOR THE APP")
            new_App_username_Entered=input()
            print("ENTER EMAIL USED FOR THE APP")
            new_App_Email_Entered=input()
            print("Enter PASSWORD USED FOR THE APP")
            new_App_password_Entered=input()

            save_app_credential(create_app_credential(new_App_Name_Entered,new_App_username_Entered,new_App_Email_Entered,new_App_password_Entered))
            print ('\n')
            print(f"New Credential for {new_App_Name_Entered} created")
            print ('\n')
        elif expression:
            pass
        # all_Details=(new_App_Name_Entered,new_App_username_Entered,new_App_Email_Entered,new_App_password_Entered)
        # checking for existing 
        # if check_new_app_name ==search_App_credential(check_new_app_name):
        #     print("This app credentials already exists!")
        #     return short_code=="na"
        # else:
        #     while False:
        #         print(f"Credentials for {new_App_Name_Entered} were succefully stored")   
        #         return acc_functions()
        # if check_new_app_name ==search_App_credential(check_new_app_name):
        #     print("This app credentials already exists!")
        #     return short_code=="na"
        # else:
        #     while False:
        #         print(f"Credentials for {new_App_Name_Entered} were succefully stored")   
        #         return acc_functions()
                 
if __name__=='__main__':
    main()
