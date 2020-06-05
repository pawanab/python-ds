import threading
'''
function that executed by threading.timer will gets executed in different thread.
'''
def this_will_execute_after_some_time():
    print('I am called by thread timer')


timer = threading.Timer(5.0, this_will_execute_after_some_time)
timer.start()

print('thread timer started')