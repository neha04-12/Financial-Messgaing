# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 10:29:08 2021

@author: SREENEHA
"""


import rsa


#function ( fileprefix)

#hashfile = fileprefix+ "hash.txt"

print("Enter 1: for recieving a file")
print("Enter 2: for sending acknowlwdgement")
print("Enter 3: exit")
option=int(input(''))

#sender publickey
f = open("Sendpublic.key", "r")
sendpubkey = f.read()
f.close()
spubkeyreloaded=rsa.PublicKey.load_pkcs1(sendpubkey.encode('utf8'))

#reciever privatekey
f = open("Recprivate.key", "r")
recprivkey = f.read()
f.close()
rprivkeyreloaded=rsa.PrivateKey.load_pkcs1(recprivkey.encode('utf8'))

if (option==1):

    #open the signed hash from sender
    f = open("signedhash.txt", "rb")
    signedhash = f.read()
    f.close()

    #open the encrypted message from sender
    f = open("encmessage.txt", "rb")
    encmessage = f.read()
    f.close()

    
    #decrypt the message with reciever private key
    decMessage = rsa.decrypt(encmessage, rprivkeyreloaded).decode()


    #verify hash
    if (rsa.verify(decMessage.encode(), signedhash, spubkeyreloaded)):
        print("Success")

elif (option==2):
    
    #open the response file
    f = open("response.json", "r")
    response = f.read()
    f.close()
    

    #encryption of response
    encResponse = rsa.encrypt(response.encode(), spubkeyreloaded)
    f = open('encresponse.txt', 'wb')
    f.write(encResponse)
    f.close()


    #hashing response
    hashedres = rsa.compute_hash(response.encode(), 'SHA-1')


    #signing the hashed response with reciever private key
    signedhashres = rsa.sign_hash(hashedres, rprivkeyreloaded, 'SHA-1')
    f= open('signedhashres.txt', 'wb')
    f.write(signedhashres)
    f.close()
    
    print("Now we need to recieve the response from the sender side")
    

