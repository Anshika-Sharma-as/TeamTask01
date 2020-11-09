import os


def hadoop():
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
