import time

from subprocess import *
PATH = "/home/richie_rich/OSProj/redis-Hash-master/src/redis-cli"

p1 = Popen([PATH], shell=True, stdin=PIPE)
p1.communicate(input="FLUSHALL")

strength = 10000
rangeVal = strength + 1
string = "hset myhash "
string1 = ""
count = 0
for i in xrange(1,10001):
    count = count + 1
    string1 = string1 + string + str(i) + " richa \n"
    if (i % 1000) == 0 : 
        p1 = Popen([PATH], shell=True, stdin=PIPE)
        p1.communicate(input=string1)
        string = "hset myhash "
        string1 = ""

print "Inserted %d items" %(count)
