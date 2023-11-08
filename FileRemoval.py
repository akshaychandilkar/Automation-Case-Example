from sys import *
import os
import hashlib
import time

def DeleteFiles(dict1):
    result = list(filter(lambda x: len(x) > 1, dict1.values()))

    icent = 0;
    if len(result) > 0:
        for result in result:
            for subresult in result:
                icent+=1
                if icent >=2:
                    os.remove(subresult)
            icent = 0
    else:
        print("NO duplicate files found.")

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is :"+dirName)
            for filen in fileList:
                path = os .path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups 
    else:
        print("Invalid Path")

def printResult(dict1):
    result = list(filter(lambda x: len(x) > 1,dict1.values()))

    if len(result) > 0:
        print('Duplicate Found:')
        print('The following files are duplicate')
        for result in result:
            for subresult in result:
                print('\t\t%s' % subresult)

    else: 
        print("No duplicate files found.")

def main():
    print("----Marvellous Infosystems bu piyush Khairnar----")

    print("Application name: "+argv[0])

    if (len(argv) !=2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific dirctory and delete duplicate files")
        exit()

    if(argv[1] == "-u") or (argv[1]) == "-U":
        print("Usage : ApplicationName AbsolutePath_of_Dirctory Extention")
        exit()

    try:
        arr = {}
        starttime = time.time()
        arr = findDup(argv[1])
        printResult(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.'% (endTime - starttime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid Input",E)
        
if __name__ == "__main__":
    main()