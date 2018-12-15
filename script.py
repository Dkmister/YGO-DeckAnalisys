

import difflib
import sys



"""
Input: List of lines of a deck
Output: Groups of list separated by its specific caracteristic

Function that returns 3 groups of cards:

index 0 => main deck
index 1 => extra deck
index 2 => side deck
"""
def return_groups(deck):
	main_lst = []
	extra_lst = []
	side_lst = []

	main = False
	extra = False
	side = False

	for line in lines_deck1:
		if line == "#main\n":
			main = True
		if line == "#extra\n":
			main = False
			extra = True
		if line == "!side\n":
			extra = False
			side = True
		if main:
			main_lst.append(line)
		if extra:
			extra_lst.append(line)
		if side:
			side_lst.append(line)
	
	return main_lst,extra_lst,side_lst


"""
Diff of groups

"""
def diff_groups(g1,g2):
	log = open("log.txt","w")
	lst_diff = []
	for i in range(0,3):
		diff_ = difflib.ndiff(g1[i],g2[i])
		diff_ = (''.join(diff_))
		if i == 0:
			log.write("Main Deck Difference:\n")
			log.write(diff_)
		if i == 1:
			log.write("Extra Deck Diferrence:\n")
			log.write(diff_)
		if i == 2:
			log.write("Side Deck Diferrence:\n")
			log.write(diff_)
		lst_diff.append(''.join(diff_))
	return lst_diff


def analyze_g2(g1,g2):
	#TODO 
# main script

deck1 = sys.argv[1]
deck2 = sys.argv[2]

lines_deck1 = open(deck1).readlines()
lines_deck2 = open(deck2).readlines()

diff = difflib.ndiff(lines_deck1,lines_deck2)


group1 = return_groups(lines_deck1)
group2 = return_groups(lines_deck2)

d = diff_groups(group1,group2)


