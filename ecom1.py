# Project : 01 (ecom project)

import time
import os

t1 = time.time()
fr = open("Category.txt")

d1 ={}
d2 = {}
remain = []

for line in fr:
    k,v = line.split(":")
    d1[k.strip()] = v.strip()

fr = open("data1.txt","r")
for line in fr:
    for word,cat in d1.items():
        if word in line:
            d2.setdefault(cat,[]).append(line)
            break
    else:
        remain.append(line)

os.chdir("sorted")

for k,v in d2.items():
    new_name = k+".txt"
    fr = open(new_name,"w")
    fr.writelines(v)
    fr.close()

fr = open("remain.txt","w")
fr.writelines(remain)
fr.close()
t2 = time.time()
print("time taken",t2-t1)
