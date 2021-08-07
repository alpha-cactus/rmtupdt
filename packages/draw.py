from packages.status import stat
from packages.types import error_t
import os

def redraw():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('LAST SENT MSG:\t', stat.last_sent_msg)
    print('LAST RECV MSG:\t', stat.last_recv_msg)
    print('BUS:\t\t', stat.bus)
    print('PROGRAM STATUS:\t', error_t.to_string(stat.error))
    print('\n')
