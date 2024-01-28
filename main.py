import os
import mysql.connector
from dotenv import load_dotenv
from datetime import  datetime

#db setting

load_dotenv()
mydb=mysql.connector.connect(
    host=os.environ['host'],
    user=os.environ['user'],
    password=os.environ['password'],
    database=os.environ['database'],
    auth_plugin='mysql_native_password'


)
dbCursor=mydb.cursor()






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
def Customer_signIn():
    f_name=input("please input your first name:")
    l_name=input("please input your last_name:")
    email=input("please input your email :")
    password=input("please input your password:")

    return f_name,l_name,email,password

def signUp_signIn():
    username=input("please input your username")
    password=input("please input your password")
    return username,password


def Customer_view():
    print("--------------------------------------------Customer----------------------------------------")
def manager_view():
    print("--------------------------------------------Manager--------------------------------------------")

def DB_Insert(command,val):
    # try:
        dbCursor.execute(command,val)
        mydb.commit()
        print(dbCursor.rowcount, "record inserted.")
    # except:
    #     print("an error has occurred")
def DB_QUERY(command):
    try:
        dbCursor.execute(command)
        myresult = dbCursor.fetchall()
        print("ok!")
        return myresult
    except:
        print("an error has occurred")
        return None;
def DB_QUERY_where(command,where):
    try:
        dbCursor.execute(command,where)
        myresult = dbCursor.fetchall()
        print("ok!")
        return myresult
    except:
        print("an error has occurred")
        return None;
def DB_delete(command,where):
    try:
        # sql = "DELETE FROM customers WHERE address = %s"
        # adr = ("Yellow Garden 2",)

        dbCursor.execute(command, where)

        mydb.commit()

        print(dbCursor.rowcount, "record(s) deleted")
    except:
        print("an error has occurred")
def DB_drop(command):
    try:
        dbCursor.execute(command)
        print("ok")
    except:
        print("an error has occurred")
def DB_update(sql,val):
    try:
        # sql = "UPDATE customers SET address = %s WHERE address = %s"
        # val = ("Valley 345", "Canyon 123")

        dbCursor.execute(sql, val)

        mydb.commit()

        print(dbCursor.rowcount, "record(s) affected")

    except:
        print("an error has occurred")






def DB_SIGN_IN(val):
    SQL="INSERT INTO customer (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    dbCursor.execute(SQL,val)
    mydb.commit()
    print(dbCursor.rowcount, "record inserted.")




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
            # user, password = custo()
            f_name,l_name,email,pwd=Customer_signIn()
            cmd="SELECT * FROM customer WHERE email=s"
            y=DB_QUERY_where(cmd,(email,))
            if y!=None:
                now = datetime.now()
                #sign_up
                command="INSERT INTO customer (first_name, last_name,email,number_of_late,create_date,password) VALUES (%s, %s,%s,%s,%s,%s)"
                val=(f_name,l_name,email,0,now.strftime('%Y-%m-%d %H:%M:%S'),pwd)
                DB_Insert(command,val)
                x=1         #go to customer menu
            else:
                print("this email has registered by another user!")
                x=1


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


