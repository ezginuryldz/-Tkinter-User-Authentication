from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3

def basari_mesaji_goster(isim):
   
    mesaj_pencere = Toplevel(pencere)
    mesaj_pencere.geometry("300x180")
    mesaj_pencere.title("Bilgi")
    mesaj_pencere.configure(bg="#2C1D11")
    mesaj_pencere.resizable(False, False)
    mesaj_pencere.grab_set()


    x = pencere.winfo_x() + 50
    y = pencere.winfo_y() + 100
    mesaj_pencere.geometry(f"+{x}+{y}")

    Label(mesaj_pencere, text="✨", bg="#2C1D11", fg="#F5EBE0", font=("Arial", 20)).pack(pady=(15, 0))
    Label(mesaj_pencere, text="Başarıyla Giriş Yapıldı!", bg="#2C1D11", fg="#F5EBE0", font=("Arial", 11, "bold")).pack(pady=5)
    Label(mesaj_pencere, text=f"Hoş geldiniz, {isim}", bg="#2C1D11", fg="#D7CCC8", font=("Arial", 9)).pack(pady=(0, 15))

    Button(mesaj_pencere, text="Tamam", command=mesaj_pencere.destroy, bg="#8D6E63", fg="#F5EBE0", font=("Arial", 9, "bold"), width=12, relief=RAISED).pack()

def kayit():
    ad = text.get()
    sifre = text1.get()

    try:    
        conn=sqlite3.connect("user.db")
        cursor=conn.cursor()

        cursor.execute(
            'SELECT * FROM "user" WHERE mail=? AND sifre=?',
            (ad,sifre)
        )

        kullanici=cursor.fetchone()
        conn.close()

        if kullanici:
           
            kullanici_adi = f"{kullanici[1]} {kullanici[2]}" if len(kullanici) > 2 else ad
            basari_mesaji_goster(kullanici_adi)
            text.delete(0, END)
            text1.delete(0, END)
        else:
            messagebox.showerror("UPPS","Hatalı Giriş!")

    except sqlite3.Error as hata:
        messagebox.showerror(
            "Veritabanı  Hatası",
            f"Bir hata oluştu:\n{hata}"
        )

def ana_menuye_don():
    pencere.destroy()
    subprocess.Popen([sys.executable, "main.py"])

def kayit_ekranina_gec():
    pencere.destroy()
    subprocess.Popen([sys.executable, "kayit.py"])

pencere = Tk()
pencere.geometry("400x400")
pencere.title("Giriş Ekranı")
pencere.configure(bg="#2C1D11")

LABEL_BG = "#2C1D11"
LABEL_FG = "#F5EBE0"

Label(pencere, text="Kullanıcı Adı", bg=LABEL_BG, fg=LABEL_FG, font=("Arial", 10, "bold")).place(x=70, y=80)
text = Entry(pencere, width=25, bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11")
text.place(x=170, y=80)

Label(pencere, text="Şifre", bg=LABEL_BG, fg=LABEL_FG, font=("Arial", 10, "bold")).place(x=70, y=130)
text1 = Entry(pencere, width=25, show="*", bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11")
text1.place(x=170, y=130)

Button(pencere, text="Giriş", command=kayit, bg="#8D6E63", fg="#F5EBE0", font=("Arial", 10, "bold"), width=10, relief=RAISED).place(x=170, y=180)
Button(pencere, text="Çıkış", command=pencere.destroy, bg="#3E2723", fg="#D7CCC8", font=("Arial", 10, "bold"), width=10, relief=RAISED).place(x=260, y=180)


Button(pencere, text="Ana Menüye Dön", command=ana_menuye_don, bg="#4E342E", fg="#F5EBE0", font=("Arial", 9, "bold"), width=15).place(x=70, y=250)
Button(pencere, text="Kayıt Ol'a Git", command=kayit_ekranina_gec, bg="#6D4C41", fg="#F5EBE0", font=("Arial", 9, "bold"), width=15).place(x=215, y=250)

pencere.mainloop()