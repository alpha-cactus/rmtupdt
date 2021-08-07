
#controller pflash sector object used for creating a virtual image of the controller
class pflash_sector_t():

    def __init__(self, start_addr, end_addr, size):
        #pflash sector start address
        self.start_addr = int(start_addr, 16) 

        #pflash sector end address
        self.end_addr = int(end_addr, 16)

        #size of the pflash sector used for flash and erase ccp commands
        self.size = size

        #pflash sector data to be flashed
        self.image = dict()

        self.init_image()


    def init_image(self):
        working_addr = self.start_addr
    
        while working_addr < self.end_addr:
            offset = working_addr - self.start_addr
            
            data = [0x0, 0x0, 0x0, 0x0]
            
            self.image[offset] = data            
    
            working_addr = working_addr + 0x4

        


class error_t():
    E_OK = 0
    E_FAILED_SEND = 1
    E_BAD_RETURN_CODE = 2
    E_BUS_TIMEOUT = 3

    def to_string(err):
        if err == 0:
            return 'E_OK'
        elif err == 1:
            return 'E_FAILED_SEND'
        elif err == 2:
            return 'E_BAD_RETURN_CODE'
        elif err == 3:
            return 'E_BUS_TIMEOUT'


class ccp_t():
    CONNECT = 0x01
    SET_MTA = 0x02
    DNLOAD = 0x03
    UPLOAD = 0x04
    DISCONNECT = 0x07
    FLASH = 0x18
    
