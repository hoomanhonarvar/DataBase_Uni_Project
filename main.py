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
def manager_menu():
    print("--------------------------------------------welcome----------------------------------------")
    print("\t28. customers info")
    print("\t29. film rental info")
    print("\t30. active rental")
    print("\t31. check requests")
    print("\t32. start or end rental")
    print("\t33. view store info")
    print("\t34. update store info")
    print("\t35. film_list")
    print("\t36. search")
    print("\t37. payments info")
    print("\t38. most sell")
    print("\t39. log out")


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


def DB_Insert(command,val):
    # try:
        dbCursor.execute(command,val)
        mydb.commit()
        print(dbCursor.rowcount, "record inserted.")
    # except:
    #     print("an error has occurred")
def DB_QUERY(command):
    # try:
        dbCursor.execute(command)
        myresult = dbCursor.fetchall()
        # print("ok!")
        return myresult
    # except:
        print("an error has occurred")
        return None;
def DB_QUERY_where(command,where):
    # try:
        dbCursor.execute(command,where)
        myresult = dbCursor.fetchall()
        # print("ok!")
        return myresult
    # except:
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
user_id=0


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
                    x=26            #manager menu


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
            email,password=Customer_signIn()
            cmd = "SELECT * FROM manager WHERE email = %s"
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
                    user_id=y[0][0]
                    x=26
            else:
                print('you did not register . please sign up first')
                x=1




            print('SK')
        case 9:
            #manager sing up
            # user, password = signUp_signIn()
            f_name, l_name, email, pwd = Customer_signUp()
            username=input("\tenter your username:")
            store_1=input("\tenter your store id1  (0 for nothing:")
            store_2=input("\tenter your store id2  (0 for nothing):")

            cmd = "SELECT * FROM manager WHERE email=%s"
            y = DB_QUERY_where(cmd, (email,))
            if y != None:
                now = datetime.now()
                # sign_up
                command = "INSERT INTO manager (first_name, last_name,email,username,password,store_1,store_2) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val = (f_name, l_name, email, username, pwd,store_1,store_2)
                DB_Insert(command, val)
                x = 1  # go to customer menu
            else:
                print("this email has registered by another user!")
                x = 1

            print('2')
        case 11:
            #add store
            name=input("\tinput your store name:")


                # try:
            cmd = " INSERT INTO store(name)VALUES( %s)"
            y = DB_Insert(cmd, (name,))
            x=0
        case 12:
            #add film to a store
            film=int(input("enter the film id"))
            number=int(input("enter the number of film "))
            store=int(input("enter the store id "))
            cmd="INSERT INTO inventory(store_id,film_id,number)VALUES( %s,%s,%s)"

            DB_Insert(cmd,(store,film,number))

        case 13:
            #delete store
            print("fuck")
            id=input("\tinput your store id:")
            cmd="DELETE from store where store_id=%s"
            DB_delete(cmd,id)
            print("deleted!")


        case 14:
            #delete films from store

            film = int(input("enter the film id"))
            store = int(input("enter the store id "))
            cmd = "DELETE FROM inventory(store_id,film_id) where film_id=%s and store_id=%s"
            DB_delete(cmd, (store, film))

        case 7|15|10|25|39:#to first_menu
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
            sql_f = "UPDATE customers SET f_name = %s WHERE email = %s"
            sql_l = "UPDATE customers SET l_name = %s WHERE email = %s"
            sql_p = "UPDATE customers SET pwd = %s WHERE email = %s"

            DB_update(sql_f,(f_name,email))
            DB_update(sql_l,(l_name,email))
            DB_update(sql_p,(pwd,email))
            print("\tupdated")
            x=26

        case 19:  # film_list
            film_id = []
            cmd1="select * from category"
            categ_name_list=DB_QUERY(cmd1)
            cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category "
            film_list = DB_QUERY(cmd)
            for i in categ_name_list:
                cmd2 = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category where category_id=%s"
                film_categ_list=DB_QUERY_where(cmd2,(i[0],))
                for j in film_categ_list :
                    print(i[1] ,":",j[2])




            x=26
        case 20:#search

            print('search by actor,gener,title,language,released_year')
            search=input("enter search field:")
            match search:
                case "actor":
                    first_name=input("please input the actor's first_name:")
                    last_name=input("please input the actor's last_name:")

                    cmd = "select * from (film inner join film_actor on film.film_id=film_actor.film_id)natural join actor where first_name=%s and last_name=%s"
                    answer = DB_QUERY_where(cmd, (first_name,last_name))
                    print(answer)
                    # query
                    cmd="select * from film where "
                case "gener":
                    gener=input("please input the category:")
                    cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category where name=%s"
                    answer = DB_QUERY_where(cmd, (gener,))
                    print(answer)
                case "title":
                    title = input("please input the name:")
                    cmd = "select * from film where title=%s"
                    answer = DB_QUERY_where(cmd, (title,))
                    print(answer)
                case "language":
                    language = input("please input the language:")
                case "released_year":
                    released_year=input("please input the released_year:")
                    cmd="select * from film where release_year=%s"
                    answer=DB_QUERY_where(cmd,(released_year,))
                    print(answer)
                case "_":
                    print("invalid input")
                    exit=input("exit? yes/no:")
                    match exit:
                        case "yes":
                            x=26
                        case "no":
                            x=20
                        case "_":
                            x=26

        case 21:  # rent information of each film
            print('')
        case 22:  # active films of user
            print('')
        case 23:  # available films
            print('')
        case 24:  # request for film
            print('')

        case 27:# manager menu
            manager_menu()
            x = int(input("please input your option:\t"))
            if x < 27 or x > 39:
                print("invalid input")
        case 28:#customers info
            cmd="select * from customer where customer_id in( select customer_id from rental inner join manager on rental.manager_id=%s)"
            customer_list=DB_QUERY_where(cmd,(user_id,))
            for i in customer_list:
                print (i)
            x=27
        case 29:#next
            #film rental info
            cmd = "select * from rental "
            rentalFilm_list = DB_QUERY(cmd)
            for i in rentalFilm_list:
                print(i)
            x=27
        case 30:#active rental
            cmd1="select store_1,store_2 from managre where manager_id=%s"
            store_id=DB_QUERY_where(cmd1,(user_id,))
            cmd = "select * from rental  where return_date='' and request_accepted=1 and store_id in %s"
            activeFilm_list = DB_QUERY_where(cmd,(cmd1[0]))
            for i in activeFilm_list:
                print(i)
            x = 27
        case 31:    #check requests
            cmd = "select * from rental  where request_accepted=0"
            notReturned_rentalFilm_list = DB_QUERY_where(cmd, (user_id,))
            for i in notReturned_rentalFilm_list:
                print(i)
            x = 27
        case 32:#start or end rental
            print('')
            cmd1 = "select store_1,store_2 from managre where manager_id=%s "
            store_id = DB_QUERY_where(cmd1, (user_id,))

            start_end=input("enter the action : start / end:")
            if start_end=="start":
                query="select number from "




                rental_id=int(input("\t enter the rental request id"))
                manager = "UPDATE rental SET manager_id = %s WHERE rental_id = %s"
                accept = "UPDATE rental SET request_accepted = %s WHERE rental_id = %s"
                date = "UPDATE rental SET return_date = %s WHERE rental_id = %s"
                DB_update(manager, (user_id, rental_id))
                DB_update(accept, (1, rental_id))
                DB_update(date, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rental_id))
            else:
                rental_id = int(input("\t enter the rental request id"))
                date = "UPDATE rental SET rental_start_date = %s WHERE rental_id = %s"
                DB_update(date, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rental_id))
            print("done!")
            x=27

        case 33:
            cmd1 = "select store_1,store_2 from managre where manager_id=%s"
            store_id = DB_QUERY_where(cmd1, (user_id,))
            cmd = "select * from store  where  store_id in %s"
            stores = DB_QUERY_where(cmd, (store_id[0]))

            for i in stores[0]:
                print(i)
        case 34:#next
            store_id=int(input("\t enter store_id"))
            print('nothing to change I am sorry maby be fixed')
        case 35:
            film_id = []
            cmd1 = "select * from category"
            categ_name_list = DB_QUERY(cmd1)
            cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category "
            film_list = DB_QUERY(cmd)
            for i in categ_name_list:
                cmd2 = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category where category_id=%s"
                film_categ_list = DB_QUERY_where(cmd2, (i[0],))
                for j in film_categ_list:
                    print(i[1], ":", j[2])

            x=27

        case 36:
            print('search by actor,gener,title,language,released_year')
            search = input("enter search field:")
            match search:
                case "actor":
                    first_name = input("please input the actor's first_name:")
                    last_name = input("please input the actor's last_name:")

                    cmd = "select * from (film inner join film_actor on film.film_id=film_actor.film_id)natural join actor where first_name=%s and last_name=%s"
                    answer = DB_QUERY_where(cmd, (first_name, last_name))
                    print(answer)
                    # query
                    cmd = "select * from film where "
                case "gener":
                    gener = input("please input the category:")
                    cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category where name=%s"
                    answer = DB_QUERY_where(cmd, (gener,))
                    print(answer)
                case "title":
                    title = input("please input the name:")
                    cmd = "select * from film where title=%s"
                    answer = DB_QUERY_where(cmd, (title,))
                    print(answer)
                case "language":
                    language = input("please input the language:")
                case "released_year":
                    released_year = input("please input the released_year:")
                    cmd = "select * from film where release_year=%s"
                    answer = DB_QUERY_where(cmd, (released_year,))
                    print(answer)
                case "_":
                    print("invalid input")
                    exit = input("exit? yes/no:")
                    match exit:
                        case "yes":
                            x = 27
                        case "no":
                            x = 36
                        case "_":
                            x = 27
        case 37:
            print("\t1.rentals in store")
            print("\t2.rentals base on customer")
            print("\t3.rentals base film")
            print("\t4.exit")
            option=int(input("\t choose option:"))
            match option:
                case 1:

                    store_id = DB_QUERY_where("select store_1,store_2 where manager_id=%s",(user_id,))
                    print(store_id)
                    flag=False


                    if flag:
                        cmd="select * from rental natural join payment where store_id=%s"
                        output=DB_QUERY_where(cmd,(store_id,))
                        print(output)

                case 2:
                    store_id = DB_QUERY_where("select store_1,store_2 where manager_id=%s", (user_id,))

                    print(store_id)


                    customer=int(input("\tenter your customer id:"))
                    cmd = "select * from rental natural join payment where store_id=%s and customer_id"
                    output = DB_QUERY_where(cmd, (store_id,customer))
                    print(output)

                case 3:
                    film_id=int(input("\t enter film_id"))
                    cmd = "select * from rental natural join payment where film_id=%s"
                    output = DB_QUERY_where(cmd, (film_id,))
                    print(output)
                case 4:


                    x=27

        case 38:#next
            print("\t1.The most sell in category")
            print("\t2.The most sell base on film")
            print("\t3.The most sell base actor")
            print("\t4.exit")
            option = int(input("\t choose option:"))

            match option:
                case 1:
                    print('')
                case 2:
                    cmd="select * from rental where "
                    print('')
                case 3:
                    print('')
                case 4:
                    x=27