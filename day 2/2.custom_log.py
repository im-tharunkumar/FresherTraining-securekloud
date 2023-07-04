import logging
 
#declare custom log
log=logging.getLogger(__name__) #variable name declare as log

log.setLevel(logging.DEBUG) #set log level

file=logging.FileHandler('2.custom_log.log', mode = 'w') #declare lof file and mode is write

f=logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s') #setting format

file.setFormatter(f) #assign format to file

log.addHandler(file) #assign file to log

#Lets try custom log with program that finds user is a major or not

def Ismajor(age):
    if age<0:
        log.critical("age is undefined")
    elif age==0:
        log.error("age enter as 0")
    elif age<18:
        log.warning("You are not major")
    else:
        log.info("User is major")

try:
    a=input("Enter your name:\n")
    b=int(input("Enter age:\n"))
    log.debug("User enter their information")
    Ismajor(b)
except ValueError as ve:
    log.exception("Excpetion", str(ve))