import subprocess
import os
import datetime
import time
start_time = time.time()
with open('module-list') as fp:
   line = fp.readline()
   while line:
       data=line.strip()
       cmd = 'ansible-doc '+data+'>/root/ansible-documents/modules/modules-notes/'+'ansible_doc_'+data+'.txt'
       #os.system(cmd)
       line = fp.readline()
print("--- %s seconds ---" % (time.time() - start_time))
