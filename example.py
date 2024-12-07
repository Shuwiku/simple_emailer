# -*- coding: utf-8 -*-
"""Example of using simple_emailer."""

from simple_emailer import close_connection, create_connection, send_email


recipient_email: str = ""
sender_mail: str = ""
sender_password: str = ""
subject: str = "Your email subject."

with open("email.html", mode="r", encoding="utf-8") as f:
    email_text = f.read()

create_connection(
    sender_email=sender_mail,
    sender_password=sender_password
)
send_email(
    email_text=email_text,
    recipient_email=recipient_email,
    sender_email=sender_mail,
    subject=subject
)
close_connection()

print("Email sent.")
