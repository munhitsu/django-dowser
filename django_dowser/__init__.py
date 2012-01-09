import gc
import threading
import time
from django.utils.html import escape

from collections import deque
import itertools

#maximum from all old periods is being promoted to next one
DOWSER_MAXENTRIES = [12,120,60,60]
DOWSER_TICKS = [5,6,48,28]
DOWSER_NAMES = ["1m","1h","1d","4w"]

#DOWSER_MAXENTRIES = [2,2,4]
#DOWSER_TICKS = [2,2,2]


class Dowser(object):
    """
    A working thread to gather type usage
    """
    history = {}
    samples = []
    
    def __init__(self):
        #TODO: how to limit it only to server process not the monitor
        #TODO: cover multi-process configuration - maybe as separate daemon...
        self.samples = [0] * len(DOWSER_MAXENTRIES)
        self.runthread = threading.Thread(target=self.start)
        self.runthread.daemon = True
        self.runthread.start()
    

    def start(self):
        self.running = True
        while self.running:
            self.tick()
            time.sleep(DOWSER_TICKS[0])
    
    def tick(self):
        gc.collect()
        
        typecounts = {}

        for obj in gc.get_objects():
            objtype = type(obj)
            typename = objtype.__module__ + "." + objtype.__name__
            if typename in typecounts:
                typecounts[typename] += 1
            else:
                typecounts[typename] = 1
        
        for typename, count in typecounts.iteritems():
#            typename = objtype.__module__ + "." + objtype.__name__
            if typename not in self.history:
                self.history[typename] = map(lambda x: deque([0] * x), DOWSER_MAXENTRIES)
            self.history[typename][0].appendleft(count)
                
        self.samples[0] = self.samples[0] + 1
        promote = [False] * (len(DOWSER_MAXENTRIES)-1)
        
        #let's calculate what we promote
        for i in range(len(self.samples)-1):
            if self.samples[i] >= DOWSER_TICKS[i]:
                promote[i] = True
                self.samples[i+1] = self.samples[i+1] + 1
                self.samples[i] = 0

        for typename, hist in self.history.iteritems():
            history = self.history[typename]
            #let's promote max from (set of entries to lower granulity history) 
            for i in range(len(self.samples)-1):
                if promote[i]:
                    history[i+1].appendleft(max(itertools.islice(history[i],0,DOWSER_TICKS[i])))
            #let's limit history to DOWSER_MAXENTRIES
            for i in range(len(self.samples)):
                if len(history[i]) > DOWSER_MAXENTRIES[i]:
                    history[i].pop()

    def stop(self):
        self.running = False



dowser = Dowser()
