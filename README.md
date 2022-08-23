`The OpenSSL Project develops and maintains the OpenSSL software - a robust, commercial-grade, full-featured toolkit for general-purpose cryptography and secure communication`


## Generate CA's Private Key and Self-Signed Certificates


### Create/ Generate Certificate and Signature
`openssl req -x509 -newkey rsa:4096 -days 365 -keyout ca-key.pem -out ca-cert.pem`

#### View Certificate Detailes
`openssl x509 -in ca-cert.pem -noout -text`

## Verify Signatures
`python ver.py`
