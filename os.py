import os
import time
osn = open("osname.txt")
usrls = [open("usr1"), open("usr2"), open("usr3"), open("usr4"), open("usr5"), open("usr6"), open("usr7"), open("usr8"), open("usr9"), open("usr10")]
i = 0
os.system("clear")
print("Who Are You?")
while not i = len(usrls) - 1:
  print(str(i) + ": " + usrls[i])
  i = i + 1
usrid = ""
while not int(usrid) > 10:
  usrid = input("User # (On Side): ")
os.system("clear")
while True:
  command = input("<" + osn + ">-" + usr + " | ")
  if command == "hlp" or command == "help":
    print("echo")
    print("updat")
  else:
    if command == "echo":
      tmp = input("Text To Display: ")
    else:
      if command == "updat":
        os.system("cd ~ && rm -rf derpos-backup && mkdir derpos-backup")
        os.system("cp os.py ~/derpos-backup")
        print("BACKUP CREATED!")
        print("/home/derpos-backup/os.py")
        os.system("cd ~ && git clone https://github.com/BenPI88/derpos-update && cd derpos-update && cp -f os.py ..")
        print("Setup Completed! Restarting in 10 seconds...")
        time.sleep(10)
        os.system("shutdown -r")
      else:
        print("Invalid Command")
