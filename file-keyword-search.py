# simple program to allow users to enter a filename and type in strings to search for in the file, then close the file.
# the program will count the number of times that each of the requested keyword is encountered.
#
# note:  this is a simple example and is not meant to scale for production.
# note1:  this example uses the argparse library.
#
# Author:  John Chen

import argparse

def count_word_in_file(v, file_contents, word):
	if v:
		print("Looking for keyword:  ", str(word))
	return file_contents.count(word)
	

def main():
	#create ArgumentParser object.
	parser = argparse.ArgumentParser(description='File keyword frequency searcher')

	#add arguments
	parser.add_argument("-f", "--filename", required=True, help="Name of the file to be parsed...")
	parser.add_argument("-v", "--verbose", help="Turn on verbose mode...", action='store_true')
	parser.add_argument("-k", "--keyword", required=True, help="Keyword to search for...", action='append')
	args = parser.parse_args()

	#print the user input parameters if in verbose mode.
	if args.verbose:
		print ("Filename: ", args.filename)
		print ("# of Keywords: ", len(args.keyword))
		print ("Keyword buffer type", type(args.keyword))
		print ("Keywords to search for:", args.keyword)

	try:
		# try to open the file
		with open(args.filename) as f_obj:
			if args.verbose:
				print("File found, Opening")

			# read the contents of the file
			contents = f_obj.read()
		
			# count each keyword in the file.
			for x in args.keyword:
				#count_word_in_file(contents, x)
				print("Found", count_word_in_file(args.verbose, contents, x), "instances of the word:", x)

			# Done, close the file
			f_obj.close()
	except FileNotFoundError:
		# oops - file does not exist.  Fail gracefully.
		print("ERROR:  file not found")

	print("DONE!")

if __name__ == "__main__":
	main()


