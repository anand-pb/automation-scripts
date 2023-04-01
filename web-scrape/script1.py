import webbrowser, sys, pyperclip

sys.argv # ['', '', '', .....]

# check if command line arguments have passed
if len(sys.argv) > 1 :
    # 335 Pioneer Way, Mountain View, CA
    # ['script1.py', '335', 'Pioneer', 'Way', 'Mountain', 'View', 'CA']
    address = ' '.join(sys.argv[1:])
else :
    address = pyperclip.paste()

# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/' + address)