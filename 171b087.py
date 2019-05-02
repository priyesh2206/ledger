from Tkinter import*
import sqlite3
from tkMessageBox import * 
con=sqlite3.Connection('my bro.db')
cur=con.cursor()
cur.execute("create table if not exists buss(billno varchar(10) PRIMARY KEY,custname varchar(15),custadd varchar(25),product varchar(25),Qty number,price number,total number,payment number,amtleft number,date number)")

root=Tk()
root.resizable(width=False,height=False)
root.state('zoomed')
root.title("BUSINESS RECORDS")
root.geometry('1450x800')

n1=StringVar()

har=0
global f1
global f4
global f5 
global f6
global f7

def fun2(f1):
    f1.destroy()
    f2=Frame(root,width=300,height=300,bg="silver")
    f2.place(x=500,y=250)
    lb0=Label(f2,text="LOGIN",font="courier 30 bold", bg="lightgrey").place(x=85,y=10)
    lb1=Label(f2,text="Enter The User Name").place(x=11,y=82)
    entry1=Entry(f2,bd=5)
    entry1.place(x=150,y=80)
    lb2=Label(f2,text="Enter The Password").place(x=10,y=137)
    entry2=Entry(f2,show="*",bd=5)
    entry2.place(x=150,y=130)
    Label(f2,text="@copyright reversed",font="courier 10 bold").place(x=90,y=260)
    def Login():
        if entry1.get()=="1" and entry2.get()=="1":
            showinfo('LOGIN','Login sucessfully')
            f2.destroy()
            f3=Frame(root,width=550,height=550,bg="lightgrey")
            f3.place(x=200,y=150)

            Label(f3,text=" BILL DETAILS ",relief="ridge",font="courier 20 bold",bg="lightgrey").place(x=150,y=10)
            Label(f3,text="Enter The Bill Number -",font="courier 15 bold").place(x=10,y=50)
            bill=Entry(f3,bd=5,width=20,font="courier 10 bold")
            bill.place(x=300,y=50)
            
            Label(f3,text="Customer Name -",font="courier 15 bold").place(x=12,y=100)
            custname=Entry(f3,bd=5,width=20,font="courier 10 bold")
            custname.place(x=225,y=100)
            
            Label(f3,text="Customer Address -",font="courier 15 bold").place(x=14,y=150)
            custadd=Entry(f3,bd=5,width=20,font="courier 10 bold")
            custadd.place(x=250,y=150)

            OPTIONS =[
                "MAIDA",
                "RAWA",
                "OIL CAKE",
                "ATTA",
                "COCONUTS",
                "SUGAR",
                "POHA",
                "RICE",
                "PUFFED RICE", 
                "SUJI",
                "GUR",
                "GRAINS"
                ]
            variable = StringVar()
            
            variable.set(OPTIONS[0])
   
            Label(f3,text="Products Purchased -",font="courier 15 bold").place(x=16,y=200)
            item=OptionMenu(f3, variable, *OPTIONS)
            item.place(x=290,y=200)
            
            Label(f3,text=" Quantity (in kg) -",font="courier 15 bold").place(x=17,y=250)
            Qty=Entry(f3,bd=5,width=20,font="courier 10 bold")
            Qty.place(x=290,y=250)
            
            Label(f3,text="price(in Rs)-",font="courier 15 bold").place(x=19,y=300)
            pr=Entry(f3,bd=5,width=20,font="courier 10 bold")
            pr.place(x=200,y=300)
            
            Label(f3,text="Payment by CUS.-",font="courier 15 bold").place(x=22,y=350)
            pc=Entry(f3,bd=5,width=20,font="courier 10 bold")
            pc.place(x=250,y=350)
            
            Label(f3,text="Date of purchased -",font="courier 15 bold").place(x=23,y=400)
            dp=Entry(f3,bd=5,width=20,font="courier 10 bold")
            dp.place(x=300,y=400)
            
            def insert():
                global har
                har=1
                A=int(pr.get())
                B=int(Qty.get())
                C=A*B

                p=int(pc.get())
                l=C-p
                
                global f4
                cur.execute("insert into buss values(?,?,?,?,?,?,?,?,?,?)",(bill.get(),custname.get(),custadd.get(),variable.get(),Qty.get(),pr.get(),C,pc.get(),l,dp.get()))
                con.commit()
                t=cur.execute("select quantity from stock where productname=?",(variable.get(),))
                temp=t.fetchall()
                simmi=temp[0][0]
                lol=simmi-B
                cur.execute('UPDATE stock set quantity=? where productname=?',(lol,variable.get()))
                con.commit()
                
                f4=Frame(root,width=400,height=400,bg="grey")
                f4.place(x=850,y=200)
                tol="Total Amount is {}".format(C)
                py="Amount paid by customer is {}".format(p)
                lf="Amount Due is {}".format(l)
                Label(f4,text="BILL",relief="ridge",font="courier 20 bold",bg="lightgrey").place(x=175,y=10)
                Label(f4,text=tol,width=25,font="courier 13 bold").place(x=50,y=100)
                Label(f4,text=py,width=32,font="courier 13 bold").place(x=50,y=200)
                Label(f4,text=lf,width=25,font="courier  13 bold").place(x=50,y=300)
            Button(f3,text="ENTRY",width=13,bd=5,bg="lightgreen",command=insert).place(x=220,y=500)
            def stock():
                global f6
            
                f6=Frame(root,width=400,height=400,bg="silver")
                f6.place(x=850,y=200)
                lb0=Label(f6,text="LOGIN",font="courier 30 bold", bg="lightgrey").place(x=120,y=10)
                lb1=Label(f6,text="Enter The User Name").place(x=11,y=120)
                entry1=Entry(f6,bd=5)
                entry1.place(x=150,y=120)
                lb2=Label(f6,text="Enter The Password").place(x=10,y=160)
                entry2=Entry(f6,show="*",bd=5)
                entry2.place(x=150,y=160)

                def login2():
                    global f7
                    global f6
                    if entry1.get()=="2" and entry2.get()=="2":
                        showinfo('LOGIN','Login sucessfully')
                        f6.destroy()
                        f7=Frame(root,width=400,height=400,bg="lightgrey")
                        f7.place(x=850,y=200)
                        Label(f7,text="STOCK RECORDS",relief="ridge",font="courier 20 bold",bg="lightgrey").place(x=115,y=10)
                        OPTION =[
                                "MAIDA",
                                "RAWA",
                                "OIL CAKE",
                                "ATTA",
                                "COCONUTS",
                                "SUGAR",
                                "POHA",
                                "RICE",
                                "PUFFED RICE", 
                                "SUJI",
                                "GUR",
                                "GRAINS"
                               ]
                        variabled = StringVar()
            
                        variabled.set(OPTION[0])
   
            
                        Label(f7,text="PRODUCT NAME",font="courier 15 bold").place(x=16,y=100)
                        pro=OptionMenu(f7, variabled, *OPTION)
                        pro.place(x=200,y=100)
                        Label(f7,text=" Quantity -",font="courier 15 bold").place(x=17,y=150)
                        Qt=Entry(f7,bd=5,width=20,font="courier 10 bold")
                        Qt.place(x=200,y=150)
                        Label(f7,text="price(in ws)-",font="courier 15 bold").place(x=19,y=200)
                        wpr=Entry(f7,bd=5,width=20,font="courier 10 bold")
                        wpr.place(x=200,y=200)
                        def Mstock():
                            A=variabled.get()
                            B=Qt.get()
                            C=wpr.get()
                            cur.execute('UPDATE stock set quantity=?, wprice=? where productname=?',(B,C,A))
                            con.commit()
                            showinfo('stock','your Stock has been updated')
                        def show():
                            t=cur.execute("select quantity from stock where productname=?",(variabled.get(),))
                            temp=t.fetchall()
                            simmi=temp[0][0]
                            priyesh=variabled.get()
                        
                        
                            m="your {} stock is:-  {}".format(priyesh,simmi)
    
                            showinfo('Showing Data',m)
                            
                            

                            
                        Button(f7,text="MODIFY STOCK",width=13,bd=5,bg="lightblue",command=Mstock).place(x=100,y=300)
                        Button(f7,text="SHOW",width=13,bd=5,bg="lightblue",command=show).place(x=220,y=300)
                    else:
                        showerror('Error','Invalid username and password')
            
                Button(f6,text="LOGIN",command=login2,bd=5,width=15).place(x=160,y=300)
     
            
            Button(f3,text="STOCK",command=stock,width=18,bd=5,bg="lightblue").place(x=350,y=500)
            def back():
                global f4
                global f7
                if(har==1):
                    f3.destroy()
                    f4.destroy()
                    f7.destroy()
                    main(1)
                else:
                    f3.destroy()
                    main(1)
            Button(f3,text="Back",width=18,bd=5,bg="red",command=back).place(x=50,y=500)

        else:
            showerror('Error','Invalid username and password')
         
    Button(f2,text="login",bd=5,width=15,command=Login).place(x=160,y=200)

