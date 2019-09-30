import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#hostname = input("Enter host IP address: ")
#username = input("Enter SSH Username: ")
#password = input("Enter SSH Password: ")

hostname = "172.16.0.2"
username = "nayan"
password = "nayan"
port = 22

ssh.connect(hostname, port, username, password, look_for_keys=False, allow_agent=False)
cmd = input("enter command: ")
#cmd = "show run"
#stdin,stdout,stderr = ssh.exec_command(cmd)
stdin,stdout,stderr = ssh.exec_command(cmd)
output = stdout.readlines()

#print ('\n'.join(output))
#with open(path, mode='wt', encoding='utf-8') as myfile:

path = 'E:\\Programming-test\\Python-cmd-app\\PythonApplication1\\router.txt'
openfile = open(path,'w')
openfile.write('\n'.join(output))
openfile.close()

#openread = open(path,'r')
#file = openread.read()
#print (file)

with open(path) as file:
    line = file.readline()
    while line:
        print (line.strip())
        line = file.readline()
    #cnt=1
    #while line:
    #    print ("Line {}: {}".format(cnt, line.strip()))
    #    line = file.readline()
    #    cnt += 1

#openread.close()

