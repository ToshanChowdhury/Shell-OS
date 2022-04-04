import sys
import os
import time

print("Welcome to the Shell OS Setup.")
print("")
username = input("Let's start by knowning your name: ")
print("")
password = input("Let's set up a password for"+" "+username+": ")
time.sleep(4)

with open("CD Drive/UsersData/username.user", "w") as a:
	a.writelines(username)

with open("CD Drive/UsersData/password.pass", "w") as b:
	b.writelines(password)

print("")
print("Setup was complete!!!")
choice = input()

if choice == "start":
	os.startfile("ShellOS.py")

if choice == "Start":
	os.startfile("ShellOS.py")

if choice == "exit":
	sys.exit()

if choice == "Exit":
	sys.exit()