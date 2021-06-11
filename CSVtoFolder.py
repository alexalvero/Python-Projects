# PURPOSE: Get CSV File and make folders for each row(DEXCOM)

# CREATED : 03-JUNE-2021
# LAST EDIT : 04-JUNE-2021
# AUTHORS : ALEXANDER ALVERO III (alveroalexander@gmail.com)

import os
from datetime import date

fullpath = os.getcwd()
date = str(date.today())
folderpath = str(f"{fullpath}\{date}")

def getFilename():
    filename = input('Filename: ')

    while True:
        try:
            str(filename)
            return(filename)
        except ValueError:
            print('Import Valid Filename:')

def todaymkFolder(date):
    try:
        os.mkdir(folderpath)   
    except FileExistsError:
        print("Folder already exist!")

    
def mkFolder(filename,folderpath):   
    try:
        with open(filename) as infile:
            for line in infile:
                y = line.replace("\n", "")
                x = y.replace(",", " ")
                try:
                    x = os.mkdir(os.path.join(folderpath, x.strip()))
                except FileExistsError:
                    print(f'{x} already exists!')
    except FileNotFoundError:
        print(f'{filename} does not exists!')
        



def main():
    filename = getFilename()
    todaymkFolder(date)
    mkFolder(filename,folderpath)
    

        

if __name__ == '__main__':
    main()
