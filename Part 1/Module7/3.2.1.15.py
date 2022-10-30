class QueueError:  # Choose base class for the new exception.
    pass
    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        self.__stk = []
        #
        # Write code here
        #

    def put(self, elem):
        self.__stk.append(elem)
        #
        # Write code here
        #

    def get(self):
        val = self.__stk[0]
        del self.__stk[0]
        return val
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
