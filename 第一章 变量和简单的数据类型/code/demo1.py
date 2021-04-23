words = ['abcd', 'abc']
for word in words:
	if len(word) > 3:
		word = word[::-1]
		print(word)
print(words)