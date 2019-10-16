from flask import Flask
import jinja2
from flask import Flask, request, render_template
import base64 
import paramiko 
       
app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
SERVER_IP='0.0.0.0'
IP_PORT=5000

@app.route("/")

def home():
    return render_template('index.html')

@app.route("/task",methods=['GET','POST'])

def task():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        #connectToRemoteHost.py is used to execute commands on remote host from your local computer using python library.
        host = request.form['hostname'] 
        cmdd = request.form['cmd']
        #print(cmdd)
        bios = request.form['bios']      
        #bios = "/root/scripts/"+bios
        bios = cmdd
        #print(bios)
        #Credential
        username = 'root' 
        passwd = 'admin' 
        #key = paramiko.RSAKey(data=base64.b64decode(b'AAA...')) 
        data = []
        host = host
        try:         
            client = paramiko.SSHClient()         
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())         
            client.load_system_host_keys()         
            client.connect(host, username= username, password= passwd)         
            cmd = cmdd
            stdin, stdout, stderr = client.exec_command(bios)
            ern = stderr.read()
            for line in stdout:             
                line = line.strip()
                data.append(line.replace('\n',''))
                client.close()     
        except Exception as e:         
            print(e)    
        return render_template('index.html',data=data,error=ern)
    else:
        return "Try Again" 

if __name__ == "__main__":
    app.run(debug=True, host=SERVER_IP, port=IP_PORT, threaded=True)
   

