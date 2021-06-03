# PURPOSE: Get CSV File and make folders for each row

# CREATED : 03-JUNE-2021
# LAST EDIT : 
# AUTHORS : ALEXANDER ALVERO III (alveroalexander@gmail.com)

import os
import csv

path = os.getcwd()
def getFilename():
    filename = input('Filename: ')

    while True:
        try:
            str(filename)
            return(filename)
        except ValueError:
            print('Import Valid Filename:')
    
def mkFolder(filename):   
    try:
        with open(filename) as infile:
            for line in infile:
                y = line.replace("\n", "")
                x = y.replace(",", " ")
                try:

                    x = os.mkdir(os.path.join(path, x.strip()))
                except FileExistsError:
                    print(f'{x} already exists!')
    except FileNotFoundError:
        print(f'{filename} does not exists!')
        



def main():
    filename = getFilename()
    mkFolder(filename)

        

if __name__ == main():
    main()
