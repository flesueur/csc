#!/usr/bin/python3

# Avoir une lib avec des briques prêtes
# Avoir un script qui crée les fichiers de password SHA/PB/etc. pour pouvoir les manipuler en texte
# TD : associer les briques pour évaluer les attaques sur un pass / une base

import re
import time
import random
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64
import os
import urllib.request
import string

# returns an array of a dictionary of passwords
def getPassDict(nbpasswords):
    try:
        f = open("files/passwords.txt")
    except FileNotFoundError:
        print("Downloading a passwords list...")
        urllib.request.urlretrieve("https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt?raw=true", "files/passwords.txt")
        print("Done !")
        f = open("files/passwords.txt")
    passwords = []
    #nbpasswords = 10000
    passtogen = nbpasswords
    for password in f:
        passwords.append(password.strip())
        passtogen-=1
        if passtogen == 0:
            break
    return passwords

def genRandomPassword():
    length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

# reads/writes shadow-style files
def readfile(filename):
    f = open("files/"+filename)
    res = []
    for line in f:
        output = line.strip().split(":")
        res.append(output)
    return res

def writeFile(filename, array):
    f = open("files/"+filename,'w')
    for line in array:
        towrite = ""
        for item in line:
            towrite+=item + ":"
        towrite = towrite[:-1]
        f.write(towrite)
        f.write('\n')


# Plain storage
def genplain(nblogins,nbpasswords):
    passwords = getPassDict(nbpasswords)
    logins = []
    for i in range(0,nblogins):
        login = "user" + str(i)
        if (random.randint(0,10) < 4):
            logins.append((login,passwords[random.randint(0,len(passwords)-1)]))
        else:
            logins.append((login,genRandomPassword()))
    return logins

def authplain(login, passwd, database):
    for i in database:
        if i[0] == login:
            current = i[1]
    return (current == passwd)

# Encrypted storage
def genencrypted(logins):
    encdb = []
    key = Random.new().read(16)
    iv = Random.new().read(AES.block_size)
    f = open("files/enckey",'wb')
    f.write((base64.b64encode(key)))
    f.write(b":")
    #f = open("files/enciv",'wb')
    f.write((base64.b64encode(iv)))
    for i in logins:
        cipher = AES.new(key, AES.MODE_CFB, iv)
        enc =  (base64.b64encode(cipher.encrypt(i[1].encode('utf-8')))).decode("utf-8")
        encdb.append((i[0],enc))
        #print(enc)
    return encdb

def authencrypted(login, passwd, database):
    for i in database:
        if i[0] == login:
            current = i[1]
    keyiv = readfile("enckey")[0]
    key = base64.b64decode(keyiv[0])
    iv = base64.b64decode(keyiv[1])
    #key = base64.b64decode(readfile("enckey")[0][0])
    #iv =  base64.b64decode(readfile("enciv")[0][0])
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return (passwd == cipher.decrypt(base64.b64decode(current)).decode('utf-8'))

def decrypt(keyiv,data):
    key = base64.b64decode(keyiv[0])
    iv = base64.b64decode(keyiv[1])
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(base64.b64decode(data)).decode('utf-8')


# SHA storage
def gensha(logins):
    db = []
    for i in logins:
        csum = hashlib.sha256(i[1].encode('utf-8')).hexdigest()
        db.append((i[0],csum))
    return db

def authsha(login, passwd, database):
    for i in database:
        if i[0] == login:
            current = i[1]
    return (current == hashlib.sha256(passwd.encode('utf-8')).hexdigest())

def genshahashes(passwords):
    hashes = []
    for passwd in passwords:
        hashes.append([hashlib.sha256(passwd.encode('utf-8')).hexdigest(),passwd])
    return hashes

def getpassfromshahash(hashes, hash):
    for j in hashes:
        if j[0] == hash:
            return j[1]
    return None

