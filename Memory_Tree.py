#!/usr/bin/python3
import os
from itertools import chain
import textwrap
import time
import heapq
import logging

logging.basicConfig(filename='log.log',level=logging.DEBUG)

class node(object):
	def __init__(self,name):
		self.memsize=0
		self.name=name
		self.kiddir=[]
		self.kidfile=[]
		self.dist=0
		self.depth=0
	def add_subdir(self,kid_node):
		self.kiddir.append(kid_node)
	def add_subfile(self,kid_node):
		self.kidfile.append(kid_node)
	def update_memsize(self,memory):
		self.memsize=memory
	def update_dist(self,dist):
		self.dist=dist
	def update_depth(self,depth):
		self.depth=depth

class Mem_Tree(object):
	def __init__(self):
		self.root=None
		self.depth=0
		self._list=[]
	def initialize(self,rootpath):
		if len(rootpath)==1:								#If only one rootpath provided
			Root=node(rootpath[0])
			self.root=Root
			waitlist=[Root]
		else:
			Root=node('&&'.join(rootpath))					#If several path are provided in a list
			self.root=Root
			waitlist=[]
			for i in rootpath:
				new_node=node(i)
				if os.path.isdir(i):
					Root.add_subdir(new_node)
				else:
					Root.add_subfile(new_node)
				waitlist.append(new_node)
		while waitlist:
			cur_node=waitlist.pop()
			cur_path=cur_node.name
			try:
				names=os.listdir(cur_path)
			except PermissionError as err:
				logging.warning(err)
			for name in names:
				complete_path=os.path.join(cur_path,name)
				new_node=node(complete_path)
				if os.path.isdir(complete_path):
					cur_node.add_subdir(new_node)
					waitlist.append(new_node)
				else:
					cur_node.add_subfile(new_node)
					try:
						memory=os.path.getsize(complete_path)
						new_node.update_memsize(memory)
						tmp={}
						tmp['name']=new_node.name
						tmp['mem']=memory
						self._list.append(tmp)
					except PermissionError as err:
						logging.warning(err)
					except FileNotFoundError as err:
						logging.warning(err)
					

	def search(self,filename):
		#Search the path for a certain filename
		DFS=[self.root]
		result=[]
		while DFS:
			cur_node=DFS.pop()
			if os.path.isdir(cur_node.name):
				try_path=os.path.join(cur_node.name,filename)
				if os.path.exists(try_path):
					result.append(try_path)
			for k in cur_node.kiddir:
				DFS.append(k)
		if not result:
			print("Sorry, mission failed. T_T")
		else:
			print("The file (%s) is found in the following place(s)" % filename)
			for i in result:
				print(i)
					
	def update_memory_all(self):
		#Update the memory used in each node
		DFS=[self.root]
		DFS1=[]
		dist=0
		depth=0
		while DFS:
			cur_node=DFS.pop()
			DFS1.append(cur_node)
			for k in chain(cur_node.kiddir,cur_node.kidfile):
				DFS.append(k)
				k.update_dist(cur_node.dist+1)
		while DFS1:
			n=DFS1.pop()
			if os.path.isdir(n.name):
				result=0
				depth=0
				for k in chain(n.kiddir,n.kidfile):
					result+=k.memsize
					if k.depth>depth:
						depth=k.depth
				depth+=1
				n.update_memsize(result)
				n.update_depth(depth)
		self.depth=self.root.depth	
	
	def maxN(self,N):
		#Find the max N memory consuming files
		top=heapq.nlargest(N,self._list,key=lambda s:s['mem'])
		print("The max (%d) memory consuming files are: " %(N))
		for i in top:
			print(i)

	def pretty_print(self,m=True,f=False):
		#Print the files and folders under root, with their memory usage if m(with_memory)=True
		#Only print folders is f(folders_only)=True
		base=3
		width=self.depth*base+50
		DFS=[self.root]
		while DFS:
			cur_node=DFS.pop()
			indent_size=cur_node.dist*base
			name=os.path.basename(cur_node.name)
			star_size=width-indent_size-len(name)
			try:
				if m:
					print(textwrap.indent(name,''.join([' ']*indent_size)),''.join(['.']*star_size),cur_node.memsize)
				else:
					print(textwrap.indent(name,''.join([' ']*indent_size)))
			except UnicodeEncodeError as err:
				logging.debug(err)
			for k in cur_node.kiddir:
				DFS.append(k)
			if not f:
				for k in cur_node.kidfile:
					indent_size=k.dist*base
					name=os.path.basename(k.name)
					star_size=width-indent_size-len(name)
					try:
						if m:
							print(textwrap.indent(name,''.join([' ']*indent_size)),''.join(['.']*star_size),k.memsize)
						else:
							print(textwrap.indent(name,''.join([' ']*indent_size)))
					except UnicodeEncodeError as err:
						print ('Handling unicode encode error',err)

# start_time=time.time()	
# path=['D:/','C:/']
# T=Tree()
# T.initialize(path)
# T.search('UG_PA13130.pdf')
# T.maxN(10)
# T.update_memory_all()
# T.pretty_print(folders_only=True)
# end_time=time.time()
# print("Running time is: ",end_time-start_time)


