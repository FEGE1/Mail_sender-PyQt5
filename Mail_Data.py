import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import sqlite3


class Data():
    def __init__(self):

        self.baglanti_olustur()
        self.yazi_olustur()
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("MailDataBase.db")
        self.cursor=self.baglanti.cursor()

        self.cursor.execute("Create Table If Not Exists mailler (mail TEXT)")
        self.baglanti.commit()

    def yazi_olustur(self):
        self.cursor.execute("Create Table If Not Exists yazılar (yazı TEXT)")
        self.baglanti.commit()

    def yazi_değiştir(self,yeni_yazı):
        self.cursor.execute("Select * From yazılar")
        eski_yazi = self.cursor.fetchall()
        eski_yazi=eski_yazi[0][0]
        self.cursor.execute("Update yazılar set yazı=? where yazı=?", (yeni_yazı,eski_yazi))
        self.baglanti.commit()

    def yazi_göster(self):
        self.cursor.execute("Select * From yazılar")
        yazi = self.cursor.fetchall()
        yazi = yazi[0][0]
        return yazi

    def mailler(self):
        mail_liste=[]
        self.cursor.execute("Select * From mailler")
        mailler=self.cursor.fetchall()
        for i in mailler:
            i = i[0]
            mail_liste.append(i)
        return mail_liste



    def mail_ekle(self,mail):
        self.cursor.execute("Select * From mailler where mail=?",(mail,))
        a=self.cursor.fetchall()
        if len(a)==0:
            self.cursor.execute("Insert Into mailler Values(?)",(mail,))
            self.baglanti.commit()
        else:
            print("Bu Mail Zaten Mevcut")


    def mail_sil(self,mail):
        self.cursor.execute("Delete From mailler where mail=?",(mail,))
        self.baglanti.commit()

    def mailleri_gönder(self):
        self.cursor.execute("Select * From mailler")
        self.mailler=self.cursor.fetchall()
        self.cursor.execute("Select * From yazılar")
        yazi = self.cursor.fetchall()
        yazi = yazi[0][0]
        if len(self.mailler)==0:
            print("Herhangi Bir Mail Bulunmuyor !")
        else:
            for kime in self.mailler:
                mesaj = MIMEMultipart()

                mesaj["From"] = "your_mail"

                mesaj["To"] = kime[0]

                mesaj["Subject"] = "Python Mail Deneme"

                yazı = """
 Arayüz deneme Maili.
        
                """

                mesaj_gövdesi = MIMEText(yazi, "plain")

                mesaj.attach(mesaj_gövdesi)

                try:
                    mail = smtplib.SMTP("smtp.gmail.com",587)  # Hangi smtp serverine bağlanacak, Hangi port (587) gmailin kullanıma izin verdiği port

                    mail.ehlo()  # Bağlan!

                    mail.starttls()  # Şifreleme

                    mail.login("your_username", "your_password")  # Hesaba Giriş-gmail ve şifresi

                    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

                    print(kime[0], "'a mail gönderme başarılı !")


                    mail.close()  # smtp serveri ile bağlantıyı kesmek

                except:
                    sys.stderr.write("Bir sorun oluştu!")
                    sys.stderr.flush()



data=Data()

data.mailler()





