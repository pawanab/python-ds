from enum import IntEnum


class StatusEn(IntEnum):
    OPEN = 1
    IN_PROGRESS = 2
    CLOSED = 3

def handle_open_status():
    print('I will handle all OPEN status.')


def handle_in_progress_status():
    print('I will handle IN Progess status.')


def handle_close_status():
    print('I will handle all closed status.')



handle_options = {
    StatusEn.OPEN.value : handle_open_status,
    StatusEn.IN_PROGRESS.value : handle_in_progress_status,
    StatusEn.CLOSED.value : handle_close_status
}


    





if __name__ == '__main__':
    handler = handle_options[StatusEn.OPEN.value]
    handler()
    
        
