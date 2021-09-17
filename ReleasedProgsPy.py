# ReleasedProgsPy.py
# Sean Bittner
# 5/26/2021
# Scans all Modus CMM programs for specific "test only" text, and if it doesn't exist add the name of...
# this program to "ReleasedPrograms.txt" file that is used for "Lord Of The REVO" automation.
# Docs: *removed*


import os
import datetime

# Constants
DEFINEMASTER = r'C:\Users' # *removed due to proprietary *C:\Users' # *removed due to proprietary *
DEFINERELEASED = r'C:\Users' # *removed due to proprietary *
KEYTEXT = 'TEXT/OPER,\'DO NOT RUN PROGRAM!! OFFLINE ONLY.\''


def checkForKeyText(fileToCheck):
    with open(fileToCheck, 'r') as tempFile:
        fileText = tempFile.read()
        tempFile.close()

        if KEYTEXT in fileText:
            return True
        else:
            return False



def updateList(fileToAdd):
    with open(DEFINERELEASED, 'w') as tempFile:
        tempFile.write(fileToAdd)
        tempFile.close()


def main():
    prog_list = []
    sanity_count = 0
    print("Running: ReleasedProgsPy.py  --->>")
    with os.scandir(DEFINEMASTER) as iterMaster:
        for entryMaster in iterMaster:
            if os.path.isdir(entryMaster):
                pathMaster = os.path.abspath(entryMaster)
                pathMasterFull = pathMaster + '/MASTER'
                if os.path.exists(pathMasterFull):
                    with os.scandir(pathMasterFull) as iterProgram:
                        for entryProgram in iterProgram:
                            pathProgram = os.path.abspath(entryProgram)
                            if os.path.isfile(pathProgram):
                                nameProgram = os.path.basename(pathProgram)
                                if nameProgram.endswith('.dmi') and nameProgram.startswith('#'):
                                    if not (checkForKeyText(pathProgram)):
                                        prog_list.append(nameProgram)
                                        sanity_count += 1
                                        #print('Released ' + str(sanity_count) + ' : ' + nameProgram)

    print("\nFinishing...")
    with open(DEFINERELEASED, 'w') as tempFile:
        for line in prog_list:
            tempFile.write('%s\n' % line)

        current_time = datetime.datetime.now()
        tempFile.write('\n')
        tempFile.write('Updated ' + str(sanity_count) + ' files :: ' + str(current_time))
        tempFile.close()


if __name__ == '__main__':
    main()