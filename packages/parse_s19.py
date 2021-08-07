from packages.types import error_t, pflash_sector_t
from packages.pflash_sectors import pf0_sectors, pf1_sectors, pf2_sectors
from packages.helpers import get_data


#TODO verify checksum
def strip_s19(filename):
    """
    string the leading data, newline, carriage return, and checksum from the s19 file lines
    return a list of the stripped lines
    """

    #read in all lines from the s19 file
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    stripped_lines = []
    #strip s19 and checksum from lines
    for line in lines:
        print(line)
        line = line[4:-3]
        line = line.strip('\r')
        line = line.strip('\n')

        if len(line) > 0:
            stripped_lines.append(line)
    
    #sort by address
    stripped_lines.sort()
    
    return stripped_lines



def parse_s19_line(line):
    """
    parses an s19 line that was stripped by the strip_s19() function
    the line data and address are parsed into the appropriate pflash sector obejct
    """

    #return dictionary object
    ret_data = dict()

    #parse s19 line into a base address and data string
    addr = int('0x'+line[0:8], 16) 
    data = line[8:]

    #convert cached addresses (0x80000000) to non cached equivalent (0xA0000000)
    #0x8 bitwise OR with 0x2 = 0xA
    addr = addr | int('0x20000000', 16)
    

    #parse data into byte list
    data_list = get_data(data)

    q = int(len(data_list) / 4)  #quotient
    r = len(data_list) % 4  #remainder   

    #create address objects for each address
    for i in range(0, q):

        #assign 4 bytes to the address object
        addr_data = []
        for j in range(0,4):
            addr_data.append(data_list.pop(0))

        #add the data to the return dictionary object
        ret_data[addr] = addr_data
       
        #post increment the address 
        addr = addr + 4


    #create address object for remaining bytes
    if r > 0:

        addr_data = []
        for i in range(0, r):
            addr_data.append(data_list.pop(0))

        ret_data[addr] = addr_data

    return ret_data



def parse_s19(filename):
    """
    takes the filepath of an s19 file as an argument
    parses the s19 file into pflash sector objects for flashing
    """

    #strip unneeded data from the s19 lines 
    lines = strip_s19(filename)

    #iterate through each s19 line that was in the file
    for line in lines:
        print(line)
        #parse the s19 line into address objects
        #each address object has an address and 4 bytes associated with that address
        parsed_data = parse_s19_line(line)
 
        #for each address object
        for entry in parsed_data:
            print(line)
            addr = entry
            data = parsed_data[entry]

            #this is a brute force approach, I have not run into any speed problems yet
            #TODO find a more optimized approach
            
            #iterate through all pflash sectors and find which sector the address belongs to
            for sector in pf0_sectors:
                #if the address is the the sector range then add the data to that sector
                if sector.start_addr <= addr and addr <= sector.end_addr:
                    offset = addr - sector.start_addr
                    sector.image[offset] = data
                    break
                     
            for sector in pf1_sectors:
                if sector.start_addr <= addr and addr <= sector.end_addr:
                    offset = addr - sector.start_addr
                    sector.image[offset] = data
                    break            

            for sector in pf2_sectors:
                if sector.start_addr <= addr and addr <= sector.end_addr:
                    offset = addr - sector.start_addr
                    sector.image[offset] = data
                    break
                    










