import csv
import codecs


f1=open('target.txt','a')


with codecs.open('test.txt', mode='r', encoding='UTF-8', errors='strict', buffering=1) as f:

    for line in f:
           line=line.encode('ascii','ignore').decode('UTF-8','ignore')
           f1.write(line)
    
    f1.close()