def getbill(f1):
    try: 
        global f5
        aa=n1.get()
        t=cur.execute("select * from buss where billno=?",(aa,))
        pri=t.fetchall()
        A=pri[0][0]
        B=pri[0][1]
        C=pri[0][2]
        D=pri[0][3]
        E=pri[0][4]
        F=pri[0][5]
        G=pri[0][6]
        H=pri[0][7]
        I=pri[0][8]
        J=pri[0][9]
        AA="Bill Number is :- {}".format(A)
        BB="Customer name is :- {}".format(B)
        CC="customer delivery Address is :- {}".format(C)
        DD="Products Purchased is :- {}".format(D)
        EE="Quantity of Products is :- {}".format(E)
        FF="Price of Porducts is :- {} ".format(F)
        GG="Total is :- {}".format(G)
        HH="Payment received by customer :- {}".format(H)
        II="Amount to be paid later :- {}".format(I)
        JJ="Date of Purchased :- {}".format(J)
        if(aa==pri[0][0]):
            f1.destroy()
            f5=Frame(root,width=600,height=580,bg="lightgrey")
            f5.place(x=380,y=125)
           
            Label(f5,text=" CHANDANSONS",font="courier 20 bold",bg="lightgrey").place(x=200,y=10)
            
            Label(f5,text=" GST no:-12354BR888",font="courier 10 bold",bg="lightgrey").place(x=10,y=40)
            
            Label(f5,text=" CONTACT NUMBER-9664778761",font="courier 10 bold",bg="lightgrey").place(x=370,y=40)

            Label(f5,text="-----------------------------------------------------------------------------------------------------------------------------------<",bg="lightgrey").place(x=5,y=60)
            
            Label(f5,text=AA,font="courier 15 bold").place(x=10,y=80)
                
            Label(f5,text=BB,font="courier 15 bold").place(x=10,y=120)
                
            Label(f5,text=CC,font="courier 15 bold").place(x=10,y=160)
        
            Label(f5,text=DD,font="courier 15 bold").place(x=10,y=200)
                
            Label(f5,text=EE,font="courier 15 bold").place(x=10,y=240)
                
            Label(f5,text=FF,font="courier 15 bold").place(x=10,y=280)
            
            Label(f5,text=GG,font="courier 15 bold").place(x=10,y=320)
                
            Label(f5,text=HH,font="courier 15 bold").place(x=10,y=360)
            
            Label(f5,text=II,font="courier 15 bold").place(x=10,y=400)
            
            Label(f5,text=JJ,font="courier 15 bold").place(x=10,y=440)
            
            Label(f5,text="-----------------------------------------------------------------------------------------------------------------------------------<",bg="lightgrey").place(x=5,y=480)
            Label(f5,text="*PRODUCT PURCHASED IS NOT REFUNDABLE *",bg="red").place(x=10,y=500)
            Label(f5,text="THANKYOU FOR SHOPPING :)",font="courier 15 bold").place(x=175,y=540)
            def backing():
                global f5
                f5.destroy()
                main(1)
            Button(f5,text="Back",command=backing).place(x=500,y=550)

        else:
            showerror('error','NO BILL FOUND PLEASE CHECK THE BILL NUMMBER')
    except IndexError:
        showerror('error','NO BILL FOUND PLEASE CHECK THE BILL NUMMBER')
            

