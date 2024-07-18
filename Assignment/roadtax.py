print("Application opens")

price  = float(input('Enter the cost of a car: '))

if price < 1000000:
	tax = price * 0.10
	print("tax:", tax)

elif price < 3000000:
	tax = price * 0.15
	print("tax:", tax)
elif price <5000000 :
	tax = price * 0.20
	print("tax:", tax)

else:
	tax = price * 0.25
	print("tax:", tax)


print("Application closes") 