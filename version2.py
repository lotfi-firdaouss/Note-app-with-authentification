from tkinter import *
import os
import tkinter.messagebox
import Image, ImageTk
from tkinter import filedialog

def delete2():
    screen2.destroy()#pour fermer screen2

def delete4():
    screen4.destroy()#pour fermer screen4

def delete5():
    screen5.destroy()#pour fermer screen5

def save():
    name = note_name.get()
    notes = file_notes.get()
    #on ouvre le ficher note pour ajouter la nouvelle note
    file=open("notes","a")
    #on ajoute les informations comme suit:
    file.write("owner:"+username1+"\nnote name:"+name+"\nnotes:"+notes+"\n")
    file.close()
    #on affiche un message déclarant que la note a été bien enregistré
    tkinter.messagebox.showinfo('alert','the note has been saved!')

def create_notes():
    global note_name
    note_name = StringVar()
    global file_notes
    file_notes = StringVar()
    #ici on crée un onglet qui permet à l'utilisateur de créer la note qu'il désire en introduisant le nom de la note
    #et puis son contenu et on a mit un bouton qui va appeler la fonction save qui enregistra la nouvelle note dans le ficher
    #des notes appellé notes
    screen7 = Toplevel(root)
    screen7.title("Info")
    screen6.geometry("400x350")
    Label(screen7, text="Please enter the name of the note").pack()
    Entry(screen7, textvariable=note_name).pack()
    Label(screen7, text="Please enter the notes").pack()
    Entry(screen7, textvariable=file_notes).pack()
    Button(screen7, text="SAVE", command=save).pack()

def view():
    screen9 = Toplevel(root)
    screen9.title("Info")
    screen9.geometry('400x400')
    note_name=raw_file_name.get()
    note_name="note name:"+note_name
    #ici on doit parcourir le fichier notes qui contient les notes de tout les utilisateurs pour trouver la note avec
    #owner=nom d'utilisateur et note name=le nom de la note que l'utilisateur a choisit
    file = open("notes", "r")
    lines = file.read()
    lines = lines.splitlines()
    owner = "owner:" + username1
    p=0
    for i, line in enumerate(lines):
        if owner in line and note_name in lines[i+1:i+2]:#si on trouve la note on l'affiche et on donne 1 à p
             Label(screen9, text=lines[i + 1:i + 3]).pack()
             p=1
             break
    if p==0:#sinon ca veut dire que p=0 et on afficher que la note n'a pas été trouvé
        Label(screen9,text="note not found").pack()
    file.close()

def view_notes():
    screen8 = Toplevel(root)
    screen8.title("Info")
    screen8.geometry('400x400')
    Label(screen8, text="").pack()
    Label(screen8,text="please choose one of the notes below:").pack()
    #on affiche les notes que l'utilisateur peut voir , ce sont les notes qui possédent
    file=open("notes","r")
    lines=file.read()
    lines=lines.splitlines()
    owner="owner:"+username1
    #pour les afficher on parcourt la variable lines en utilisant une boucle for bouclant en utilisant l'index et les elements de la variable
    for i,line in enumerate(lines):
        if owner in line:
            Label(screen8,text=lines[i+1:i+2]).pack()
    file.close()
    #on ajoute une zone de texte dont l'utilisateur introduit la note qu'il désire voir
    global raw_file_name
    raw_file_name=StringVar()
    Entry(screen8,textvariable=raw_file_name).pack()
    Button(screen8,text="OK",command=view).pack()

def delete():
    note_name=raw_filename.get()
    note_name="note name:"+note_name
    owner="owner:"+username1
    #ici on ouvre une autre fois le fichier notes pour supprimer la note spécifié
    f = open("notes", "r")
    lines = f.read()
    lines = lines.splitlines()
    f.close()
    #ici on cherche le contenu de la note et on le stocke dans la variable nomé notes1
    for i, line in enumerate(lines):
        if owner in line and note_name in lines[i+1:i+2]:
             global notes1
             notes1="".join(lines[i + 2:i + 3])
             break
    #ici on va supprimer la note en utilisant la méthode suivante: en fait on va réécrire le fichier notes en sautant
    #cette fois ci les 3 lines qui présentent notre note(ownername/notename/note itself)
    f = open("notes", "w")
    for i, line in enumerate(lines):
        if owner in line and note_name in lines[i + 1:i + 2]:
            continue
        if note_name in line:
            continue
        if notes1 in line:
            continue
        f.write(line + "\n")
    f.close()
    #on affiche un message indiquant que la note a été supprimé
    tkinter.messagebox.showinfo('alert',note_name+" is removed!")

