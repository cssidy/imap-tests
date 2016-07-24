#! /usr/bin/python3

# most gullible email bot, the "gullibot"
# cassidy brooke 2016


import imaplib
import re

from imaplib-connect import open_connection
from imaplib-list-mailboxes-parse import parse_list_response

with open_connection() as c:
    typ, data = c.list()
    for line in data:
        flags, delimiter, mailbox = parse_list_response(line)
        print('Mailbox:', mailbox)
        status = c.status(
            '"{}"'.format(mailbox),
            '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)',
            # Shows how many emails are in each mailbox folder.
            # MESSAGES The number of messages in the mailbox.
            # RECENT The number of messages with the \Recent flag set.
            # UIDNEXT The next unique identifier value of the mailbox.
            # UIDVALIDITY The unique identifier validity value of the mailbox.
            # UNSEEN The number of messages which do not have the \Seen flag set.
        )
        print(status)