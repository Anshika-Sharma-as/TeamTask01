import os

TGREEN = '\033[32m'
TWHITE = '\033[37m'
TYELLOW = '\033[33m'
TBLUE = '\033[34m'
TRED = '\033[31m'
TCYAN = '\033[36m'

print(TGREEN, '\t \t Welcome to the command assistant ')
status = 1


def aboutSystem():
    os.system('clear')
    print(TGREEN, '\t \t Welcome to the System Info ')
    while (True):
        if status == 1:
            print(TGREEN, ''' \t List of option to get information about the System :-
                       - Show the date : {} press 1 {}
                       - show the calender of this month : {} press 2 {}
                       - Show the calender of some specific month/year : {} press 3 {}
                       - Show the IP configurations : {} press 4 {}
                       - Show the Commands help : {} press 5 {}
                       - Show the list of files : {} press 6 {}
                       - Show the firewall status : {} press 7 {}
                       - Show availabe/unavailable softwares : {} press 8 {}
                       - Show the java version : {} press 9 {}
                       - Show the actual software name : {} press 10 {}
                       - Show the CPU information : {} press 11 {}
                       - Exit the program : {} press 0
            '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
            choice = int(input('Enter your choice, how may i help you : '))
            if choice == 0:
                print(TYELLOW, 'Exiting the program .....')
                break
            else:
                if choice == 1:
                    print(TYELLOW, 'Showing the date.....', TWHITE)
                    os.system('date')

                elif choice == 2:
                    print(TYELLOW, 'showing the calender of this month .....', TWHITE)
                    os.system('cal')

                elif choice == 3:
                    print(
                        TYELLOW, 'Showing the calender of some specific month/year .....', TWHITE)
                    month = int(input('enter the month : '))
                    year = int(input('enter the year : '))
                    os.system('cal {} {} '.format(month, year))

                elif choice == 4:
                    print(TYELLOW, 'Showing the IP configurations .....', TWHITE)
                    os.system('ifconfig')

                elif choice == 5:
                    print(TYELLOW, 'Showing the commands  help  .....', TWHITE)
                    os.system('help')

                elif choice == 6:
                    print(TYELLOW, 'Showing the list of files .....', TWHITE)
                    os.system('ls ')

                elif choice == 7:
                    print(TYELLOW, 'Showing the firewall status .....', TWHITE)
                    os.system('systemctl status firewalld ')

                elif choice == 8:
                    print(
                        TYELLOW, 'Showing availabe/unavailable softwares .....', TWHITE)
                    softname = input(
                        'enter the name of software to check its availability : ')
                    os.system('rpm -q {}'.format(softname))

                elif choice == 9:
                    print(TYELLOW, 'Showing the java version .....', TWHITE)
                    os.system('java -version')

                elif choice == 10:
                    print(TYELLOW, 'Showing the actual software name .....', TWHITE)
                    softname = input(
                        'enter the value to fetch actual software name : ')
                    os.system('which  {} '.format(softname))

                elif choice == 11:
                    print(TYELLOW, 'Showing the CPU information .....', TWHITE)
                    os.system('lscpu ')

                else:
                    print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                    continue

            print(TBLUE, '\n ')
            cont = input(
                'Do you wants to continue with the System informatons ?[y/n] : ')
            if (cont == 'y') or (cont == 'Y'):
                continue
            else:
                break


def manageMultipleProgram():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to Multi Task Manager \n \n  ', TWHITE)
        pgname = input('Enter the program name to be executed :  ')
        os.system('{} & '.format(pgname))

        print(TBLUE, '\n')
        cont = input(
            'Do you wants to execute more programs ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def cacheManager():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to the cache Manager \n  ')
        print('''  \t List of operations that can be performed on the Cache memory :-
                    - Show the cache status : {} press 1 {}
                    - Remove the cache memory : {} press 2 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        choice = int(
            input('Enter your choice, how may i help you in cache Management : '))
        if choice == 0:
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if choice == 1:
                print(TYELLOW, 'Showing the cache memory status ..... ', TWHITE)
                os.system('free -m ')

            elif choice == 2:
                print(TYELLOW, 'Removing cache memory ..... ', TWHITE)
                os.system('echo  3 > /proc/sys/vm/drop_caches')

            else:
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the System informatons ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def binaryCalulator():
    os.system('clear')
    print(TYELLOW, 'Once the mathematical calculation is done, enter "quit" to come out of it !!', TWHITE)
    while (True):
        os.system('bc')
        print(TGREEN, '\n \n ')
        cont = input('Do you wants to use Binary Calculator again ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def fileManager():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to the file Manager \n  ')
        print('''  \t List of operations that can be performed with file Manager  :-
                    - Show a file's content : {} press 1 {}
                    - Create a new file : {} press 2 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        choice = int(
            input('Enter your choice, how may i help you in file Management : '))
        if choice == 0:
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if choice == 1:
                print(TYELLOW, 'Showing the File Conetent ..... ', TWHITE)
                fileName = input(
                    'Enter the file name (with extension like abc.py, ab.txt ) : ')
                os.system('cat {}'.format(fileName))

            elif choice == 2:
                print(TYELLOW, 'Opening file editor ..... ', TWHITE)
                fileName = input(
                    'Enter the file name (with extension like abc.py, ab.txt ) : ')
                print(
                    TYELLOW, 'After writing your data to the file, Press Esc key then type :wq  then press Enter !!', TWHITE)
                os.system('vi  {}'.format(fileName))

            else:
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the File Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def connectionChecker():
    os.system('clear')
    print(TGREEN, '\t \t Welcome to connection checker ', TWHITE)
    while(True):
        ip = input('Enter the IP where you wants to check the connection : ')
        os.system('ping -c 3 {}'.format(ip))
        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the connection checker ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def processManager():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to the Process Manager \n  ')
        print('''  \t List of operations that can be performed with Process Manager :-
                    - Show the Stopped background processes : {} press 1 {}
                    - Show the running processes : {} press 2 {}
                    - Kill any running process : {} press 3 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        choice = int(
            input('Enter your choice, how may i help you in Process Management : '))
        if choice == 0:
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if choice == 1:
                print(
                    TYELLOW, 'Showing the Stopped background processes  ..... ', TWHITE)
                os.system('jobs ')

            elif choice == 2:
                print(TYELLOW, 'Showing the running processes ..... ', TWHITE)
                os.system('ps -aux ')

            elif choice == 3:
                print(TYELLOW, 'Kill any running process ..... ')
                print('Showing list of running processes :- ', TWHITE)
                os.system('ps -aux ')
                id = int(
                    input('Enter the ID of the process that you wants to kill : '))
                os.system('kill {}'.format(id))
                print(TYELLOW, 'Killed the process with PID {} '.format(id), TWHITE)

            else:
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the Process Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def userManager():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to the User Manager \n  ')
        print('''  \t List of operations that can be performed with User Manager :-
                    - Show the available users : {} press 1 {}
                    - Add a new user : {} press 2 {}
                    - Switch to any user : {} press 3 {}
                    - Exit the cache manager : {} press 0
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        choice = int(
            input('Enter your choice, how may i help you in User Management : '))
        if choice == 0:
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if choice == 1:
                print(
                    TYELLOW, 'Showing the available users  ..... ', TWHITE)
                os.system('cat /etc/passwd ')

            elif choice == 2:
                print(TYELLOW, 'Adding a new user ..... ', TWHITE)
                name = input('Enter the name for new user : ')
                os.system('useradd {} '.format(name))

            elif choice == 3:
                print(TYELLOW, 'Switch to any user ..... ')
                name = input(
                    'Enter the name of the user to switch the account : ')
                os.system('su - {} '.format(name))


def aws():
    os.system('clear')
    name = input("how do i what to call you!:")
    os.system("clear")
    print("hello \'"+name+"\' \nhow can i help!")
    print()
    print("\t\t\tThis is the menu!\n")
    print("select the following options "+name+"! :\n")
    print("1>AWS instance launch.")
    choose = int(input("\nwhich one you what?:"))

    if choose == 1:
        print(name+" may i know your credentials so that i can acess your account for this time!")
        s = input("if its ok to you! please enter[y/n]:")
        if s == "y":
            os.system("aws configure")
            print(name+" it's better to create a key pair now,it is useful for ssh")
            keyname = input("enter the keypair name:")
            keycreate = "aws ec2 create-key-pair --key-name --query ""KeyMaterial " + \
                keyname+" --output text > "+keyname+".pem"
            os.system(keycreate)
            print("\n..key hasbeen created and stored in the current working directory..")
            private = "chmod 400 "+keyname+".pem"
            os.system(private)
            enterkey = input(
                "\nEnter the key-pair-name with which you are having:")
            createsys = "aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --key-name "+enterkey
            os.system(createsys)
            os.system("clear")
            print(name+" successfully instance created...")
        elif s == "n":
            print("terminated")
    else:
        print("no")
    print("its done plz check in ur aws site")


def hadoop():
    os.system('clear')
    print("1>config name node.\n2>config data node.\n3>ssh to the aws instance.\n")

    s = input("select a option:")
    choice = int(s)

    if choice == 1:
        ipm = input("enter the ipaddress of the name-node:")
        key = input(
            "enter the key associated to the instance, include extension(.pem):")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        trs = "scp -i "+key
        dirname = input("enter a diretory name for the name-node:")
        h = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/" + \
            dirname+"</value>\n</property>\n</configuration>"
        c = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>\n</configuration>"
        f = open("hdfs-site.xml", "w")
        f.write(h)
        f.close()
        ff = open("core-site.xml", "w")
        ff.write(c)
        ff.close()
        os.system(trs+" hdfs-site.xml ec2-user@"+ipm+":/home/ec2-user/hdfs-site.xml ;" +
                  trs+" core-site.xml ec2-user@"+ipm+":/home/ec2-user/core-site.xml")
        os.system(ssh+" sudo mv hdfs-site.xml /etc/hadoop/ ;" +
                  ssh+" sudo mv core-site.xml /etc/hadoop/")
        os.system("rm -f hdfs-site.xml core-site.xml")
        os.system("clear")
        print("..the name node at the ip \""+ipm+"\" configured successfully!")
        os.system(ssh+" hadoop namenode -format")
        os.system(ssh+" hadoop-daemon.sh start namenode")
        os.system("clear")
        print("..the name-node started")
    elif choice == 2:
        ipm = input("enter the ipaddress of the name-node:")
        key = input(
            "enter the key associated to the instance, include extension(.pem):")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        trs = "scp -i "+key
        dirname = input("enter a diretory name for the data-node:")
        h = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/" + \
            dirname+"</value>\n</property>\n</configuration>"
        c = "<?xml versio=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" herf=\"configuration.xsl\"?>\n<!--put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://" + \
            ipm+":9001</value>\n</property>\n</configuration>"
        f = open("hdfs-site.xml", "w")
        f.write(h)
        f.close()
        ff = open("core-site.xml", "w")
        ff.write(c)
        ff.close()
        os.system(trs+" hdfs-site.xml ec2-user@"+ipm+":/home/ec2-user/hdfs-site.xml ;" +
                  trs+" core-site.xml ec2-user@"+ipm+":/home/ec2-user/core-site.xml")
        os.system(ssh+" sudo mv hdfs-site.xml /etc/hadoop/ ;" +
                  ssh+" sudo mv core-site.xml /etc/hadoop/")
        os.system("rm -f hdfs-site.xml core-site.xml")
        os.system("clear")
        print("..the data node at the ip \""+ipm+"\" configured successfully!")
        os.system(ssh+" hadoop-daemon.sh start datanode")
        os.system("clear")
        print("..the datanode started")
    elif choice == 5:
        ipm = input("enter the ipaddress of the instance:")
        key = input(
            "enter the key associated to the instance, include extension(.pem):")
        os.system("clear")
        ssh = "ssh -i "+key+" ec2-user@"+ipm
        os.system(ssh)

    print("......Thank you.......")


def createPV(diskName):
    print(TYELLOW, 'Creating Physical volume')
    print(TBLUE)
    # diskName = input('enter the disk name that you wants to create physical volume(pv): ')
    os.system('pvcreate  {}'.format(diskName))


def createVG(diskName, d1, d2):
    print(TYELLOW, 'Creating Volume Group ')
    print(TBLUE)
    # diskName = input('enter the name that you wants to create volume group(vg): ')
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
    print(TYELLOW, 'Displaying the physical volume {} '.format(pvName))
    print(TWHITE)
    os.system('pvdisplay  {}'.format(pvName))


def displayVG(vgName):
    print(TYELLOW, 'Displaying the volume group {} '.format(vgName))
    print(TWHITE)
    os.system('vgdisplay  {}'.format(vgName))


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
        os.system('clear')
        print(TGREEN, "\t \t \t Welcome to the LVM Task ")
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


def docker():
    while (True):
        os.system('clear')
        print(TGREEN, '\t \t Welcome to the Docker Manager \n  ')
        print('''  \t List of operations that can be performed with Docker Manager :- 
                    - Install Docker : {} press 1 {}
                    - Show the list of docker images : {} press 2 {}
                    - Pull a docker image : {} press 3 {}
                    - Create a docker container : {} press 4 {}
                    - Start a docker : {} press 5 {}
                    - Go inside a docker : {} press 6 {}
                    - Setup webServer over docker : {} press 7 {}  
                    - check the docker status : {} press 8 {}        
                    - Exit the cache manager : {} press 0        
        '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
        choice = int(
            input('Enter your choice, how may i help you in Process Management : '))
        if choice == 0:
            print(TYELLOW, 'Exiting the program ..... ')
            break
        else:
            if choice == 1:
                print(TYELLOW, 'Installing  Docker  ..... ', TWHITE)
                os.system('yum install git -y')
                os.system('mkdir /dockerRepo')
                os.system(
                    'git clone https://github.com/Anshika-Sharma-as/docker-repo.git /dockerRepo')
                os.system(
                    'cp /dockerRepo/docker.repo  /etc/yum.repos.d/docker.repo ')
                os.system('rm -f /dockerRepo')
                os.system('yum install docker-ce --nobest -y')
                os.system('systemctl start docker')

            elif choice == 2:
                print(TYELLOW, 'Showing the list of docker images ..... ', TWHITE)
                os.system('docker images ')

            elif choice == 3:
                print(TYELLOW, 'Pulling a docker image ..... ', TWHITE)
                imageName = input('Enter the name of docker image : ')
                os.system('docker pull {} '.format(imageName))

            elif choice == 4:
                print(TYELLOW, 'Creating a docker container ..... ', TWHITE)
                name = input('Enter the name for docker container : ')
                imageName = input('Enter the name of docker image : ')
                os.system(
                    'docker run -dit --name {}  {}'.format(name, imageName))
                os.system('docker ps -a')

            elif choice == 5:
                print(TYELLOW, 'Starting a docker  ..... ', TWHITE)
                name = input('Enter the name of Container to be started : ')
                os.system('docker start {} '.format(name))
                os.system('docker ps ')

            elif choice == 6:
                print(TYELLOW, 'Going inside a docker ..... ', TWHITE)
                name = input('Enter the name of Container to be started : ')
                os.system('docker exec -it {} /bin/bash '.format(name))

            elif choice == 7:
                print(TYELLOW, 'Setup webServer over docker ..... ', TWHITE)
                name = input(
                    'Enter the name of Container to perform operations : ')
                os.system('docker start {}'.format(name))
                os.system(
                    'docker exec -dit {} yum install httpd -y'.format(name))
                os.system('docker exec -dit {} /usr/sbin/httpd '.format(name))
                os.system('docker exec -dit {} mkdir /dockerRepo'.format(name))
                os.system('docker exec -dit {} yum install git -y'.format(name))
                os.system(
                    'docker exec -dit {} git clone https://github.com/Anshika-Sharma-as/docker-repo.git /dockerRepo'.format(name))
                os.system(
                    'docker exec -dit {} cp /dockerRepo/web.html /var/www/html'.format(name))
                os.system('docker exec -dit {} rm -rf /dockerRepo'.format(name))
                print('Access your web page on below IP : ')
                os.system(
                    'docker exec -dit {} yum install net-tools -y'.format(name))
                os.system('docker exec -dit {} ifconfig '.format(name))
                print('http://IP_Address/web.html')
                ip = input('Enter the IP to access the webserver : ')
                os.system('http://{}/web.html'.format(ip))

            elif choice == 8:
                print(TYELLOW, 'Checking the docker status ..... ', TWHITE)
                os.system('systemctl status docker ')

            else:
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the Docker Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def mainMenu():
    while(True):
        if status == 1:
            os.system('clear')
            print(TGREEN, ''' List of every operation, choose anyone to process:-
                -  About my system : {} press 1 {}
                -  Manage my AWS Cloud remotely : {} press 2 {}
                -  Setup and Manage Hadoop Cluster : {} press 3 {}
                -  Manage multiple programs at single time : {} press 4 {}
                -  Managing users in the system : {} press 5 {}
                -  Use File Manager Program : {} press 6 {}
                -  Check connections with other systems : {} press 7 {}
                -  Use Binary Calculator : {} press 8 {}
                -  Managing Cache memory : {} press 9 {}
                -  Manage background processes : {} press 10 {}
                -  Manage Containers through Docker : {} press 11 {}
                -  Managing storage :{} press 12 {}
                -  Exit the program : {} press 0 

            '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
            choice = int(input('Enter your choice, how may I help you : '))
            if choice == 0:
                print(TYELLOW, 'Exiting the program .....')
                break
            else:
                if choice == 1:
                    print('Opening about the system .....')
                    aboutSystem()

                elif choice == 2:
                    print('managing AWS cloud .....')
                    aws()

                elif choice == 3:
                    print('Opening Hadoop Manager .....')
                    hadoop()

                elif choice == 4:
                    print('Opening Multi program setup .....')
                    manageMultipleProgram()

                elif choice == 5:
                    print('Opening user management program  .....')
                    userManager()

                elif choice == 6:
                    print('Opening file manager program .....')
                    fileManager()

                elif choice == 7:
                    print('Opening connection checker .....')
                    connectionChecker()

                elif choice == 8:
                    print('Opening Binary calculator .....')
                    binaryCalulator()

                elif choice == 9:
                    print('Opening cache Manager .....')
                    cacheManager()

                elif choice == 10:
                    print('Opening Background process Manager .....')
                    processManager()

                elif choice == 11:
                    print('Opening Docker Manager .....')
                    docker()

                elif choice == 12:
                    print('Opening Storage Manager .....')
                    lvmManager()

                else:
                    print('Choose a valid option !!!')
                    continue

            print(TGREEN, '\n \n ')
            cont = input(
                'Do you wants to continue with the Command Assistant ?[y/n] : ')
            if (cont == 'y') or (cont == 'Y'):
                continue
            else:
                break


mainMenu()
print(TGREEN, '\t \t Execution Done !! ', TWHITE)
