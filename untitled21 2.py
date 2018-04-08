# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 18:39:41 2018

@author: admin
"""

"""@author: admin
""""""
# -*- coding: utf-8 -*-

Created on Sun Mar 25 13:39:46 2018

@author: admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:34:45 2018

@author: admin
"""
import csv;
import time;
import datetime;
import numpy as np;
import pandas as pd;
import warnings;
import matplotlib.pyplot as plt;
from sklearn import preprocessing
warnings.filterwarnings("ignore")

"""
"column=f.Destination;
"column2=f.ServiceNo;"""
def fun(nae,k):
   # print(k)
    file21=open('C:/Users/admin/Desktop/Route1.csv','r');
    f=csv.reader(file21);
    for row in f:
        if row:
            if row[k] == nae:
                print("The buses available are with bus number",format(row[0]),"with sevice numbers",format(row[1]))

    file21.close();
    if(k<33):
        k=k+1;
        fun(nae,k)

def fun1(m):
       data=m.split(':');
       s=(int(data[0])*60)+int(data[1]);
       return s;
#delay estimation time
def delay(k):

    data=k.split(':');
    if int(data[0])>17 and int(data[0])<21:
        delay=2;
    elif int(data[0])>7 and int(data[0])<10:
            delay=2;
    else:
        delay=1.2;
    return delay;

def fun2(l,m,i,row):
    k=5;sum=0;
    while(k<=i):
        #sum of all the previous stops delays
        sum=sum+delay(row[k])
        k=k+2
    #print(sum)
    #p=delay(l);
    #q=delay(m);
    k=0;
    #k=(fun1(l)+fun1(m)+sum)/3;
    #the time at which it arrives current time plus delay
    k=fun1(m)+sum
    #print(k)
    #conversion
    w=int(k/60);
    t=int(k%60);

    return w,":",t;

name=input("Enter your destination");
file1=open('C:/Users/admin/Desktop/Route1.csv','r');
localtime = time.asctime( time.localtime(time.time()) )
fs=csv.reader(file1);
#file=pd.read_csv('C:/Users/admin/Desktop/Route.csv');
#print(file);
flag=0;flag1=0;flag2=0;flag3=0;
#now = time.time.now()
#print(now)

#for row in fs:
   # print (row);
i=0;
fun(name,3);

              #print("The buses available are with bus number",format(row[0]),"with sevice numbers",format(row[1]))

                    #print("The buses available are with bus number",format(row[0]),"with sevice numbers",format(row[1]))

                   #print("The buses available are with bus number",format(row[0]),"with sevice numbers",format(row[1]))


                   #print("The buses available are with bus number",format(row[0]),"with sevice numbers",format(row[1]))


number=input("Enter your choice");

file1.close();

file2=open('C:/Users/admin/Desktop/Route1.csv','r');
fsv=csv.reader(file2);
for row in fsv:
   if row:
         if row[1] == number:
             k=5;
             while(k<33):
                 if row[k]==name:
                     print("The buses available are with bus number",format(row[0]),"service number",format(row[1]),"arriving at time",format(row[k+1]))
                     m=format(row[k+1]);
                     p=format(row[k-1]);
                     s=fun1(m);
                     l=fun1(p);
                     o=fun2(m,p,k,row);
                    # print("Your bus with delay will be arriving in ",o,"minutes");
                 k=k+1
        #var=int(row[k+1]);
        #print("You can expect your bus in",now.minute-var);

file2.close();
file2=open('C:/Users/admin/Desktop/Route1.csv','r');

