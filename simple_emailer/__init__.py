# -*- coding: utf-8 -*-
"""Simple functions for sending emails."""

# This allows importing functions directly from the module
# Instead of:   from simple_emailer.connection import close_connection
# It will be:   from simple_emailer import close_connection
from .connection import (  # noqa: F401
    close_connection,
    create_connection
)
from .send_email import send_email  # noqa: F401
from .send_email_quick import send_email_quick  # noqa: F401
from .simple_emailer_error import SimpleEmailerError  # noqa: F401
