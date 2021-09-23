"""
File: largest_digit.py
Name: An Lee
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
ANS = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, given a number.
	:return: return the largest digit of the given number.
	"""
	return find_largest_digit_helper(abs(n), 0, 0)


def find_largest_digit_helper(number, a, maximum):
	# Set the first and next digit
	now = number // 10 ** a % 10
	next = number // 10 ** (a+1) % 10
	# Set the Base Case.
	if now == 0:
		return maximum
	else:
		# Compare two digit.
		if now < next:
			maximum = next
		else:
			if maximum < now:
				maximum = now
			else:
				pass
		return find_largest_digit_helper(number, a+1, maximum)
	# if number % 10 > maximum:
	# 	maximum = number % 10
	# if number//10 == 0:
	# 	return maximum
	# else:
	# 	return find_largest_digit_helper(number//10, maximum)


if __name__ == '__main__':
	main()
