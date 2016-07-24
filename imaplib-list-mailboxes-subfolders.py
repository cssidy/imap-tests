#! /usr/bin/python3



import imaplib

from imaplib-connect import open_connection

with open_connection() as c:
    typ, data = c.list(directory='INBOX')
    # In this example, INBOX has not children.
    # Choose a folder with children to see the subfolders.

print('Response code:', typ)

for line in data:
    print('Server response:', line)