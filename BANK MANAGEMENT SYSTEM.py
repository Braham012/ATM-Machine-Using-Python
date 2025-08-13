import mysql.connector

connection = mysql.connector.connect( host = 'localhost' , database = 'bank' , user = 'root' , password = 'root' )

print("======================")
print("    WELCOME TO ATM    ")
print("======================")
print("")
print("1 - REGISTRATION")
print("2 - LOGIN")
print("3 - EXIT")
option = int(input("SELECT THE PROCESS : "))

if option == 1:

    Name = input("Please Enter Your First And Last Name As Per  Your GOVERNMENT Document :")
    Identification = int(input("Please Enter Your Customer ID Provided by Bank :"))
    Password = int(input("Please Create Your Desired PIN :"))
    Amount = int(input("Please Enter The Amount You Want to Deposit :"))

    val = (Name,Identification,Password,Amount)

    sql = "INSERT INTO customer_details( CUSTOMER_NAME , CUSTOMER_ID , PIN , AMOUNT )  VALUES ( %s , %s , %s , %s )"
    print("==========================")
    print("    SUCCESSFULLY ADDED    ")
    print("==========================")
    mycursor = connection.cursor()

    mycursor.execute(sql,val)
    connection.commit()

if option == 2:

    Identification = int(input("ENTER YOUR CUSTOMER ID :"))
    Password = int(input("ENTER YOUR PIN :"))
    mycursor = connection.cursor()
    mycursor.execute("Select * from customer_details where CUSTOMER_ID = '%s'" % (Identification))
    row = mycursor.fetchone()
    
    if mycursor.rowcount == 1:

        mycursor.execute("Select * from customer_details where PIN = '%s'" % (Password))
        row = mycursor.fetchone()
    
        if mycursor.rowcount == 1:
            
            print("======================")
            print("   LOGIN SUCCESSFUL   ")
            print("======================")
            print("1 - DEPOSIT")
            print("2 - WITHDRAW")
            print("3 - CHECK BALANCE")
            print("4 - EXIT")
            user = int(input("SELECT THE OPERATION TO EXECUTE :"))

            if user == 1:
                a = int(input("How Much You Want To Deposit :"))
                mycursor.execute("Select AMOUNT from customer_details where PIN = '%s'" % (Password))
                b = mycursor.fetchone()
                x = list(b)

                for i in x:
                    z = (int(i))
                    c = z + a
                mycursor.execute("UPDATE customer_details SET AMOUNT='%s' where PIN = '%s'" % (c , Password))
                connection.commit()
            
            if user == 2:
                a = int(input("How Much You Want To Withdraw :"))
                mycursor.execute("Select AMOUNT from customer_details where PIN = '%s'" % (Password))
                b = mycursor.fetchone()
                x = list(b) 

                if a > x[0]:
                    print(" !! INSUFFICIENT BALANCE IN YOUR BANK ACCOUNT !! ")
                    print(" !! PLEASE TRY AGAIN")

                else:
                    for i in x:
                        z = (int(i))
                        c = z - a
                    mycursor.execute("UPDATE customer_details SET AMOUNT ='%s' where CUSTOMER_ID = '%s'" % (c , Identification))
                    connection.commit()

            if user == 3:
                mycursor.execute("Select AMOUNT from customer_details where CUSTOMER_ID = '%s'" % (Identification))
                b = mycursor.fetchone()
                
                for i in b:
                    print(i)

            if user == 4:
                exit
        
        else:
            print("==============================")
            print("    !! INVALID PASSWORD !!    ")
            print("    !! PLEASE TRY AGAIN !!    ")
            print("==============================")
    
    else:
        print("=======================================")
        print("    !! CUSTOMER ID DOESN'T EXIST !!    ")
        print("        !! PLEASE TRY AGAIN !!         ")
        print("=======================================")
print("====================================")
print("    THANKU FOR USING OUR SERVICE    ")
print("====================================")