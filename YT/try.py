import threading
class CounterClass:
    def __init__(self):
        self.counter = 0
        # self.lock = threading.Lock()
    def increment(self, value):
        # with self.lock:
            self.counter = self.counter + int(value)
def ThreadMethod(x):
    for _ in range(1000000):
        myobj.increment(x)
myobj = CounterClass()
x=threading.Thread(target=ThreadMethod,args=(1,))
y=threading.Thread(target=ThreadMethod,args=(1,))
x.start()
x.join()
y.start()


y.join()
print (myobj.counter)