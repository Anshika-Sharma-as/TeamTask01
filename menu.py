import os


def aws():
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
