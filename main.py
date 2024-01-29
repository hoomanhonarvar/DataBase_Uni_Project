import os
import mysql.connector
from dateutil import relativedelta
from dotenv import load_dotenv
from datetime import  date,datetime,timedelta

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
    print("\t23. request for film")
    print("\t24. rating a film ")
    print("\t240.registering to being customer of store")
    print("\t241.payment information")
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
            if len(y)==1:
                if(password!=y[0][6]):
                    print("wrong password")
                    x=1
                else:
                    print("you signed up with out any error!")
                    user_email=email
                    user_id=y[0][0]
                    x=26            #customer menu


            else:
                print('you did not register . please sign up first')
                x=1

        case 6:#customer sign up
            f_name,l_name,email,pwd=Customer_signUp()
            cmd="SELECT * FROM customer WHERE email=%s"
            y=DB_QUERY_where(cmd,(email,))
            if len(y)==0:
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
            if len(y)==1:
                if(password!=y[0][5]):
                    print("wrong password")
                    x=2
                else:
                    print("you signed up with out any error!")
                    user_email=email
                    user_id=y[0][0]
                    x=27
            else:
                print('you did not register . please sign up first')
                x=2
        case 9:
            #manager sing up
            # user, password = signUp_signIn()
            f_name, l_name, email, pwd = Customer_signUp()
            username=input("\tenter your username:")
            store_1=input("\tenter your store id1  (0 for nothing):")
            store_2=input("\tenter your store id2  (0 for nothing):")

            cmd = "SELECT * FROM manager WHERE email=%s"
            y = DB_QUERY_where(cmd, (email,))
            if len(y) == 0:
                now = datetime.now()
                # sign_up
                command = "INSERT INTO manager (first_name, last_name,email,username,password,store_1,store_2) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val = (f_name, l_name, email, username, pwd,store_1,store_2)
                DB_Insert(command, val)
                x =2   # go to manager menu
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
            x=7
        case 13:
            #delete store
            print("fuck")
            id=input("\tinput your store id:")
            cmd="DELETE from store where store_id=%s"
            DB_delete(cmd,id)
            print("deleted!")
            x=7

        case 14:
            #delete films from store

            film = int(input("enter the film id"))
            store = int(input("enter the store id "))
            cmd = "DELETE FROM inventory(store_id,film_id) where film_id=%s and store_id=%s"
            DB_delete(cmd, (store, film))
            x=7

        case 7|15|10|25|39:#to first_menu
            user_email=''
            user_id=0
            x=0
    #customer menu
        case 26:
            customer_menu()
            x = int(input("please input your option:\t"))
            if x < 16 or x > 25 or x!=241 or x!=240:
                print("invalid input")
        case 16:#shops              #next
            cmd="select store.store_id,name from store inner join store_customer on store.store_id=store_customer.store_id where customer_id=%s"
            query=DB_QUERY_where(cmd,(user_id,))
            if len(query)!=0:
                for i in query:
                    print(i)
            else:
                print("nothing to show")
            x=26

        case 17:#view profile
            cmd="SELECT * FROM customer WHERE email = %s"
            info=DB_QUERY_where(cmd,(user_email,))
            list=("id","first name","last name","email","late number","created time","password")
            for i in range(0,len(info[0])) :
                print(list[i],":",info[0][i])
            x = 26

        case 18:#update profile
            f_name,l_name,pwd=Customer_info()
            sql_f = "UPDATE customer SET first_name = %s WHERE email = %s"
            sql_l = "UPDATE customer SET last_name = %s WHERE email = %s"
            sql_p = "UPDATE customer SET password = %s WHERE email = %s"

            DB_update(sql_f,(f_name,email))
            DB_update(sql_l,(l_name,email))
            DB_update(sql_p,(pwd,email))
            print("\tupdated")
            x=26

        case 19:  # film_list
            store_id=int(input("input the store that you want to see it's films:"))
            film_id = []
            cmd1="select * from category"
            categ_name_list=DB_QUERY(cmd1)
            cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category "
            film_list = DB_QUERY(cmd)
            for i in categ_name_list:
                cmd2 = "select * from (film as F inner join film_category as FC on F.film_id=FC.film_id)natural join category where category_id=%s and F.film_id in(select i.film_id from inventory as i where store_id=%s) "
                film_categ_list=DB_QUERY_where(cmd2,(i[0],store_id))
                for j in film_categ_list :
                    print(i[1] ,":",j[2]," and film_id = ",j[0])


            cmd="select film.film_id,title,rate,description from film inner join rental on film.film_id=rental.film_id where rate=(select max(rate)from rental) "
            print("-------------------most rated-------------------------")
            most_rated=DB_QUERY(cmd)#most rated
            for i in most_rated:
                print(most_rated)
            print("--------------------most rated in categories------------------")
            for i in categ_name_list:#most rated in category
                cmd2 = "select p.film_id,p.category_id,p.name,rental.rate from (select F.film_id,FC.category_id,name from (film as F inner join film_category as FC on F.film_id=FC.film_id)  natural join category where category_id=%s)as p inner join rental on p.film_id=rental.film_id where rate=(select max(rate)from rental)"
                rate_film_categ_list = DB_QUERY_where(cmd2, (i[0],))
                for j in rate_film_categ_list:
                    print(i[1], ":", j[2])

            x=26
        case 20:#search

            print('search by actor,gener,title,language,released_year     or exit?')
            search=input("enter search field:")
            match search:
                case "actor":
                    first_name=input("please input the actor's first_name:")
                    last_name=input("please input the actor's last_name:")

                    cmd = "select * from (film inner join film_actor on film.film_id=film_actor.film_id)natural join actor where first_name=%s and last_name=%s"
                    answer = DB_QUERY_where(cmd, (first_name,last_name))
                    if len(answer )!=0:
                        for i in answer:
                            # for j in i:
                            #     print(j)
                            print(i)
                    else:
                        print("we don't have films of this actor")
                    # query
                    cmd="select * from film where "
                case "gener":
                    gener=input("please input the category:")
                    cmd = "select * from (film inner join film_category on film.film_id=film_category.film_id)natural join category where name=%s"
                    answer = DB_QUERY_where(cmd, (gener,))
                    if len(answer) != 0:
                        for i in answer:
                            # for j in i:
                            #     print(j)
                            print(i)
                    else:
                        print("we don't have films in this gener")
                case "title":
                    title = input("please input the name:")
                    cmd = "select * from film where title=%s"
                    answer = DB_QUERY_where(cmd, (title,))
                    if len(answer) != 0:
                        for i in answer:
                            # for j in i:
                            #     print(j)
                            print(i)
                    else:
                        print("we don't have films with this title")
                case "language":
                    language = input("please input the language:")
                    cmd = "select * from film natural join language where name=%s"
                    answer = DB_QUERY_where(cmd, (language,))
                    if len(answer) != 0:
                        for i in answer:
                            # for j in i:
                            #     print(j)
                            print(i)
                    else:
                        print("we don't have films with this language")



                case "released_year":
                    released_year=input("please input the released_year:")
                    cmd="select * from film where release_year=%s"
                    answer=DB_QUERY_where(cmd,(released_year,))
                    if len(answer) != 0:
                        for i in answer:
                            # for j in i:
                            #     print(j)
                            print(i)
                    else:
                        print("we don't have films of this year")
                case "exit":
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
            option=0
            print("1.rent numbers of each film:")
            print('2.average of rate in films:')
            print("3.exit")
            option=int(input("enter an option:"))
            match option:
                case 1:
                    print('')
                    cmd="select  number_of_count , title from film inner join  (select count(rental_id)as number_of_count ,film_id from rental where request_accepted=1 group by film_id)as t on film.film_id=t.film_id "
                    query=DB_QUERY(cmd)
                    for i in  query:
                        print(i)
                case 2:
                    cmd="select  rate_avg , title from film inner join  (select avg(rate)as rate_avg ,film_id from rental where request_accepted=1 group by film_id)as t on film.film_id=t.film_id"
                    query=DB_QUERY(cmd)
                    for i in query:
                        print(i)
                case 0|3:
                    x=26
        case 22:  # active films of user and request
            print("\t 1. past rentals ")
            print("\t 2. active rentals ")

            option=int(input("choose an option: "))
            match option:
                case 1:
                    cmd = "select title,rental_start_date,rental_end_contract,store_id,number_of_films from rental inner join film on rental.film_id=film.film_id where customer_id=%s and return_date IS NOT NULL "
                    query = DB_QUERY_where(cmd, (user_id,))

                    if len(query) != 0:
                        for i in query:
                            print("title:", i[0], " start:", i[1], " end:", i[2], "number :", i[4], "from :", i[3],)
                    else:
                        print("there is nothing to show!")

                case 2:
                    cmd="select title,rental_start_date,rental_end_contract,store_id,number_of_films from rental inner join film on rental.film_id=film.film_id where customer_id=%s and return_date IS NULL "
                    query=DB_QUERY_where(cmd,(user_id,))

                    if len(query)!=0:
                        for i in query:
                            date1 = i[1]
                            date2 = i[2]

                            # Calculate the difference between the two dates
                            difference = relativedelta.relativedelta(date2, date1)
                            print("title:",i[0]," start:",i[1]," end:",i[2],"number :",i[4] ,"from :",i[3],"remained days: ",difference.days)
                    else :
                        print("there is nothing to show!")


            x=26
            print('')
        case 23:  # available films
            print("1.available film:")
            print("2.create a rental")
            print("3.exit")
            option=0
            option=int(input("input a option"))
            match option:
                case 1:
                    cmd="select inventory.film_id,title,number,store_id from inventory inner join film on inventory.film_id=film.film_id where store_id in(select store_id from store_customer where customer_id=%s) and number<>0"
                    query=DB_QUERY_where(cmd,(user_id,))
                    if len(query)!=0:
                        for i in query :
                            print("film_id=",i[0]," title=",i[1]," available number =",i[2]," stoer_id= ",i[3])
                    else:
                        print("there is no films in non of the stores that you are their customer")

                case 2:
                    print('')
                    now=date.today().strftime('%Y-%m-%d')
                    film_id=int(input("enter your film_id :"))
                    store_id=int(input("enter your store_id :"))
                    number_of_films=int(input("enter your request number for film :"))
                    year=int(input("when will you bring it back to store? year"))
                    month=int(input("when will you bring it back to store? month"))
                    day=int(input("when will you bring it back to store? day"))
                    end = date(year, month, day)

                    command = "INSERT INTO rental (rental_start_date, rental_end_contract,film_id,store_id,customer_id,number_of_films,request_accepted,rate) VALUES ( %s, %s,%s,%s,%s,%s,0,0)"

                    DB_Insert(command, (now,end,film_id,store_id,user_id,number_of_films))
                    print("ok")
                    check=DB_QUERY_where("select rental_id from rental where film_id=%s and customer_id=%s and rental_end_contract=%s",(film_id,user_id,end))
                    print("your rental id is :",check[0])
                    print("check it later")

                case 3|0:
                    x=26
        case 24:
            rental_id=int(input("input your rental id :"))
            rate=int(input("input your rate 1 ... 5"))
            if rate<1 or rate>5:
                print("invalid input")
                x=26
            else:
                cmd="UPDATE rental SET rate = %s WHERE rental_id = %s and customer_id=%s"
                DB_update(cmd,(rate,rental_id,user_id))
                print("ok!")
            x=26

        case 240:

            stoer_LIST_cmd="select * from store"
            list=DB_QUERY(stoer_LIST_cmd)
            for i in list:
                print (i)
            store_id=int( input("please input the store that you want buy or rent from it: "))
            cmd ="INSERT INTO store_customer (store_id, customer_id) VALUES (%s, %s)"
            try:
                DB_Insert(cmd,(store_id,user_id))
                print('ok!')
            except:
                print("you were registered before")
            x=26
        case 241:
            cmd="select * from payment where customer_id=%s"
            output=DB_QUERY_where(cmd,(user_id,))
            for i in output:
                print("payment id:" ,i[0],"manager_id:" ,i[2]," rental id:" ,i[3]," amount :" ,i[4],"payment date:" ,i[5])

            x=26
        case 27:# manager menu
            manager_menu()
            x = int(input("please input your option:\t"))
            if x < 27 or x > 39:
                print("invalid input")
        case 28:#customers info
            #store_1
            cmd="select customer_id ,first_name,last_name,email,Number_of_late from store_customer as s inner join customer as c on s.customer_id=c.customer_id where s.store_id =(select store_1 from manager where manager_id=%s)"
            customer_list=DB_QUERY_where(cmd,(user_id,))
            print("customer of your first store")
            for i in customer_list:
                print (i)

            cmd = "select first_name,last_name,email,Number_of_late  from store_customer as s inner join customer as c on s.customer_id=c.customer_id where s.store_id =(select store_2 from manager where manager_id=%s)"
            customer_list = DB_QUERY_where(cmd, (user_id,))
            print("customer of your second store")
            for i in customer_list:
                print(i)
            x=27
        case 29:#next
            #film rental info
            cmd = "select * from rental where store_id =(select store_2 from manager where manager_id=%s) or store_id =(select store_1 from manager where manager_id=%s)"
            rentalFilm_list = DB_QUERY_where(cmd,(user_id,user_id))
            if len(rentalFilm_list)!=0:
                for i in rentalFilm_list:
                    print("rental id:",i[0],"start: ",i[1],"end :",i[2],"film_id :",i[3],"store_id: ",i[4],"customer id: ",i[5],"return date: ",i[6],"manager_id: ",i[7],"numbers : ",i[8],"accepted? : ",i[9],"rate  : ",i[10])
            else:
                print("nothin to show")

            x=27
        case 30:#active rental

            cmd = "select * from rental  where return_date IS NULL and request_accepted=1 and (store_id =(select store_2 from manager where manager_id=%s) or store_id =(select store_1 from manager where manager_id=%s))"
            activeFilm_list = DB_QUERY_where(cmd,(user_id,user_id))
            if len(activeFilm_list)!=0:
                for i in activeFilm_list:
                    print("rental id:",i[0],"start: ",i[1],"end :",i[2],"film_id :",i[3],"store_id: ",i[4],"customer id: ",i[5],"return date: ",i[6],"manager_id: ",i[7],"numbers : ",i[8],"accepted? : ",i[9],"rate  : ",i[10])

            x = 27
        case 31:    #check requests
            cmd = "select * from rental  where request_accepted=0 and (store_id =(select store_2 from manager where manager_id=%s) or store_id =(select store_1 from manager where manager_id=%s))"
            notAccepted_rentalFilm_list = DB_QUERY_where(cmd, (user_id,user_id))
            for i in notAccepted_rentalFilm_list:
                print("rental id:", i[0], "start: ", i[1], "end :", i[2], "film_id :", i[3], "store_id: ", i[4],
                      "customer id: ", i[5], "return date: ", i[6], "manager_id: ", i[7], "numbers : ", i[8],
                      "accepted? : ", i[9], "rate  : ", i[10])
            x = 27
        case 32:#start or end rental            //next
            print('')
            cmd1 = "select store_1,store_2 from manager where manager_id=%s "
            store_id = DB_QUERY_where(cmd1, (user_id,))
            rental_id = int(input("\t enter the rental request id"))
            cmd11 = "select number_of_films,film_id,store_id,customer_id,rental_start_date   ,rental_end_contract from rental where rental_id=%s"

            getting_rentalInfo = DB_QUERY_where(cmd11, (rental_id,))

            print(getting_rentalInfo[0][3])

            cmd1 = "select number from inventory where film_id=%s and store_id=%s"
            inventory_info = DB_QUERY_where(cmd1, (getting_rentalInfo[0][1], getting_rentalInfo[0][2]))

            cmd1 = "select count(rental_id) from rental where customer_id=%s and request_accepted=1 and return_date IS NULL"
            active_rent = DB_QUERY_where(cmd1, (getting_rentalInfo[0][3],))

            cmd = "select number_of_late from customer where customer_id=%s"
            late_number = DB_QUERY_where(cmd, (getting_rentalInfo[0][3],))

            start_end=input("enter the action : start / end:")
            if start_end=="start":
                flag=True
                if len(inventory_info)!=0:
                    if inventory_info[0][0]<getting_rentalInfo[0][0]:
                        flag=False
                        print("this amount is not available in inventory")
                else:
                    flag=False
                    print("this store doesn't have this film_id")

                print(active_rent[0][0])
                if active_rent[0][0]>=3:
                    print("customer has used the maximum number of renting ")
                    flag=False


                delta=getting_rentalInfo[0][5]-getting_rentalInfo[0][4]
                if delta.days>14 or delta.days<1:
                    flag=False
                    print("rental time is not valid should be between 14 , 1 !")

                if late_number[0][0]>10:
                    flag=False
                    print("customer has been late more than 10 times!")

                if flag:
                    manager = "UPDATE rental SET manager_id = %s WHERE rental_id = %s"
                    accept = "UPDATE rental SET request_accepted = %s WHERE rental_id = %s"

                    # date = "UPDATE rental SET return_date = %s WHERE rental_id = %s"
                    DB_update(manager, (user_id, rental_id))
                    DB_update(accept, (1, rental_id))
                    number_film_id=DB_QUERY("select number_of_films,film_id from rental where rental_id=rental_id")
                    # number_of_films=DB
                    # DB_update(date, (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rental_id))
                else:
                    print("rent is not acceptable!")
            else:#end
                # date = "UPDATE rental SET rental_start_date = %s WHERE rental_id = %s"
                now_time=date.today()
                delta_1 = getting_rentalInfo[0][5] - getting_rentalInfo[0][4]
                delta_2=now_time-getting_rentalInfo[0][4]
                fee=0
                if delta_2.days<=delta_1.days:
                    #creating payment
                    fee=delta_2.days*2

                else:
                    #creating payment
                    fee=delta_1.days*2 + (delta_2.days-delta_1.days )*3

                    #adding lates
                    new_late_number=late_number[0][0]+1
                    late_cmd="UPDATE customer SET Number_of_late=%s where customer_id=%s"
                    DB_update(late_cmd,(new_late_number,getting_rentalInfo[0][3]))

                cmd = "INSERT INTO payment (customer_id,manager_id, rental_id,amount,payment_date) VALUES (%s, %s,%s, %s,%s)"
                DB_Insert(cmd,(getting_rentalInfo[0][3],user_id,rental_id,fee,now_time))
                print('payment added')
                date = "UPDATE rental SET return_date = %s WHERE rental_id = %s"
                DB_update(date, (now_time, rental_id))
            print("done!")
            x=27

        case 33:
            cmd1 = "select store_1,store_2 from manager where manager_id=%s"
            store_id = DB_QUERY_where(cmd1, (user_id,))
            cmd = "select * from store  where  store_id= %s or store_id=%s"
            stores = DB_QUERY_where(cmd, (store_id[0][0],store_id[0][1]))

            for i in stores:
                print(i)
            x=27
        case 34:#next
            store_id=int(input("\t enter store_id"))
            name=input("\tenter new name")
            cmd="UPDATE store set name=%s where store_id=%s"
            DB_QUERY_where(cmd,(name,store_id))
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
            search = input("enter search field: or exit")
            match search:
                case "actor":
                    first_name = input("please input the actor's first_name:")
                    last_name = input("please input the actor's last_name:")

                    cmd = "select * from (film inner join film_actor on film.film_id=film_actor.film_id)natural join actor where first_name=%s and last_name=%s"
                    answer = DB_QUERY_where(cmd, (first_name, last_name))
                    print(answer)
                    for i in answer:
                        print(i)
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
                case "exit":
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
            store_id = DB_QUERY_where("select store_1,store_2 from manager where manager_id=%s", (user_id,))

            match option:
                case 1:

                    print(store_id)
                    flag=True


                    if flag:
                        print("store_1: ")
                        cmd="select * from rental inner join payment on rental.rental_id=payment.rental_id  where store_id=%s"
                        output=DB_QUERY_where(cmd,(store_id[0][0],))
                        for i in output:
                            print(i)

                        print("store_2: ")
                        cmd = "select * from rental inner join payment on rental.rental_id=payment.rental_id  where store_id=%s"
                        output = DB_QUERY_where(cmd, (store_id[0][1],))
                        for i in output:
                            print(output)

                case 2:



                    customer=int(input("\tenter your customer id:"))
                    number=int(input("\t in which of your stores 1 or 2?"))
                    if number==1:
                        cmd = "select * from rental natural join payment where store_id=%s and customer_id=%s"
                        output = DB_QUERY_where(cmd, (store_id[0][0],customer))
                        for i in output:
                            print(i)
                    else:
                        cmd = "select * from rental natural join payment where store_id=%s and customer_id=%s"
                        output = DB_QUERY_where(cmd, (store_id[0][1], customer))
                        for i in output:
                            print(i)
                case 3:
                    film_id=int(input("\t enter film_id"))
                    cmd = "select * from rental natural join payment where film_id=%s"
                    output = DB_QUERY_where(cmd, (film_id,))

                    for i in output:
                        print(i)
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
                     cmd = "select  count(rental_id)as number,film_id from(select * from (film_actor inner join film on film_actor.film_id=film.film_id) as p inner join actor on p.actor_id=actor_id)   group by film_id order by number desc  limit 1"
                     query=DB_QUERY(cmd)
                     print(query[0])
                     print('')
                case 3:
                    print('')
                case 4:
                    x=27