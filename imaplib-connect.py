#! /usr/bin/python3

import imaplib
import configparser
import os


def open_connection(verbose=True):
    # Read the config file
    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    hostname = ('imap.gmail.com')
    if verbose:
        print('Connecting to', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    email_account = ('user@gmail.com')
    password = ('password')
    if verbose:
        print('Logging in as', email_account)
    connection.login(email_account, password)
    return connection

# prints results of def open_connection
if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)