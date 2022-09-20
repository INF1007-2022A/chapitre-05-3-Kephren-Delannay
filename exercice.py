#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	result = 0
	for char in text:
		result += 1 if str.isalnum(char) else 0
	return result

def get_word_length_histogram(text):
	hist = [0]
	words = text.split()
	test = []
	for w in words:
		n = get_num_letters(w)
		test.append(n)
		if len(hist) < n + 1:
			to_add = (n) - len(hist) + 1
			add = [0 for x in range(to_add)]
			hist += add
			hist[n] += 1
		else:
			hist[n] += 1
	return hist

def format_histogram(histogram):
	ROW_CHAR = "*"
	result = ""
	for index in range(1, len(histogram)):
		value = histogram[index]
		result += f'{index:>2}' + ' ' + ROW_CHAR * value + '\n'
	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	result = ""

	highest = histogram.copy()
	highest.sort()
	highest = highest[-1]

	for i in range(highest, 0, -1):
		for j in range(1, len(histogram)):
			if histogram[j] >= i:
				result += BLOCK_CHAR
			else:
				result += ' '
		result += '\n'
	result += LINE_CHAR * len(histogram)
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
