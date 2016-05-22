#!/usr/bin/python3

import threading
import time
import random

exitFlag = 0



class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print("Preparado " + self.name +" cobrar " + str(self.counter) + " Productos.")
        print_time(self.name, random.randrange(9), self.counter)
        print("Finalizado " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: Faltan %s productos, procesando en %s segundos por producto" % (threadName, counter, delay))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Cajero1", random.randrange(30))
thread2 = myThread(2, "Cajero2", random.randrange(30))
thread3 = myThread(3, "Cajero3", random.randrange(30))
thread4 = myThread(4, "Cajero4", random.randrange(30))
thread5 = myThread(5, "Cajero5", random.randrange(30))

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

