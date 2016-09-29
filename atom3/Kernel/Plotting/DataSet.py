import os

class DataSet:
    def __init__(self, titles=(), source='unknown'):
        self.data = []
        self.titles = titles
        self.source = source
        self.listeners = []

    def __str__(self):
        return self.source

    def addListener(self, listener):
        self.listeners.append(listener)
        if self.data: listener.dataSetExtended(len(self.data))

    def removeListener(self, listener):
        self.listeners.remove(listener)

    def append(self, x):
        self.data.append(x)
        for l in self.listeners:
            l.dataSetExtended()

    def extend(self, x):
        self.data.extend(x)
        for l in self.listeners:
            l.dataSetExtended(len(x))

    def clear(self):
        self.data = []
        for l in self.listeners:
            l.dataSetCleared()

    def writeToFile(self, filename):
        outfile = open(filename, 'w')
        outfile.write('# ')
        for title in self.titles:
            outfile.write(title + '\t')
        outfile.write('\n\n')
        for datum in self.data:
            for x in datum:
                outfile.write(`x` + '\t')
            outfile.write('\n')
        outfile.close()

    def readFromFile(self, filename):
        self.source=os.path.basename(filename)
        infile = open(filename, 'r')
        self.titles = infile.readline().split()
        line = infile.readline()
        while line:
            fields = line.split()
            if len(fields) == len(self.titles):
                self.data.append([float(x) for x in fields])
            line = infile.readline()
        infile.close()
