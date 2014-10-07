import os.path
import re
from collections import defaultdict
import tokenize
import binascii
import csv
import struct

#work_dir ='/Users/yuhan/Documents/applied_machine_leanring/project/faces';
facelist=open('file_name','r');

glassdict=defaultdict(int);

pixels=defaultdict(int);

uid_count=0;

for line in facelist:
    #f=open(line.strip('[\n]'),'r');
    elts=re.split(r'[\_.]',line);
    last_index = len(elts);
    if elts[last_index-3]=="open":#-3 for *_4 data, -2 for original data
        glassdict[uid_count]=0
    else:
        glassdict[uid_count]=1
    facedata =open(line.strip('[\n]'), 'rb');
    facedata.readline();
    facedata.readline();
    facedata.readline();
    pixels[uid_count]=facedata.read();
    facedata.close();
    uid_count+=1;

#with open('features.csv','w') as o:
#   writer = csv.writer(o);
    #row=['glass'];
    #row[0] = 'glass';
    #for j in range(0, 15360):
    #    row.append(j);
    #writer.writerow(row);
outfile = open('wekadata','w');

outfile.write('Glass');

#print the title column
for i in range(0,960):
    outfile.write(' ');
    outfile.write(str(i));
outfile.write('\n');

#print the data in the file
#first print glassdict as the data result than print pixels


for i in range(0,uid_count):
        # row = [glassdict[i],re.split('^[\w]',pixels[i])];
        # writer.writerow(row);
    outfile.write(str(glassdict[i]));
    data = struct.unpack("960c",pixels[i]);
    #data = re.split('[^0-9]',pixels[i]);
    for j in range(0,960):
        outfile.write(' ');
        outfile.write(str(ord(data[j])));
    outfile.write('\n');
outfile.close();