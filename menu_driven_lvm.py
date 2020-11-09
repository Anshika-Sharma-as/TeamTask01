import os

TGREEN = '\033[32m'
TWHITE = '\033[37m'
TYELLOW = '\033[33m'
TBLUE = '\033[34m'
TRED = '\033[31m'

print(TGREEN, "\t \t \t Welcome to the LVM Task ")


def createPV(diskName):
    print(TYELLOW, 'Creating Physical volume')
    print(TBLUE)
    #diskName = input('enter the disk name that you wants to create physical volume(pv): ')
    os.system('pvcreate  {}'.format(diskName))


def createVG(diskName, d1, d2):
    print(TYELLOW, 'Creating Volume Group ')
    print(TBLUE)
    #diskName = input('enter the name that you wants to create volume group(vg): ')
    os.system('vgcreate  {} {} {} '.format(diskName, d1, d2))


def displayAllPV():
    print(TYELLOW, 'Displaying all the physical volumes available ')
    print(TWHITE)
    os.system('pvdisplay ')


def displayAllVG():
    print(TYELLOW, 'Displaying all the  volume groups available ')
    print(TWHITE)
    os.system('vgdisplay ')


def displayPV(pvName):
    print(TYELLOW, 'Displaying the physical volume {} '.format(diskName))
    print(TWHITE)
    os.system('pvdisplay  {}'.format(pvName))


def displayVG(vgName):
    print(TYELLOW, 'Displaying the volume group {} '.format(vgName))
    print(TWHITE)
    os.system('vgdisplay  {}'.format(diskName))


def createLV(lvName, vgName, size):
    print(TYELLOW, 'Creating the logical volume ')
    print(TWHITE)
    os.system('lvcreate {} --size {} --name {}'.format(vgName, size, lvName))


def formatt(vgName, lvName):
    print(TYELLOW, 'Formating the logical volume ')
    print(TWHITE)
    os.system('mkfs.ext4 /dev/{}/{} '.format(vgName, lvName))


def extend(size, vgName, lvName):
    print(TYELLOW, 'Extending the logical volume ')
    print(TWHITE)
    os.system('lvextend --size {} /dev/{}/{}'.format(size, vgName, lvName))


def resize(vgName, lvName):
    print(TYELLOW, 'Reformatting the logical volume ')
    print(TWHITE)
    os.system('resize2fs /dev/{}/{}'.format(vgName, lvName))


def displayBlocks():
    print(TYELLOW, 'Showing the blocks available ')
    print(TWHITE)
    os.system('lsblk ')


def mounting(vgName, lvName, direc):
    print(TYELLOW, 'mounting the partition to the given directory ')
    print(TWHITE)
    os.system('mount /dev/{}/{} /{}'.format(vgName, lvName, direc))


def makingDirectory(diskName):
    print(TYELLOW, 'Making a new directory ')
    print(TWHITE)
    os.system('mkdir {} '.format(diskName))


def disks():
    print(TYELLOW, 'Showing available disks ')
    print(TWHITE)
    os.system('fdisk -l')


def lvmManager():
    while (True):
        print(TGREEN)
        print(''' Follow the menu, to perform some task : 
            -> To see the storage devices available : press 1
            -> To create a Physical volume : press 2
            -> To create a Volume group : press 3
            -> To Display the Physical Volumes available : press 4
            -> To display the volume group available : press 5
            -> To display a specific Volume group : press 6
            -> To display a specific Physical volume : press 7
            -> To create a logical volume as per the storage requirements : press 8
            -> To format the logical volume partition : press 9
            -> To extend the space of the logical volume : press 10
            -> To format the unformatted part : press 11
            -> To see the block devices along with their mount point : press 12
            -> To mount the logical volume to some directory, to be used : press 13
            -> To create a directory : press 14
            -> To exit the program : press 0  
        ''')

        print(TBLUE)
        option = int(input('Enter your option here : '))

        if option == 0 or option == ' ':
            print(TYELLOW, 'Exiting from the program ....')
            break

        elif (option > 0 and option < 15):
            print(TYELLOW, 'processing request.....')
            if option == 1:
                disks()

            elif option == 2:
                print(TBLUE)
                diskName = input(
                    'Enter the name of disk that you need to make a physical volume : ')
                createPV(diskName)

            elif option == 3:
                print(TBLUE)
                d1 = input('enter the physical volume to be added : ')
                d2 = input('enter the physical volume to be added : ')
                diskName = input(
                    'Enter the name that you wants to give to your Volume group : ')
                createVG(diskName, d1, d2)

            elif option == 4:
                displayAllPV()

            elif option == 5:
                displayAllVG()

            elif option == 6:
                print(TBLUE)
                vgName = input(
                    'Enter the volume group name that you wants to retrieve  : ')
                displayVG(vgName)

            elif option == 7:
                print(TBLUE)
                pvName = input(
                    'Enter the physical volume name that you wants to retrieve  : ')
                displayPV(pvName)

            elif option == 8:
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                size = input('Enter the size of logical device you want : ')
                lvName = input(
                    'Enter the name of your choice for Logical volume : ')
                createLV(lvName, vgName, size)

            elif option == 9:
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                formatt(vgName, lvName)

            elif option == 10:
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                size = input('Enter the size to be extended : ')
                lvName = input('Enter the Logical volume name : ')
                extend(size, vgName, lvName)

            elif option == 11:
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                resize(vgName, lvName)

            elif option == 12:
                displayBlocks()

            elif option == 13:
                print(TBLUE)
                vgName = input('Enter the volume group name : ')
                lvName = input('Enter the Logical volume name : ')
                direc = input(
                    'Enter the directory name to be linked with this Logical volume :')
                mounting(vgName, lvName, direc)

            elif option == 14:
                print(TBLUE)
                diskName = input(
                    'Enter the name for the directory that you wants to create : ')
                makingDirectory(diskName)

            else:
                print(TRED, 'Enter valid options only !!!')
                continue


print(TYELLOW, 'Execution done!!!!', TWHITE)
