# Simple Emailer

A small script that allows you to connect to the GMail SMTP server and send emails.

---

### Basic Usage

```python
from simple_emailer import close_connection, create_connection, send_email


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
```

For more details, see the [example files](https://github.com/Shuwiku/Shuwiku/tree/main/simple_emailer).

---

### Brief Documentation

- ```python
    connection._get_connection() -> smtplib.SMTP: ...
    ```

    Returns an SMTP connection to the GMail server. Not used directly by the user, only from `sendemail.sendemail`. If the connection has not been established, it will raise `SimpleEmailerError` exception.

- ```python
    connection.close_connection() -> None: ...
    ```

    Closes the SMTP connection to the GMail server. Use at the very end of the program to avoid creating a new connection each time. If the connection has not been established, it will raise `SimpleEmailerError` exception.

- ```python
    connection.create_connection(  
        sender_email: str,
        sender_password: str
    ) -> None: ...
    ```

    Creates an SMTP connection to the GMail server and secures it with TLS protocol. Use at the very beginning of the program and forget about this function's existence.

    - `sender_email: str` - the email address from which messages will be sent;

    - `sender_password: str` - application password. Note that this is **NOT** your Google account password, but specifically an application password. For more details, see the "App passwords" section in the "Security" section of your Google account.

- ```python
    send_email.send_email(
        email_text: str,
        recipient_email: str,
        sender_email: str,
        subject: str,
        email_type: str = "html"
    ) -> None:
    ```

     Sends a message.

    - `email_text: str` - the text of the email;

    - `recipient_email: str` - the email address of the recipient;

    - `sender_email: str` - the email address from which messages will be sent;

    - `sender_password: str` - application password. Note that this is **NOT** your Google account password, but specifically an application password. For more details, see the "App passwords" section in the "Security" section of your Google account.

    - `subject: str` - the subject of the email;

    - `email_type: str` - the formatting type of the email text (e.g., "plain" or "html"). Default is "html".

- ```python
    send_email_quick.send_email_quick(
        email_text: str,
        recipient_email: str,
        sender_email: str,
        sender_password: str,
        subject: str,
        email_type: str = "html"
    ) -> None: ...
    ```

    Establishes a connection, sends the email, and closes the connection. It is a combination of the functions `create_connection`, `close_connection`, and `send_email`.

    - `email_text: str` - the text of the email;

    - `recipient_email: str` - the email address of the recipient;

    - `sender_email: str` - the email address from which messages will be sent;

    - `subject: str` - the subject of the email;

    - `email_type: str` - the formatting type of the email text (e.g., "plain" or "html"). Default is "html".

- ```python
    simple_emailer_error.SimpleEmailerError()
    ```

    The exception that is raised for any error during the script's execution.

---

### Data Security

Although in the `example.py` I stored all data directly in the code, I strongly advise against doing so. I made it this way for brevity and clarity, but in a real project, I would recommend storing the email address from which messages are sent, as well as its password, in environment variables.
