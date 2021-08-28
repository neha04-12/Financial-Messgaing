# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:26:24 2021

@author: SREENEHA
"""


import rsa


KEYLENGTH = 2048
#sender

publicKey, privateKey = rsa.newkeys(KEYLENGTH)

priv_key_file = open('Sendprivate.key', 'w')
priv_key_file.write(privateKey.save_pkcs1().decode('utf-8'))
priv_key_file.close()
    
pub_key_file = open('Sendpublic.key', 'w')
pub_key_file.write(publicKey.save_pkcs1().decode('utf-8'))
pub_key_file.close()

#receiver

publicKey, privateKey = rsa.newkeys(KEYLENGTH)

priv_key_file = open('Recprivate.key', 'w')
priv_key_file.write(privateKey.save_pkcs1().decode('utf-8'))
priv_key_file.close()
    
pub_key_file = open('Recpublic.key', 'w')
pub_key_file.write(publicKey.save_pkcs1().decode('utf-8'))
pub_key_file.close()