def main(e):
    k1.destroy()
    f1=Frame(root,width=500,height=400,bg="grey")
    f1.place(x=400,y=200)
    Label(root,text="WELCOME TO CHANDAN SONS SHOP MEMO",relief="ridge",bg='lightgrey',font="courier 50 bold").place(x=20,y=33)
    Label(f1,text="ENTER THE BILL NUMBER",font="courier 15 bold").place(x=10,y=100)
    bills=Entry(f1,textvariable=n1,bd="5",width=15,bg="lightgrey",font="courier 15 bold")
    bills.place(x=300,y=98)    
    Button(f1,text="GET BILL",width=10,font="courier 15 bold",bd=5,bg="red",command=lambda: getbill(f1)).place(x=200,y=195)
    Button(f1,text="ENTRY",width=10,font="courier 15 bold" ,bd=5,bg="red",command=lambda: fun2(f1)).place(x=350,y=195)
    Label(f1,text="!*For entry of customer click on 'ENTRY' button",font="courier 10 bold").place(x=20,y=300)
    Label(f1,text="!*For fetching details click on 'GET BILL'  button",font="courier 10 bold").place(x=20,y=350)
#main()

k1=Frame(root,width=1450,height=800,bg="antiquewhite2")
k1.place(x=10,y=10)
a=PhotoImage(file="img4.GIF")
global l
l=Label(k1,image=a,width=300,height=390)
l.place(x=200,y=150)
l.bind('<Motion>',main)
Label(k1,text="!!WELCOME!!",relief="ridge",font='courier 50 bold',bg="silver").place(x=500,y=20)
Label(k1,text="NAME:-PRIYESH RATHORE",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=800,y=250)
Label(k1,text="ERNO.:-171B087",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=800,y=350)
Label(k1,text="BATCH:-B3",relief="ridge",font='courier 20 bold',bg="lightblue").place(x=800,y=450)

root.mainloop()

