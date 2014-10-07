import os.path
import re
from collections import defaultdict




filename = open('file_name','w');

work_dir ='/Users/yuhan/Documents/applied_machine_leanring/project/faces';
for root, dir, files in os.walk(work_dir):
    dir_name = root;
    for names in files:
        if (re.match(r'[a-z0-9A-Z_]*_4',names)):
        # if (re.match(r'^\.',names)==None) and (re.match(r'[a-z0-9A-Z_]*_2',names)==None) and (re.match(r'[a-z0-9A-Z_]*_4',names)==None):
                filename.write(dir_name);
                filename.write("/");
                filename.write(names);
                filename.write("\n");
filename.close();
#generate a list of filename, output it for debugging

fileopen = open('file_name','r');



facelist = open('face_data','w')

for line in fileopen:
    if (re.match(r'^\.',line)==None) and (re.match(r'[a-z0-9A-Z_]*_2',line)==None) and (re.match(r'[a-z0-9A-Z_]*_4',line)==None):
        facelist.write(line);
fileopen.close();
facelist.close();





