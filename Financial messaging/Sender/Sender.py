# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:50:14 2021

@author: SREENEHA
"""
import rsa

print("Enter 1: for sending a file")
print("Enter 2: for recieving acknowlwdgement")
print("Enter 3: exit")
option=int(input(''))

#sender privatekey
f = open("Sendprivate.key", "r")
sendprivkey = f.read()
f.close()
sprivkeyreloaded=rsa.PrivateKey.load_pkcs1(sendprivkey.encode('utf8'))


#receiver publickey
f = open("Recpublic.key", "r")
recpubkey = f.read()
f.close()
rpubkeyreloaded=rsa.PublicKey.load_pkcs1(recpubkey.encode('utf8'))

if(option==1):
    #open the message file
    f = open("transaction.json", "r")
    msg = f.read()
    f.close()

    #encryption of message
    encMessage = rsa.encrypt(msg.encode(), rpubkeyreloaded)
    f = open('encmessage.txt', 'wb')
    f.write(encMessage)
    f.close()


    #hashing message
    hashedmsg = rsa.compute_hash(msg.encode(), 'SHA-1')


    #signing with sender private key
    signedhash = rsa.sign_hash(hashedmsg, sprivkeyreloaded, 'SHA-1')
    f= open('signedhash.txt', 'wb')
    f.write(signedhash)
    f.close()
    
    print("Now we need to recieve the file from the reciver side")

elif(option==2):
    
    #open the signed hash response from reciever
    f = open("signedhashres.txt", "rb")
    signedhashres = f.read()
    f.close()

    #open the encrypted response from reciever
    f = open("encresponse.txt", "rb")
    encresponse = f.read()
    f.close()

    #decrypt the response
    decResponse = rsa.decrypt(encresponse, sprivkeyreloaded).decode()


    #verify hash of response
    if (rsa.verify(decResponse.encode(), signedhashres, rpubkeyreloaded)):
        print("Success")
