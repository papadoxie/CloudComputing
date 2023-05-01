#!/usr/bin/env python3

import psutil
import threading
import time

class UtilManager:
    logs = []
    
    def __init__(self):
        task = threading.Thread(target=self.update)
        task.start()

    def getCurrent(self):
        return self.cpu, self.memory
    
    # Get the last k logs
    def getLogs(self, k):
        return self.logs[-k:]

    def update(self):
        while True:
            self.cpu = psutil.cpu_percent()
            self.memory = psutil.virtual_memory().percent
            self.logs.append((time.time(), self.cpu, self.memory))
            time.sleep(60)