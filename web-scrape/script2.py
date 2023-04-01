import requests

dld_file = requests.get('https://www.gutenberg.org/files/1661/1661-0.txt')

print('status code ' + str(dld_file.status_code))

print('length (in characters) ' + str(len(dld_file.text)))

textfile = open('sherlock_holmes.txt', 'wb')

for chunk in dld_file.iter_content(1000000000) : # no. of bytes each chunk will contain, 1000000000 bytes = 1 gigabyte
    textfile.write(chunk)

textfile.close()