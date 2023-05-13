#Program to read log files based on uuid
#TESTFILE Currently also creates its own UUID for debug purposes. 

import logging
import uuid 
import re
import random as r

IDD = re.sub('\D', '', str(uuid.uuid4())[0:5])
logging.basicConfig(filename=IDD+'.log', filemode='w',level = logging.DEBUG, format='%(message)s')
balls = input("Type your uniqe ID : ")
with open(balls + ".log") as f:
    for line in f:
        print(line)