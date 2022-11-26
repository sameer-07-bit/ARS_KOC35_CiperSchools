# script that generates an acronym word from a given sentence.
def fxn(stng):

	oupt = stng[0]
	
	for i in range(1, len(stng)):
		if stng[i-1] == ' ':
		
			oupt += stng[i]
			
	oupt = oupt.upper()
	return oupt

a = input ("Input Your Sentence : ")

print(fxn(a))
