#!/usr/bin/python3

from sys import argv, stderr, exit


class Error(Exception):
    def __init__(self, message, errors="Error"):
        super().__init__(message)
        self.errors = errors
