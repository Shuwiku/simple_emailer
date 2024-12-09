# -*- coding: utf-8 -*-
"""The exception that is raised for any error during the script's execution."""


class SimpleEmailerError(Exception):
    """Raised for any error during the script's execution."""

    def __init__(
        self,
        message: str
    ) -> None:
        """Exception initialization.

        Args:
            message (str): Message with exception information.
        """
        super().__init__(message)
