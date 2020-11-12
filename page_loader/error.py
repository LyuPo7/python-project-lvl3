# This Python file uses the following encoding: utf-8

"""Errors module."""


class PathError(Exception):
    '''Path Exception.'''
    pass


class ConnectionError(Exception):
    '''Connection Exception.'''
    pass


class RequestError(Exception):
    '''Base Exception.'''
    pass
