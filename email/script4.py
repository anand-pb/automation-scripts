from imapclient import IMAPClient

HOST = "imap.gmail.com"
USERNAME = "apb.softdev@gmail.com"
PASSWORD = "" # enter app pwd here

server = IMAPClient(HOST)
server.login(USERNAME, PASSWORD)
server.select_folder("INBOX")

server.idle()
print("connection is now in IDLE mode, send yourself an email or quit with ^C")

while True:
    try:
        responses = server.idle_check(timeout = 30)
        print("server sent:", responses if responses else "nothing")
    except KeyboardInterrupt:
        break

server.idle_done()
print("\nIDLE mode done") 
server.logout()           