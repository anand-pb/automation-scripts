import imapclient

import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)

conn.login('apb.softdev@gmail.com', '') # enter app pwd here

conn.select_folder('INBOX', readonly = True)

# print(conn)

UIDs = conn.search(['FROM', 'apb7912953@gmail.com'])

# print(UIDs)

# print(conn.fetch([28], ['BODY[]', 'FLAGS']))

rawMessage = conn.fetch([28], ['BODY[]', 'FLAGS'])

pyzmail.PyzMessage.factory(rawMessage[28][b'BODY[]'])

message = pyzmail.PyzMessage.factory(rawMessage[28][b'BODY[]'])

print(message.text_part.get_payload().decode('UTF-8'))