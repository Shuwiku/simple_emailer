# -*- coding: utf-8 -*-
"""Establishes a connection, sends the email, and closes the connection."""

from .connection import create_connection, close_connection
from .send_email import send_email


def send_email_quick(
    email_text: str,
    recipient_email: str,
    sender_email: str,
    sender_password: str,
    subject: str,
    email_type: str = "html"
) -> None:
    """Establishes a connection, sends the email, and closes the connection.

    Args:
        email_text (str): The text of the email.
        recipient_email (str): The recipient's email address.
        sender_email (str): The sender's email address.
        sender_password (str): The password for the email account.
        subject (str): The subject of the email.
        email_type (str, optional): The format type of the text.
            Defaults to 'html'.
    """
    create_connection(
        sender_email=sender_email,
        sender_password=sender_password
    )
    send_email(
        email_text=email_text,
        email_type=email_type,
        recipient_email=recipient_email,
        sender_email=sender_email,
        subject=subject
    )
    close_connection()
