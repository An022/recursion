"""
File: anagram.py
Name: An Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
dic = []


def main():
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    search = str(input('Find anagrams for:'))
    if search == EXIT:
        print('Process finished with exit code 0')
    else:
        find_anagrams(search)
        while True:
            search = str(input('Find anagrams for:'))
            if search == EXIT:
                break
            else:
                find_anagrams(search)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word_lst = line.strip()
            dic.append(word_lst)


def find_anagrams(s):
    """
    :param s: str, the user will input a word.
    :return: list, this function will find those anagrams.
    """
    a = find_anagrams_helper(s, '', [], [])
    print(str(len(a)) + ' anagrams:' + str(a))


def find_anagrams_helper(s, new, word_lst, index):
    # Set the Base Case 1: if the length of new word equals the length of the given word.
    # Set the Base Case 2: if the new word can be found in dictionary, in other words the new word has meaning.
    # Set the final Base Case: Combine those two conditions.
    if len(s) == len(new) and new in dic:
        if new not in word_lst:
            print('Searching...')
            word_lst.append(new)
            print('Found:' + new)
    else:
        for i in range(len(s)):
            if i not in index:
                # Choose
                new += s[i]
                index.append(i)
                # Explore
                if has_prefix(new):
                    find_anagrams_helper(s, new, word_lst, index)
                # Un-choose
                new = new[:-1]
                index.pop()
    return word_lst


def has_prefix(sub_s):
    """
    :param sub_s: str, those characters that have been input so far.
    :return: check these characters exist in the dictionary or not, if it exists then return True.
    """
    for i in dic:
        if i.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
