# assignment (08 march) 
# find out the duplicate line from sample1.

i=0
list1= []
fr = open("sample1.txt","r")
for each in fr:
    if each in list1:
        print("duplicate line is :",each) 
        print(each)
    list1.append(each)    
    i=i+1
print (list1)