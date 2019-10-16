from flask import Flask
import jinja2
from flask import Flask, request, render_template
import base64 
import paramiko 
#print(bios)
        #Credential
username = 'root' 
passwd = 'admin' 
    #key = paramiko.RSAKey(data=base64.b64decode(b'AAA...')) 

def ssh_node(host,cmd,scripts):
    host= host
    cmd = cmd
    scripts =  scripts
    data = []
    val = [cmd,scripts]
    for i in val:
        try:         
            client.connect(host, username= username, password= passwd)
            stdin, stdout, stderr = client.exec_command(cmd)
            ern = stderr.read()
            for line in stdout:             
                line = line.strip()
                data.append(line.replace('\n',''))
                client.close()
            
        except Exception as e:         
            print(e)
    return data,ern    

        