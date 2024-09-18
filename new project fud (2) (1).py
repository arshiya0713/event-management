
print("_"*141)
print("~"*141)
print("")
print("")
print("\t\t\t\t\t\t\t     HAPPENING PRODUCTION")
print("\t\t\t\t\t\t  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
print("\t\t\t\t\t\t\t      TIRUNELVELI-627011")
print("")
print("_"*141)
print("~"*141)
print("")
print("")
print("\t\t\t\t\t\t\tWELCOME TO HAPPENING PRODUCTION")
print("")
print("\t\t\t\t\t NOTE THAT WE ONLY OPERATE INSIDE TAMIL NADU, THANK YOU =)")
print("\n")
import sys

#Database Connection

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", user="root", passwd="root", database="eventers",buffered=True)
cursor=mycon.cursor()

#create table
sql="create table if not exists LOGIN(USERNAME varchar(35) primary key,NAME varchar(35),PASSWORD varchar(20), CONTACT varchar(15) unique)"
cursor.execute(sql)
mycon.commit()

sql="create table if not exists EVEINFO(NO int(11) primary key,USER char(35),EVENAME char(35),TYPE char(35),DISTRICT char(35),ADDRESS char(50),COST varchar(35),PAID varchar(35))"
cursor.execute(sql)
mycon.commit()

sql="create table if not exists CREATION(NO int(11) primary key,USERNAME varchar(35),EVNT_NAME varchar(35),PEOPLE varchar(11),CHAIRS varchar(35),QTY_C varchar(11),EXTRA_CH varchar(35),QTY_EXT_C varchar(11),M_S varchar(35),SPEAKER_QTY varchar(11),MICRO_QTY varchar(11),PHGRAPH varchar(25),PHGRAPH_QTY varchar(11),WATER varchar(25),WAT_QTY varchar(11),RFR_TAB varchar(25),DJ varchar(25))"
cursor.execute(sql)
mycon.commit()

sql="create table if not exists CUSTOM(NO int(11) primary key,USERNAME varchar(35),EVNT_NAME varchar(35),PEOPLE varchar(11),PACKAGE varchar(35),CHAIRS varchar(35),EXTRA_CH varchar(11))"
cursor.execute(sql)
mycon.commit()

sql="create table if not exists DEC_FUD_SNACK(NO int(11) primary key, USERNAME varchar(35),DECORATONS varchar(35),THEME varchar(35),COLOURS varchar(35),GAS varchar(35),FLOWERS varchar(35),FOOD varchar(35),BUF_SER varchar(10),VEG_MIX varchar(35),BREAKFAST varchar(35),PACK_B varchar(35),LUNCH varchar(35),PACK_L varchar(35),DINNER varchar(35),PACK_D varchar(35),SNACKS varchar(10))"
cursor.execute(sql)
mycon.commit()

def chairs_(people):
   
   chairs=input("DO YOU WANT CHAIRS IN THE EVENT(Y/N):")
   for i in range(0,400):

      global chyn
      global chair
      global ccost
      global extrch
      global extra
      global excc      
      if chairs.lower()=="y":
         chyn="YES"
         chair=people+200
         print(chair,"CHAIRS WILL BE PROVIDED")
         ccost=chair*10
         print("")
         print("COST OF CHAIRS=",ccost)
         extr=input("DO YOU REQUIRE EXTRA CHAIRS(Y/N):")
         
         for i in range(500):
            

            
            if extr.lower()=="y":               
               extrch="YES"
               print("")
               extra=int(input("ENTER THE NUMBER OF CHAIRS YOU WOULD REQUIRE EXTRA:"))
               print(extra," EXTRA CHAIRS WILL BE PROVIDED")
               excc=extra*10
               print("")
               print("COST OF EXTRA CHAIRS=",excc)
               print("")
               print("TOTAL COST OF CHAIRS=",ccost+excc)
               break
            
            if extr.lower()=="n":
               extrch="NO"
               extra="NONE"
               print("NO EXTRA CHAIRS")
               print("TOTAL COST OF CHAIRS=",ccost)
               excc=0
               break
            
            else:
               print("ENTER A VALID CHOICE:")
               extr=input("DO YOU REQUIRE EXTRA CHAIRS(Y/N):")
         break
      
      if chairs.lower()=="n":
         chyn="NO"
         chair="NULL"
         extrch="NO"
         extra="NULL"
         
         print("NO CHAIRS REQUIRED")
         excc=0
         ccost=0
         break
      
      else:
         print("ENTER A VALID CHOICE:")
         chairs=input("DO YOU WANT CHAIRS IN THE EVENT(Y/N):")

def dec():
   print("")
   decor=input("DO YOU REQUIRE DECORATIONS(Y/N):")
   global mcl
   global colour
   global gas
   global flower
   global dec
   global tco

   while True:   
      if decor.lower()=="y":

         dec="YES"
         
         print("")
         print("THE DECORATIONS WILL BE DONE ACCORDING TO THE COLOUR THEME YOU CHOOSE")
         print("")
         print("CHOOSE ANY ONE:")
         print(" 1-MONO COLOUR")
         print(" 2-TWO COLOUR")
         print(" 3-MULTI COLOUR")
         print("")
         
         theme=int(input("WHAT THEME DO YOU PREFER:"))

         while True:
          if theme==1:
            colour="MONO "
            print("YOU HAVE CHOOSEN MONO COLOURED THEME")
            print("")
            mcl=input("WHAT COLOUR DO YOU PREFER:")
            print("THE DECORATIONS WILL BE BASED ON THE COLOUR",mcl)
            print("")
            print("TOTAL COST FOR MONO COLOURED THEME=20,000")
            tco=20000
            break

          elif theme==2:
            colour="DOUBLE "
            print("YOU HAVE CHOOSEN TWO COLOURED THEME")
            print("")
            mcl=input("WHAT TWO COLOURS DO YOU PREFER:")
            print("THE DECORATIONS WILL BE BASED ON THE COLOURS",mcl)
            print("")
            print("TOTAL COST FOR TWO COLOURED THEME=30,000")
            tco=30000
            break
         
          elif theme==3:
            colour="MULTI "
            print("YOU HAVE CHOOSEN MULTI COLOURED THEME")
            print("")
            print("DO YOU PREFER:")
            print(" 1-BRIGHT COLOURS")
            print(" 2-PASTEL COLOURS")
            print(" 3-DARK COLOURS")
            print("")
            mulcl=int(input("ENTER THE THEME YOU WOULD LIKE (1/2/3):"))
            print("")
            while True:
               if mulcl==1:
                  mcl="BRIGHT"
                  print("TOTAL COST FOR MULTI COLOURED(BRIGHT) THEME=50,000")
                  tco=50000
                  break
               elif mulcl==2:
                  mcl="PASTEL"
                  print("TOTAL COST FOR MULTI COLOURED(PASTEL) THEME=55,000")
                  tco=55000
                  break
               elif mulcl==3:
                  mcl="DARK"
                  print("TOTAL COST FOR MULTI COLOURED(DARK) THEME=50,000")
                  tco=50000
                  break
               else:
                  mulcl=int(input("ENTER THE THEME YOU WOULD LIKE (1/2/3):"))
                  exit
                  
            print("")
            print("YOU DECORATIONS WILL BE BASED ON",mcl,"COLOURS")
            break
         
          else:
            print("THE DECORATIONS WILL BE DONE ACCORDING TO THE COLOUR THEME YOU CHOOSE")
            exit
           
         print("")
         print("1-HELIUM GAS")
         print("2-NORMAL GAS")
         print("")
         bal=input("WHAT WOULD YOU LIKE TO FILL IT WITH (1/2) :")
         
         while True:
          if bal=='1':
            gas="HELIUM"
            print("THE BALLOONS WILL BE FILLED WITH HELIUM GAS")
            break
          elif bal=='2':
            gas="NORMAL"
            print("THE BALLOONS WILL BE FILLED WITH NORMAL GAS")
            break
          else:
            print("")
            print("1-HELIUM GAS")
            print("2-NORMAL GAS")
            print("")
            bal=input("WHAT WOULD YOU LIKE TO FILL IT WITH (1/2) :")
            exit
            
         print("")
         floral=input("DO YOU PREFER: \n1-REAL FLOWERS \n2-ARTIFICIAL FLOWERS \n\nENTER THE TYPE OF FLOWER YOU'D LIKE(1/2):")
         
         while True:
           if floral=='1':
              flower="REAL"
              print("YOUR DECORATIONS WILL BE DONE WITH REAL FLOWERS")
              print("")
              break
           elif floral=='2':
              flower="ARTIFICIAL"
              print("YOUR DECORATIONS WILL BE DONE WITH ARTIFICIAL FLOWERS")
              print("")
              break
           else:
              floral=input("DO YOU PREFER: \n1-REAL FLOWERS \n2-ARTIFICIAL FLOWERS \n\nENTER THE TYPE OF FLOWER YOU'D LIKE(1/2):")
              print("")
              exit
         break
              
      if decor.lower()=="n":
         print("NO DECORATIONS REQUIRED")

         dec="NO"
         colour="NULL"
         mcl="NULL"
         gas="NULL"
         flower="NULL"
         tco=0
         break

      else:
         print("IT SEEMS YOU HAVE ENTERED THE WRONG INFO")
         print("PLEASE TRY AGAIN")
         print("")
         decor=input("DO YOU REQUIRE DECORATIONS(Y/N):")
         exit
         
                 
         
def ms():
   
   print("")
   sm=input("DO YOU REQUIRE MICROPHONE AND SPEAKERS(Y/N):")
   global mis
   global speaker
   global micro
   global scost
   global mcost
   
   while True:
      if sm.lower()=="y" :
         mis="YES"         
         speaker=int(input("\nENTER NUMBER OF SPEAKERS REQUIRED:"))
         micro=int(input("ENTER NUMBER OF MICROPHONES REQUIRED:"))
         scost=speaker*1000
         mcost=micro*500
         print("")
         print("COST OF SPEAKERS=",scost)
         print("COST OF MICROPHONES=",mcost)
         print("")
         print("TOTAL COST FOR SPEAKERS AND MICROPHONES=",scost+mcost)
         break
      elif sm.lower()=="n" :         
         mis="NO"
         speaker="NULL"
         micro="NULL"
         print("NO SPEAKERS AND MICROPHONES REQUIRED")
         scost=0
         mcost=0
         break
      else:
         print("")
         sm=int(input("DO YOU REQUIRE MICROPHONE AND SPEAKERS(Y/N):"))
         exit


def pics():
   
   pic=input("\nDO YOU REQUIRE PHOTOGRAPHERS(Y/N):")
   global pic_s
   global nopic
   global pcost
   while True:
      if pic.lower()=="y":         
         pic_s="YES"         
         nopic=int(input("ENTER NUMBER OF PHOTOGRAPHERS REQUIRED:"))
         pcost=nopic*5000
         print("")
         print("TOTAL COST FOR PHOTOGRAPHERS=",pcost)
         break
      if pic.lower()=="n":
         pic_s="NO"
         nopic="NULL"
         print("NO PHOTOGRAPHERS REQUIRED")
         pcost=0
         break
      else:
         print("")
         pic=input("\nDO YOU REQUIRE PHOTOGRAPHERS(Y/N):")
         exit


def snw():
   
   water=input("\nDO YOU REQUIRE WATER BOTTLES DURING THE EVENT(Y/N):")
   global wat
   global no
   global wcost
   
   while True:
      if water.lower()=="y":
         global wat
         wat="YES"
         global no 
         no=int(input("ENTER NUMBER OF WATER BOTTLES REQUIRED:"))
         wcost=no*10
         print("")
         print("TOTAL COST FOR WATERBOTTLES=",wcost)
         print("")
         break
      elif water.lower()=="n":         
         wat="NO"         
         no="NULL" 
         print("NO WATER BOTTLES REQUIRED")
         print("")
         wcost=0
         break
      else:
         water=input("\nDO YOU REQUIRE WATER BOTTLES DURING THE EVENT(Y/N):")
         exit


def djs():
   
   dj=input("DO YOU REQUIRE DJ'S(Y/N):")
   global dj_s
   global dcosj
   
   while True:
      if dj.lower()=="y" :         
         dj_s="YES"
         print("A DJ WILL BE AVAILABLE FOR YOU")
         print("")
         print("TOTAL COST FOR DJ=15000")
         dcosj=15000
         break
      elif dj.lower()=="n":
         dj_s="NO"
         print("NO DJ'S REQUIRED")
         dcosj=0
         break
      else:
         dj=dj=input("\nDO YOU REQUIRE DJ'S(Y/N):")
         exit


def packages(people):
   
   global packages_p
   global chairc
   global exchair
   global ccost
   global excc
   global pacost
   while True :
      if people>=2000:
          
         packages_p="LARGE"                        
         print("")
         print("YOU'LL BE PROVIDED WITH A LARGE PACKAGE: ")
         chairc=people+200
         ccost=chairc*10
         
         print("CHAIR QUANTITY:",chairc)
         print("EXTRA CHAIRS: 500")
         exchair=500
         excc=exchair*10
         print("")
         print("DJ, SNACKS, SPEAKERS AND MICROPHONES PROVIDED")
         print("REFRESHMENT TABLE ALSO PROVIDED")
         print("\nFOOD SERVICE CUSTOMISABLE")
         print("TOTAL COST FOR LARGE PACKAGE=1,00,000")
         pacost=100000
         print("") 
         break  
      elif people>100 and people<2000:

         packages_p="MEDIUM"              
         print("")
         print("YOU'LL BE PROVIDED WITH A MEDIUM PACKAGE:")
         chairc=people+200
         ccost=chairc*10
         
         print("CHAIR QUANTITY:",chairc)
         print("EXTRA CHAIRS: 100")
         exchair=100
         excc=exchair*10
         print("")
         print("DJ, SNACKS, SPEAKERS AND MICROPHONES PROVIDED")
         print("REFRESHMENT TABLE ALSO PROVIDED")
         print("\nFOOD SERVICE CUSTOMISABLE")
         print("TOTAL COST FOR MEDIUM PACKAGE=75,000")
         pacost=75000
         print("")
         break
      elif people<=100:
     
         packages_p="SMALL"
         print("")
         print("YOU'LL BE PROVIDED WITH A SMALL PACKAGE")
         chairc=people+10
         ccost=chairc*10
         
         print("CHAIR QUANTITY:",chairc)
         print("EXTRA CHAIRS: 25")
         exchair=25
         excc=exchair*10
         print("")
         print("DJ, SNACKS, SPEAKERS AND MICROPHONES PROVIDED")
         print("REFRESHMENT TABLE ALSO PROVIDED")
         print("\nFOOD SERVICE CUSTOMISABLE")
         print("TOTAL COST FOR SMALL PACKAGE=50,000")
         pacost=50000
         print("")
         break

def ref():

   print("")

   refer=input("DO YOU WANT REFRESHMENT TABLE IN THE EVENT(Y/N):")
   while True:
       global refresh
       global rcost
       if refer.lower()=="y":
          refresh="YES"
          print("")
          print("THE REFRESMENT TABLE WILL BE PROVIDED WITH")
          print("GLUCOSE")
          print("SUGAR")
          print("ENERGY DRINKS")
          print("WATER BOTTLES")
          print("")
          print("TOTAL COST FOR REFRESHMENT TABLE=2000")
          rcost=2000
          break
         
       elif refer.lower()=="n":
          refresh="NO"
          print("NO REFRESHMENT TABLE REQUIRED")
          rcost=0
          break
         
       else:
          refer=input("DO YOU WANT REFRESHMENT TABLE IN THE EVENT(Y/N):")
          exit
def report():
   global tcosts
   print("\n\t\t\t\t\t     HAPPENING PRODUCTION")
   print("\t\t\t\t  1A,G-14, SIVANTHIPATTI ROAD, MAHARAJANAGAR")
   print("\t\t\t\t\t      TIRUNELVELI-627011")
   print("\t\t\t\t\t\tPH: 9789000425")
   print("\t\t\t\t\t     GST: 33AAPFN1783J1ZW")
   print('')
   print('\t\t\t\t                ***INVOICE***')
   print("USER ID: ",user)
   print('')
   print('-'*120)
   print("")
   print("\t\t\t\t    CATEGORY OF THE EVENT:",event)
   print("")
   print("LOCATION:",address)
   print("DISTRICT:",placenew)
   print("DATE:",date)
   print("TIME:",start,hours,"-",end,hour)

   print("")

   print("")



   if types=="CREATION     |":
      print("NAME OF YOUR EVENT:",evntname)
      print("NO. OF PEOPLE ATTENDING:",people)
      print("")
      print("")
      print("\n\t\t\t\t\t\t\t    QUANTITY\t\t\t\t     COST")
      print("")
       
      if chyn=="YES":
         print("NO. OF CHAIRS \t\t\t\t\t\t    ",chair,"\t\t\t\t  ",ccost)
      if extrch=="YES":
         print("NO. OF EXTRA CHAIRS\t\t\t\t\t    ",extra,"\t\t\t\t  ",excc)
      if mis=="YES":
         print("NO. OF SPEAKERS\t\t\t\t\t\t    ",speaker,"\t\t\t\t  ",scost)
         print("NO. OF MICROPHONES\t\t\t\t\t    ",micro,"\t\t\t\t  ",mcost)
      if pic_s=="YES":       
         print("NO OF PHOTOGRAPHERS \t\t\t\t\t    ",nopic,"\t\t\t\t\t  ",pcost)
      if wat=="YES":
         print("NO OF WATERBOTTLES\t\t\t\t\t    ",no,"\t\t\t\t  ",wcost)
      if dj_s=="YES":         
         print("DJ \t\t\t\t\t\t\t     -\t\t\t\t\t   15000")
      if refresh=="YES":
         print("REFRESHMENT TABLE\t\t\t\t\t     1\t\t\t\t\t   2000")
      if dec=="YES":
         print("DECORATIONS \t\t\t\t\t\t     -\t\t\t\t\t  ",tco)
      if sn_a=="YES":
         print("SNACKS \t\t\t\t\t\t\t     -\t\t\t\t\t  ",s_cost)
      if fud=="YES":

         print("FOOD\t\t\t\t\t\t\t\t\t\t\t\t  ",f_cost)
         print("FOOD TYPE        :\t",vm)
         if breakfast=="YES":
             print("BREAKFAST PACKAGE:\t",b_pack)
         if lunch=="YES":
             print("LUNCH PACKAGE    :\t",l_pack)
         if dinner=="YES":
             print("DINNER PACKAGE   :\t",d_pack)


      print('-'*120)
      cgst=(2.5/100)*tcost
      sgst=(2.5/100)*tcost
      print("\t\t\t\t\t\t\t\t    CGST:2.5%\t\t",cgst)
      print("\t\t\t\t\t\t\t\t    SGST:2.5%\t\t",sgst)
      print("")
      print("-"*120)
      
      total=tcost+cgst+sgst
      import math
      tcosts=math.ceil(tcost)
      print("\t\t\t\t\t\t\t\t    GRAND TOTAL:  \tRs ",tcosts)
      print("")
      print("-"*120)
      print("\t\t\t\t       FSSAI LIC NO:12419026000669")
      print("\t\t\t\t\t\t THANKS")
      
   if types=="CUSTOMISATION|":
     print("NAME OF YOUR EVENT:",eventname)
     print("NO. OF PEOPLE ATTENDING:",people)
     print("")
     print("")
     print("\n\t\t\t\t\t\t\t    QUANTITY\t\t\t\t     COST")
     print("")
     
     print("NO. OF CHAIRS \t\t\t\t\t\t    ",chairc,"\t\t\t\t  ",ccost)
     print("NO. OF EXTRA CHAIRS\t\t\t\t\t    ",exchair,"\t\t\t\t  ",excc)
     if mis=="YES":
       print("NO. OF SPEAKERS\t\t\t\t\t\t    ",speaker,"\t\t\t\t  ",scost)
       print("NO. OF MICROPHONES\t\t\t\t\t    ",micro,"\t\t\t\t  ",mcost)
     if pic_s=="YES":       
        print("NO OF PHOTOGRAPHERS \t\t\t\t\t    ",nopic,"\t\t\t\t\t  ",pcost)
     if wat=="YES":
        print("NO OF WATERBOTTLES\t\t\t\t\t    ",no,"\t\t\t\t  ",wcost)
     print("DJ \t\t\t\t\t\t\t     -\t\t\t\t\t   15000")
     print("REFRESHMENT TABLE\t\t\t\t\t     1\t\t\t\t\t   2000")
     if dec=="YES":
        print("DECORATIONS \t\t\t\t\t\t     -\t\t\t\t\t  ",tco)
     if sn_a=="YES":
        print("SNACKS \t\t\t\t\t\t\t     -\t\t\t\t\t  ",s_cost)
     if fud=="YES":

        print("FOOD\t\t\t\t\t\t\t\t\t\t\t\t  ",f_cost)
        print("FOOD TYPE        :\t",vm)
        if breakfast=="YES":
            print("BREAKFAST PACKAGE:\t",b_pack)
        if lunch=="YES":
            print("LUNCH PACKAGE    :\t",l_pack)
        if dinner=="YES":
            print("DINNER PACKAGE   :\t",d_pack)


     print('-'*120)
     cgst=(2.5/100)*tcost
     sgst=(2.5/100)*tcost
     print("\t\t\t\t\t\t\t\t    CGST:2.5%\t\t",cgst)
     print("\t\t\t\t\t\t\t\t    SGST:2.5%\t\t",sgst)
     print("")
     print("-"*120)
     total=tcost+cgst+sgst
     import math
     tcosts=math.ceil(tcost)
     print("\t\t\t\t\t\t\t\t    GRAND TOTAL:  \tRs ",tcosts)
     print("")
     print("-"*120)
     print("\t\t\t\t       FSSAI LIC NO:12419026000669")
     print("\t\t\t\t\t\t THANKS")        
      

def final_payment():
     print("TOTAL AMOUNT:",tcosts)
     apay=tcosts//2
     print("ADVANCE AMOUNT:",apay)
     print("")
     print("THE FINAL AMOUNT CAN BE PAID AFTER THE COMPLETION OF EVENT, CURRENTLY YOU HAVE TO PAY THE ADVANCE AMOUNT FOR US TO MANAGE THE EVENT")
     print("")
     import random
     final=input("ARE YOU SURE YOU WANT TO PAY THE ADVANCE FOR THE EVENT(Y/N):")
     
     if final.lower()=="y": 
        print("1.CREDIT CARD\n2.GPAY\n3.DEBIT CARD")
        print("")
        print("THE TOTAL AMOUNT WILL BE WIRED FROM YOUR ACCOUNT ONCE YOU HAVE ENTERED YOUR PASSWORD")
        mode=int(input("ENTER YOUR TYPE OF PAYMENT:"))

#credit card
        if mode==1:
            name=input("ENTER YOUR NAME:")
            print("")
            card_no=int(input("ENTER YOUR CARD NUMBER:"))
            while len(str(card_no))!=16:
               print("WRONG INPUT!!!")
               card_no=int(input("ENTER YOUR CARD NUMBER:"))

            print("")
            pin=int(input("ENTER YOUR CARD PIN:"))
            print("")
            y_otp=random.randint(100,999)
            print("YOUR OTP:",y_otp)
            otp=int(input("ENTER OTP:"))
            while otp!=y_otp:
                print("WRONG OTP!")
                otp=int(input("Enter the OTP:"))
            print("AMOUNT RECIEVED SUCCESSFULLY")
            pay="PAID"
            sql="insert into EVEINFO (NO,USER,EVENAME,TYPE,DISTRICT,ADDRESS,COST,PAID)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,event,types,placenew,address,tcosts,pay)
            cursor.execute(sql)
            mycon.commit()

            print("")
            print("")
            print("YOUR EVENT WILL BE MANAGED SUCCESSFULLY BY HAPPENING PRODUCTION")
            print("")

                
#gpay
            
        if mode==2:
            mobile=input("ENTER YOUR MOBILE NUMBER: ")
            while len(mobile)!=10:
                    print("INVALID MOBILE NUMBER")
                    mobile=input("RE-ENTER MOBILE NUMBER: ")
                    
            print("PIN FOR RECIEVER PHONE NUMBER",random.randint(100,999))
            print("")
            y_otp=random.randint(100,999)
            print("YOUR OTP:",y_otp)
            otp=int(input("ENTER OTP:"))
            while otp!=y_otp:
                print("WRONG OTP!")
                otp=int(input("ENTER OTP:"))
            print("AMOUNT RECIEVED SUCCESSFULLY")
            pay="PAID"
            sql="insert into EVEINFO (NO,USER,EVENAME,TYPE,DISTRICT,ADDRESS,COST,PAID)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,event,types,placenew,address,tcosts,pay)
            cursor.execute(sql)
            mycon.commit()
            
            print("")
            print("")
            print("YOUR EVENT WILL BE MANAGED SUCCESSFULLY BY HAPPENING PRODUCTION")
            print("")
            
#debit card
            
        if mode==3:
            name=input("ENTER YOUR NAME:")
            print("")
            card_no=int(input("ENTER YOUR CARD NUMBER:"))
            while len((card_no))!=16:
               print("WRONG INPUT!!!")
               card_no=int(input("ENTER YOUR CARD NUMBER:"))

            print("")
            pin=int(input("ENTER YOUR CARD PIN:"))
            print("")
            y_otp=random.randint(100,999)
            print("YOUR OTP:",y_otp)
            otp=int(input("ENTER OTP:"))
            while otp!=y_otp:
                print("WRONG OTP!")
                otp=int(input("Enter the OTP:"))
            print("AMOUNT RECIEVED SUCCESSFULLY")
            pay="PAID"
            sql="insert into EVEINFO (NO,USER,EVENAME,TYPE,DISTRICT,ADDRESS,COST,PAID)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,event,types,placenew,address,tcosts,pay)
            cursor.execute(sql)
            mycon.commit()

            print("")
            print("")
            print("YOUR EVENT WILL BE MANAGED SUCCESSFULLY BY HAPPENING PRODUCTION")
            print("")

         

     else:
         re=input("ARE YOU SURE YOU DO NOT WANT TO PAY FOR THE EVENT(Y/N):")
         if re.lower()=="n":
             final_payment()
         else:
             pay="NOT PAID"
             sql="insert into EVEINFO (NO,USER,EVENAME,TYPE,DISTRICT,ADDRESS,COST,PAID)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,event,types,placenew,address,tcosts,pay)
             cursor.execute(sql)
             mycon.commit()
             print("")

             




            
                     

def printChoices(menu):
    for key in menu:
        print(key, ".", menu[key])
        
# Snack Module
def snacks():
    print()
    snack = input("DO YOU WISH TO HAVE SNACKS ITEMS IN THE MENU(Y/N):")
    global sn_a
    global categ
    global s_cost
    while True:
        if snack.lower() == "y":
            sn_a="YES" 
            print()
            print("@SPICY CHATS\n@ICECREAMS\n@BEVERAGES\n@POPCORNS\n@SANDWICH&BURGERS\n@KULFI\n")
            while True:
                # Handle case when user accidentally enters an alphabet or a special character
                try:
                    packk = int(input("ENTER NUMBER OF CHOICES YOU WOULD LIKE TO HAVE: "))
                    while packk <= 0 or packk > 6:
                        print("INVALID CHOICE TRY AGAIN")
                        packk = int(input("ENTER NUMBER OF CHOICES YOU WOULD LIKE TO HAVE: "))
                    break
                except:
                    print("PLEASE ENTER A VALID NUMBER.")
            
            print("YOU WILL BE PROVIDED WITH", packk, "CHOICES\n")
            
            # A dictionary to convert number to ordinal text (e.g., 1 to "FIRST")
            numberToText = {1 : "FIRST",
                2 : "SECOND",
                3 : "THIRD",
                4 : "FOURTH",
                5 : "FIFTH", 
                6 : "SIXTH"
                }
            
            # Display the available categories
            print("1-SPICY CHATS\n2-ICECREAMS\n3-BEVERAGES\n4-POPCORNS\n5-SANDWICH&BURGERS\n6-KULFI\n")

            # To store user's category choices
            categories = []
            categ=[]

            # Get user's choices for categories
            for i in range(1, packk + 1):
                while True:
                    # Handle case when user accidentally enters an alphabet or a special character
                    try: 
                        choice = int(input(f"ENTER YOUR {numberToText[i]} CHOICE:"))
                        while choice > 6:
                            print("INVALID CHOICE!! TRY AGAIN!!!! ")
                            choice = int(input(f"ENTER YOUR {numberToText[i]} CHOICE:"))
                        break
                    except:
                        print("YOUR CHOICE MUST BE ASSOCIATED WITH THE CATEGORY!!!\n")

                categories.append(choice)

            # Reorder categories with beverage always at last
            if 3 in categories:
                categories.remove(3)
                categories.append(3)
            
            # Display items under each selected category    
            for category in categories:
                if category == 1:
                    choices="SPICY CHATS" 
                    print("\nSPICY CHATS:")
                    chat = {
                        "1": "PANI PURI",
                        "2": "BHEL PURI",
                        "3": "SEV PURI",
                        "4": "MASALA PURI",
                        "5": "DAHI ALOO CHAT",
                        "6": "MAYONISE PURI",
                        "7": "KATORI CHAT"
                    }
                    printChoices(chat)

                    categ.append(choices)
        
                elif category == 2:
                    choices="ICECREAMS"
                    print("\nICECREAMS:")
                    desserts = {
                        "1": "FRENCH VANILLA",
                        "2": "STRAWBERRY",
                        "3": "COFFEE WALNUT",
                        "4": "COOKIES N CREAM",
                        "5": "ROASTED ALMONDS",
                        "6": "KESAR PISTA",
                        "7": "MIXED BERRIES",
                        "8": "SEA SALT CARAMEL",
                        "9": "MANGO",
                        "10": "CHOCO CHIPS"
                    }
                    printChoices(desserts)
                    categ.append(choices)
                    
                elif category == 3:
                    print("\nBEVERAGES:")
                    print("1-TEA\n2-COFFEE\n3-COCKTAILS\n4-MOCKTAILS")
                    while True:
                        try: 
                            bevg = int(input("ENTER YOUR CHOICE:"))
                            while bevg not in [1, 2, 3, 4]:
                                print("INVALID CHOICE !!")
                                bevg = int(input("1-TEA\n2-COFFEE\n3-COCKTAILS\n4-MOCKTAILS\nENTER YOUR CHOICE OF BEVERAGE:"))
                            break
                        except: 
                            print("YOUR CHOICE SHOULD BE THE NUMBER ASSOCIATED WITH THE BEVERAGE'S CATEGORY!!!\n")
                    
                    if bevg == 1:
                        choices="TEA"
                        print("\nTEA")
                        tea = {
                            "1": "GREEN",
                            "2": "ROYAL ENGLISH",
                            "3": "CHAI",
                            "4": "VANILLA",
                            "5": "BLACK"
                        }
                        printChoices(tea)
                        categ.append(choices)
                        
                    elif bevg == 2:
                        choices="COFFEE"
                        print("\nCOFFEE")
                        coffee = {
                            "1": "ESPRESSO",
                            "2": "LATTE",
                            "3": "CARAMEL",
                            "4": "AMERICANO",
                            "5": "CAPPUCCINO"
                        }
                        printChoices(coffee)
                        categ.append(choices)
                        
                    elif bevg == 3:
                        choices="COCKTAILS"
                        print("\nCOCKTAILS")
                        cocktails = {
                            "1": "MOJITO",
                            "2": "LEMON DROP",
                            "3": "GREEN PARADISE",
                            "4": "PINK LADY"
                        }
                        printChoices(cocktails)
                        categ.append(choices)
                        
                    elif bevg == 4:
                        choices="MOCKTAILS"
                        print("\nMOCKTAILS")
                        mocktails = {
                            "1": "STRAWBERRY DELIGHT",
                            "2": "CRANBERRY COOLER",
                            "3": "E&S SEASONS BEST"
                        }
                        printChoices(mocktails)
                        categ.append(choices)
                        
                elif category == 4:
                    choices="POPCORNS"
                    print("\nPOPCORNS:")
                    pops = {
                        "1": "CHEESE POPCORN",
                        "2": "CARAMEL CRISP",
                        "3": "BUTTER POPCORN",
                        "4": "SWEET POPCORN",
                        "5": "SPICY POPCORN",
                        "6": "CHOCOLATE POPCORN"
                    }
                    printChoices(pops)
                    categ.append(choices)
                   
                elif category == 5:
                    choices="SANDWICH & BURGERS"
                    print("\nSANDWICH & BURGERS:")
                    bs = {
                        "1": "VEG-CHEESE SANDWICH",
                        "2": "BBQ PANEER SANDWICH",
                        "3": "BUTTER CHICKEN BURGER",
                        "4": "AMERICAN CLASSIC",
                        "5": "SMOKE STACK",
                        "6": "CREAMY MUSHROOM"
                    }
                    printChoices(bs)
                    categ.append(choices)
                   
                else:
                    choices="KULFI"
                    print("\nKULFI:")
                    kulfi = {
                        "1": "STICK KESAR PISTA",
                        "2": "STICK PAAN",
                        "3": "STICK ALMOND JAGGERY",
                        "4": "MALAI MATKA",
                        "5": "SLICE"
                    }
                    printChoices(kulfi)
                    categ.append(choices)

            c=0
            for i in categ:
               c=c+1
            s_cost=c*300*people
            print("TOTAL COST OF SNACKS :",s_cost)          
            break
        if snack.lower() == "n":
            categ="NULL"
            sn_a="NO"
            print("NO SNACKS WILL BE PROVIDED")
            s_cost=0
            break
            exit
        else:
            print("INVALID CHOICE ! !")
            snack=input("DO YOU WISH TO HAVE SNACKS ITEMS IN THE MENU(Y/N):")
        continue


       

     
def fud():
   
   
   print("")
   food=input("DO YOU WISH TO HAVE FOOD CATERED BY OUR GROUP(Y/N):")
   global fud
   global bs
   while True:
      if food.lower()=="y":

         fud="YES"
         print("")
         chf={ "1":"BUFFET", "2":"SERVED"}
         for key in chf:
            print(key,".",chf[str(key)])
         chef=int(input("\nENTER YOUR CHOICE:"))

         while True :
            if chef==1:
               chefs=chf[str(chef)]
               print("YOU'LL BE SERVED WITH A WONDERFUL BUFFET")
               bs="BUFFET"
               break
            elif chef==2:
               chefs=chf[str(chef)]
               print("YOU'LL BE SERVED WONDERFULLY")
               bs="SERVED"
               break
            else:
               print("OH NO, IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print("TRY AGAIN")
               print("")
               chef=int(input("\nENTER YOUR CHOICE:"))
               exit                            

         while True:
            print("")
            foodch=int(input("DO YOU PREFER TO HAVE VEG OR MIXED FOOD(1 FOR VEG,2 FOR MIXED):"))
            
            global breakfast
            global lunch
            global dinner
            global vm
            global b_pack
            global l_pack
            global d_pack
            global f_cost
            
            if foodch==1:
               print("")
               if (apm==1 and start<=10):
                  vm="VEG"

                  #only b
                  if maps==1 and end<=12:
                     breakfast="YES"
                     lunch="NULL"
                     dinner="NULL"
                     print("BREAKFAST WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     l_pack="NULL"
                     d_pack="NULL"
                     while True:
                         if b_pp==1:
                             f_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             f_cost=people*200
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)
                     
                  #b and l     
                  elif maps==2 and end<=5:

                     breakfast="YES"
                     lunch="YES"
                     dinner="NULL"

                     print("BREAKFAST AND LUNCH WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     d_pack="NULL"
                     while True:
                         if b_pp==1:
                             b_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             b_cost=people*200
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                             
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     while True:
                         if l_pp==1:
                             l_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     f_cost=b_cost+l_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                  #b, l and d     
                  elif maps==2 and end<=11:

                     breakfast="YES"
                     lunch="YES"
                     dinner="YES"
                     
                     print("BREAKFAST, LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if b_pp==1:
                             b_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             b_cost=people*200                         
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
        
                        
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     while True:
                         if l_pp==1:
                             l_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))


                        
                     print("")
                     print("DINNER MEALS:")
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             d_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             d_cost=people*200                            
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=b_cost+l_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)


               if (apm==1 and (start<12 and start>10)):
                  
                  if maps==2 and end<=5:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="NULL"

                     print("LUNCH WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     d_pack="NULL"        
                     while True:
                         if l_pp==1:
                             f_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             f_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             f_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)



                  #l and d
                  elif maps==2 and end<=11:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="YES"
                     
                     print("LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     while True:
                         if l_pp==1:
                             l_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))

                     print("")
                     print("DINNER MEALS:")
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             l_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             l_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=l_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                        
               if (apm==2 and (start<5 and start>=1)):

                  #only l
                  if maps==2 and end<=5:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="NULL"
                     print("LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     d_pack="NULL"
                     while True:
                         if l_pp==1:
                             f_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             f_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             f_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)



                  #l and d
                  elif maps==2 and end<=11:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="YES"
                     
                     print("LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH SAMBAR, RASAM,BUTTER MILK, CURD RICE, CARROT-CABBAGE FRY, CAULIFLOWER FRY), PAYASAM - Rs.150 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIED RICE, PANEER FRY (KETCHUP ALONG WITH SEASONINGS AND MYONNISE), PINEAPPLE JAM - Rs.120 PER MEAL")
                     print("PACKAGE 3- VEG BIRYANI, CAULIFLOWER FRY, ONION ON CURD, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     while True:
                         if l_pp==1:
                             l_cost=people*150
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*120
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))


                     print("")
                     print("DINNER MEALS:")
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             d_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             d_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=l_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                           

               if apm==2 and (start<=12 and start>=6):
                     breakfast="NULL"
                     lunch="NULL"
                     dinner="YES"
                     
                     print("DINNER WILL BE PROVIDED")
                     print("")
                     print("DINNER MEALS:")
                     print("PACKAGE 1- IDLY,DOSA,PURI WITH POTATO ALONG WITH SAMBAR AND 2 VARIETY CHUTNEY,VADA,KESARI - Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH PANEER BUTTER MASALA, MUSHROOM MASALA, CAULIFLOWER GRAVY, GULAB JAMUN - Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     l_pack="NULL"
                     b_pack="NULL"
                     while True:
                         if d_pp==1:
                             f_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             f_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                             
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

               sql="insert into DEC_FUD_SNACK(NO,USERNAME,DECORATONS,THEME,COLOURS,GAS,FLOWERS,FOOD,BUF_SER,VEG_MIX,BREAKFAST,PACK_B,LUNCH,PACK_L,DINNER,PACK_D,SNACKS)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,dec,colour,mcl,gas,flower,fud,bs,vm,breakfast,b_pack,lunch,l_pack,dinner,d_pack,sn_a)
               cursor.execute(sql)
               mycon.commit()

               break         

                  

            if foodch==2:
               print("")
               vm="MIX"
               if (apm==1 and start<=10):

                  #only b
                  if maps==1 and end<=12:

                     breakfast="YES"
                     lunch="NULL"
                     dinner="NULL"
                     
                     print("BREAKFAST WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     l_pack="NULL"
                     d_pack="NULL"
                     while True:
                         if b_pp==1:
                             f_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             f_cost=people*200
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                     break 
                  
                  #b and l     
                  elif maps==2 and end<=5:

                     breakfast="YES"
                     lunch="YES"
                     dinner="NULL"
                     
                     print("BREAKFAST AND LUNCH WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                                            
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     d_pack="NULL"
                     while True:
                         if b_pp==1:
                             b_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             b_cost=people*200                             
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                  

                        
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     while True:
                         if l_pp==1:
                             l_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=b_cost+l_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)


                             
                     break

                  #b, l and d     
                  elif maps==2 and end<=11:

                     breakfast="YES"
                     lunch="YES"
                     dinner="YES"
                     
                     print("BREAKFAST, LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("\nBREAKFAST MEALS:")                                                            
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if b_pp==1:
                             b_cost=people*120
                             b_pack="PACKAGE 1"
                             break
                         elif b_pp==2:
                             b_cost=people*200
                             b_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             b_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                        
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     while True:
                         if l_pp==1:
                             l_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                             
                  
                     print("")   
                     print("\nDINNER MEALS:")                                                            
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             d_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             d_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     
                     f_cost=l_cost+b_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)


                     
                     break 
                  

               if (apm==1 and (start<12 and start>10)):
                  
                  if maps==2 and end<=5:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="NULL"
                     
                     print("LUNCH WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     d_pack="NULL"
                     while True:
                         if l_pp==1:
                             f_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             f_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             f_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)


                             
                     break
                  
                  #l and d
                  elif maps==2 and end<=11:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="YES"
                     
                     print("LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     while True:
                         if l_pp==1:
                             l_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))


                  
                     print("")   
                     print("\nDINNER MEALS:")                                                            
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             d_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             d_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=l_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                     
                     break 
                  
                  

                        
               if (apm==2 and (start<5 and start>=1)):
                  
                  #only l
                  if maps==2 and end<=5:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="NULL"
                     
                     print("LUNCH WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     d_pack="NULL"
                     while True:
                         if l_pp==1:
                             f_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             f_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             f_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)


                             
                     break

                  #l and d
                  elif maps==2 and end<=11:

                     breakfast="NULL"
                     lunch="YES"
                     dinner="YES"
                     

                     print("LUNCH AND DINNER WILL BE PROVIDED")
                     print("")
                     print("LUNCH MEALS:")
                     print("PACKAGE 1- FULL MEALS (RICE WITH MUTTON GRAVY, CHICKEN DEEP FRY, CURDRICE), BREAD HALWA - Rs.200 PER MEAL")
                     print("PACKAGE 2- NOODLES, FRIEDRICE, CHICKEN FRY (KETCHUP ALONG WITH SEASONINGS AND MAYONNAISE), PINEAPPLE JAM - Rs.150 PER MEAL")
                     print("PACKAGE 3- MUTTON BRIYANI, CHICKEN FRY, HALWA - Rs.200 PER MEAL")
                     l_pp=int(input("ENTER 1 FOR PACKAGE 1, 2 FOR PACKAGE 2 AND 3 FOR PACKAGE 3\nYOUR CHOICE : "))
                     b_pack="NULL"
                     while True:
                         if l_pp==1:
                             l_cost=people*200
                             l_pack="PACKAGE 1"
                             break
                         elif l_pp==2:
                             l_cost=people*150
                             l_pack="PACKAGE 2"
                             break
                         elif l_pp==3:
                             l_cost=people*200
                             l_pack="PACKAGE 3"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("PLEASE TRY AGAIN")
                             print("")
                             l_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                             
                  

                     print("")                                                         
                     print("DINNER WILL BE PROVIDED")
                     print("")
                     print("DINNER MEALS:")                                                       
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     while True:
                         if d_pp==1:
                             d_cost=people*120
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             d_cost=people*200
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     f_cost=l_cost+d_cost
                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                     break 
                  


               if apm==2 and (start<=12 and start>=6):
                     breakfast="NULL"
                     lunch="NULL"
                     dinner="YES"
                     
                     print("DINNER WILL BE PROVIDED")
                     print("")
                     print("DINNER MEALS:")                                                       
                     print("PACKAGE 1- IDLY, DOSA, MUTTON/CHICKEN GRAVY, VADA, KESARI-Rs.120 PER MEAL")
                     print("PACKAGE 2- CHAPPATHI, PAROTTA, NAAN WITH BUTTER CHICKEN WITH CHICKEN FRY,FISH GRAVY WITH FISH FRY,GULAB JAMUN-Rs.200 PER MEAL")
                     d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))
                     b_pack="NULL"
                     l_pack="NULL"
                     while True:
                         if d_pp==1:
                             f_cost=people*150
                             d_pack="PACKAGE 1"
                             break
                         elif d_pp==2:
                             f_cost=people*150
                             d_pack="PACKAGE 2"
                             break
                         else:
                             print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                             print("TRY AGAIN")
                             print("")
                             d_pp=int(input("ENTER 1 FOR PACKAGE 1 AND 2 FOR PACKAGE 2\nYOUR CHOICE : "))

                     print("")
                     print("TOTAL COST FOR FOOD :",f_cost)

                     break 
                  


               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

               sql="insert into DEC_FUD_SNACK(NO,USERNAME,DECORATONS,THEME,COLOURS,GAS,FLOWERS,FOOD,BUF_SER,VEG_MIX,BREAKFAST,PACK_B,LUNCH,PACK_L,DINNER,PACK_D,SNACKS)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,dec,colour,mcl,gas,flower,fud,bs,vm,breakfast,b_pack,lunch,l_pack,dinner,d_pack,sn_a)
               cursor.execute(sql)
               mycon.commit()


    
            break            
         break

                        
      if food.lower()=="n":
         print("NO FOOD REQUIRED")
         fud="NO"
         bs="NULL"
         vm="NULL"
         breakfast="NULL"
         lunch="NULL"
         dinner="NULL"
         f_cost=0
         b_pack="NULL"
         l_pack="NULL"
         d_pack="NULL"

         cursor.execute("select * from EVEINFO")
         cursor.fetchall()
         no=cursor.rowcount
         sno=no+1

         sql="insert into DEC_FUD_SNACK(NO,USERNAME,DECORATONS,THEME,COLOURS,GAS,FLOWERS,FOOD,BUF_SER,VEG_MIX,BREAKFAST,PACK_B,LUNCH,PACK_L,DINNER,PACK_D,SNACKS)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,dec,colour,mcl,gas,flower,fud,bs,vm,breakfast,b_pack,lunch,l_pack,dinner,d_pack,sn_a)
         cursor.execute(sql)
         mycon.commit()

         
         break
      else:
         print("ENTER A VALID CHOICE")
         food=input("DO YOU WISH TO HAVE FOOD CATERED BY OUR GROUP(Y/N):")
         print("")
         exit


