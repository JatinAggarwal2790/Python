import re
'''
#from 'C:\\Users\\JATIN\\PycharmProjects\\Training\\Week3\\539_m3_datasets_v1.0\\Customer.py' import Customer

import Customer.py

from .Customer import Customer

cust = Customer()

cust.getFname()
'''

class Customer:
    title = ""
    fname = ""
    lname = ""
    isblacklisted = 0;

    def __init__(self):
        self.title = ""

    def __str__(self):
        #return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname + " Blacklisted:" + self.isblacklisted
        return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" + self.lname

    def setIsblacklisted(self,isblacklisted):
        self.isblacklisted = isblacklisted

    def isblacklisted(self):
        return self.isblacklisted

    def setTitle(self,title):
        self.title = title

    def getTitle(self):
        return self.title

    def setFname(self,fname):
        self.fname = fname

    def getFname(self):
        return self.fname

    def setLname(self,lname):
        self.lname = lname

    def getLname(self):
        return self.lname

f=open('C:\\Users\\JATIN\\PycharmProjects\\Training\\Week3\\539_m3_datasets_v1.0\\FairDealCustomerData.csv', mode='r')
l=f.read().split("\n")
#print(l)

#m = re.match(r"(\w+) (\w+)", l)
name=[]
for l1 in l:
    if l1 != 0:
        temp = l1.split(",")
        for t in temp[1:3]:
            name.append(t)


print(name)
c1 = Customer()

for f1 in name:
    m = (re.split('\s+', f1))
    print(m)
    #print(m[1], m[2], m[3])

    c1.setTitle(title=m[1])
    c1.setFname(m[2])
    c1.setLname(m[3])
    print(c1.__str__())
