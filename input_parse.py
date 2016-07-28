#!/usr/bin/python3
import sys
import os

def input_parse(argv):
	#print(argv[0].strip('./\\'))
	if argv[0].strip('./\\')=='memory_summary.py':
		if len(argv)<2:
			print ("Not enough arguments.")
			return None,None
		i=len(argv)-1
		input=[]
		flags={'-m':True,'-f':False}
		while i>0:
			if argv[i] in ['0','1']:
				if i<=2:
					print ("Wrong arguments. Please double check")
					return None,None
				else:
					flag=argv[i-1]
					if flag[0]=='-':
						flags[flag]=True if argv[i]=='1' else False
						i-=1
					else:
						print ("Please input flag value pairs in the right order.")
						print("The flag is either -m(means without memory size or not), or -f(means folder only or not)")
						return None,None
			elif os.path.exists(argv[i]):
				input.append(argv[i])
			else:
				try:
					with open(argv[i],'r') as f:
						for line in f:
							line=line.strip()
							input.append(line)
				except FileNotFoundError as err:
					print("error with input directory or input file")
					return None,None
			i-=1
		return input,flags
	elif argv[0].strip('./\\')=='search_file.py':
		input=[]
		if len(argv)<3:
			print ("Not enough arguments.")
			return None,None
		filename=argv[-1]
		for i in range(1,len(argv)-1):
			if os.path.exists(argv[i]):
				input.append(argv[i])
		if not input:
			print('Please input valid searching path')
			return None,None
		return input,filename
	elif argv[0].strip('./\\')=='memoryeat_file.py':
		input=[]
		if len(argv)<3:
			print ("Not enough arguments.")
			return None,None
		N=int(argv[-1])
		for i in range(1,len(argv)-1):
			if os.path.exists(argv[i]):
				input.append(argv[i])
		if not input:
			print('Please input valid searching path')
			return None,None
		return input,N
			
		
				
		
	