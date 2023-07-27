import subprocess as sp
import time
import os
import sys

#the environment variable
cptdir = os.getenv('CPTDIR')

#support for runnning multiple instances
fn_procL = ['videos.txt']


mtime_oldL = [0.0 for k in range(len(fn_procL))]

while True:
    for i,fn_proc in enumerate(fn_procL):
        mtime_old = mtime_oldL[i]
        try:#sometimes file is temporary unavailable
            mtime = os.path.getmtime(fn_proc)
        except:
            pass


        if mtime!=mtime_old:
            proc = sp.run(['python3', cptdir+'/makeslides.py', fn_proc, '--strictlocal', '--definitions', 'globaldefs.txt'])
            mtime_oldL[i] = mtime
            print(".", end="")
            sys.stdout.flush()

    time.sleep(1)