def delete_notes():
    screen10 = Toplevel(root)
    screen10.title("Info")
    screen10.geometry('400x400')
    Label(screen10, text="").pack()
    Label(screen10, text="please choose one of the notes below:").pack()
    #ici on va donner le choix à l'utilisateur de supprimer une note, n'oublions pas qu'il n'a le droit de supprimer que les notes
    #qui lui appartiennent
    file = open("notes", "r")
    lines = file.read()
    lines = lines.splitlines()
    #on a ouvert alors le fichier notes contenant les notes de tout les utilisateurs et on va essayer de n'aficher que les notes qui appartiennent à notre
    #utilisateur
    owner = "owner:" + username1
    for i, line in enumerate(lines):
        if owner in line:
            Label(screen10, text=lines[i + 1:i + 2]).pack()
    file.close()
    #ici on a ajouté une zone de texte dans laquelle l'utilisateur introduit la note qu'il désire supprimer
    #et un bouton qui executera cette demande en appelant la fonction delete
    global raw_filename
    raw_filename = StringVar()
    Entry(screen10, textvariable=raw_filename).pack()
    Button(screen10, text="OK", command=delete).pack()

def session():
    global screen6
    #cette fonction crée un onglet qui va contstituer le menu de notre petite application donnant le choix à l'utilisateur
    #d'ajouter une note , de supprimer une note ou de voir une note tout en associant chaque bouton à sa fonction correspondante
    screen6 = Toplevel(root)
    screen6.title("dashboard")
    screen6.geometry('400x400')
    Label(screen6, text="").pack()
    Label(screen6, text="welcome to the dashboard").pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Create note", width="100", command=create_notes).pack()
    Button(screen6, text="View note", width="100",command=view_notes).pack()
    Button(screen6, text="delete note", width="100",command=delete_notes).pack()

def login_success():
    session()#fait appel à la fonction session()

def password_not_recognized():
    global screen4
    #il s'agit simplement d'un onglet qui va vous declarer que le mot de passe est éroné et au click de OK va
    #appeller la fonction delete4 qui va le supprimer
    screen4 = Toplevel(root)
    screen4.title("Fail")
    screen4.geometry("200x150")
    Label(screen4, text="Password not recognized!").pack()
    Button(screen4, text="OK", command=delete4).pack()

def user_not_found():
    global screen5
    #il s'agit simplement d'un onglet qui va vous declarer que l'utilisateur n'est pas trouvé et au click de OK va
    #appeller la fonction delete5 qui va le supprimer
    screen5 = Toplevel(root)
    screen5.title("Fail")
    screen5.geometry("200x150")
    Label(screen5, text="user not found!").pack()
    Button(screen5, text="OK", command=delete5).pack()

def login_verify():
    global username1
    global password1
    #on recupère les informations introduit par l'utilisateur
    username1 = username_verify.get()
    password1 = password_verify.get()
    #on ouvre le fichier informations et on met tout les lignes de ce dernier dans une variable lines
    file1 = open("informations", "r")
    lines=file1.readlines()
    #on parcourt la variable lines pour verifier la combinaison nom d'utilisateur/mot de passe
    p=0
    for line in lines:
        if username1 in line:#ca veut dire que le nom d'utilisateur existe
            if password1 in line:#ca veut dire que le mot de passe introduit est valide
                login_success()#on appelle cette fonction
            else:
                password_not_recognized()#sinon le mot de passe est éroné
            p=1
            break
    if p==0:#on a parcouru lines et on arrive pas à trouver le nom de l'utilisateur introduit
        user_not_found()#on appelle cette fonction
    delete2()#à la fin on appelle la fonction delete2() qui va supprimer cette onglet

