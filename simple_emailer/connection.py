# -*- coding: utf-8 -*-
"""Functions for managing the connection to the GMail SMTP server."""

import sys
from smtplib import SMTP


__connection: SMTP


def _get_connection(
) -> SMTP:
    """Returns the connection to the GMail SMTP server.

    Returns:
        SMTP: The connection to the GMail server.
    """
    try:
        return __connection
    except NameError:
        print("It seems you tried to send a message "
              "without creating a connection.")
        sys.exit()


def close_connection(
) -> None:
    """Closes the connection to the GMail SMTP server."""
    global __connection

    try:
        __connection.quit()
        del __connection
    except NameError:
        print("It seems you tried to close a connection without creating it.")
        sys.exit()


def create_connection(
    sender_email: str,
    sender_password: str
) -> None:
    """Creates a connection to the GMail SMTP server.

    Args:
        sender_email (str): The email address from which messages will be sent.
        sender_password (str): The password for the email account.
    """
    global __connection

    __connection = SMTP(
        host="smtp.gmail.com",
        port=587
    )
    __connection.starttls()
    __connection.login(
        user=sender_email,
        password=sender_password
    )
