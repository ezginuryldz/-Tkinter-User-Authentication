
from tkinter import *
import subprocess
import sys

def kayit_ekranina_git():
    menu_pencere.destroy() 
    subprocess.Popen([sys.executable, "kayit.py"])  

def giris_ekranina_git():
    menu_pencere.destroy() 
    subprocess.Popen([sys.executable, "gui.py"])  

menu_pencere = Tk()
menu_pencere.geometry("350x300")
menu_pencere.title("Ana Menü")
menu_pencere.configure(bg="#2C1D11")

Label(menu_pencere, text="Hoş Geldiniz", bg="#2C1D11", fg="#F5EBE0", font=("Segoe UI", 16, "bold")).pack(pady=35)
Button(menu_pencere, text="Kayıt Ol", command=kayit_ekranina_git, bg="#6D4C41", fg="#F5EBE0", font=("Segoe UI", 11, "bold"), width=18, relief=RAISED, cursor="hand2").pack(pady=10)
Button(menu_pencere, text="Giriş Yap", command=giris_ekranina_git, bg="#8D6E63", fg="#F5EBE0", font=("Segoe UI", 11, "bold"), width=18, relief=RAISED, cursor="hand2").pack(pady=10)

menu_pencere.mainloop()