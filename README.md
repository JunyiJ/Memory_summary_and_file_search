# Memory summarize and file search (Python3)

## Introduction

A lot people are bothered by finding out where a specific file is. The search
function provided by the computer sometimes does not work well or can be very
slow. Sometimes it if not very convenient to find out the size of a specific folder
and its content on your computer by just one click. If you are searching for solutions
to these problems or ideas that might inspire you, you are at the right place. 
The scripts provided here aim to:
  - Provide a complete folder structure(list all files and subfolders within it) and memory usage upon your request.
  - Assit you to search a file and provide a complete path to it
  - List all the memory-consuming files in the folder you provided.
  
## Usage
	1. To get the folder structure and memory usage summary on it (for example, the folder name is 'D:/').
		you can provided several paths or you can list all the paths in a file(separated by new line) and feed the file
		name to the command.
		- list path directly in command line
		python .\memory_summary.py 'D:/'
		- list path in a file and feed the file (path_all.txt) to command line
		python .\memory_summary.py 'path_all.txt'
		There are also two flags -m (default 1) and -f (default 0).
		set -m 1 means show the memory usage as well and set -m 0 means do not show memory
		set -f 1 means only show folders and subfolders and set -m 1 means show both folders and files
		for example: python .\memory_summary.py 'D:/' -m 0 -f 1 means show only folders in folder D without memory summary
	2. To search a file in a suspect folder or several foldes, in your command line type:
		python .\search_file.py 'D:/'  filename
	3. To find the most N memory consuming files, run this command, in your commandline, type:
		python .\memoryeat_file.py 'D:/'  5
		This will find the most 5 memory consuing file in folder D
		


## Dependency
Python 3 on your computer
(I will pulish a python 2 version later)
