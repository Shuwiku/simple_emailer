# -*- coding: utf-8 -*-
"""Sends an email."""

from smtplib import SMTP
from email.mime.text import MIMEText

from loguru import logger

from .connection import _get_connection


def send_email(
    email_text: str,
    recipient_email: str,
    sender_email: str,
    subject: str,
    email_type: str = "html"
) -> None:
    """Sends an email.

    Args:
        email_text (str): The text of the email.
        recipient_email (str): The recipient's email address.
        sender_email (str): The sender's email address.
        subject (str): The subject of the email.
        email_type (str, optional): The format type of the text.
            Defaults to 'html'.
    """
    email_message: MIMEText = MIMEText(
        email_text,
        email_type
    )
    email_message["From"] = sender_email
    email_message["Subject"] = subject
    email_message["To"] = recipient_email

    connection: SMTP = _get_connection()
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=recipient_email,
        msg=email_message.as_string()
    )

    logger.debug("Email sent successfully.")  # Logging
