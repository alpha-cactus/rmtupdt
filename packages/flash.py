from packages.ccp_commands import ccp_set_mta, ccp_dnload, ccp_flash
from packages.draw import redraw

def flash(bus, pfN_sectors):

    for sector in pfN_sectors:

        redraw()        
        print('Performing DNLOAD for Sector: %X-%X' %(sector.start_addr, sector.end_addr))        
        
        for offset in sector.image:
            ccp_set_mta(bus, offset)

            ccp_dnload(bus, len(sector.image[offset]), sector.image[offset])
        
        ccp_set_mta(bus, sector.start_addr)
        
        redraw()
        print('Performing FLASH for Sector: %X-%X' %(sector.start_addr, sector.end_addr))        
        ccp_flash(bus, sector.size)


    return
