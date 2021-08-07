from packages.types import error_t


#status object used for trackign program status
#there should only ever be one global instance of this object
#vlaues of the status object can be updated/read from anywhere
class status_t():
    __instance = None

    def get_instance():
        if status_t.__instance == None:
            status_t()

        return status_t.__instance



    def __init__(self):
        if status_t.__instance != None:
            raise Exception('This class is a singleton')
        else:
            self.error = error_t.E_OK
            self.last_sent_msg = None
            self.last_recv_msg = None
            self.bus = None
            status_t.__instance = self


#create the singleton instance of the status object
stat = status_t()
