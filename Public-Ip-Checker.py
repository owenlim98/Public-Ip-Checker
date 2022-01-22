from requests import get
import os
import webbrowser

fileName = "PublicIp.txt"
fileLocation = "F:\Minecraft Servers\PublicIp.txt"
filePath = "F:\Minecraft Servers"

publicIp = get("https://api.ipify.org").text

def checkIfFileExist(fileLocation):
    return os.path.exists(fileLocation)

def checkIfPublicIpStillTheSame(publicIp):
    if currentIp != publicIp:
        print("Oops your public IP seems to have changed \nCurrent public IP is " + currentIp + "\nNew public IP is " + publicIp)
        webbrowser.open_new_tab("https://www.noip.com/")
        saveNewIP(publicIp)
        print("Save new public IP to file!")
    
    else:
        fileOpen.close()
        print("Current public IP still the same as before!")

def saveNewIP(publicIp):
    fileOpen.write(publicIp)
    fileOpen.close()
    

if checkIfFileExist(fileLocation):
    fileOpen = open(fileLocation, "r+")
    currentIp = fileOpen.read()
    print("Current IP " + currentIp + "\nChecking if Public IP Changed")
    checkIfPublicIpStillTheSame(publicIp)

else:
    print("File does not exist, creating file now!")
    fileCreation = open(fileLocation, "w+")
    fileOpen = fileCreation
    ip = input("Public Ip please\n")
    saveNewIP(ip)
    print("Saved public IP to file!")