def login():
    global screen2
    screen2 = Toplevel(root)
    screen2.title("login")
    screen2.geometry("300x310")
    Label(screen2, text="").pack()

    global username_entry1
    global password_entry1

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    # cette partie concerne le logo de l'utilisateur qu'on a utilisé
    Label(screen2, text="").pack()
    pil_image = Image.open("C:/Users/firdaouss/PycharmProjects/loginSystem/login.png")
    image200x100 = pil_image.resize((70, 90), Image.ANTIALIAS)
    image200x100.save("login200x100.png")
    image = ImageTk.PhotoImage(image200x100)
    panel = Label(screen2, image=image)
    panel.image = image
    panel.pack()
    #on ajoute les elements de l'interface graphique tout en spécifiant les fonctions qu'on appelle au click du bouton
    Label(screen2, text="Username ", font=("Calibri", 15)).pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password ", font=("Calibri", 15)).pack()
    password_entry1 = Entry(screen2, textvariable=password_verify,show="*")
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=2, command=login_verify, bg='snow', fg='black').pack()
    Label(screen2, text="").pack()

def register_user():
    #ici on récupère les informations introduit par l'utilisateur
    user_info = username.get()
    password_info = password.get()
    #on ouvre le fichier informations déjà crée pour ajouter les informations du nouveau utilisateur
    file1 = open("informations", "r")
    lines = file1.readlines()
    p = 0
    global label1
    for line in lines:
        if user_info in line: #si on trouve user_info dans une ligne du fichier ca veut dire que le nom d'utilisateur est déjà assigné à un autre utilisateur
            p=1
            #pour vider les zones de textes
            username_entry.delete(0, END)
            password_entry.delete(0, END)

            label1=Label(screen1, text="username not avaible!!", fg="red", font="calibri")
            label1.pack()
            break
    if p == 0: #si p=0 ca veut dire que le user_info est valable pour etre utilisé en tant que nom d'utilisateur
        #ici on ouvre le fichier pour ajouter les informations du nouveau utilisateur
        file1=open("informations","a+")
        file1.write(user_info+","+password_info+"\n")
        file1.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(screen1, text="registration successful !", fg="green", font="calibri").pack()


def register():
    global screen1
    screen1 = Toplevel(root)
    screen1.title("Register")
    screen1.geometry("300x310")

    global username
    username = StringVar()
    global password
    password = StringVar()

    #cette partie concerne le logo de l'utilisateur qu'on a utilisé
    Label(screen1, text="").pack()
    pil_image = Image.open("C:/Users/firdaouss/PycharmProjects/loginSystem/login.png")
    image200x100 = pil_image.resize((70, 90), Image.ANTIALIAS)
    image200x100.save("login200x100.png")
    image = ImageTk.PhotoImage(image200x100)
    panel = Label(screen1, image=image)
    panel.image = image
    panel.pack()
    #on déclare ces variables comme global pour pouvoir les utiliser ailleurs
    global username_entry
    global password_entry
    #ici on met des zones de texte pour récupérer les informations introduits par l'utilisateur
    Label(screen1, text="Username ",font=("Calibri", 15)).pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password",font=("Calibri", 15)).pack()
    password_entry = Entry(screen1, textvariable=password,show='*')
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=2, command=register_user,bg='snow',fg='black').pack()

def main_screen():
    #on commence par créer un onglet vide
    global root
    root = Tk()
    root.title("notes")#on donne un nom à l'onglet
    #ici on ajoute une image dans un label
    img = ImageTk.PhotoImage(Image.open("C:/Users/firdaouss/PycharmProjects/loginSystem/pic.jpg"))
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    #et à chaque fois on ajoute une composante sur l'image en precisant la position
    l1 = Label(text="Choose one of the options bellow", bg='snow', font=("Calibri", 12))
    l1.place(relx=0.75, rely=0.2, anchor=SE)
    #on précise les fonctions à appeler lorsqu'on appuie sur chaque boutton
    b1 = Button(text="Login", width="33", height="2", bg="grey", fg="white",command=login)
    b1.place(relx=0.88, rely=0.88, anchor=SE)

    b2 = Button(text="Register", width="33", height="2", bg="grey", fg="white",command=register)
    b2.place(relx=0.88, rely=0.70, anchor=SE)

    root.resizable(width=False, height=False)
    root.mainloop()

main_screen()