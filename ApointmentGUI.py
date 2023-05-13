#Main Program for creating apointments with a unique ID
#you are the patient/receptionist

import tkinter as tk
import logging 
import uuid
import re
import logging
import uuid 
import re
import random as r


#Fields for GUI

Field1 = "First Name"

Field2 = "Last Name"

Field3 = "Check-In Date: mm-dd"

Field4 = "Checkout Date: mm-dd"

Field5 = "Check-In Time :2:31pm"

Field6 = "Checkout Time :2:31pm"

Field7 =  "Room Number"

Field8 =  "Credit Card Infromation"

Field9 = "Look Up Info. Type UID here"


#Create Unique UUID, create log file with unique id and field information
UID = re.sub('\D', '', str(uuid.uuid4())[0:5])
logging.basicConfig(filename=UID+'.log', filemode='w',level = logging.DEBUG, format='%(message)s')
fields = [Field1, Field2, Field3, Field4, Field5, Field6, Field7, Field8, Field9]

#Getting entries for fields 
def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        print('%s: "%s"' % (field, text)) 
        logging.info('%s: "%s"' % (field, text))

#Populating the fields for the GUI

def makeform(root, fields):
    entries = []
    Data = []
    print(entries)
    TestEnt = tk.Label(root, text= "Unique ID : " + UID)
    TestEnt.pack()
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=25, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
        Data.append((ent))
    return entries

def login(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        if(field == Field9):
            if(text == ""):
                print("Didnt Login")
            else:
                IDD = re.sub('\D', '', str(uuid.uuid4())[0:5])
                logging.basicConfig(filename=IDD+'.log', filemode='w',level = logging.DEBUG, format='%(message)s')
                balls = text
                with open(balls + ".log") as f:
                    for line in f:
                        print(line)

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b1 = tk.Button(root, text='Save',
    command=(lambda e=ents: fetch(e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    b3 = tk.Button(root, text='Login',
    command=(lambda e=ents: login(e)))
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

