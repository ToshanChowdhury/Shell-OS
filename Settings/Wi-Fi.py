import os

print("""
[1] Disconnect Wi-Fi
[2] Reconnect Wi-Fi
[3] Exit
""")
print("")
Wi_Fi = input("[?]: ")

if Wi_Fi == "1":
    print("Settings Were Successfully Applied!!!")
    input("Press Enter to Exit.")

if Wi_Fi == "2":
    print("Settings Were Successfully Applied!!!")
    input("Press Enter to Exit.")

if Wi_Fi == "3":
    exit(code=1)