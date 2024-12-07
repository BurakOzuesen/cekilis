import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

kisiler = ["Ece", "Burak", "Samet", "Şeyma", "Berkay", "Irmak", "Oğuzhan", "Nisa", "Buğra", "Duygu"]
sevgililer = {"Burak": "Ece", "Ece": "Burak",
              "Samet": "Şeyma", "Şeyma": "Samet",
              "Berkay": "Irmak", "Irmak": "Berkay",
              "Oğuzhan": "Nisa", "Nisa": "Oğuzhan",
              "Buğra": "Duygu", "Duygu": "Buğra"}

def karistir_ve_eslestir(kisiler, sevgililer):
    while True:
        random.shuffle(kisiler)
        hediye_eslesmeleri = {}

        for i, kisi in enumerate(kisiler):
            hediye_eslesmeleri[kisi] = kisiler[(i + 1) % len(kisiler)]

        if all(hediye_eslesmeleri[kisi] != sevgili for kisi, sevgili in sevgililer.items()):
            return hediye_eslesmeleri

hediye_eslesmeleri = karistir_ve_eslestir(kisiler, sevgililer)

for kisi, hediye_alacak in hediye_eslesmeleri.items():
    dosya_adi = f"{kisi}.txt"
    with open(dosya_adi, "w", encoding="utf-8") as dosya:  # UTF-8 formatında yazılıyor
        dosya.write(f"Merhaba {kisi},\n\nHediye alacağınız kişi: {hediye_alacak}\n")

def email_gonder(gonderici_email, gonderici_sifre, alici_email, konu, mesaj, dosya_adi):
    try:
        msg = MIMEMultipart()
        msg['From'] = gonderici_email
        msg['To'] = alici_email
        msg['Subject'] = konu

        # Mesaj içeriğini UTF-8 olarak ayarla
        msg.attach(MIMEText(mesaj, 'plain', 'utf-8'))

        # Ek dosyayı UTF-8 olarak oku ve ekle
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            attachment = MIMEText(dosya.read(), 'plain', 'utf-8')
            attachment.add_header('Content-Disposition', 'attachment', filename=dosya_adi)
            msg.attach(attachment)

        # SMTP bağlantısı
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(gonderici_email, gonderici_sifre)
            server.send_message(msg)

        print(f"E-posta başarıyla gönderildi: {alici_email}")
    except Exception as e:
        print(f"E-posta gönderiminde hata oluştu: {str(e)}")



email_adresleri = {
    "Person1": "person1@gmail.com"
}

# E-posta bilgileri
# Burada örnek olarak Gmail kullanıldı. Gerçek e-posta gönderimi için kendi bilgilerinizi ekleyin.
# Bu kısım şu an sadece açıklama olarak bırakılmıştır.
# gonderici_email = "example@mail.com"
# gonderici_sifre = "password"
for kisi in kisiler:
    alici_email = email_adresleri[kisi]  # Alıcı e-posta adresini uygun şekilde ayarlayın
    konu = "Hediyeleşme Bilgisi"
    mesaj = f"Merhaba {kisi},\n\nHediye alacağınız kişi bilgisi ektedir."
    dosya_adi = f"{kisi}.txt"
    email_gonder(gonderici_email, gonderici_sifre, alici_email, konu, mesaj, dosya_adi)