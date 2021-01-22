
password = "Mypassword1234"
ask_for_password = input("Password?")
tries = 0

while ask_for_password != password:   #  !=  means not equals
    tries += 1                         #we add 1 to our try, if you write your password wrong, it'll add 1 trie to it
    if tries == 3:                     #if it reach 3 tries
        print("Rendszer lezárva!")   #our system close
        break                        #close
    print("Wrong password, try again")
    ask_for_password = input("Password")


if ask_for_password == password:
    print("Succesfully login")