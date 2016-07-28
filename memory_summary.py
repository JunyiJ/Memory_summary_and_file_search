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
	Summarize the memory usage in provided folders with two flag options:
		-m:default=1,meaning print with memory usage, 0 meaning print without memory
		-f:default=0,meaning print with both folders and files, 1 meaning print only folders
		To run this command, in your commandline, type:
		python .\memory_summary.py 'D:/'  -f 1
'''

start_time=time.time()	

input,flags=input_parse(sys.argv)
print(input)
print(flags)
if not input:
	print("There is some problem with your input. Please follow the example below")
	print ("for example, python './memory_summary' 'C:/' -m 0 -f 1")
else:
	T=Mem_Tree()
	T.initialize(input)
	T.update_memory_all()
	T.pretty_print(m=flags['-m'],f=flags['-f'])

end_time=time.time()
print("Running time is: ",end_time-start_time)


