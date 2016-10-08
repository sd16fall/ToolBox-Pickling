""" A program that stores and updates a counter using a Python pickle file"""

import os # need to include global os class
from os.path import exists
import sys
import pickle
from pickle import dump, load

# note: reset flag is false by default
def update_counter(file_name, reset=False):
	# checks for file existence (nested 1)
	if (os.path.exists(file_name) and (reset == False)):
		# opens the file in counter, with reading plus permissions
		counter = open(file_name, 'r+')
		# stores the string value as an integer
		counterValue = pickle.load(counter)
		# resets counter head to beginning
		counter.seek(0,0)
		counterValue += 1
		# dumps the incremented counter into the pickle field
		pickle.dump(counterValue,counter)
	# runs if file does not not exist, or if the reset flag is true
	else:
		# reopens file in write mode and reinitializes counter value to 1
		counter = open(file_name,'w') #write mode clears all data by default
		pickle.dump(1,counter) # using standard ASCII protocol

	# close original file access
	counter.close()
	# create new handler to parse the information ('w' mode does not support reads)
	counter2 = open(file_name,'r')
	# uses pickle to load the current counter value (generic operation)
	finalValue = pickle.load(counter2)
	counter2.seek(0,0)
	counter2.close()
	return finalValue

""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
"""


if __name__ == '__main__':
	print update_counter('blah.txt',True)
	print update_counter('blah.txt')
	print update_counter('blah2.txt',True)
	print update_counter('blah.txt')
	print update_counter('blah2.txt')

	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
