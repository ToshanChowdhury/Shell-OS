import os
import time
import sys

login_username = open("CD Drive/UsersData/username.user")
l_un = login_username.read()

data_names = l_un, "Admin"

ask_names = input("UserName: ")

if ask_names == l_un:
    time.sleep(1)
    os.startfile("NormalUser.py")

if ask_names == "Admin":
    time.sleep(1)
    os.startfile("AdminLogin.py")

if ask_names == "Guest":
    os.startfile("ShellOSGuest.py")