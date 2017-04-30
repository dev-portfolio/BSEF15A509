import Queue
class newProcesses :

    processName = ""
    burstTime = 0
    arrivalTime = 0

    def __init__(self, pName, pBurstTime, pArrivalTime):

        self.processName = pName
        self.burstTime = pBurstTime
        self.arrivalTime = pArrivalTime

    def display(self):
        print self.processName + "    " + str(self.burstTime) + "    " + str(self.arrivalTime)

    def clear(self):
        self.processName = ""
        self.burstTime = 0
        self.arrivalTime = 0


# an instance of class newProcesses is made
obj = newProcesses("P0", 0, 0)
list = [newProcesses]


# file where processes are present is being read
fo = open("input.txt", "r")

i = 0
j = 0
del list[:]

# file is read line by line and processes are picked up from the filr then entered in the list.
import re
with open("input.txt") as f:
    for line in f:
        line_str = "";
        for word in re.findall(r'\w+', line):


               if i == 0 :
                   obj.processName = word
               elif i == 1 :
                   obj.burstTime = int(word)
               elif i == 2 :
                  obj.arrivalTime = int(word)

               i = i + 1
               if i == 3 :
                    obj.display()
                    list.append(obj)
                    i = 0

# Close opend file
fo.close()

#till here we succefully have populated the list where we are receiving new incoming processes


# Due to some unknown reason, data in list is not being populated correctly.
# Even after spending huge time on trying to resolve the issue I couldn't sort it out
# Thus I have hardcoded the data for the time being.

obj1 = newProcesses("P1", 7, 0)
obj2 = newProcesses("P2", 5, 1)
obj3 = newProcesses("P3", 9, 2)
obj4 = newProcesses("P4", 4, 4)
obj5 = newProcesses("P5", 7, 7)

del list[:]

list.append(obj1)
list.append(obj2)
list.append(obj3)
list.append(obj4)
list.append(obj5)


# list populated

print "\n\n"

# time slice for RR algo
quantum = 3

time = 0

# creating Ready Queue
readyQueue = Queue.Queue()

print "queue size : " , readyQueue.qsize()

temp = newProcesses("", 0, 0)
tempArrivalTime = 0

while list.__len__() > 0 :

    if readyQueue.qsize() > 0 :
        #print "if"
        temp = readyQueue.get()
        if temp.burstTime / quantum > 0 :
            tempArrivalTime = time
            time += quantum
            temp.burstTime -= quantum

            if temp.burstTime == 0 :
                print temp.processName + " (finishes)    ", tempArrivalTime, "    ", time, "   ", readyQueue.qsize()
            else :
                print temp.processName + "               ", tempArrivalTime, "    ", time, "   ", readyQueue.qsize()
                while list[0].arrivalTime <= time:
                    readyQueue.put(list[0])
                    list.pop(0)
                readyQueue.put(temp)
        else :
            time += temp.burstTime % quantum
            print temp.processName + " (finishes)    ", tempArrivalTime, "    ", time


    else :
        while list[0].arrivalTime <= time :
            readyQueue.put(list[0])
            list.pop(0)
            print "###---" + list[0].processName + "---###"
            #print "else"




