import sys

print("Change Battery Settings")
print("")
print("""
[1] Turn On Power Saver
[2] Turn Off Power Saver
[3] Exit
""")
print("")
Battery = input("[?]: ")

if Battery == "1":
    print("Settings Were Successfully Applied!!!")
    input("Press Enter To Exit.")

if Battery == "2":
    print("Settings Were Successfully Applied!!!")
    input("Press Enter to Exit.")

if Battery == "3":
    exit(sys.exit())