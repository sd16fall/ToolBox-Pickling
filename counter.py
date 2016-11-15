""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import os
import sys
import pickle
from pickle import dump, load
def update_counter(file_name, reset=False):
	if os.path.exists(file_name) == False:
		counter = open(file_name,"w")
		line = "1"
		counter.write(line)
		counter.close()
	else:
		if reset == False:
			gg = open(file_name,"r")
			for line in gg:
				x=line
			print x
			gg.close()
			y=int(x)+1
			g=open (file_name,"r+")
			for line in g:
			    if line != "afds":
			        g.write(line)
			g.close()
			ggg = open(file_name,"w")
			line = str(y)
			ggg.write(line)
			ggg.close()
		if reset == True:
			g=open (file_name,"r+")
			for line in g:
			    if line != "afds":
			        g.write(line)
			g.close()
			ggg = open(file_name,"w")
			line = "1"
			ggg.write(line)
			ggg.close()



update_counter("hahya",True)




if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
