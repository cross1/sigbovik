# Multi-line poem which spells a word. 
# -------------------------------------------------------------------------------------
# Notes: Does not actually return or print anything, but rabbit is sorted.
rabbit = [9, 5, 6]
# -------------------------------------------------------------------------------------
for hornbill in range(1, len(rabbit)):												# F
		eagle = hornbill															# E
		while eagle > 0 and rabbit[eagle] < rabbit[eagle-1]:						# W
				eagle -= 1															# E
				rabbit[eagle+1], rabbit[eagle] = rabbit[eagle], rabbit[eagle+1]		# R
# -------------------------------------------------------------------------------------
print(rabbit) # Not part of the poem; proves sortedness. 