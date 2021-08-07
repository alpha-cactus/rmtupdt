import can
import sys
from tkinter import filedialog
from packages.ccp_commands import ccp_connect, ccp_set_mta, ccp_dnload, ccp_flash, ccp_disconnect
from packages.types import error_t, ccp_t, pflash_sector_t
from packages.pflash_sectors import pf0_sectors, pf1_sectors, pf2_sectors
from packages.parse_s19 import parse_s19
from packages.helpers import get_file_path, display_menu
from packages.draw import redraw
from packages.flash import flash
from packages.read import read

#the status varaible is a singleton object that reflects the program status
from packages.status import stat


#TODO make bus global
def main_loop():

    bus = None

    #infinite loop
    while True: 
        display_menu()
              
        user_input = input('> ') 

        #TODO add more connection functionality(user input)
        if user_input == '0':
            bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=500000)
            ccp_connect(bus)
            stat.bus = bus
            
            redraw()
            if bus != None:
                print('CONNECT SUCCESSFUL')
            else:
                print('CONNECT UNSUCCESSFUL')
 
        if user_input == '1':
            #open file dialog to prompt use for file 
            file_path = get_file_path()    
            redraw()
            print('PARSING: ', file_path.upper())    
    
            #parse the file into the virtual controller image
            parse_s19(file_path)
            redraw()            
            print('PARSE COMPLETE')

        elif user_input == '2':
            flash(bus, pf0_sectors)
            flash(bus, pf1_sectors)
            flash(bus, pf2_sectors)
            redraw()

        elif user_input == '3':
            read(bus, pf0_sectors)
            read(bus, pf1_sectors)
            read(bus, pf2_sectors)
            redraw()

        elif user_input == '4':
            output_virtual_image(pf0_sectors)
            output_virtual_image(pf1_sectors)
            output_virtual_image(pf2_sectors)
            redraw()
 
        elif user_input == '5':            
            if bus != None:
                ccp_disconnect(bus) 
            break
    
        else:
            redraw()
            print('INVALID COMMAND: ', user_input.upper())

    return
    

 
if __name__ == '__main__':
    main_loop()

















