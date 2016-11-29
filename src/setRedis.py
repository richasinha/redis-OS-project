import time

from subprocess import *
PATH = "/home/richie_rich/OSProj/redis-OS-project/src/redis-cli"

p1 = Popen([PATH], shell=True, stdin=PIPE)
p1.communicate(input="FLUSHALL")

strength = 100000
rangeVal = strength + 1
string = "set key"
string1 = ""
count = 0
for i in xrange(1,rangeVal):
    count = count + 1
    string1 = string1 + string + str(i) + " val" + str(i) + "\n"
    if (i % 1000) == 0 : 
        p1 = Popen([PATH], shell=True, stdin=PIPE)
        p1.communicate(input=string1)
        string = "set key"
        string1 = ""

print string1
print "Inserted %d items" %(count)
