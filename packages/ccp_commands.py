import can
from packages.helpers import build_msg, get_data
from packages.types import error_t, ccp_t
from packages.status import stat
from packages.draw import redraw



#TODO add message count verification	
def recv_msg(bus, arbitration_id=0x26):
    """
    polls bus waiting for reception of message with the specified arbitration id(default 0x26)
    
    returns the received message
    """
    stat.error = error_t.E_OK

    #TODO add timeout
    while True:
        msg = bus.recv(timeout=5.0)
    
        if msg is None:
            stat.error = error_t.E_BUS_TIMEOUT    
            return
 
        if msg.arbitration_id == 0x26:
            stat.last_recv_msg = msg
 
            if msg.data[1] != 0x00:
                stat.error = error_t.E_BAD_RETURN_CODE
        
            return

def send_msg(bus, msg):
    """
    send a single message on the bus
    """
    stat.error = error_t.E_OK
    
    stat.last_sent_msg = msg

    try:
        bus.send(msg)
    except can.CanError:
        stat.error = error_t.E_FAILED_SEND

    return

def ccp_connect(bus):
    """
    builds a ccp connect(ID=0x01) message and sends it on the bus
    """
    stat.error = error_t.E_OK   
 
    msg = build_msg([ccp_t.CONNECT, 0x00, 0xCC, 0xCC, 0x00, 0x00, 0x00, 0x00])

    send_msg(bus, msg)

    recv_msg(bus)
    return



def ccp_set_mta(bus, addr):
    """
    builds a ccp set mta(ID=0x02) message using the specified address and sends it on the bus
    """
    stat.error = error_t.E_OK
    
    byte4 = (addr & 0xFF000000) >> 24
    byte5 = (addr & 0x00FF0000) >> 16
    byte6 = (addr & 0x0000FF00) >> 8
    byte7 = (addr & 0x000000FF) >> 0

    msg = build_msg([ccp_t.SET_MTA, 0x00, 0x00, 0x00, byte4, byte5, byte6, byte7])

    send_msg(bus, msg)

    recv_msg(bus)
    return

def build_ccp_set_mta(addr):
    byte4 = (addr & 0xFF000000) >> 24
    byte5 = (addr & 0x00FF0000) >> 16
    byte6 = (addr & 0x0000FF00) >> 8
    byte7 = (addr & 0x000000FF) >> 0

    msg = build_msg([ccp_t.SET_MTA, 0x00, 0x00, 0x00, byte4, byte5, byte6, byte7])

    return msg


def ccp_dnload(bus, data_len, dnload_data):
    """
    builds a ccp dnload(ID=0x03) message using the first 4 bytes of dnload_data and sends it on the bus
    """
    stat.error = error_t.E_OK

    #create initial message data
    msg_data = [ccp_t.DNLOAD, 0x00, data_len]
    msg_data = msg_data + dnload_data   
    
    #build the dnload message
    msg = build_msg(msg_data) 
    
    #attempt to send the message to the ECU
    send_msg(bus, msg)
    
    #block until there is a proper response message from the ECU
    recv_msg(bus)
    return

def build_ccp_dnload(data_len, dnload_data):
    #create initial message data
    msg_data = [ccp_t.DNLOAD, 0x00, data_len]
    msg_data = msg_data + dnload_data   
    
    #build the dnload message
    msg = build_msg(msg_data) 

    return msg

def ccp_flash(bus, block_size):
    """
    build a ccp flash(ID=0x18) message and sends it on the bus
    """
    stat.error = error_t.E_OK

    msg = build_msg([ccp_t.FLASH, 0x00, block_size, 0x00, 0x00, 0x00, 0x00, 0x00])
    
    send_msg(bus, msg)
    
    recv_msg(bus)
    return



def ccp_disconnect(bus):
    """
    builds a ccp disconnect(ID=0x07) message and sends it on the bus
    """
    stat.error = error_t.E_OK   
 
    msg = build_msg([ccp_t.DISCONNECT, 0x00, 0x01, 0x00, 0xCC, 0xCC, 0x00, 0x00])

    send_msg(bus, msg)

    recv_msg(bus)
    return


def ccp_upload(bus, data_len):
    """
    builds a ccp upload(ID=0x04) message and sends it on the bus
    """
    stat.error = error_t.E_OK

    msg = build_msg([ccp_t.UPLOAD, 0x00, data_len, 0x00, 0x00, 0x00, 0x00, 0x00])

    send_msg(bus, msg)

    recv_msg(bus)
    return


