import base64
import ssl
import pem
import OpenSSL.SSL, crypto
# context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
from ssl import Purpose
from datetime import datetime

def check_associate_cert_with_private_key(cert, private_key):
    try:
        private_key_obj = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, private_key)
    except OpenSSL.crypto.Error:
        raise Exception('Private key is not correct: %s' % private_key)

    try:
        cert_obj = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    except OpenSSL.crypto.Error:
        raise Exception('Certificate is not correct: %s' % cert)

    context = OpenSSL.SSL.Context(OpenSSL.SSL.TLSv1_METHOD)
    context.use_privatekey(private_key_obj)
    context.use_certificate(cert_obj)
    try:
        context.check_privatekey()
        return("Valid Certificate")
    except OpenSSL.SSL.Error:
        return("Invalid Certificate")


# cert = crypto.load_certificate(crypto.FILETYPE_PEM, ca-cert) 
# priv=crypto.load_privatekey(crypto.FILETYPE_PEM, private_key_text)
cert = pem.parse_file("ca-cert.pem")
priv = pem.parse_file("ca-key.pem")
# print(cert[0])
print(check_associate_cert_with_private_key(str(cert[0]),str(priv[0])))