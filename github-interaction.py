# simple program to allow users to enter a user name and an 'action' to allow the user to interact with github
#
# Please make sure PyGithub requests are installed (pip3 install PyGithub requests)
#
# Author:  John Chen
# Date:  10/29/2022

import argparse
import requests
from pprint import pprint
import base64
from github import Github

def user_print_repos(current_user):
	for repo in current_user.get_repos():
		print(repo)


def main():
	#create ArgumentParser object.
	parser = argparse.ArgumentParser(description='Git interactions using Python')

	#add arguments
	parser.add_argument("-u", "--username", required=True, help="Github Username...")
	args = parser.parse_args()

	#pygithub object
	g = Github()
	#get the user by username
	user = g.get_user(args.username)
	user_print_repos(user)

	print("DONE!")

if __name__ == "__main__":
	main()


