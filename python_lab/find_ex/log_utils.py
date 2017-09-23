import os
import os.path
import codecs
import random


class Logger:
    def __init__(self):
        self.logCache = []
        self.logIndex = 1

    def LogDebug(self, log):
        temp = (str)(self.logIndex) + " " + "--Debug-- " + log
        self.logCache.append(temp)
        self.logIndex = self.logIndex + 1
        print(temp)
        return

    def LogWarn(self, log):
        temp = (str)(self.logIndex) + " " + "--Warning-- " + log
        self.logCache.append(temp)
        self.logIndex = self.logIndex + 1
        print(temp)
        return

    def LogError(self, log):
        temp = (str)(self.logIndex) + " " + "--Error-- " + log
        self.logCache.append(temp)
        self.logIndex = self.logIndex + 1
        print(temp)
        return

    def LogOutput(self, path):
        temp = ''
        for i in self.logCache:
            temp += i + '\r\n'
        fileObject = codecs.open(path, 'w', encoding='utf-8')
        fileObject.write(temp)
        fileObject.close()
        return