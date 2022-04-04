# -*- coding: utf-8 -*-
#import pip
#pip.main(['install','mysql-connector-python-rf'])
from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector
#establishing connection
conn = mysql.connector.connect(
   user='root', password='root', host='localhost', database='iredadmin')
"""
here in my case there is no password so password='' is blank
root is username
localhost is server or host name 
you can also use 127.0.0.1 in place of local host
pythondata is the name of Database
"""
#defining register function
def register():
    #getting form data
    nom1=nom.get()
    prenom1=prenom.get()
    mail1=mail.get()
    password1=password.get()
    confirm_password1=confirm_password.get()
   
    #applying empty validation
    if nom1=='' or prenom1==''or mail1=='' or password1=='' or confirm_password1=='':
        message.set("Veuillez remplir les champs vides!!!")
    elif password1 != confirm_password1:
        message.set("Les mots de passe ne se correspondent pas!!!")
    else:
       # Creating a cursor object using the cursor() method
       cursor = conn.cursor()
       # Preparing SQL query to INSERT a record into the database.
       insert_stmt = (
           "INSERT INTO user(nom, prenom, mail, password, confirm_password)"
           "VALUES (%s, %s, %s, %s, %s)"
       )
       data = (nom1, prenom1,mail1,password1,confirm_password1)
       try:
           #executing the sql command
           cursor.execute(insert_stmt,data)
           #commit changes in database
           conn.commit()
       except:
           conn.rollback()
       message.set("Donnees bien enregistrees")

#defining Registrationform function
def Registrationform():
    global user_screen
    user_screen = Tk()
    #Setting title of screen
    user_screen.title("Formulaire d'enregistrement")
    #setting height and width of screen
    user_screen.geometry("350x400")
    #declaring variable
    global  message;
    global nom
    global prenom
    global mail
    global password
    global confirm_password

    nom = StringVar()
    prenom = StringVar()
    mail=StringVar()
    password=StringVar()
    confirm_password=StringVar()
    message = StringVar()
    
    #Creating layout of Registration form
    Label(user_screen,width="300", text="Entrez svp vos informations ici", bg="blue",fg="black").pack()
    #nom Label
    Label(user_screen, text="Nom * ").place(x=20,y=40)
    #nom textbox
    Entry(user_screen, textvariable=nom).place(x=90,y=42)
    
    #prenom Label
    Label(user_screen, text="Prenom * ").place(x=20,y=80)
    #prenom textbox
    Entry(user_screen, textvariable=prenom).place(x=90,y=82)

    # email Label
    Label(user_screen, text="Mail * ").place(x=20, y=120)
    # email textbox
    Entry(user_screen, textvariable=mail).place(x=90, y=122)

    # password Label
    Label(user_screen, text="Password * ").place(x=20, y=160)
    # password textbox
    Entry(user_screen, textvariable=password).place(x=90, y=162)

    # confirm_password Label
    Label(user_screen, text="Confirmation password * ").place(x=20, y=200)
    # confirm_password textbox
    Entry(user_screen, textvariable=confirm_password).place(x=90, y=202)
    
    Label(user_screen, text="", textvariable= message).place(x=95, y=264)

    #Login button
    Button(user_screen, text="Envoyer", width=10, height=1, bg="blue",command=register).place(x=105,y=300)
    user_screen.mainloop()
#calling function Registrationform
Registrationform()