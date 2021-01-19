#!/usr/bin/env python3

import time
import sys
from toolbox import *

# You should tweak these values during the work
nblogins = 10         # would be larger in real-life
nbpasswords = 1000000 # would be larger in real-life
nbiterations = 10     # 10000 is currently recommended, should be adapted to the usecase and changed with time (improvement of computation power), like a key size


############################################
# Part of the script to edit               #
############################################

# Hint : you can call decrypt(key,data) to decrypt data using key
def crackencrypted(database):
    key = readfile("enckey")[0]
    crackeddb = []
    for i in database:
        # i[0] is the login, i[1] is the encrypted password
        #...
        crackeddb.append((i[0],i[1])) # second argument should contain cleartext password
    return crackeddb

# Hint : - genshahashes(passwords) returns all the hashes of passwords dictionary
#        - getpassfromshahash(hashes, hash) returns the password which hashed as "hash" in hashes
def cracksha(database):
    global nbpasswords
    passwords = getPassDict(nbpasswords) # passwords contains a dictionary of passwords
    #...
    crackeddb = []
    for i in database:
        # i[0] is the login, i[1] is the hashed password
        #...
        crackeddb.append((i[0],i[1])) # second argument should contain cleartext password
    return crackeddb

# Hint : salthash(password, salt) return the salted hash of password
def cracksaltedsha(database):
    global nbpasswords
    passwords = getPassDict(nbpasswords)
    crackeddb = []
    for i in database:
        # i[0] is the login, i[1] is the hashed password, i[2] is the salt
        #...
        crackeddb.append((i[0],i[1])) # second argument should contain cleartext password
    return crackeddb

# Hint : pbkdf2(password, salt, nbiterations) returns the pbkdf2 of password using salt and nbiterations
def crackpbkdf2(database):
    global nbpasswords
    passwords = getPassDict(nbpasswords)
    crackeddb = []
    for i in database:
        # i[0] is the login, i[1] is the hashed password, i[2] is the salt, i[3] is the iteration count
        #...
        crackeddb.append((i[0],i[1])) # second argument should contain cleartext password
    return crackeddb



############################################
# Nothing to change after this line !      #
############################################


if __name__ == '__main__':
    # When called with init
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        initworkspace(nblogins,nbpasswords,nbiterations)
        print("Workspace initialized in files/ subdirectory")
        exit(0)

    # Test whether init has been called before
    try :
        readfile("plain")
    except FileNotFoundError:
        initworkspace(nblogins,nbpasswords,nbiterations)
        print("Workspace initialized in files/ subdirectory")

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
    start = time.time()
    crackedenc = crackencrypted(encdb)
    end = time.time()
    print("Time to crack encrypted DB : " + str(end-start) + " seconds")
    print("Cracked encrypted DB is " + str(crackedenc))

    #test SHA db
    print("\n============\nSHA storage:")
    shadb = readfile("sha")
    print("SHA DB is " + str(shadb))
    print("Authenticating with SHA DB : " + str(authsha(plaindb[0][0],plaindb[0][1],shadb)))
    start = time.time()
    crackedsha = cracksha(shadb)
    end = time.time()
    print("Time to crack SHA DB : " + str(end-start) + " seconds")
    print("Cracked SHA DB is " + str(crackedsha))

    #test Salted SHA db
    print("\n============\nSalted SHA storage:")
    saltedshadb = readfile("saltedsha")
    print("Salted SHA DB is " + str(saltedshadb))
    print("Authenticating with Salted SHA DB : " + str(authsaltedsha(plaindb[0][0],plaindb[0][1],saltedshadb)))
    start = time.time()
    crackedsaltedsha = cracksaltedsha(saltedshadb)
    end = time.time()
    print("Time to crack salted SHA DB : " + str(end-start) + " seconds")
    print("Cracked salted SHA DB is " + str(crackedsaltedsha))

    # test PBKDF2 DB
    print("\n============\nPBKDF2 storage:")
    pbkdf2db = readfile("pbkdf2")
    print("PBKDF2 DB is " + str(pbkdf2db))
    print("Authenticating with PBKDF2 DB : " + str(authpbkdf2(plaindb[0][0],plaindb[0][1],pbkdf2db)))
    start = time.time()
    crackedpbkdf2 = crackpbkdf2(pbkdf2db)
    end = time.time()
    print("Time to crack PBKDF2 DB : " + str(end-start) + " seconds")
    print("Cracked PBKDF2 DB is " + str(crackedpbkdf2))
