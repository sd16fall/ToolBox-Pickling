""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle
import anydbm

def update_counter(file_name, reset=False):
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

	db = anydbm.open('update_counter.db', 'c') #created new database if there wasn't already one
	file_name_str = str(file_name) #turns filename into string just incase it is not already

	if reset == True: #creates new line if input is true
		count = 1
		db[file_name_str] = pickle.dumps(count)
	else: #reads from old input and incriments it one
		count = pickle.loads(db[file_name_str]) + 1
		db[file_name_str] = pickle.dumps(count)

	print count #prints the current count of the db line

	db.close() #closes database

############################### DOC TEST #######################################

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
