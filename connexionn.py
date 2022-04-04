from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="projet_python")
cursordb = connectiondb.cursor()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="black")

    global mail_verification
    global password_verification
    Label(root2, text='Cliquez sur le bouton pour entrer les details de connexion', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="black",
    bg="pink",width=200).pack()
    mail_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="mail :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=mail_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="pink", fg='black', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Connexion reussie!... Bienvenue {} ".format(mail_verification.get()), fg="black", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Deconnexion", bg="pink", fg='black', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Message invalide")
    failed_message.geometry("500x100")
    Label(failed_message, text="Login ou mot de passe incorrect", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="pink", fg='black', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()


def login_verification():
    user_verification = mail_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from user where mail = %s and password = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()



def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root,text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="black",
    bg="pink",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="black",
    bg="pink",command=login).pack()
    Label(root,text="").pack()
    # Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    # bg="blue",command=Exit).pack()
    Label(root,text="").pack()

main_display()
root.mainloop()