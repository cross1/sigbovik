# A five line poem with syllable counts 1-2-3-4-1, respectively.
#---------------------------------------------------------------
rawr = range(1) # We want to sort once.
cubs = [3, 2, 1]
prideArray = []

def populate(array):
	array.extend([5, 8, 2])

def cat():
	print(prideArray) # Checking if sorted.
	print("The lions have been sorted.")
#---------------------------------------------------------------
lions = []													 # 1
populate(lions)												 # 2
lions.extend(cubs)											 # 3
prideArray = sorted(lions)									 # 4
cat()														 # 1
#---------------------------------------------------------------