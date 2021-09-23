"""
File: boggle.py
Name: An Lee
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

COUNTER = 0

# global variable
dic = []
boggle_dic = {}
word_list = []


def main():
	"""
	TODO:
	"""
	global boggle_dic
	read_dictionary()
	search_row1 = str(input('1 row of letters: '))
	if check_input_form(search_row1) is False:
		print('Illegal input')
	else:
		row1 = create_map(search_row1)
		search_row2 = str(input('2 row of letters: '))
		if check_input_form(search_row2) is False:
			print('Illegal input')
		else:
			row2 = create_map(search_row2)
			search_row3 = str(input('3 row of letters: '))
			if check_input_form(search_row3) is False:
				print('Illegal input')
			else:
				row3 = create_map(search_row3)
				search_row4 = str(input('4 row of letters: '))
				if check_input_form(search_row4) is False:
					print('Illegal input')
				else:
					row4 = create_map(search_row4)
					boggle_dic[0] = row1
					boggle_dic[1] = row2
					boggle_dic[2] = row3
					boggle_dic[3] = row4
	for y in range(4):
		for x in range(4):
			start_point = boggle_dic[x][y]
			find_answer(boggle_dic, x, y, str(start_point), [(x, y)])
	print('There are ' + str(COUNTER) + ' words in total.')


def create_map(input_words):
	row = []
	ch = input_words.split()
	row.append(ch)
	return ch


def check_input_form(string):
	for i in range(len(string)):
		if i % 2 == 1:
			if string[i] != ' ':
				return False


def find_answer(boggle_dic, x, y, start_point, index):
	"""
	:param : dic, containing all the boggle data.
	:return:
	"""
	find_answer_helper(boggle_dic, x, y, start_point, index)


def find_answer_helper(boggle_dic, x, y, start_point, index):
	global COUNTER
	if len(start_point) >= 4 and start_point in dic:
		if start_point not in word_list:
			word_list.append(start_point)
			print('Found:' + start_point)
			COUNTER += 1
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x + i < 4 and 0 <= y + j < 4:
					if (x+i, y+j) not in index:
						# Choose
						start_point += boggle_dic[x+i][y+j]
						index.append((x+i, y+j))
						# Explore
						if has_prefix(start_point):
							find_answer_helper(boggle_dic, x + i, y + j, start_point, index)
						# Un-choose
						start_point = start_point[:-1]
						index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word_lst = line.strip()
			dic.append(word_lst)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in dic:
		if i.startswith(sub_s):
			return True


if __name__ == '__main__':
	main()
