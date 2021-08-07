from packages.ccp_commands import ccp_set_mta, ccp_upload
from packages.status import stat
from packages.draw import redraw

def read(bus, pfN_sectors):

    for sector in pfN_sectors:
        
        for offset in sector.image:
            read_addr = sector.start_addr + offset

            ccp_set_mta(bus, read_addr)

            ccp_upload(bus, 4)
    
            data = []
            for i in range(3,7):
                data.append(stat.last_recv_msg.data[i])
            
            sector.image[offset] = data

