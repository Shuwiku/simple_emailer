# -*- coding: utf-8 -*-
"""Functions for managing the connection to the GMail SMTP server."""

from smtplib import SMTP, SMTPAuthenticationError

from .simple_emailer_error import SimpleEmailerError


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
        raise SimpleEmailerError(
            message="It seems you tried to send a message "
                    "without creating a connection."
        )


def close_connection(
) -> None:
    """Closes the connection to the GMail SMTP server."""
    global __connection

    try:
        __connection.quit()
        del __connection
    except NameError:
        raise SimpleEmailerError(
            message="It seems you tried to close a connection "
                    "without creating it."
        )


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
    try:
        __connection.login(
            user=sender_email,
            password=sender_password
        )
    except SMTPAuthenticationError:
        raise SimpleEmailerError(
            message="The email address and password were not "
                    "accepted by the Gmail server."
        )
