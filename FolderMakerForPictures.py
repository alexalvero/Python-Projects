# PURPOSE: Get CSV File and make folders for Pictures(DEXCOM)

# CREATED : 04-JUNE-2021
# LAST EDIT : 
# AUTHORS : ALEXANDER ALVERO III (alveroalexander@gmail.com)


"""Module Imports"""

try:
    import os
    from datetime import date
except ModuleNotFoundError:
    print("Module import Error!")


mkFolderList = {"009", "010", "045", "046", "047", "048", "076", "077", "109", "112", "118", "121", "2013"}
notMkFolderList = {"012", "013", "020", "021", "022", "023","025", "042", "071", "075", "096", "108", "113", "115", "116"}

"""Variables Declarations"""
fullpath = os.getcwd()
date = str(date.today())
folderpath = str(f"{fullpath}\{date}")
csvItems = []


def getFilename():
    filename = input('Filename: ')

    while True:
        try:
            str(filename)
            return(filename)
        except ValueError:
            print('Import Valid Filename')

def todaymkFolder(date):
    try:
        os.mkdir(folderpath)   
    except FileExistsError:
        print("Folder already exists!")

def mkFolder(filename,folderpath):   
    try:
        with open(filename) as infile:
            for line in infile:
                
                y = line.replace("\n", "")
                x = y.replace(",", " ")
                z = x.split(" ")
                csvItems.append(z)
                # try:
                #     x = os.mkdir(os.path.join(folderpath, x.strip()))
                # except FileExistsError:
                #     print(f'{x} already exists!')
    except FileNotFoundError:
        print(f'{filename} does not exists!')            

def main():
    filename = getFilename()
    todaymkFolder(date)
    mkFolder(filename,folderpath)
    
    for items in csvItems:
        if items[4] in mkFolderList:
            try:      
                os.mkdir(os.path.join(folderpath, items[1]))
            except FileExistsError:
                print("Folder already exists!")


if __name__ == '__main__':
    main()