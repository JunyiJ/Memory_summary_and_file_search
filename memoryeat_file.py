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
	Find the most N memory consuming files
	To run this command, in your commandline, type:
	python .\memoryeat_file.py 'D:/'  5
	This will find the most 5 memory consuing file in folder D
'''

start_time=time.time()	
input,N=input_parse(sys.argv)
if not input:
	print("There is some problem with your input. Please follow the example below")
	print ("for example, python './memory_summary' 'C:/' -m 0 -f 1")
else:
	T=Mem_Tree()
	T.initialize(input)
	T.update_memory_all()
	T.maxN(N)
end_time=time.time()
print("Running time is: ",end_time-start_time)


