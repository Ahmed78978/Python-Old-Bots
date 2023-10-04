import os
import time

def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
file=2
os.startfile('loginAMAZON - Copy (1).py')
time.sleep(90)
while(1):
  f= "loginAMAZON - Copy (",str(file),") - Copy.py"
  files=convertTuple(f)
  os.startfile(files)
  time.sleep(100)
  if(file>=1508):
  	break
  file=file+1	