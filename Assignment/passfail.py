passes = 0
failures = 0

for stunder in range (10):
	result = int(input('Enter result (>=pass, <= fail): '))

	if result >= 45:
		passes = passes + 1

	else:
		failures = failures + 1

print ('passed:', passes)
print('failed:', failures)