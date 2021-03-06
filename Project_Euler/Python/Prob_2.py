'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def sum_even_fib(max):
	Sum = 0
	First = 1
	Second = 2
	while Second < max:
		Lookback_1 = First
		Lookback_2 = Second
		First = Lookback_2
		Second = Lookback_1 + Lookback_2
		Sum += Lookback_2 if Lookback_2 % 2 == 0 else 0
		print Sum
	return Sum

if '__name__' == '__main__':
	print sum_even_fib(4000000)
