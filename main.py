import requests
import hashlib


def request_data(query_char):
    url = 'http://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        print("error")
    return res


def count(data, my_tail):
    hashes = (line.split(':') for line in data.text.splitlines())
    for h, c in hashes:
        if h == my_tail:
            return c
    return 0


def check(password1):
    hashed = hashlib.sha1(password1.encode('utf-8')).hexdigest().upper()
    first5_char, tail = hashed[:5], hashed[5:]
    response = request_data(first5_char)
    return count(response, tail)


password = input("enter a password: ")
count = check(password)
print(f"{password} has been found {count} times")
