import time
import mysql.connector
conn=mysql.connector.connect(host='localhost',database='bank',user='root',password='root')
cursor=conn.cursor()
def main():
 adminid="root"
 adminpass="root"
 print("************************************************************")
 print("MAIN MENU")
 choice=input("1.SIGNUP\n2.SIGN IN\n3.SIGN IN(ADMIN)\n4.QUIT\nPlease enter your choice:")
 if(choice==1):
    print("\n***SIGN UP***\nPlease enter your details:")
    firstname=raw_input("First name:")
    lastname=raw_input("Last name:")
    address=raw_input("Address:")
    username=raw_input("Please choose a user name:")
    password=raw_input("Please choose a password:")
    cursor.execute("insert into tab1 values('"+firstame+"','"+lastname+"','"+address+"','"+username+"','"+password+"',0,0)")
    cursor.fetchone()
    print("Details Succesfully Stored!\nRestoring Control to Main Menu")
    main()
 
 elif(choice==2):
    print("\n***SIGN IN***")
    user=raw_input("Username:")
    pas=raw_input("Password:")
    cursor.execute("select count(*) from tab1 where username='"+user+"' and password='"+pas+"'")
    opt1=cursor.fetchall()
    if (opt1==[(1,)]):
     ch2=input("1.Change Address\n2.Deposit\n3.Withdrawal\n4.Print Statement\n5.Account Closure\n6.Logout\nPlease enter your choice:")
     if(ch2==1):
      add=raw_input("Enter new address")
      cursor.execute("update tab1 set address='"+add+"' where username='"+user+"' and password='"+pas+"'")     
      cursor.fetchone()
     elif(ch2==2):
         depo =input("Enter the deposited amount")
         cursor.execute("update tab1 set deposit='"+depo+"' where username='"+usr+"' and password='"+pas+"'")     
         cursor.fetchone()
     elif(ch2==3):
         withdraw=input("Enter the withdrawn amount")
         cursor.execute("update tab1 set withdrawal='"+withdraw+"' where username='"+usr+"' and password='"+pas+"'")     
         cursor.fetchone()
     elif(ch2==4):
         print("BANK STATEMENT")
         cursor.execute("select * from tab1 where username='"+usr+"' and password='"+pas+"'")     
         aaa=cursor.fetchall()
         print aaa
     elif(ch2==5):    
         print("Account Terminating...")
         cursor.execute("insert closed select * from tab1 where username='"+usr+"' and password='"+pas+"'")   
         cursor.fetchone()   
         conn.commit()
         cursor.execute("delete from tab1 where username='"+usr+"' and password='"+pas+"'")       
         cursor.fetchone()   
     elif(ch2==6):
         print("Logging Out....")
         time.sleep(3)
     else:
         print("Invalid Choice")    
    else:
        print("Invalid Username or Password!")
    print("Returning to main menu...")
    time.sleep(1)             
    print("\n\n\n\n")
    main()    
    
        
 elif(choice==3):
    print("***SIGN IN(ADMIN)***")
    adid=raw_input("Username:")
    adpass=raw_input("Password:")
    if(adid==adminid and adpass==adminpass):
        print("ACCESS GRANTED\nWELCOME ADMIN")  
        adchoice=input("Enter your Choice\n1.Print Closed Account History\n2.Admin Logout")
        if(adchoice==1):
            print("Closed")
        elif(adchoice==2):
            print("\n\n\n\n")
            main()
        else:
            print("Invalid Choice")
            print("Returning to main menu...")
            time.sleep(1)             
            print("\n\n\n\n")
            main() 
    else:
        print("Access Denied")
        time.sleep(1)
        print("Returning to main menu...")
        time.sleep(1)             
        print("\n\n\n\n")
        main() 
                 
     
 elif(choice==4):
      print("Closing the application")
      time.sleep(1)
      print("Application Closed...")
      time.sleep(1)
      exit()  
 else:
    print("Invalid Choice")
    time.sleep(2)
    print("Returning to main menu...")
    time.sleep(1)             
    print("\n\n\n\n")
    main() 

conn.commit()    
conn.close()
main()
