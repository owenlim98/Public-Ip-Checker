from requests import get
import os
import webbrowser

fileName = "PublicIp.txt"
fileLocation = "F:\Minecraft Servers\PublicIp.txt"
filePath = "F:\Minecraft Servers"

publicIp = get("https://api.ipify.org").text
currentIp = ""

def checkIfFileExist(fileLocation):
    return os.path.exists(fileLocation)

def checkIfPublicIpStillTheSame(publicIp):
    print("Current Public Ip is " + currentIp, "\nNew Public Ip is " + publicIp)
    if currentIp != publicIp:
        print("Oops your public IP seems to have changed")
        webbrowser.open_new_tab("https://www.noip.com/")
        saveNewIP()
        print("Save new public IP to file!")
    
    else:
        print("Current public IP still the same as before!")

def saveNewIP():
    fileOpen.write(publicIp)
    fileOpen.close()
    

if checkIfFileExist(fileLocation):
    fileOpen = open(fileLocation, "w+")
    currentIp = fileOpen.read()
    print("Checking if Public IP Changed")
    checkIfPublicIpStillTheSame(publicIp)

else:
    print("File does not exist, creating file now!")
    fileCreation = open(fileLocation, "w+")
    saveNewIP()
    print("Saved public IP to file!")