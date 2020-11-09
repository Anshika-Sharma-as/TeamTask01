import os

TGREEN = '\033[32m'
TWHITE = '\033[37m'
TYELLOW = '\033[33m'
TBLUE = '\033[34m'
TRED = '\033[31m'
status = 1


def aboutSystem():
    print(TGREEN, '\t \t Welcome to the System Info ')
    while (True):
        if status == 1:
            print(''' \t List of option to get information about the System :- 
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
                       - Exit the program : {} press 0  
            '''.format(TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW, TGREEN, TYELLOW))
            choice = int(input('Enter your choice, how may i help you : '))
            if choice == 0:
                print(TYELLOW, 'Exiting the program .....')
                break
            else:
                if choice == 1:
                    print('Showing the date.....')

                elif choice == 2:
                    print('showing the calender of this month .....')

                elif choice == 3:
                    print('Showing the calender of some specific month/year .....')

                elif choice == 4:
                    print('Showing the IP configurations .....')

                elif choice == 5:
                    print('Showing the commands  help  .....')

                elif choice == 6:
                    print('Showing the list of files .....')

                elif choice == 7:
                    print('Showing the firewall status .....')

                elif choice == 8:
                    print('Showing availabe/unavailable softwares .....')

                elif choice == 9:
                    print('Showing the java version .....')

                elif choice == 10:
                    print('Showing the actual software name .....')

                else:
                    print('Choose a valid option !!!')
                    continue
            cont = input(
                'Do you wants to continue with the System informatons ?[y/n] : ')
            if (cont == 'y') or (cont == 'Y'):
                continue
            else:
                break


def manageMultipleProgram():
    while (True):
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

            else:
                print(TYELLOW, 'Choose a valid option !!!', TWHITE)
                continue

        print(TBLUE, '\n ')
        cont = input(
            'Do you wants to continue with the User Manager ?[y/n] : ')
        if (cont == 'y') or (cont == 'Y'):
            continue
        else:
            break


def docker():
    while (True):
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
                os.system('docker exec -dit {} /usr/sbin/httpd'.format(name))
                os.system('docker exec -dit {} mkdir /dockerRepo'.format(name))
                os.system('docker exec -dit {} yum install git -y'.format(name))
                os.system(
                    'docker exec -dit {} git clone https://github.com/Anshika-Sharma-as/docker-repo.git /dockerRepo'.format(name))
                os.system(
                    'docker exec -dit {} cp /dockerRepo/web.html /var/www/html'.format(name))
                print('Access your web page on below IP : ')
                os.system('docker exec -dit {} ifconfig'.format(name))
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
