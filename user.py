from getpass import getpass

username=input('enter username:-')
password= getpass('enter password:-')

if username =="sai" and password=="1234":
    print('Welcome',username)

else:
    print('invalid uname or password ')
