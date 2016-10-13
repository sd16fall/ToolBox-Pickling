""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
from pickle import dump, load
import pickle #I'm just importing all of pickle lol
counter=0 #initializing the counter

def update_counter(file_name, reset):
	if(reset==True): #if reset is true, reset to counter 1
		counter=1
		pickle.dump(counter, open(file_name,'wb'))
	if(reset==False): #if reset is not true, either create a new file or adds 1 to the counter
		try:
			counter= int(pickle.load(open(file_name, 'rb')))+1
			pickle.dump(counter, open(file_name, 'wb'))
		except:
			pickle.dump(1,open(file_name,'wb'))


#update_counter('test3.txt',False)						#these sections are for debugging! :)
#counter= pickle.load(open('test3.txt', 'rb'))
#print counter