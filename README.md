# self_learning-recursion
Reference to Stanford University’s assignment CS106AP: Programming Methodologies in Python and CS106B: Programming Abstractions as practice, focusing topic: recursion
## Projects Source Codes:
* [01_anagram](https://github.com/An022/self_learning-recursion/blob/main/01_anagram/anagram.py)\
  The Anagram program recursively finds all the anagram(s) for the word input by user and terminates when thei nput string matches the EXIT constant defined as “-1”.

  ```
  Implement this program, you should see the number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
   
  pre-condition:
  :param s: str, the user will input a word.
  post-condition:
  :return: list, this function will find those anagrams.
  ```
* [02_boggle](https://github.com/An022/self_learning-recursion/blob/main/02_boggle/boggle.py)\
  This program compares short dna sequence, s2, with subsequences of a long dna sequence, s1\
  the way of approaching this task is the same as what people are doing in the bio- industry.
  
  ```
  The Boggle program finds all possible answers for the game by recursively searching words in sequences of adjacent letters.
  
  pre-condition: 
  Inform user to input "a DNA sequence to search" and "a DNA sequence to match".
  post-condition: 
  Show user the best match DNA sequence.
  ```
* [03_largest_digit(recursion)](https://github.com/An022/self_learning-recursion/blob/main/03_largest_digit(recursion)/largest_digit.py)\
  This file recursively prints the biggest digit in 5 different integers, 12345, 281, 6, -111, -9453\
  If implementation is correct, you should see 5, 8, 6, 1, 9 on Console.

  ```
  Use the concept of Caesar Cipher to cipher the secret message.
  
  Pre-condition: 
  :param n: int, given a number.
  Post-condition: 
  :return: return the largest digit of the given number.
  ```
* [04_sierpinski](https://github.com/An022/self_learning-recursion/blob/main/04_sierpinski/sierpinski.py)\
  This file recursively prints the Sierpinski triangle on GWindow.\
  The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.\
  It is a self similar structure that occurs at different levels of iterations.
  
  ```
  pre-condition:
  :param order: How many times should the graphs repeated to be printed.
	:param length: The length of the original sierpinski triangle.
	:param upper_left_x: The x-axis of original sierpinski triangle.
	:param upper_left_y: The y-axis of original sierpinski triangle.
  post-condition:
  :return: The sierpinski triangle that be printed in "order" repeatedly.
  ```
