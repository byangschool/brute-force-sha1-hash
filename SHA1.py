from urllib2 import urlopen, hashlib    #Urlopen to open the URL of passwords, Hashlib to create SHA1 hashes
import sys, time    #sys to take system argument, time to time how long process takes
start = time.time()     #Used to time process

length = len(sys.argv)-1    #Takes the number of user input 
counter = 0     #Count number of tries
passwords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())   #Reads the URL with all the passwords

if length == 1:     #If user input = 1 
    for guess in passwords.split('\n'):     #For loop
        guessHashed = hashlib.sha1(bytes(guess)).hexdigest()    #Takes each password and converts to SHA1
        if guessHashed == str(sys.argv[1]):     #Compares each password in SHA1 hash to user input. If password is found, end timer and print
            end = time.time() 
            print("Password is :", str(guess), "Total attempts : ", +counter)
            print("Time taken : ", end-start)
            quit()  #Exit
        elif guessHashed != str(sys.argv[1]):   #If password not found, increment counter
            print("Password", str(guess), "does not match, trying next . . .")
            counter+=1
    print("Password not in database")   #If password can not be found

if length == 2:     #If user input = 2, reads the 2nd input (Salt term) first
    for saltTerm in passwords.split('\n'):  #For loop
        saltGuessHashed = hashlib.sha1(bytes(saltTerm)).hexdigest()     #Compares each password in SHA1 hash to salt term
        if saltGuessHashed == str(sys.argv[2]):     #If salt term is found, run second for loop with the included salt term
            for guess in passwords.split('\n'):     #For loop
                guessHashed = hashlib.sha1(bytes(saltTerm+guess)).hexdigest()   #Takes each password, with salt term on the left, and converts to SHA1
                if guessHashed == str(sys.argv[1]):     #Compares each password in SHA1 hash to user input. If password is found, end timer and print
                    end = time.time()   #Used to time process
                    print("Salt term is :", str(saltTerm), ". And Password is :", str(guess), "Total attempts : ", +counter)
                    print("Time taken : ", end-start)
                    quit()  #Exit
                elif guessHashed != str(sys.argv[2]):   #If password not found, increment counter
                    print("Password", str(guess), "does not match, trying next . . .")
                    counter+=1
        elif saltGuessHashed != str(sys.argv[2]):   #If password not found, increment counter
            print("Password", str(saltTerm), "does not match, trying next . . .")
            counter+=1
    print("Password not in database")   #If password can not be found
    
if length == 3:     #If user input = 3. 1.HashValue 2.two 3.term
    for guess in passwords.split('\n'):
        for guess2 in passwords.split('\n'):
            guessHashed = hashlib.sha1(bytes(guess+" "+guess2)).hexdigest()
            if guessHashed == str(sys.argv[1]):
                end = time.time()
                print("Password is :", str(guess+" "+guess2), "Total attempts : ", +counter)
                print("Time taken : ", end-start)
                quit()
            elif guessHashed != str(sys.argv[1]):
                print("Password", str(guess+" "+guess2), "does not match, trying next . . .")
                counter+=1
    print("Password not in database")
    
if length > 3:  #If invalid number of inputs
    print("Invalid")

