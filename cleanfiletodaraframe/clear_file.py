"""
Hi guys here i use a for to clena a entire .csv file of an specific character
in this case "=" to be used for dataframe in pandas.
"""

text = open('csfinv.csv')
output = open('output.csv', 'w')
for char in text.readlines():
	for char in line:
		if char in '='
			output.write('')
		else:
			output.write(char)
text.close()
output.close()
