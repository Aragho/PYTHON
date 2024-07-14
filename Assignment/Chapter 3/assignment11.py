total_miles = 0
total_gallon_used = 0
gallons_used = 0


while gallons_used != -1:

	gallons_used = float(input('Enter the gallons used (-1 to end): '))
	if gallons_used == -1:
		break
	miles_driven = float(input('Enter the miles driven: '))

	mile_per_gallon = miles_driven/gallons_used

	total_miles += miles_driven
	total_gallon_used += gallons_used

	print("The miles/gallon for this tank was ", mile_per_gallon)



average = total_miles / total_gallon_used

print("The overall average miles/gallon was  ", average)
	