#info abt event
      
def evecus(user):

   print("")
   print("")
   print("BEFORE PROCEEDING FURTHER, WE WOULD LIKE TO GET SOME BASIC INFORMATION")
   print("")
   print("|********************|")
   place={"1":" TIRUNELVELI   |",
          "2":" CHENNAI       |",
          "3":" MADURAI       |",
          "4":" TUTICORIN     |",
          "5":" COIMBATORE    |",
          "6":" TRICHY        |",
          "7":" KANNIYAKUMARI |",
          "8":" KANCHIPURAM   |",
          "9":" NILGIRI       |",
          "10":"TIRPUR        |",
          "11":"TENKASI       |",
          "12":"KARUR         |",
          "13":"ERODE         |",
          "14":"RAMANATHAPURAM|",
          "15":"VIRUDHUNAGAR  |",
          "16":"NAMAKKAL      |",
          "17":"SALEM         |",
          "18":"TANJORE       |",
          "19":"DHARMAPURI    |",
          "20":"THENI         |"}
   for key in place:
     print("|",key,".",place[key])
   print("|********************|")
   print("")
   print("PLEASE ENTER THE DISTRICT YOU WOULD LIKE TO HOLD YOUR EVENT IN\n")

   placereal=int(input("ENTER THE DISTRICT NUMBER:"))
   while True :
      if (placereal>=1 and placereal<=20):
         global placenew
         placenew=place[str(placereal)]
         break
      else:
         placereal=int(input("ENTER A VALID CHOICE:"))
         exit
   print("")
   global address
   address=input("ENTER THE ADDRESS OF THE EVENT:") 
   print("")

   #event type

   type1=print("PLEASE SELECT THE TYPE OF EVENT YOU WISH TO HOLD FROM THE FOLLOWING")
   event1={"1":"ENTERTAINMENT EVENTS","2":"SOCIAL EVENTS","3":"CORPORATE EVENTS","4":"SPORTS EVENT","5":"EDUCATIONAL EVENTS"}

   for key in event1:
      print(key,".",event1[key])
   eventmain=int(input("\nENTER THE TYPE OF EVENT : "))
   print("")

   global date
   import datetime
   from datetime import date
   today = date.today()

   date=input("ENTER THE DATE IN WHICH YOU WOULD TO HAVE YOU'RE EVENT(YYYY-MM-DD):")

   while True:
       try:
           event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
           print("")
           break
       except ValueError:
           print("IT SEEMS YOU'VE ENTERED IN THE RIGHT FORMAT. TRY AGAIN!")
           print("")
           date=input("ENTER THE DATE IN WHICH YOU WOULD TO HAVE YOU'RE EVENT(YYYY-MM-DD):")
           exit
           
   print("")
   amp={"1":"AM","2":"PM"}
   global apm
   for key in amp:
      print(key,".",amp[key])
   apm=int(input("ENTER WHETHER THE EVENT IS STARTING AT AM OR PM:"))

   global s_time
   global hours
   global start

   if apm==1:
      print("")
      start=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL START:"))
      print("THE EVENT WILL START AT",start,"a.m")
      s_time=start
      hours="a.m"
      print("")

      
   elif apm==2:
      print("")
      start=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL START:"))
      print("THE EVENT WILL START AT",start,"p.m")
      s_time=start
      hours="p.m"
      print("")
      
   while apm not in [1,2]:
      print("")
      print("IT SEEMS YOU'VE ENTERED THE WRONF INFO")
      print("CHECK AGAIN")
      print("")
      apm=int(input("ENTER WHETHER THE EVENT IS STARTING AT AM OR PM:"))
      if apm==1:
         print("")
         start=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL START:"))
         print("THE EVENT WILL START AT",start,"a.m")
         s_time=start
         hours="a.m"
      
      elif apm==2:
         print("")
         start=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL START:"))
         print("THE EVENT WILL START AT",start,"p.m")
         s_time=start
         ehours="p.m"



   print("")
   amp={"1":"AM","2":"PM"}
   global maps
   for key in amp:
      print(key,".",amp[key])
   maps=int(input("ENTER WHETHER THE EVENT IS ENDING AT AM OR PM:"))
   
   global e_time
   global hour
   global end
   
   if maps==1:
      print("")
      end=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL END APPROXIMATELY:"))
      print("THE EVENT WILL END AT",end,"a.m")
      e_time=end
      hour="a.m"
      print("")
      
   elif maps==2:
      print("")
      end=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL END APPROXIMATELY:"))
      print("THE EVENT WILL END AT",end,"p.m")
      e_time=end
      hour="p.m"
      print("")
      
   while maps not in [1,2]:
      print("")
      print("IT SEEMS YOU'VE ENTERED THE WRONF INFO")
      print("CHECK AGAIN")
      print("")
      maps=int(input("ENTER WHETHER THE EVENT IS ENDING AT AM OR PM:"))
      if maps==1:
         print("")
         end=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL END APPROXIMATELY:"))
         print("THE EVENT WILL END AT",end,"a.m")
         e_time=end
         hour="a.m"
         print("")
         
      elif maps==2:
        print("")
        end=int(input("ENTER THE HOUR AT WHICH THE EVENT WILL END APPROXIMATELY:"))
        print("THE EVENT WILL END AT",end,"p.m")
        e_time=end
        hour="p.m"
        print("")
   


   while True:
      global sno
      global people
      global tcost
      global event
      global types
      global eventname
      global evntname
      if eventmain==1:#entertainment

         event="ENTERTAINMENT|"
         print("")
         print("")
         print("\t\t\t\t\t\t\tENTERTAINMENT EVENTS")
         print("\n\n")
         ch=int(input("1. DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\nPLEASE ENTER WHAT YOU WOULD LIKE:"))
         for i in range(0,400):
            if ch==1:
               types="CREATION     |"
               print("")
               evntname=input("ENTER THE NAME OF YOUR EVENT:")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               
               chairs_(people)
               
               ms()

               pics()

               snw()

               djs()

               dec()

               ref()

               snacks()

               fud()

               tcost=ccost+excc+tco+scost+mcost+pcost+wcost+dcosj+rcost+s_cost+f_cost
 
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1


               sql="insert into CREATION (NO,USERNAME,EVNT_NAME,PEOPLE,CHAIRS,QTY_C,EXTRA_CH,QTY_EXT_C,M_S,SPEAKER_QTY,MICRO_QTY,PHGRAPH,PHGRAPH_QTY,WATER,WAT_QTY,RFR_TAB,DJ)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,chyn,chair,extrch,extra,mis,speaker,micro,pic_s,nopic,wat,no,refresh,dj_s)
               cursor.execute(sql)
               mycon.commit()

               break
            
            elif ch==2:
               types="CUSTOMISATION|"
               print("")
               print("")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               print("HERE IS A LIST OF ALREADY AVAILABLE EVENTS,PLEASE SELECT FROM THEM")
               entevt={
                  "1":"WEDDING CELEBRATION",
                  "2":"BIRTHDAY PARTY",
                  "3":"RECEPTION",
                  "4":"CONCERT"}
               for key in entevt:
                  print(key,".",entevt[key])
               evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
               while True :
                  if (evntname>=1 and evntname<5):
                     eventname=entevt[str(evntname)]
                     print("THE EVENT YOU ARE GOING TO HOST IS A",eventname)
                     break
                  else:
                     print("OH NO, IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                     print("PLEASE TRY AGAIN")
                     print("")
                     evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
                     exit
                     
               packages(people)

               dec()

               ms()

               pics()

               snw()

               snacks()

               fud()


               tcost=tco+s_cost+f_cost+pacost+15000+wcost+scost+mcost+pcost
    
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1
               
               
               sql="insert into CUSTOM (NO,USERNAME,EVNT_NAME,PEOPLE,PACKAGE,CHAIRS,EXTRA_CH)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,packages_p,chairc,exchair)
               cursor.execute(sql)
               mycon.commit()

            else:
               print("OH NO, IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print("PLEASE TRY AGAIN")
               print("")
               ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\nPLEASE ENTER WHAT YOU WOULD LIKE:"))
            break
         break
      
      if eventmain==2:#social

         event="SOCIAL       |"
         print("")
         print("")
         print("\t\t\t\t\t\t\t\tSOCIAL EVENTS")
         print("\n\n")
         ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
         for i in range(0,400):
            if ch==1:
               types="CREATION     |"
               print("")
               evntname=input("ENTER THE NAME OF YOUR EVENT:")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               
               chairs_(people)
               
               ms()

               pics()

               snw()

               djs()
               
               dec()

               ref()

               snacks()

               fud()

               tcost=ccost+excc+tco+scost+mcost+pcost+wcost+dcosj+rcost+s_cost+f_cost

               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1
               

               sql="insert into CREATION (NO,USERNAME,EVNT_NAME,PEOPLE,CHAIRS,QTY_C,EXTRA_CH,QTY_EXT_C,M_S,SPEAKER_QTY,MICRO_QTY,PHGRAPH,PHGRAPH_QTY,WATER,WAT_QTY,RFR_TAB,DJ)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,chyn,chair,extrch,extra,mis,speaker,micro,pic_s,nopic,wat,no,refresh,dj_s)
               cursor.execute(sql)
               mycon.commit()
               
               break
            
            elif ch==2:
               types="CUSTOMISATION|"
               print("")
               print("")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               print("HERE IS A LIST OF ALREADY AVAILABLE EVENTS, SELECT FROM THEM")
               print("")
               entevt={
                  "1":"CHARITY",
                  "2":"POLITICAL EVENT",
                  "3":"HERITAGE CELEBRATION",
                  "4":"PUBLIC FILM SCREENING"}
               for key in entevt:
                  print(key,".",entevt[key])
               print("")
               evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
               while True :
                  if (evntname>=1 and evntname<5):
                     eventname=entevt[str(evntname)]
                     print("THE EVENT YOU ARE GOING TO HOST IS A",eventname)
                     break
                  else:
                     print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                     print(" TRY AGAIN")
                     print("")
                     evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
                     exit
         
               packages(people)

               dec()

               ms()

               pics()

               snw()

               snacks()

               fud()


               tcost=tco+s_cost+f_cost+pacost+15000+wcost+scost+mcost+pcost
               
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

               sql="insert into CUSTOM (NO,USERNAME,EVNT_NAME,PEOPLE,PACKAGE,CHAIRS,EXTRA_CH)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,packages_p,chairc,exchair)
               cursor.execute(sql)
               mycon.commit()

                 
            else:
               print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print(" TRY AGAIN")
               print("")
               ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
            break
         break
      if eventmain==3:#corporate

         event="CORPORATE    |"
         print("")
         print("")
         print("\t\t\t\t\t\t\tCORPORATE EVENTS")
         print("\n\n")
         ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
         for i in range(0,400):
            if ch==1:
               types="CREATION     |"
               print("")
               evntname=input("ENTER THE NAME OF YOUR EVENT:")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               
               chairs_(people)

               ms()

               pics()

               snw()

               djs()

               dec()

               ref()

               snacks()

               fud()

               tcost=ccost+excc+tco+scost+mcost+pcost+wcost+dcosj+rcost+s_cost+f_cost               

               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

               
               sql="insert into CREATION (NO,USERNAME,EVNT_NAME,PEOPLE,CHAIRS,QTY_C,EXTRA_CH,QTY_EXT_C,M_S,SPEAKER_QTY,MICRO_QTY,PHGRAPH,PHGRAPH_QTY,WATER,WAT_QTY,RFR_TAB,DJ)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,chyn,chair,extrch,extra,mis,speaker,micro,pic_s,nopic,wat,no,refresh,dj_s)
               cursor.execute(sql)
               mycon.commit()               
               
               break
            
            elif ch==2:
               types="CUSTOMISATION|"
               print("")
               print("")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               print("HERE IS A LIST OF ALREADY AVAILABLE EVENTS, SELECT FROM THEM")
               print("")
               entevt={
                  "1":"SEMINAR",
                  "2":"LAUNCH PARTY",
                  "3":"FUND RAISING",
                  "4":"APPRECIATION EVENT",
                  "5":"BOARD MEETING",
                  "6":"TEAM BUILDING ACTIVITY",
                  "7":"SHAREHOLDER MEETING",
                  "8":"AWARD CEREMONY",
                  "9":"COMPANY MILESTONE"}
               for key in entevt:
                  print(key,".",entevt[key])
               print("")
               evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
               while True :
                  if (evntname>=1 and evntname<10):
                     eventname=entevt[str(evntname)]
                     print("THE EVENT YOU ARE GOING TO HOST IS A",eventname)
                     break
                  else:
                     print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                     print("TRY AGAIN")
                     print("")
                     evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
                     exit
         
               packages(people)

               dec()

               ms()

               pics()

               snw()

               snacks()

               fud()


               tcost=tco+s_cost+f_cost+pacost+15000+wcost+scost+mcost+pcost
    
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1


               sql="insert into CUSTOM (NO,USERNAME,EVNT_NAME,PEOPLE,PACKAGE,CHAIRS,EXTRA_CH)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,packages_p,chairc,exchair)
               cursor.execute(sql)
               mycon.commit()

               
            else:
               print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print("TRY AGAIN")
               print("")
               ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
            break
         break

      if eventmain==4:#sports

         event="SPORTS       |"
         print("")
         print("")
         print("\t\t\t\t\t\t\tSPORTS EVENTS")
         print("\n\n")
         ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
         for i in range(0,400):
            if ch==1:
               types="CREATION     |"
               print("")
               evntname=input("ENTER THE NAME OF YOUR EVENT:")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               
               chairs_(people)

               ref()
               
               ms()

               pics()

               snw()

               djs()

               dec()

               ref()

               snacks()

               fud()

               tcost=ccost+excc+tco+scost+mcost+pcost+wcost+dcosj+rcost+s_cost+f_cost

               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

 

               sql="insert into CREATION (NO,USERNAME,EVNT_NAME,PEOPLE,CHAIRS,QTY_C,EXTRA_CH,QTY_EXT_C,M_S,SPEAKER_QTY,MICRO_QTY,PHGRAPH,PHGRAPH_QTY,WATER,WAT_QTY,RFR_TAB,DJ)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,chyn,chair,extrch,extra,mis,speaker,micro,pic_s,nopic,wat,no,refresh,dj_s)
               cursor.execute(sql)
               mycon.commit()
               
               break
            
            elif ch==2:
               types="CUSTOMISATION|"
               print("")
               print("")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               print("HERE IS A LIST OF ALREADY AVAILABLE EVENTS, SELECT FROM THEM")
               print("")
               entevt={
                  "1":"INDUVIDUAL SPORTS",
                  "2":"EXTREME SPORTS",
                  "3":"TEAM SPORTS",
                  "4":"PARTNER SPORTS"}
               for key in entevt:
                  print(key,".",entevt[key])
               print("")
               evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
               while True :
                  if (evntname>=1 and evntname<10):
                     eventname=entevt[str(evntname)]
                     print("THE EVENT YOU ARE GOING TO HOST IS ",eventname)
                     break
                  else:
                     print(" IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                     print("TRY AGAIN")
                     print("")
                     evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
                     exit
         
               packages(people)

               dec()

               ms()

               pics()

               snw()

               snacks()

               fud()

               tcost=tco+s_cost+f_cost+pacost+15000+wcost+scost+mcost+pcost
    
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1


               sql="insert into CUSTOM (NO,USERNAME,EVNT_NAME,PEOPLE,PACKAGE,CHAIRS,EXTRA_CH)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,packages_p,chairc,exchair)
               cursor.execute(sql)
               mycon.commit()

                
               
            else:
               print("OH NO, IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print("TRY AGAIN")
               print("")
               ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
            break
         break   
      if eventmain==5:#education
         
 
         event="EDUCATION    |"
         print("")
         print("")
         print("\t\t\t\t\t\t\tEDUCATIONAL EVENTS")
         print("\n\n")
         ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
         for i in range(0,400):
            if ch==1:
               types="CREATION     |"
               print("")
               evntname=input("ENTER THE NAME OF YOUR EVENT:")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               
               chairs_(people)
               
               ms()

               pics()

               snw()

               djs()

               dec()

               ref()

               snacks()

               fud()

               tcost=ccost+excc+tco+scost+mcost+pcost+wcost+dcosj+rcost+s_cost+f_cost
 
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1

               sql="insert into CREATION (NO,USERNAME,EVNT_NAME,PEOPLE,CHAIRS,QTY_C,EXTRA_CH,QTY_EXT_C,M_S,SPEAKER_QTY,MICRO_QTY,PHGRAPH,PHGRAPH_QTY,WATER,WAT_QTY,RFR_TAB,DJ)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,chyn,chair,extrch,extra,mis,speaker,micro,pic_s,nopic,wat,no,refresh,dj_s)
               cursor.execute(sql)
               mycon.commit()

                              
               break
         
            elif ch==2:
               types="CUSTOMISATION|"
               print("")
               print("")
               people=int(input("ENTER THE NUMBER OF PEOPLE ATTENDING:"))
               print("")
               print("HERE IS A LIST OF ALREADY AVAILABLE EVENTS, SELECT FROM THEM")
               print("")
               entevt={
                  "1":"GRADUATION",
                  "2":"FAREWELL",
                  "3":"ANNUAL DAY",
                  "4":"SPORTS DAY",
                  "5":"FOOD CARNIVAL",
                  "6":"MUSIC FESTIVAL",
                  "7":"TALENT DAY",
                  "8":"SCHOOL COMPETITIONS"}
               for key in entevt:
                  print(key,".",entevt[key])
               print("")
               evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
               while True :
                  if (evntname>=1 and evntname<9):
                     eventname=entevt[str(evntname)]
                     print("THE EVENT YOU ARE GOING TO HOST IS A",eventname)
                     break
                  else:
                     print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
                     print("TRY AGAIN")
                     print("")
                     evntname=int(input("ENTER THE EVENT YOU'D LIKE TO HOST:"))
                     exit
         
               packages(people)

               dec()

               ms()

               pics()

               snw()

               snacks()

               fud()

               tcost=tco+s_cost+f_cost+pacost+15000+wcost+scost+mcost+pcost
               
                
               cursor.execute("select * from EVEINFO")
               cursor.fetchall()
               no=cursor.rowcount
               sno=no+1


               sql="insert into CUSTOM (NO,USERNAME,EVNT_NAME,PEOPLE,PACKAGE,CHAIRS,EXTRA_CH)values('{}','{}','{}','{}','{}','{}','{}')".format(sno,user,evntname,people,packages_p,chairc,exchair)
               cursor.execute(sql)
               mycon.commit()

                 
               
               
            else:
               print("IT SEEMS YOU'VE ENTERED THE WRONG INFO")
               print("TRY AGAIN")
               print("")
               ch=int(input("1.DO YOU WISH TO HAVE THE EVENT CUSTOMISED BY YOURSELF \n2. CHECK ALREADY AVAILABLE EVENTS\n\n ENTER WHAT YOU WOULD LIKE:"))
            break
         break



def log():

#login

   print("")
   print("TO LOGIN ENTER THE FOLLOWING DETAILS")
   print("")
   global user
   user=input("ENTER USER ID: ")
   pw=input("ENTER PASSWORD: ")
   login=False
   sql="select * from login"
   cursor.execute(sql)
   for i in cursor:
      if i[0]==user and i[2]==pw:
         print("")
         print("WELCOME ",user,", WE HOPE TO FULFILL YOUR DREAMS")
         login=True
         continue
   if login==True:
      homepage(user)

   if login==False:
      print("IT SEEMS YOU  MIGHT HAVE ENTERED THE WRONG INPUT")
      print("DO YOU WISH TO CONTINUE OR STOP THE PROCESS")
      print("\nIF YOU WISH TO CONTINUE ENTER 0")
      print("IF YOU WISH TO STOP ENTER 1")
      last=int(input("\nSO, ENTER YOUR CHOICE:"))
      if last==0:
         print("")
         print("WE WELCOME YOU AGAIN TO HAPPENING PRODUCTION\n")
         mainmenu()
      elif last==1:
         print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
         print("\n\t\t\t\t\t\t\t     VISIT AGAIN")
         sys.exit()


def sign():

#sign up
   global name
   print("")
   print("TO SIGN UP ENTER THE FOLLOWING DETAILS")
   print("")
   name=input("ENTER NAME: ")
   while name.isdigit()==True or name.isalpha==False:
         print("NAME YOU'VE ENTERED IS WRONG")
         print("TRY AGAIN")
         print("")
         name=input("ENTER NAME: ")

         
   user=input("CREATE USER ID: ")
   while True:
      cursor.execute("select USERNAME from LOGIN where USERNAME='" + user + "'")
      data=cursor.fetchall()
      while data:
         cursor.execute("select USERNAME from LOGIN where USERNAME='" + user + "'")
         data=cursor.fetchall()  
         for i in data:
            if i[0]==user:           
              print("")
              print("THIS USERNAME'S ALREADY TAKEN")
              print("USE ANOTHER =)")
              print("")
              user=input("CREATE USER ID: ")
              
            else:
              break
     
      break
          
      
      
   

   pw=input("CREATE A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")
   while len(pw)<8 or len(pw)==8:
      print("YOU'VE ENTERED THE WRONG INPUT")
      print("CHECK AGAIN")
      pw=input("\nENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")


   contact=(input("ENTER YOUR CONTACT NUMBER: "))
   while len(contact)!=10 or contact.isdigit()!=True:
      print("YOU'VE ENTERED THE WRONG INPUT")
      print("CHECK AGAIN")
      contact=input("\nENTER YOUR CONTACT NUMBER: ")

   print("")
   sql="insert into LOGIN (USERNAME,NAME,PASSWORD,CONTACT)values('{}','{}','{}','{}')".format(user,name,pw,contact)
   cursor.execute(sql)
   mycon.commit()
   print("\nACCOUNT CREATED SUCCESSFULLY")
   log()
   
mycon.commit()


def changepassword(user):
   k=input("DO YOU KNOW YOUR OLD PASSWORD(Y/N):")
   while True:
      if k.lower()=='y':
         op=input("ENTER YOUR OLD PASSWORD:")
         pw=input("ENTER NEW PASSWORD : ")
         while len(pw)<8:
            print("MINIMUM CHARACTERS REQUIRED IS 8")
            print("")
            pw=input("ENTER NEW PASSWORD : ")
            
         while op==pw:
            print("OLD PASSWORD SAME AS NEW PASSWORD")
            print("")
            pw=input("ENTER NEW PASSWORD : ")
            
         else:
             repw=input("RE-ENTER NEW PASSWORD : ")
             print()
             if pw==repw:
                 sql="update login set password='"+pw+"' where username='"+user+"'"
                 cursor.execute(sql)
                 mycon.commit()
                 print("PASSWORD CHANGED SUCCESSFULLY")

                 break
                
             else:
                 print("INVALID CREDENTIALS")


      elif k.lower()=='n':
           na=input("ENTER USERNAME:")
           ph=input("ENTER PHONE NUMBER:")
           cursor.execute("select * from login")
           for i in cursor:
               if i[0]==na and i[3]==ph:
                  pw=input("ENTER NEW PASSWORD : ")
                  while len(pw)<8:
                     print("MINIMUM CHARACTERS REQUIRED IS 8")
                     print("")
                     pw=input("ENTER NEW PASSWORD : ")
                  while op==pw:
                     print("OLD PASSWORD SAME AS NEW PASSWORD")
                     print("")
                     pw=input("ENTER NEW PASSWORD : ")
                  else:
                      repw=input("RE-ENTER NEW PASSWORD : ")
                      print()
                      if pw==repw:
                          sql="update login set password='"+pw+"' where username='"+user+"'"
                          cursor.execute(sql)
                          mycon.commit()
                          print("PASSWORD CHANGED SUCCESSFULLY")

                         
                      else:
                          print("INVALID CREDENTIALS")

      else:
           print("INVALID INPUT")

           
def inspect4():
    ch="y"
    while ch.lower()=="y":
        place={"1":"TIRUNELVELI","2": "CHENNAI","3": "MADURAI","4": "TUTICORIN ","5":"COIMBATORE","6":"TRICHY", "7": "KANNIYAKUMARI","8":"KANCHIPURAM", "9": "NILGIRI", "10":"TIRPUR", "11": "TENKASI" ,"12": "KARUR" ,"13": "ERODE" ,"14": "RAMANATHAPURAM", "15": "VIRUDHUNAGAR" ,"16":"NAMAKKAL","17":"SALEM","18": "TANJORE","19": "DHARMAPURI", "20": "THENI"}
        print("ENTER THE DISTRICT YOU WOULD LIKE TO SEARCH \n")
        for key in place:
            print(key,".",place[key])
        placereal=int(input("ENTER THE DISTRICT NUMBER:"))
        while True :
            if (placereal>=1 and placereal<=20):
               placenew=place[str(placereal)]
               cursor.execute("select * from eveinfo where district='" + placenew + "'")
               data=cursor.fetchall()
               if data:
                  print("")
                  print(("*"*141).center(140))
                  print("{:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
                  print(("*"*141).center(140))
                  print("")
                  for i in data:
                     print("{:5s}   {:1s}   {:10s}       {:2s}\t{:5s}\t{:5s}\t\t\t{:40s}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(10))
                  print(("_"*141).center(140))
                  mycon.commit()

                  
                  break
               else:
                  print("")
                  print("NO EVENT AVAILABLE IN THAT DISTRICT")
                  break
                  
            else:
               placereal=int(input("PLEASE ENTER A VALID CHOICE:"))
               exit
        print("")       
        ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):")

def adduser():
   print("")
   name=input("ENTER NAME: ")
   while name.isdigit()==True or name.isalpha==False:
         print("NAME YOU'VE ENTERED IS WRONG")
         print("TRY AGAIN")
         print("")
         name=input("ENTER NAME: ")
          
   user=input("ENTER USER ID: ")
   while True:
      sql="select * from login"
      cursor.execute(sql)
      for i in cursor:
         if i[0]==user:
            print("")
            print("THIS USERNAME'S ALREADY TAKEN")
            print("ENTER ANOTHER =)")
            print("")
            user=input("CREATE USER ID: ")
         else:
            break
      break   
   pw=input("CREATE A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")
   while len(pw)<8 or len(pw)==8:
      print("YOU'VE ENTERED THE WRONG INPUT")
      print("CHECK AGAIN")
      pw=input("\nENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")

   contact=(input("ENTER CONTACT NUMBER: "))
   while len(contact)!=10 or contact.isdigit()!=True:
      print("YOU'VE ENTERED THE WRONG INPUT")
      print("CHECK AGAIN")
      contact=input("\nENTER CONTACT NUMBER: ")

   print("")
   sql="insert into LOGIN (USERNAME,NAME,PASSWORD,CONTACT)values('{}','{}','{}','{}')".format(user,name,pw,contact)
   cursor.execute(sql)
   mycon.commit()
   print("\nACCOUNT CREATED SUCCESSFULLY")

def searchuser():
   print("")
   na=input("ENTER USER ID:")
   cursor.execute("select * from LOGIN where username='" + na + "'")
   data=cursor.fetchall()
   if data:
      print("")
      print(("-"*140).center(140))
      print("{:10s} \t\t{:15s}\t{:15s}\t{:20s}".format("USER","NAME","PASSWORD","CONTACT"))
      print(("-"*140).center(140))

      for i in data:
         print("{:20s}\t{:15s}\t{:15s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
      print(("-"*140).center(140))

   else:
      print("USER NOT FOUND")
      print("")

   ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):")
   
   while ch.lower()=='y':
       na=input("ENTER USER ID:")
       cursor.execute("select * from LOGIN where username='" + na + "'")
       data=cursor.fetchall()
       if data:
          print("")
          print(("-"*140).center(140))
          print("{:10s} \t\t{:15s}\t{:15s}\t{:20s}".format("USER","NAME","PASSWORD","CONTACT"))
          print(("-"*140).center(140))
          for i in data:
             print("{:20s}\t{:15s}\t{:15s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
          print(("-"*140).center(140))
          ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):")


       else:
          print("USER NOT FOUND")
          print("")
          ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):") 

       if ch.lower()=='n':
           break

def deluser():
   print("")
   na=input("ENTER THE USER ID OF THE PERSON'S DATA YOU WISH TO DELETE:")
   cursor.execute("delete from LOGIN where username='" + na + "'")
   print("DELETED SUCCESSFULLY")
   mycon.commit()


def eduser():    
     print("")
     user=input("ENTER NEW USER NAME:")
     while na==user:
        print("")
        print("THIS USERNAME'S ALREADY TAKEN")
        print("USE ANOTHER =)")
        print("")
        user=input("CREATE USER ID: ")
     cursor.execute("select * from LOGIN where username='" + na + "'")
     data=cursor.fetchall()

     print("")
     print("USER ID CHANGED SUCCESSFULLY")
     cursor.execute("update login set username='{}' where username='{}'".format(user,na))
     cursor.execute("select * from EVEINFO where username='" + na + "'")
     data=cursor.fetchall()
     cursor.execute("update EVEINFO set user='{}' where user='{}'".format(user,na))
     
     mycon.commit()  

def edname():
     print("")
     name=input("ENTER NEW NAME: ")
     while name.isdigit()==True or name.isalpha==False:
           print("NAME YOU'VE ENTERED IS WRONG")
           print("TRY AGAIN")
           print("")
           name=input("ENTER NAME: ")
     print("")
     print("NAME CHANGED SUCCESSFULLY")
     cursor.execute("update login set name='{}' where username='{}'".format(name,na))
     mycon.commit()

def edcon():

     print("")
     contact=(input("ENTER YOUR CONTACT NUMBER: "))
     while len(contact)!=10 or contact.isdigit()!=True:
        print("YOU'VE ENTERED THE WRONG INPUT")
        print("CHECK AGAIN")
        contact=input("\nENTER YOUR CONTACT NUMBER: ")
     print("") 
     print("CONTACT CHANGED SUCCESSFULLY")
     cursor.execute("update login set contact='{}' where username='{}'".format(contact,na))
     mycon.commit()

def edpw():
     print("")
     pw=input("ENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")
     while len(pw)<8 or len(pw)==8:
        print("YOU'VE ENTERED THE WRONG INPUT")
        print("CHECK AGAIN")
        pw=input("\nENTER A PASSWORD, IT SHOULD NOT BE LESS THAN 8: ")
     print("")
     print("PASSWORD CHANGED SUCCESSFULLY")
     cursor.execute("update login set password='{}' where username='{}'".format(pw,na))
     mycon.commit()

def evesearch():
     print("")
     na=input("ENTER USER ID:")
     cursor.execute("select * from eveinfo where user='" + na + "'")
     data=cursor.fetchall()
     if data:

        print(("*"*141).center(140))
        print("{:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
        print(("*"*141).center(140))
        print("")
        for i in data:
           print("{:5s}   {:1s}   {:10s}  {:2s}\t{:5s}\t\t\t{:5s}\t\t{:40s}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(10))
        print(("_"*141).center(140))
        mycon.commit()
        print("")



     else:
        print("USER NOT FOUND")
        print("")
        
     ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):")
     
     while ch.lower()=='y':
         na=input("ENTER USER ID:")
         cursor.execute("select * from eveinfo where user='" + na + "'")
         data=cursor.fetchall()
         if data:

            print("")
            print(("*"*141).center(140))
            print("{:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
            print(("*"*141).center(140))
            print("")
            for i in data:
               print("{:5s}   {:1s}   {:10s}  {:2s}\t{:5s}\t\t\t{:5s}\t\t{:40s}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(10))
            print(("_"*141).center(140))
            mycon.commit()
  
            ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):")                              

         else:
            print("USER NOT FOUND")
            print("")
            ch=input("DO YOU WISH TO SEARCH FOR MORE USERS?(Y/N):") 


def deleve():
   print("")
   na=input("ENTER USER ID:")
   cursor.execute("select * from eveinfo where USER='" + na + "'")
   data=cursor.fetchall()
   if data:

      print("")
      print(("*"*141).center(140))
      print("{:5} {:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t\t{:40s}".format("NO","USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
      print(("*"*141).center(140))
      print("")
      for i in data:
         print("{:1}\t{:5s}   {:1s}   {:10s}  {:2s}\t{:5s}\t\t\t{:5s}\t\t{:40s}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(10))
      print(("_"*141).center(140))
      mycon.commit()


      dele=int(input("ENTER THE NUMBER OF THE DATA WHICH YOU'D LIKE TO DELETE:"))


      for i in data:
           if i[0]==dele:
                cursor.execute("delete from eveinfo where NO={}".format(dele))
             
                print("DELETED SUCCESSFULLY")
                mycon.commit()

   else:
        print("")
        print("USER NOT FOUND")



def admin():
    print("")
    print("")
    ids="Suprathaa"
    pw="Arshi_sudar"
    ida=input("ENTER THE USER ID :")
    pwd=input("ENTER THE PASSWORD :")
    if ida==ids and pwd==pw:
        print("_"*141)
        print("~"*141)
        print("\n\t\t\t\t\t\t\t\tWELCOME ADMIN")
        print("_"*141)
        print("~"*141)
        print("")        
        print("")
        print("HAPPENING PRODUCTION INFO'S:")
        print("1-USER INFO")
        print("2-EVENT INFO")
        print("3-EDIT")
        print("4-SEARCH BY DISTRICT")
        print("")
        def inspects():
           inspect=int(input("WHICH INFO WOULD YOU LIKE TO INSPECT (1/2/3/4): "))
           while True:
              if inspect==1:
                 sql="create table if not exists USERINFOAD(USER varchar(35) primary key,NAME varchar(35),PASSWORD varchar(20), CONTACT varchar(15) unique)"
                 cursor.execute(sql)
                 cursor.execute("select count(USERNAME) from login ")
                 for i in cursor:
                     i=str(i)
                 a=i[1:-2]
                 if a=="0":
                     cursor.execute("select count(USER) from userinfoad ")
                     for i in cursor:
                         i=str(i)
                     a=i[1:-2]
                     if a=="0":
                        cursor.execute("insert into USERINFOAD values('Jayx    ','Jayden     ','JAyden23-  ','7887602567')")
                        cursor.execute("insert into USERINFOAD values('Sway    ','Swyana     ','Swyana@12  ','9197832488')")
                        cursor.execute("insert into USERINFOAD values('Sanx    ','Sandru     ','SAndrU.l   ','6127988532')")
                        cursor.execute("insert into USERINFOAD values('ANa13   ','Anathika   ','ANathi13@  ','6748817426')")
                        cursor.execute("insert into USERINFOAD values('Omsi    ','Omia       ','Omimi293   ','8079562857')")
                        cursor.execute("insert into USERINFOAD values('Yanu    ','Yanuesh    ','YANa123+   ','7477043039')")
                        cursor.execute("insert into USERINFOAD values('Chris.x ','Chrissie   ','Chriss-    ','7887660378')")
                        cursor.execute("insert into USERINFOAD values('Sava    ','Savana     ','Savanaaa-2 ','9525023902')")
                        cursor.execute("insert into USERINFOAD values('Pran.v  ','Pranav     ','Pravv123   ','9811046724')")
                        cursor.execute("insert into USERINFOAD values('V.arnish','Varnish    ','21VArnish  ','4055240099')")
                        cursor.execute("insert into USERINFOAD values('Sunny   ','Sunil      ','Sunny123-  ','8022446571')")
                        cursor.execute("insert into USERINFOAD values('Samyu   ','Samyuktha  ','Samyu.ktha ','7955121427')")
                        cursor.execute("insert into USERINFOAD values('KUshi   ','Kushi Gupta','KUgu2432-  ','2084425481')")
                        cursor.execute("insert into USERINFOAD values('Amfa    ','Ameer      ','Gohan19295 ','6284422881')")
                        cursor.execute("insert into USERINFOAD values('Javis   ','Javidh     ','JAvidh1212@','9084422481')")
                        cursor.execute("insert into USERINFOAD values('Akshi   ','Akshitha   ','akshi.tha  ','9512924696')")
                        cursor.execute("insert into USERINFOAD values('Alasa   ','Alasa      ','Alasai.you ','6549798853')")
                        cursor.execute("insert into USERINFOAD values('K.mar   ','Kumar      ','Kumar123   ','1231545456')")
                        cursor.execute("insert into USERINFOAD values('Manju   ','Manjula    ','Manju1243  ','6464732178')")
                        cursor.execute("insert into USERINFOAD values('Sub.sh  ','Subash     ','Subash@987 ','5246473655')")   
                        cursor.execute("insert into USERINFOAD values('Shruthi ','Shruthi    ','Shru.thi   ','5344213421')")
                        cursor.execute("insert into USERINFOAD values('Vishal  ','Vishal     ','Vishal9876 ','9364376584')")
                        cursor.execute("insert into USERINFOAD values('Yasar   ','Yasar      ','YA.sar213  ','8985232545')")
                        cursor.execute("insert into USERINFOAD values('Vishnu  ','Vishnu     ','Vish.nu@-  ','4563545644')")
                        cursor.execute("insert into USERINFOAD values('Krish   ','Krishna    ','Krish.xx.na','3542543545')")
                        cursor.execute("select * from USERINFOAD")
                        data=cursor.fetchall()

                        print(("*"*140).center(140))
                        print("{:10s} \t\t{:15s}\t{:15s}\t{:20s}".format("USER","NAME","PASSWORD","CONTACT"))
                        print(("*"*140).center(140))

                        for i in data:
                           print("{:20s}\t{:15s}\t{:15s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
                        print(("*"*140).center(140))

                     else:
                        cursor.execute("select * from userinfoad")
                        data=cursor.fetchall()

                        print(("*"*140).center(140))
                        print("{:10s} \t\t{:15s}\t{:15s}\t{:20s}".format("USER","NAME","PASSWORD","CONTACT"))
                        print(("*"*140).center(140))

                        for i in data:
                           print("{:20s}\t{:15s}\t{:15s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
                        print(("*"*140).center(140))
                         
                 else:
                    cursor.execute("select * from LOGIN")
                    data=cursor.fetchall()
                    print("")
                    print(("*"*140).center(140))
                    print("{:10s} \t\t{:15s}\t{:15s}\t{:20s}".format("USER","NAME","PASSWORD","CONTACT"))
                    print(("*"*140).center(140))

                    for i in data:
                       print("{:20s}\t{:15s}\t{:15s}\t{:20s}".format(i[0],i[1],i[2],i[3]))
                    print(("*"*140).center(140))
                    
                 break


              if inspect==2:
                 sql="create table if not exists EVEINFOAD(USER varchar(35),EVENAME varchar(35),TYPE varchar(35),DISTRICT varchar(35),ADDRESS varchar(50),COST varchar(35),PAID varchar(35))"
                 cursor.execute(sql)
                 cursor.execute("select count(USER) from EVEINFO")
                 for i in cursor:
                     i=str(i)
                 a=i[1:-2]
                 if a=="0":
                     cursor.execute("select count(USER) from EVEINFOAD")
                     for i in cursor:
                         i=str(i)
                     a=i[1:-2]
                     if a=="0":
                        cursor.execute("insert into EVEINFOAD values('Jayx    ','SPORTS       ','CREATION     ','TIRUNELVELI   ','ANNA STADIUM              ','100000','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Sway    ','ENTERTAINMENT','CUSTOMISATION','CHENNAI       ','KALACHETRAM               ','55000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Sanx    ','SOCIAL       ','CREATION     ','THENI         ','ANNA STADIUM              ','35000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('ANa13   ','CORPORATE    ','CREATION     ','MADURAI       ','NEWLAND AUDITORIUM        ','45000 ','NOT PAID')")      
                        cursor.execute("insert into EVEINFOAD values('Omsi    ','EDUCATION    ','CUSTOMISATION','TRICHY        ','NIT COLLEGE               ','55000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Yanu    ','EDUCATION    ','CUSTOMISATION','VIRUDHUNAGAR  ','COLAKA SCHOOLS            ','55000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Yasar   ','SPORTS       ','CREATION     ','TUTUCORIN     ','TRACKS AND FIELD VISWAS   ','50000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Alasa   ','SOCIAL       ','CUSTOMISATION','COIMBATORE    ','PSG COLLEGE               ','30000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Vishal  ','ENTERTAINMENT','CREATION     ','ERODE         ','KONGU COLLEGE             ','200000','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Akshi   ','CORPORATE    ','CUSTOMISATION','KANNIYAKUMARI ','HOTRAN MAHAL              ','30000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Vishnu  ','EDUCATION    ','CREATION     ','KARUR         ','SAVITA SCHOOLS            ','75000,','PAID    ')")  
                        cursor.execute("insert into EVEINFOAD values('K.mar   ','SPORTS       ','CREATION     ','SALEM         ','ANNA STADIUM              ','17000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Krish   ','SOCIAL       ','CUSTOMISATION','NILGIRI       ','ST THOMAS ROAD            ','55000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Shruthi ','EDUCATION    ','CUSTOMISATION','TANJORE       ','ROSEBUDS SCHHOLS          ','30000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Chris.x ','SPORTS       ','CREATION     ','DHARMAPURI    ','DOKITO SPORTS STADIUM     ','50000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Sava    ','SOCIAL       ','CREATION     ','RAMANATHAPURAM','KIRCHOS AUDITORIUM        ','50000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('V.arnish','SPORTS       ','CREATION     ','MADURAI       ','ANNA STADIUM              ','25000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Amfa    ','ENTERTAINMENT','CUSTOMISATION','TIRUNELVELI   ','MOC MAHAL                 ','250000','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Javis   ','ENTERTAINMENT','CUSTOMISATION','TIRUNELVELI   ','BLUE MOON AUDITORIUM      ','90000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Pran.v  ','SPORTS       ','CREATION     ','SALEM         ','ALLWIN STADIUM            ','45000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Samyu   ','SOCIAL       ','CREATION     ','TENKASI       ','RAMESH STUDIOS            ','75000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('KUshi   ','CORPORATE    ','CREATION     ','TIRPUR        ','VS MANAGEMENTS            ','60000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Manju   ','EDUCATION    ','CUSTOMISATION','TIRUNELVELI   ','PUSHPALATA VIDYA MANDIR   ','75000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Sub.sh  ','SPORTS       ','CREATION     ','CHENNAI       ','PRIMROSE SCHOOLS          ','45000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Pran.v  ','SOCIAL       ','CUSTOMISATION','NAMAKKAL      ','KAMARAJAR STREET          ','70000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('V.arnish','CORPORATE    ','CREATION     ','KANCHIPURAM   ','AUDITORIUM VDS            ','90000 ','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Amfa    ','SPORTS       ','CUSTOMISATION','CHENNAI       ','MICHEAL BASKETBALL STADIUM','100000','PAID    ')")     
                        cursor.execute("insert into EVEINFOAD values('Javis   ','CORPORATE    ','CUSTOMISATION','MADURAI       ','NEWLAND STADIUM           ','700000','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('Samyu   ','CORPORATE    ','CREATION     ','MADURAI       ','NEWLAND AUDITORIUM        ','90000 ','NOT PAID')")     
                        cursor.execute("insert into EVEINFOAD values('KUshi   ','SPORTS       ','CREATION     ','CHENNAI       ','B&B FOOTBALL STADIUM      ','78000 ','PAID    ')")     
                        cursor.execute("select * from EVEINFOAD")
                        data=cursor.fetchall()
                        print("")

                        print(("*"*141).center(140))
                        print("{:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
                        print(("*"*141).center(140))
                        print("")
                        for i in data:
                           print("{:5s}   {:1s}   {:10s}   {:2s}\t{:5s}\t{:5s}\t{:40s}".format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]).center(120))
                        print(("_"*141).center(140))
                        mycon.commit()

                     else: 
                        cursor.execute("select * from EVEINFOAD")
                        data=cursor.fetchall()
                        print("")

                        print(("*"*141).center(140))
                        print("{:5s}\t   {:1s}         {:5s}  \t     {:2s} \t\t{:5s}\t\t\t\t{:5s}\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
                        print(("*"*141).center(140))
                        print("")
                        for i in data:
                           print("{:5s}   {:1s}   {:10s}   {:2s} {:5s}\t{:5s}\t{:40s}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(120))
                        print(("_"*141).center(140))
                        mycon.commit()



                 else:
                    cursor.execute("select * from EVEINFO")
                    data=cursor.fetchall()
                    print("")
                    print(("*"*141).center(140))
                    print("{:5s}\t   {:1s}         {:5s} \t   {:2s} \t\t{:5s}\t\t\t\t{:5s}\t\t{:40s}".format("USER","EVENAME","TYPE","DISTRICT","ADDRESS","COST","PAID").center(10))                                                                         
                    print(("*"*141).center(140))
                    print("")
                    for i in data:
                       print("{:5s}   {:1s}   {:10s}  {:2s}\t{:5s}\t\t\t{:5s}\t\t{:40s}".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7]).center(10))
                    print(("_"*141).center(140))
                    mycon.commit()


                    


                 break

              

              elif inspect==3:
                 print("")
                 print("WHICH INFO WOULD YOU LIKE TO EDIT")
                 print("1-USER INFO")
                 print("2-EVENT INFO")
                 print("3-EXIT")
                 ed=int(input("ENTER YOUR CHOICE: "))
                 while ed not in [1,2,3]:
                     print("INVALID CHOICE")
                     ed=int(input('''ENTER YOUR CHOICE OF SERVICE:

1.USER INFO
2.EVENT INFO 
3.EXIT

YOUR CHOICE:'''))   
                    
                    
                 if ed==1:
                    print("")
                    ed1=int(input('''ENTER YOUR CHOICE OF SERVICE:

1.ADD NEW USER
2.SEARCH FOR USER DATA
3.DELETE DATA OF USER
4.EDIT USER DETAILS

YOUR CHOICE:'''))
                    while ed1 not in [1,2,3,4]:
                       print("")
                       print("INVALID CHOICE")
                       ed1=int(input('''ENTER YOUR CHOICE OF SERVICE:

1.ADD NEW USER
2.SEARCH FOR USER DATA
3.DELETE DATA OF USER
4.EDIT USER DETAILS

YOUR CHOICE:'''))   
                    if ed1==1:
                        adduser()
                        break
                        
                    if ed1==2:
                        searchuser()
                        break
                    

                    if ed1==3:
                        deluser()
                        break
                     
                    if ed1==4:
                       global na 
                       na=input("ENTER USER ID:")
                       cursor.execute("select * from LOGIN where username='" + na + "'")
                       data=cursor.fetchall()
                       if data:
                          print("")

                          da=int(input("""WHICH DATA WOULD YOU LIKE TO EDIT
1.USERNAME
2.NAME
3.CONTACT
4.PASSWORD

YOUR CHOICE:"""))
                          if da==1:
                             eduser()
                             break
                           
                          if da==2:
                             edname()
                             break

                          if da==3:
                             edcon() 
                             break

                          if da==4:
                             edpw() 
                             break
                          else:
                             print("")
                             print("USER NOT FOUND")
                             print("") 

                       
                 if ed==2:
                    print("")
                    ed1=int(input('''ENTER YOUR CHOICE OF SERVICE:

1.SEARCH FOR USER'S EVENT
2.DELETE DATA OF EVENT
3.EXIT

YOUR CHOICE:'''))

                    while ed1 not in [1,2,3]:
                       print("")
                       print("INVALID CHOICE")
                       ed1=int(input('''ENTER YOUR CHOICE OF SERVICE:

1.SEARCH FOR USER'S EVENT
2.DELETE EVENT DATA OF USER

YOUR CHOICE:'''))
                    if ed1==1:
                       evesearch()
                       break

                    if ed1==2:
                       deleve()
                       break
                     
                    if ed1==3:
                       mainmenu()

                 if ed==3:
                    mainmenu()


                  
             
              if inspect==4:
                  inspect4()
                  break

                                                                                                                                  
              if inspect!=1 or inspect!=2 or inspect!=3 or inspect!=4:
                 print("IT SEEMS YOU'VE ENTERED THE WRONG DATA")
                 print("TRY AGAIN")
                 print("")
                 print("HAPPENING PRODUCTION INFO'S:")
                 print("1-USER INFO")
                 print("2-EVENT INFO")
                 print("3-EDIT")
                 print("4-SEARCH BY DISTRICT")
                 print("")                 
                 inspect=int(input("WHICH INFO WOULD YOU LIKE TO INSPECT (1/2/3): "))
                 exit

           

           while True:
              print("")
              ins=input("DO YOU WISH TO CHECK OTHER DATA'S(Y/N): ")
              
              if ins.lower()=="y":
                 
                 print("")
                 print("HAPPENING PRODUCTION INFO'S:")
                 print("1-USER INFO")
                 print("2-EVENT INFO")
                 print("3-EDIT")
                 print("4-SEARCH BY DISTRICT")
                 print("")
                 inspects()
                 
              if ins.lower()=="n":
                 print("")
                 print("THANK YOU ADMIN")
                 mainmenu()
                 exit
                 break


              else:
                 print("IT SEEMS YOU'VE ENTERED THE WRONG DATA")
                 print("TRY AGAIN")
                 print("")
                 ins=input("DO YOU WISH TO CHECK OTHER DATA'S(Y/N): ")
                 exit

        inspects()
    else:
       print("")
       print("WRONG CREDENTIALS")
       print("")
       mainmenu()




def homepage(user):
   
    #Homepage
    while True:
        print("")
        print("1. EVENT CUSTOMISATION")
        print("2. CHANGE PASSWORD")
        print("3. MAIN MENU")
        choice=input("ENTER CHOICE : ")
        print("")

        if choice=='1':
           evecus(user)
           print("")
           print("")
           report()
           print("")
           print("")
           final_payment()
           print("")
           print("")
           print("DO YOU WISH TO CONTINUE OR STOP THE PROCESS")
           print("\nIF YOU WISH TO CONTINUE ENTER 0")
           print("IF YOU WISH TO STOP ENTER 1")
           last=int(input("\nENTER YOUR CHOICE:"))
           if last==0:
              print("WE WELCOME YOU AGAIN TO HAPPENING PRODUCTION\n")
              mainmenu()
           elif last==1:
              print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
              print("\n\t\t\t\t\t\t\t        VISIT AGAIN")
              sys.exit()           

           print("")           
   
        elif choice=='2':
           changepassword(user)

        elif choice=='3':
           mainmenu()
            
        else:
           print("OH NO, IT SEEMS YOU  MIGHT HAVE ENTERED THE WRONG INPUT")
           print("DO YOU WISH TO CONTINUE OR STOP THE PROCESS")
           print("\nIF YOU WISH TO CONTINUE ENTER 0")
           print("IF YOU WISH TO STOP ENTER 1")
           last=int(input("\nENTER YOUR CHOICE:"))
           if last==0:
              print("WE WELCOME YOU AGAIN TO HAPPENING PRODUCTION\n")   
           elif last==1:
              print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
              print("\n\t\t\t\t\t\t\t        VISIT AGAIN")
              sys.exit()           
           

def mainmenu():
   while True:
      print("|***************************************|")
      print("|                                       |")
      print("|          HAPPENING PRODUCTION         |")
      print("|                                       |")
      print("|***************************************|")
      print("|                 1.ADMIN               |")
      print("|                                       |")
      print("|                 2.CUSTOMER            |")
      print("|                                       |")
      print("|                 3.EXIT                |")
      print("|***************************************|")

      c=int(input("ENTER YOUR CHOICE:"))
      print("")
      print("")
      
      if c==1:

         admin()
         break

      if c==2:
         print("_"*141)
         print("~"*141)
         print("\n\t\t\t\t\t\t\t\t  MAIN MENU")
         print("_"*141)
         print("~"*141)

         print("1. LOGIN")
         print("2. SIGN UP")
         print("3. EXIT")
         ls=int(input("ENTER YOUR CHOICE :"))
         if ls==1:
            log()
            break
         elif ls==2:
            sign()
            break
         elif ls!=1 or ls!=2 or ls==3:
            print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
            print("\n\t\t\t\t\t\t\t        VISIT AGAIN")
            sys.exit()
         
      
               
      if c==3:
            print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
            print("\n\t\t\t\t\t\t\t        VISIT AGAIN")
            sys.exit()

      if c!=1 and c!=2 and c!=3:
         print("OH NO, IT SEEMS YOU  MIGHT HAVE ENTERED THE WRONG INPUT")
         print("DO YOU WISH TO CONTINUE OR STOP THE PROCESS")
         print("\nIF YOU WISH TO CONTINUE ENTER 0")
         print("IF YOU WISH TO STOP ENTER 1")
         last=int(input("\nSO, ENTER YOUR CHOICE:"))
         if last==0:
            print("WE WELCOME YOU AGAIN TO HAPPENING PRODUCTION\n")   
         elif last==1:
            print("\n\t\t\t\t\t\t THANK YOU FOR VISITING, HAVE A GREAT DAY AHEAD")
            print("\n\t\t\t\t\t\t\t        VISIT AGAIN")
            sys.exit()

mainmenu()
     

             
            
     
                                    



                                    
                                 
                           
                


















































               










