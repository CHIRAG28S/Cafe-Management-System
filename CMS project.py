#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#   CAFE MANAGEMENT SYSTEM 

print("press 1 for MENU")
user= int(input())
c=aa
li=[]
print("WELCOME TO OUR RETAURANT")
print("THANKS FOR CHOOSING US")
while(user<=4):
    print("press 1 for BEVERAGES")
    print("press 2 for MAIN COURSE")
    print("press 3 for SHAKES")
    print("press 4 for CAKES")
    print("press 5 for STOP ORDER")
    user= int(input())
    if(user==1):
        print("BEVERAGES")
        print("press 1 for TEA  50")
        print("press 2 for CAPPUCCINO  70")
        print("PRESS 3 for MOJITO  110")
        print("PRESS 4 for LIME SODA  100")
        user=int(input())
        if(user==1):
            print("TEA")
            c=c+50
            b="tea 50"
            li.append("TEA 50")
        elif(user==2):
            print("CAPPUCCINO")
            c=c+70
            li.append("CAPPUCCINO 70")
        elif(user==3):
            print("MOJITO")
            c=c+110
            li.append("MOJITO 110")
        elif(user==4):
            print("LIME SODA")
            c=c+100
            li.append("LIME SODA 100")
    elif(user==2):
        print("MAIN COURSE")
        print("press 1 for INDIAN")
        print("press 2 for MEXICAN")
        print("press 3 for CHINESE")
        print("press 4 for JAPANESE")
        user=int(input())
        if(user==1):
            print("press 1 for SPECIAL THALI 120")
            print("press 2 for  DAL TADKA 185")
            print("press 3 for PANEER  200")
            user=int(input())
            if(user==1):
                print("SPECIAL THALI")
                c=c+120
                li.append("SPECIAL THALI 120")
            elif(user==2):
                print("DAL TADKA")
                c=c+185
                li.append("DAL TADKA 185")
            elif(user==3):
                print("PANEER")
                c=c+200
                li.append("PANEER 200")
        elif(user==2):
            print("MEXICAN")
            print("press 1 for VEG NACHOS 120")
            print("press 2 NON VEG NACHOS  150 ")
            print("press 3 for FAJITA 130")
            print("press 4 for CHIPOTLE MEAT BALL WRAP 125")
            user=int(input())
            if(user==1):
                print("VEG NACHOS")
                c=c+120
                li.append("VEG NACHOS 120")
            elif(user==2):
                print("NON VEG NACHOS")
                c=c+150
                li.append("NON VEG NACHOS 150")
            elif(user==3):
                print("FAJITA")
                c=c+130
                li.append("FAJITA 130")
            elif(user==4):
                print("CHIPOTLE MEAT BALL WRAP")
                c=c+125
                li.append("CHIPOTLE MEAT BALL WRAP 125")
        elif(user==3):
            print("CHINESE")
            print("press 1 for VEG MOMOS  95 ")
            print("press 2 for VEG NOODLES 150 ")
            print("press 3 for FRIED RICE 175")
            print("press 4 for  ANHUI 200")
            user=int(input())
            if(user==1):
                print("VEG MOMOS")
                c=c+95
                li.append("VEG MOMOS 95")
            elif(user==2):
                print("VEG NOODLES")
                c=c+150
                li.append("VEG NOODLES 150")
            elif(user==3):
                print("FRIED RICE")
                c=c+175
                li.append("FRIED RICE 175")
            elif(user==4):
                print("ANHUI")
                c=c+200
                li.append("ANHUI 200")
        elif(user==4):
            print("JAPANESE")
            print("press 1 for CHAMPON  300")
            print("press 2  EDAMAME  350")
            print("press 3 for FUGU  250")
            print("press 4  for GYOZA   450")
            user=int(input())
            if(user==1):
                print("CHAMPON")
                c=c+300
                li.append("CHAMPON 300")
            elif(user==2):
                print("EDAMAME")
                c=c+350
                li.append("EDAMAME 350")
            elif(user==3):
                print("FUGU")
                c=c+250
                li.append("FUGU 250")
            elif(user==4):
                print("GYOZA")
                c=c+450
                li.append("GYOZA 450")
    elif(user==3):
        print("SHAKES")
        print("press 1 for CHOCOLATE TRUFFLE  135")
        print("press 2 for CHOCOLATE PARALINE  150")
        print("press 3 for OREO ROYAL  185")
        print("press 4  for PINEAPPLE DELIGHT  190")
        user=int(input())
        if(user==1):
            print("CHOCOLATE TRUFFLE")
            c=c+135
            li.append("CHOCOLATA TRUFFLE 135")
        elif(user==2):
            print("CHOCOLATE PARALINE")
            c=c+150
            li.append("CHOCOLATE PARALINE 150")
        elif(user==3):
            print("OREO ROYAL")
            c=c+185
            li.append("OREO ROYAL 85")
        elif(user==4):
            print("PINEAPPLE DELIGHT")
            c=c+190
            li.append("PINEAPPLE DELIGHT 90")
    elif(user==4):
        print("CAKES")
        print("press 1 for CHOCOLATE MUD  250")
        print("press 2 for CHOCOLATE REPABERRY 200")
        print("press 3 for TIRAMIU  350")
        print("press 4  for RED VELVET 160")
        user=int(input())
        if(user==1):
            print("CHOCOLATE MUD")
            c=c+250
            li.append("CHOCOLATA MUD 250")
        elif(user==2):
            print("REPABERRY")
            c=c+200
            li.append("REPABERRY 200")
        elif(user==3):
            print("TIRAMIU")
            c=c+350
            li.append("TRIAMIU 350")
        elif(user==4):
            print("RED VELVET")
            c=c+160
            li.append("RED VELVET 160")
           

    else:
        print("YOUR BILL")
        for p in li:
            print(p)
        print("YOUR TOTAL = ",c)


# In[ ]:




