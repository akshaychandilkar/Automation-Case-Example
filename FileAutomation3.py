from sys import *
import os
import time

def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)

   
    for foldername, subfoldername, filename, in os.walk(DirName):
        print("Current Directory name :",foldername)

    for subname in subfoldername:
        print("Subfolder name is:",subname)

    for fname in filename:
        print(fname)

def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to perform File Automations")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument")
        print("Example : Demo.py Marvellous")
        exit()

    else:
        starttme = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time() 
        
        print("The script took time to execute as : ",endtime-starttme)
        
if __name__ == "__main__":
    main()

# python FileAutomation.py Directory_Name