#! /usr/bin/python3

import imaplib
import imaplib-connect
from imaplib-list-mailboxes-parse import parse_list_response

with imaplib_connect.open_connection() as c:
    typ, mbox_data = c.list()
    for line in mbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(
            None, '(FROM "Google" SUBJECT "Sign-in attempt prevented")',
        )
        print(mbox_name, typ, msg_ids)

        # This returns the location of the requested email:
        # INBOX OK [b'2']
        # However, then returns an error around line 17, the search criteria