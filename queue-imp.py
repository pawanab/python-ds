import queue 

def list_to_queue(list_data):
    l_q = queue.Queue(maxsize=len(list_data))
    for l in list_data:
        l_q.put(l)

    print(l_q.qsize())
    ele = l_q.get()
    print(ele)
    print(l_q.qsize())
    l_q.put(ele)
    print(l_q.qsize())
    print(l_q.get())
    print(l_q.qsize())






if __name__ == '__main__':
    temp_list = ['pawan','arora','jaipur','India']
    list_to_queue(temp_list)


