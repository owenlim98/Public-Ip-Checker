from requests import get
import os
import webbrowser
import pyperclip
import selenium

fileName = "PublicIp.txt"
fileLocation = "F:\Minecraft Servers\PublicIp.txt"
filePath = "F:\Minecraft Servers"

publicIp = get("https://api.ipify.org").text

def checkIfFileExist(fileLocation):
    return os.path.exists(fileLocation)

def checkIfPublicIpStillTheSame(publicIp):
    currentIp = fileOpen.read()
    print("Current IP " + currentIp + "\nChecking if Public IP Changed")

    if currentIp != publicIp:
        print("Oops your public IP seems to have changed \nCurrent public IP is " + currentIp + "\nNew public IP is " + publicIp)
        webbrowser.open_new_tab("https://www.noip.com/")
        saveNewIP(publicIp)
        pyperclip.copy(publicIp)
        print("Save new public IP to file!")
    
    else:
        print("Current public IP still the same as before!")
        
    fileOpen.close()

def saveNewIP(publicIp):
    fileOpen.write(publicIp)

if checkIfFileExist(fileLocation):
    print("File Exist!")
    fileOpen = open(fileLocation, "r+")
    checkIfPublicIpStillTheSame(publicIp)
    
else:
    print("File does not exist, creating file now!")
    fileCreation = open(fileLocation, "w+")
    fileOpen = fileCreation
    ip = input("Public Ip please\n")
    saveNewIP(ip)
    print("Saved public IP to file!")