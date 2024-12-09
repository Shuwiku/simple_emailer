# -*- coding: utf-8 -*-
"""Functions for managing the connection to the GMail SMTP server."""

from smtplib import SMTP, SMTPAuthenticationError

from loguru import logger

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
        error_text: str = "It seems you tried to send a message " \
                          "without creating a connection."
        logger.error(error_text)  # Logging
        raise SimpleEmailerError(message=error_text)


def close_connection(
) -> None:
    """Closes the connection to the GMail SMTP server."""
    global __connection

    try:
        __connection.quit()
        del __connection
        logger.debug("Connection to the server is closed.")  # Logging
    except NameError:
        error_text: str = "It seems you tried to close a connection " \
                          "without creating it."
        logger.error(error_text)  # Logging
        raise SimpleEmailerError(message=error_text)


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
    logger.debug("Connected to the GMail server.")  # Logging
    try:
        __connection.login(
            user=sender_email,
            password=sender_password
        )
        # Logging
        logger.debug("Successfully authenticated on the GMail server.")
    except SMTPAuthenticationError:
        error_text: str = "The email address and password were not " \
                          "accepted by the Gmail server."
        logger.error(error_text)  # Logging
        raise SimpleEmailerError(message=error_text)
