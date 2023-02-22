from tkinter import *
from tkinter import messagebox

import base64
import os

def decrypt():

        password=code.get()
    
        if password=="1234":
            screen2=Toplevel(screen)
            screen2.title("Descriptador")
            screen2.geometry("400x200")
            screen2.configure(bg="#028f76")

            message=text1.get(1.0,END)
            decode_message=message.encode("ascii")
            base64_bytes=base64.b64decode(decode_message)
            decrypt=base64_bytes.decode("ascii")

            Label(screen2, text="Decriptado", font="Futura 12", fg="white", bg="#028f76").place(x=10,y=0)
            text2=Text(screen2,font="Futura 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40,width=380,height=150)

            text2.insert(END, decrypt)

        elif password=="":
            messagebox.showerror("Crypter","Insira a chave de acesso!")
        elif password !="1234":
                messagebox.showerror("Crypter","chave inválida!")

def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("Crypter")
        screen1.geometry("400x200")
        screen1.configure(bg="#005bc5")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="Criptografado", font="Futura 12", fg="white", bg="#005bc5").place(x=10,y=0)
        text2=Text(screen1,font="Futura 12", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40,width=380,height=150)

        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("Crypter","Insira a chave de acesso!")
    elif password !="1234":
            messagebox.showerror("Crypter","Chave inválida!")

def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("375x398")
    screen.configure(bg="#23192d")
    
    #icon
    image_icon=PhotoImage(file="./img/padlock.png")
    screen.iconphoto(False,image_icon)

    screen.title("Crypter")

    def reset():
        code.set("")
        text1.delete(1.0,END) 
    
    Label(text="Digite um texto para encriptar/decriptar:", fg="white",bg="#23192d",font="Futura 12 bold").place(x=10, y=10)
    text1=Text(font="Futura 18", bg="white", relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Digite a chave de acesso", fg="white", bg="#23192d", font="Futura 12 bold").place(x=10, y=165)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font="Futura 18", show="*").place(x=10, y=200)

    Button(text="Encriptar", font="Futura 9 bold", height="2", width=23, bg="#005bc5", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="Desencriptar",font="Futura 9 bold", height="2", width=23,bg="#005bc5",fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="Limpar", font="Futura 9 bold", height="2", width=50,bg="#028f76",fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()