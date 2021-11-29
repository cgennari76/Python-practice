#!/usr/bin/env python3
import ssl
import socket
import datetime

hostname = "etsy.com"
port = '443'
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname = hostname) as ssock:
        certificate = ssock.getpeercert()

#certificate variable is equal to a dictionary with a "notAfter" key and value is expiration date
search_key = 'notAfter'
certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
res = dict(filter(lambda x: search_key in x[0], certificate.items()))

daysToExpiration = (certExpires - datetime.datetime.now()).days

# printing result 
print("Day of expiration: " + str(list(res.values())))
print("Days until expiration: " + str(daysToExpiration))