from flask.ext.mail import Message
from app import mail
from threading import Thread
from flask import render_template
from config import ADMINS, DOMAIN_TITLE

def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    thr = Thread(target = send_async_email, args = [msg])
    thr.start()    

def password_reset_request(user, password_reset_url):
    send_email("Reset your %s password" % DOMAIN_TITLE,
        ADMINS[0],
        [user.email],
        render_template("password_reset_request.txt", 
            domain_title = DOMAIN_TITLE, password_reset_url = password_reset_url, user=user),
        render_template("password_reset_request.html", 
            domain_title = DOMAIN_TITLE, password_reset_url = password_reset_url, user=user))