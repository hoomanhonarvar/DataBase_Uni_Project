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
def Customer_signUp():
    f_name=input("please input your first name:")
    l_name=input("please input your last_name:")
    email=input("please input your email :")
    password=input("please input your password:")

    return f_name,l_name,email,password
def Customer_info():
    f_name=input("please input your first name:")
    l_name=input("please input your last_name:")
    password=input("please input your password:")

    return f_name,l_name,password

def Customer_signIn():
    email=input("please input your email:")
    password=input("please input your password:")
    return email,password


def Customer_view():
    print("--------------------------------------------Customer----------------------------------------")
def manager_view():
    print("--------------------------------------------Manager--------------------------------------------")


def customer_menu():
    print("--------------------------------------------welcome----------------------------------------")
    print("\t16. shops")
    print("\t17. view profile")
    print("\t18. update profile")
    print("\t19. film_list")
    print("\t20. search")
    print("\t21. rent information of each film")
    print("\t22. active films of user")
    print("\t23. available films")
    print("\t24. request for film")
    print("\t25. log out")



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
user_email=''



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


            email,password=Customer_signIn()
            cmd = "SELECT * FROM customer WHERE email = %s"
            y = DB_QUERY_where(cmd, (email,))
            print(y)
            print(len(y))
            if len(y)==1:
                if(password!=y[0][6]):
                    print("wrong password")
                    x=1
                else:
                    print("you signed up with out any error!")
                    user_email=email
                    x=26


            else:
                print('you did not register . please sign up first')
                x=1

        case 6:#customer sign up
            f_name,l_name,email,pwd=Customer_signUp()
            cmd="SELECT * FROM customer WHERE email=%s"
            y=DB_QUERY_where(cmd,(email))
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
            # user, password = signUp_signIn()
            print('SK')
        case 9:
            #manager sing up
            # user, password = signUp_signIn()
            print('2')
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
        case 7|15|10|25:#to first_menu
            user_email=''
            x=0
    #customer menu
        case 26:
            customer_menu()
            x = int(input("please input your option:\t"))
            if x < 16 or x > 24:
                print("invalid input")
        case 16:#shops
            print('')

        case 17:#view profile
            cmd="SELECT * FROM customer WHERE email = %s"
            info=DB_QUERY_where(cmd,(user_email,))
            list=("id","first name","last name","email","late number","created time","password")
            for i in range(0,len(info[0])-1) :
                print(list[i],":",info[0][i])
            x = 26

        case 18:#update profile
            f_name,l_name,pwd=Customer_info()
            sql_f = "UPDATE customers SET f_name = %s WHERE address = %s"
            sql_l = "UPDATE customers SET l_name = %s WHERE address = %s"
            sql_p = "UPDATE customers SET pwd = %s WHERE address = %s"

            DB_update(sql_f,(f_name,email))
            DB_update(sql_l,(l_name,email))
            DB_update(sql_p,(pwd,email))
            print("\tupdated")
            x=26



            print('')
        case 19:#search
            print('')
        case 20:  # rent information of each film
            print('')
        case 21:  # active films of user
            print('')
        case 22:  # available films
            print('')
        case 23:  # request for film
            print('')



