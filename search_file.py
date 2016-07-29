#!/usr/bin/python3
import os
from itertools import chain
import textwrap
import time
import heapq
import sys
from Memory_Tree import Mem_Tree
from input_parse import input_parse

'''
	Search the complete path of a file provided by user from one or several paths
	Please provide a precise name for the file that you want to search
	If the file has several copies in different paths, the running result will show all paths
	To run this command, in your commandline, type:
	python .\search_file.py 'D:/'  filename
'''

start_time=time.time()	
input,filename=input_parse(sys.argv)
#print(input)
if not input:
	print("There is some problem with your input. Please follow the example below")
	print ("for example, python './memory_summary' 'C:/' -m 0 -f 1")
else:
	T=Mem_Tree()
	T.initialize(input)
	#T.update_memory_all()
	T.search(filename)
end_time=time.time()
print("Running time is: ",end_time-start_time)