# Salted SHA storage
def gensaltedsha(logins):
    db = []
    for i in logins:
        salt = str(random.randint(0,65535))
        csum = hashlib.sha256((i[1]+salt).encode('utf-8')).hexdigest()
        db.append((i[0],csum,salt))
    return db

def authsaltedsha(login, passwd, database):
    for i in database:
        if i[0] == login:
            current = i[1]
            salt = i[2]
    return (current == hashlib.sha256((passwd+salt).encode('utf-8')).hexdigest())

def salthash(password,salt):
    return hashlib.sha256((password+str(salt)).encode('utf-8')).hexdigest()

# PBKDF2 storage
def genpbkdf2(logins,nbiterations):
    db = []
    for i in logins:
        salt = str(random.randint(0,65535))
        csum = base64.b64encode(hashlib.pbkdf2_hmac('sha256',i[1].encode('utf-8'),str(salt).encode('utf-8'),nbiterations)).decode('utf-8')
        db.append((i[0],csum,salt,str(nbiterations)))
    return db

def authpbkdf2(login, passwd, database):
    for i in database:
        if i[0] == login:
            current = i[1]
            salt = i[2]
            nbiterations = int(i[3])
    return (base64.b64decode(current) == hashlib.pbkdf2_hmac('sha256',passwd.encode('utf-8'),str(salt).encode('utf-8'),nbiterations))

def pbkdf2(password,salt,nbiterations):
    nbiterations = int(nbiterations)
    return base64.b64encode(hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),str(salt).encode('utf-8'),nbiterations)).decode('utf-8')


# Generate shadow-style files
def initworkspace(nblogins,nbpasswords,nbiterations):
    print("Generating " + str(nblogins) + " logins and " + str(nbpasswords) + " passwords")
    try :
        os.mkdir("files")
    except FileExistsError:
        pass
    plaindb = genplain(nblogins,nbpasswords)
    writeFile("plain", plaindb)
    encdb = genencrypted(plaindb)
    writeFile("enc", encdb)
    shadb = gensha(plaindb)
    writeFile("sha", shadb)
    saltedshadb = gensaltedsha(plaindb)
    writeFile("saltedsha", saltedshadb)
    pbkdf2db = genpbkdf2(plaindb,nbiterations)
    writeFile("pbkdf2", pbkdf2db)



# Unit tests
if __name__ == '__main__':
    # create shadow files
    initworkspace(10,100,1000)

    print("======\nUnit tests of the toolbox, you must work in skeleton.py\n=========")

    # test plain DB
    print("\n============\nPlain storage:")
    plaindb = readfile("plain")
    print("Plain DB is : " + str(plaindb))
    print("Authenticating with plain DB : " + str(authplain(plaindb[0][0],plaindb[0][1],plaindb)))

    #test encrypted db
    print("\n============\nEncrypted storage:")
    encdb = readfile("enc")
    print("Encrypted DB is " + str(encdb))
    print("Authenticating with encrypted DB : " + str(authencrypted(plaindb[1][0],plaindb[1][1],encdb)))

    #test SHA db
    print("\n============\nSHA storage:")
    shadb = readfile("sha")
    print("SHA DB is " + str(shadb))
    print("Authenticating with SHA DB : " + str(authsha(plaindb[0][0],plaindb[0][1],shadb)))

    #test Salted SHA db
    print("\n============\nSalted SHA storage:")
    saltedshadb = readfile("saltedsha")
    print("Salted SHA DB is " + str(saltedshadb))
    print("Authenticating with Salted SHA DB : " + str(authsaltedsha(plaindb[0][0],plaindb[0][1],saltedshadb)))

    # test PBKDF2 DB
    print("\n============\nPBKDF2 storage:")
    pbkdf2db = readfile("pbkdf2")
    print("PBKDF2 DB is " + str(pbkdf2db))
    print("Authenticating with PBKDF2 DB : " + str(authpbkdf2(plaindb[0][0],plaindb[0][1],pbkdf2db)))

    print("\n======\nUnit tests of the toolbox, you must work in skeleton.py\n=========")
