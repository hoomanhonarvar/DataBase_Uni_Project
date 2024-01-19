import os
import mysql.connector
from dotenv import load_dotenv

def first_menu():
    print("---------------------------------------------------welcom----------------------------------------------------")
    print("\t1.customer")
    print("\t2.manager")
    print("\t3.settings")
    print("\t4.exit")

def Customer_signIn_signUp_Menu():
    print("----------------------------------------------Customer_signIn_signUp menu---------------------------------------------------")
    print("\t5.sign in")
    print("\t6.sign up")
    print("\t7.exit")
def Manager_signIn_signUp_Menu():
    print("----------------------------------------------Manager_signIn_signUp menu---------------------------------------------------")
    print("\t8.sign in")
    print("\t9.sign up")
    print("\t10.exit")

def setting():
    print("----------------------------------------------------------setting---------------------------------------------------")
    print("\t11.add a store")
    print("\t12.add films to store inventory")
    print("\t13.delete a store")
    print("\t14.delete films from store inventory")
    print("\t15.exit")

def get_inputList():
    inputList=input("input your list (insert between each entity a comma ',') :")
    inputList=list(inputList)
    final_list=[]
    for i in inputList:
        if i!=',':
            final_list.append(i)
    return final_list
def signUp_signIn():
    username=input("please input your username")
    password=input("please input your password")
    return username,password


def Customer_view():
    print("--------------------------------------------Customer----------------------------------------")
def manager_view():
    print("--------------------------------------------Manager--------------------------------------------")




load_dotenv()
mydb=mysql.connector.connect(
    host=os.environ['host'],
    user=os.environ['user'],
    password=os.environ['password'],
    database=os.environ['database'],
    auth_plugin='mysql_native_password'


)
# command="""
# """
#
#
# with mydb.cursor() as cursor:
#     cursor.execute(command)
#     mydb.commit()
x=0

while(x>=0):
    match x:
        case 0:
            first_menu()
            x = int(input("please input your option:\t"))
        case 1:
            Customer_signIn_signUp_Menu()
            x = int(input("please input your option:\t"))
        case 2:
            Manager_signIn_signUp_Menu()
            x = int(input("please input your option:\t"))
        case 3:
            setting()
            x = int(input("please input your option:\t"))
        case 4:#exit
            x=-1
            print("Thank you for your patience")
        case 5:#customer sign in
            user,password=signUp_signIn()
        case 6:#customer sign up
            user, password = signUp_signIn()
        case 8:
            #manager sign in
            user, password = signUp_signIn()
        case 9:
            #manager sing up
            user, password = signUp_signIn()
        case 11:
            #add store
            print("fuck")
        case 12:
            #add film to a store
            storeId_list=get_inputList()
        case 13:
            #delete store
            print("fuck")
        case 14:
            #delete films from store
            storeId_list=get_inputList()
        case 7|15|10:#to first_menu
            x=0


