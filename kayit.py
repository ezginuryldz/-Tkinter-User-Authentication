from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import sqlite3
def kayitol():
    ad = text.get().strip()
    soyad = text1.get().strip()
    mail = text2.get().strip()
    sifre = text3.get()

    if not ad or not soyad or not mail or not sifre:
        messagebox.showerror("UPSSS", "Lütfen bütün alanları doldurun!")
        return

    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM "user" WHERE mail = ?',
            (mail,)
        )
        mevcut_kullanici = cursor.fetchone()
        if mevcut_kullanici:
            messagebox.showerror(
                "Hata",
                "Bu e-mail adresi zaten kayıtlı!"
            )
            conn.close()
            return
     
        cursor.execute("""
            INSERT INTO "user" (isim,soyisim,mail,sifre)
            VALUES (?, ?, ?, ?)
        """, (ad, soyad, mail, sifre))
        conn.commit()
        conn.close()
        messagebox.showinfo(
            "Harika",
            "Kayıt başarıyla oluşturuldu!"
        )

 
        text.delete(0, END)
        text1.delete(0, END)
        text2.delete(0, END)
        text3.delete(0, END)

    except sqlite3.Error as hata:
        messagebox.showerror(
            "Veritabanı Hatası",
            f"Bir hata oluştu:\n{hata}"
        )


def ana_menuye_don():
    cerceve.destroy()
    subprocess.Popen([sys.executable, "main.py"])

def giris_ekranina_gec():
    cerceve.destroy()
    subprocess.Popen([sys.executable, "gui.py"])

cerceve = Tk()
cerceve.geometry("500x450")
cerceve.title("Kayıt Ekranı")
cerceve.configure(bg="#2C1D11")

LABEL_BG = "#2C1D11"
LABEL_FG = "#F5EBE0"

Label(cerceve, text="First Name", bg=LABEL_BG, fg=LABEL_FG, font=("Segoe UI", 10, "bold")).place(x=100, y=70)
text = Entry(cerceve, width=30, bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11", font=("Segoe UI", 10))
text.place(x=200, y=70)

Label(cerceve, text="Last Name", bg=LABEL_BG, fg=LABEL_FG, font=("Segoe UI", 10, "bold")).place(x=100, y=120)
text1 = Entry(cerceve, width=30, bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11", font=("Segoe UI", 10))
text1.place(x=200, y=120)

Label(cerceve, text="E-mail", bg=LABEL_BG, fg=LABEL_FG, font=("Segoe UI", 10, "bold")).place(x=100, y=170)
text2 = Entry(cerceve, width=30, bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11", font=("Segoe UI", 10))
text2.place(x=200, y=170)

Label(cerceve, text="Password", bg=LABEL_BG, fg=LABEL_FG, font=("Segoe UI", 10, "bold")).place(x=100, y=220)
text3 = Entry(cerceve, width=30, show="*", bd=2, relief=GROOVE, bg="#EFEBE9", fg="#2C1D11", font=("Segoe UI", 10))
text3.place(x=200, y=220)

Button(cerceve, text="Kayıt Ol", command=kayitol, bg="#8D6E63", fg="#F5EBE0", font=("Segoe UI", 10, "bold"), width=15, relief=RAISED, cursor="hand2").place(x=200, y=270)


Button(cerceve, text="Ana Menüye Dön", command=ana_menuye_don, bg="#4E342E", fg="#F5EBE0", font=("Segoe UI", 9, "bold"), width=15, relief=RAISED, cursor="hand2").place(x=100, y=330)
Button(cerceve, text="Giriş Yap'a Git", command=giris_ekranina_gec, bg="#6D4C41", fg="#F5EBE0", font=("Segoe UI", 9, "bold"), width=15, relief=RAISED, cursor="hand2").place(x=260, y=330)

cerceve.mainloop()