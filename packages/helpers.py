import can
from packages.types import error_t

import tkinter as tk

def get_file_path(): 
    root = tk.Tk()
    root.withdraw()

    file_path = tk.filedialog.askopenfilename()

    return file_path


def print_image(pfN_sectors):
    f = open('output.txt', 'a')

    for sector in pfN_sectors:
        for data in sector.image:
            val = sector.image[data][0] << 24 | sector.image[data][1] << 16 | sector.image[data][2] << 8 | sector.image[data][3]
            print('0x%X 0x%X' %(data, val))
    
    f.close()
    return        
 

def display_menu():
    print('0: CONNECT TO CONTROLLER')

    print('1: PARSE S19 FILE TO VIRTUAL IMAGE')

    print('2: FLASH VIRTUAL IMAGE TO CONTROLLER')

    print('3: READ CONTROLLER DATA TO VIRTUAL IMAGE')

    print('4: OUTPUT VIRTUAL IMAGE TO TEXT FILE')
    
    print('5: DISCONNECT FROM CONTROLLER AND EXIT')

    return


def get_data(data):
    ret_list = []

    while len(data) > 0:
        b = data[0:2]

        data = data[2:]

        b = int('0x' + b, 16)
        
        ret_list.append(b)

    return ret_list            


def build_msg(msg_data):
    """
    helper function to build a message object
    """
    msg = can.Message(arbitration_id=0x27, data=msg_data, extended_id=False) 

    return msg

