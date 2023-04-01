import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

# print(type(conn))

# print(conn)

conn.ehlo()

conn.starttls()

conn.login('apb.softdev@gmail.com', '') # enter app pwd here

conn.sendmail('apb.softdev@gmail.com', 
              'apb7912953@gmail.com', 
              'Subject: let\'s catchup \n\nhey buddy,\nthere\'s a lot to talk about, we should be meeting sometime \n\nregards\napb'
)

conn.quit()