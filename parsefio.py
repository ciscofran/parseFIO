# Francisco Londono
# May 7 2017
# Parsing raw data files from FIO benchmark file
# Pre-condition:
#  fio_raw_disk_perf_blksize1K_datasize10240MB.csv
#  fio_raw_disk_perf_blksize4K_datasize10240MB.csv
# 
# This script compares the write IOPS of synchronous (sync) and asynchronous (async) I/O

import csv
import pprint
import re
import matplotlib.pyplot as plt

s=""
asynclst  = []
synclst   = []
asynclst1 = []
synclst1  = []

with open("fio_raw_disk_perf_blksize1K_datasize10240MB.csv", 'r', encoding='utf-8') as csvfile: 
    # find the format 
    fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    # read the CSV file into a dictionary
    dictReader = csv.DictReader(csvfile, dialect=fileDialect)
	
    for row in dictReader:
      s = row['jobname']	
      if (bool(re.match("async-",s))):
        asynclst.append(row['WRITE_IOPS'])		     
		
      if (bool(re.match("sync-",s))): 
        synclst.append(row['WRITE_IOPS'])
        
with open("fio_raw_disk_perf_blksize4K_datasize10240MB.csv", 'r', encoding='utf-8') as csvfile: 
    # find the format 
    fileDialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    # read the CSV file into a dictionary
    dictReader = csv.DictReader(csvfile, dialect=fileDialect)
	
    for row in dictReader:
      s = row['jobname']	
      if (bool(re.match("async-",s))):
        asynclst1.append(row['WRITE_IOPS'])		     
		
      if (bool(re.match("sync-",s))): 
        synclst1.append(row['WRITE_IOPS'])      


		
fig = plt.figure()

fig.subplots_adjust(bottom=0.2)

ax1 = fig.add_subplot(111)

line1 = ax1.plot(asynclst,'bo-',label='async WriteIOPS 1K_blks')
line2 = ax1.plot(synclst,'go-',label='sync WriteIOPS 1Kblks')
line3 = ax1.plot(asynclst1,'ro-',label='async WriteIOPS 4K_blks')
line4 = ax1.plot(synclst1,'yo-',label='sync WriteIOPS 4K_blks')

ax1.set_ylim(0,300000)

plt.xlabel("x-axis")
plt.ylabel("write IOPS")
plt.title("Sync and Async Write IOPS")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),ncol=2)
plt.grid()
plt.show()