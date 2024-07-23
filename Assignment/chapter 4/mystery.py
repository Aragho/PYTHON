def mystery(x):
	y = 1
	for value in x:
		y += value ** 2
	return y
print(mystery(10))