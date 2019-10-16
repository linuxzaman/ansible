import subprocess
import os
import datetime
import time
start_time = time.time()
with open('names.txt') as fp:
   line = fp.readline()
   while line:
       data=line.strip()
       cmd = 'cat /root/ansible-documents/modules/modules-notes/'+data+'|grep -A 1000 EXAMPLES:>'+'/root/ansible-documents/modules/modules-examples/'+data
       os.system(cmd)
       #print(cmd)
       line = fp.readline()
print("--- %s seconds ---" % (time.time() - start_time))
